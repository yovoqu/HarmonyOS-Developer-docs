#!/usr/bin/env python3
"""Fast re-fetch pipeline using requests (no Playwright needed)."""

import requests
import json, os, re, time
from pathlib import Path
from datetime import datetime

BASE = Path("/home/yohurm/yovo-harmonyos-docs")
API_URL = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/getDocumentById"

DEVICE_MAP = {"phone": "Phone", "2in1": "PC/2in1", "tablet": "Tablet", "wearable": "Wearable", "tv": "TV"}

SESSION = None

def get_session():
    global SESSION
    if SESSION is None:
        SESSION = requests.Session()
        SESSION.headers.update({
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://developer.huawei.com",
            "Referer": "https://developer.huawei.com/consumer/cn/doc/",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        })
    return SESSION

def fetch_doc(catalog, slug):
    """Fetch document from API. Returns (title, update_time, html_content)."""
    session = get_session()
    payload = {"objectId": slug, "version": "", "catalogName": catalog, "language": "cn"}
    try:
        resp = session.post(API_URL, json=payload, timeout=15)
        data = resp.json()
        val = data.get("value", data.get("data", {}))
        title = val.get("title", "")
        update_time = val.get("displayUpdateTime", "")
        html = ""
        if val.get("content") and isinstance(val["content"], dict):
            html = val["content"].get("content", "")
        return title, update_time, html
    except Exception as e:
        return None, None, str(e)

def build_image_map(html, doc_file_path):
    """Map image URLs to existing local assets by position."""
    md_dir = Path(doc_file_path).parent
    doc_name = Path(doc_file_path).stem
    assets_dir = md_dir / "assets" / doc_name

    existing = []
    if assets_dir.exists():
        for f in sorted(assets_dir.iterdir()):
            if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.svg'):
                existing.append(str(f.relative_to(md_dir)))

    img_urls = []
    for tag in re.findall(r'<img[^>]+>', html):
        m = re.search(r'src="([^"]+)"', tag) or re.search(r"src='([^']+)'", tag)
        if m and m.group(1).startswith('http'):
            img_urls.append(m.group(1))

    mapping = {}
    for i, url in enumerate(img_urls):
        if i < len(existing):
            mapping[url] = existing[i]
    return mapping

def html_to_markdown(html, title, update_time, source_url, catalog, images_map):
    """Convert HTML to Markdown following methodology rules."""

    # Extract device-type
    device_type = ""
    h1_dev = re.search(r'<h1[^>]+device-type="([^"]+)"', html)
    if h1_dev:
        devices = h1_dev.group(1).split(',')
        device_type = " | ".join(DEVICE_MAP.get(d.strip(), d.strip()) for d in devices)

    md = html

    # ── Step 0: Extract notes inside table cells ──
    # Find notes inside <td>/<th>, convert to markdown, and insert
    # a placeholder right BEFORE the nearest preceding <table> tag.
    cell_note_placeholders = []  # (placeholder_id, note_markdown)

    def _note_in_cell(text, pos):
        before = text[:pos]
        td_o = len(re.findall(r'<td\b', before))
        td_c = len(re.findall(r'</td>', before))
        th_o = len(re.findall(r'<th\b', before))
        th_c = len(re.findall(r'</th>', before))
        return (td_o > td_c) or (th_o > th_c)

    note_matches = list(re.finditer(r'<div class="note">', md))
    for nm in reversed(note_matches):
        pos = nm.start()
        if not _note_in_cell(md, pos):
            continue
        # Find matching </div> by balanced counting
        depth = 1; p = pos + 17
        while depth > 0 and p < len(md):
            no = md.find('<div', p); nc = md.find('</div>', p)
            if nc < 0: break
            if 0 <= no < nc: depth += 1; p = no + 4
            else: depth -= 1; p = nc + 6
        note_html = md[pos:p]
        tm = re.search(r'<span class="notetitle">\s*(.*?)\s*</span>', note_html, re.DOTALL)
        bm = re.search(r'<div class="notebody">(.*?)</div>', note_html, re.DOTALL)
        nt = tm.group(1).strip().rstrip('：').rstrip(':') if tm else "说明"
        nb = re.sub(r'<[^>]+>', '', bm.group(1)).strip() if bm else ""
        note_md_text = f"\n> [!NOTE] {nt}\n> {nb}\n"
        # Remove note from HTML
        md = md[:pos] + md[p:]
        # Find nearest preceding <table> tag and insert placeholder before it
        before = md[:pos]
        table_pos = before.rfind('<table')
        if table_pos >= 0:
            pid = len(cell_note_placeholders)
            cell_note_placeholders.append((pid, note_md_text))
            md = md[:table_pos] + f"\x00TBLNOTE{pid}\x00" + md[table_pos:]

    # 1. Protect code blocks
    code_blocks = []
    def save_code(m):
        code_blocks.append(m.group(0))
        return f"\x00CODE{len(code_blocks)-1}\x00"
    md = re.sub(r'<pre[^>]*>[\s\S]*?</pre>', save_code, md)

    # 2. Extract and protect notes (those NOT in cells, still in HTML)
    notes = []
    def save_note(m):
        notes.append(m.group(0))
        return f"\x00NOTE{len(notes)-1}\x00"
    md = re.sub(r'<div[^>]*class="[^"]*note[^"]*"[^>]*>[\s\S]*?</div>', save_note, md)

    # 3. Strip div wrappers
    md = re.sub(r'<div[^>]*>', '\n', md)
    md = re.sub(r'</div>', '\n', md)

    # 4. Headings (shift +1 since # is doc title)
    # Also extract device-type from ALL heading levels
    def _device_line(heading_tag):
        """Extract device-type from a heading tag and return support line if present."""
        dt = re.search(r'device-type="([^"]+)"', heading_tag)
        if dt:
            devices = dt.group(1).split(',')
            mapped = " | ".join(DEVICE_MAP.get(d.strip(), d.strip()) for d in devices)
            return f"**支持设备：** {mapped}"
        return ""

    # Skip h1 if it matches doc title
    md = re.sub(r'<h1[^>]*>\s*' + re.escape(title) + r'\s*</h1>', '', md, flags=re.DOTALL)

    def _heading(m, prefix):
        tag = m.group(0)
        text = m.group(2)  # .group(1) is attributes, .group(2) is content
        text = re.sub(r'\[h[234]\]\s*', '', text)
        device_line = _device_line(tag)
        if device_line:
            return f'\n{prefix} {text}\n\n{device_line}\n'
        return f'\n{prefix} {text}\n'

    md = re.sub(r'<h1([^>]*?)>(.*?)</h1>', lambda m: _heading(m, '##'), md, flags=re.DOTALL)
    md = re.sub(r'<h2([^>]*?)>(.*?)</h2>', lambda m: _heading(m, '###'), md, flags=re.DOTALL)
    md = re.sub(r'<h3([^>]*?)>(.*?)</h3>', lambda m: _heading(m, '####'), md, flags=re.DOTALL)
    md = re.sub(r'<h4([^>]*?)>(.*?)</h4>', lambda m: _heading(m, '#####'), md, flags=re.DOTALL)

    # 4.5 Restore cell note placeholders: insert after preceding heading, before table
    for pid, note_md_text in cell_note_placeholders:
        placeholder = f"\x00TBLNOTE{pid}\x00"
        pos = md.find(placeholder)
        if pos < 0: continue
        # Find nearest preceding heading (##### ...)
        before = md[:pos]
        heading_match = list(re.finditer(r'^##### .+$', before, re.MULTILINE))
        if heading_match:
            last_h = heading_match[-1]
            insert_pos = last_h.end()
        else:
            insert_pos = pos
        # Insert note after heading, with blank line separating from table
        md = md[:insert_pos] + f"\n{note_md_text}\n" + md[pos + len(placeholder):]
        # Remove placeholder

    # Clean up orphaned placeholders
    md = re.sub(r'\x00TBLNOTE\d+\x00', '', md)

    # 5. Tables - with rowspan handling
    def convert_table(m):
        table_html = m.group(0)
        inner = re.sub(r'</?thead[^>]*>|</?tbody[^>]*>', '', table_html)
        rows = list(re.finditer(r'<tr[^>]*>(.*?)</tr>', inner, re.DOTALL))

        parsed = []  # [{is_header, cells: [{text, rowspan}]}]
        for tr in rows:
            row_html = tr.group(1)
            is_header = '<th' in row_html
            cells = []
            for cell in re.finditer(r'<(th|td)\b([^>]*)>(.*?)</\1>', row_html, re.DOTALL):
                attrs = cell.group(2); content = cell.group(3)
                rs = re.search(r'rowspan="(\d+)"', attrs)
                rowspan = int(rs.group(1)) if rs else 1
                text = re.sub(r'<p[^>]*>', '', content)
                text = re.sub(r'</p>', ' ', text)
                text = re.sub(r'<[^>]+>', '', text)
                text = re.sub(r'\s+', ' ', text).strip()
                text = text.replace('|', '\\|')
                cells.append({'text': text, 'rowspan': rowspan})
            parsed.append({'is_header': is_header, 'cells': cells})

        lines = []
        spans = {}  # col -> {text, rem}
        for row in parsed:
            if row['is_header']:
                texts = [c['text'] for c in row['cells']]
                lines.append('| ' + ' | '.join(texts) + ' |')
                lines.append('| ' + ' | '.join(['---'] * len(texts)) + ' |')
                continue
            out = []; ci = 0
            # Fill continuing rowspans
            for col in sorted(spans.keys()):
                while ci < col and ci < len(row['cells']):
                    out.append(row['cells'][ci]['text']); ci += 1
                out.append(spans[col]['text'])
                spans[col]['rem'] -= 1
                if spans[col]['rem'] <= 0: del spans[col]
            # Process remaining cells
            while ci < len(row['cells']):
                c = row['cells'][ci]
                out.append(c['text'])
                if c['rowspan'] > 1:
                    spans[ci] = {'text': c['text'], 'rem': c['rowspan'] - 1}
                ci += 1
            lines.append('| ' + ' | '.join(out) + ' |')
        return '\n'.join(lines) + '\n'

    md = re.sub(r'<table[^>]*>[\s\S]*?</table>', convert_table, md)

    # 6. Inline formatting
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.DOTALL)

    # 7. Lists — handle <p> inside <li>, support ol (ordered) and ul (unordered)
    def _collapse_li(inner):
        inner = re.sub(r'<p[^>]*>', '', inner)
        inner = re.sub(r'</p>', '\n', inner)
        inner = re.sub(r'\n{3,}', '\n\n', inner)
        return inner.strip()

    def _format_li(inner, prefix):
        inner = _collapse_li(inner)
        lines = inner.split('\n')
        if len(lines) > 1:
            result = f'{prefix} ' + lines[0].strip() + '\n'
            for l in lines[1:]:
                if l.strip():
                    result += '\n  ' + l.strip() + '\n'
            return result
        return f'{prefix} ' + inner + '\n'

    # Process <ol> — extract all <li> and auto-number
    def convert_ol(m):
        items = list(re.finditer(r'<li[^>]*>(.*?)</li>', m.group(0), re.DOTALL))
        result = ''
        for i, li in enumerate(items, 1):
            result += _format_li(li.group(1), f'{i}.')
        return result
    md = re.sub(r'<ol[^>]*>[\s\S]*?</ol>', convert_ol, md)

    # Process remaining <li> as unordered
    md = re.sub(r'<li[^>]*>(.*?)</li>',
        lambda m: _format_li(m.group(1), '-'), md, flags=re.DOTALL)

    # Replace ul/ol wrappers, then strip HTML indentation from list items
    md = re.sub(r'</?[ou]l[^>]*>', '\n', md)
    md = re.sub(r'^[ \t]+(\d+\. | - )', r'\1', md, flags=re.MULTILINE)
    # Also clean leading whitespace from table rows
    md = re.sub(r'^[ \t]+(\|)', r'\1', md, flags=re.MULTILINE)

    # 8. Paragraphs and breaks
    md = re.sub(r'<p[^>]*>', '\n', md)
    md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md)

    # 9. Strip span tags
    md = re.sub(r'</?span[^>]*>', '', md)

    # 10. Restore code blocks
    for i, block in enumerate(code_blocks):
        # Detect language
        lang = "text"
        block_lower = block.lower()
        if '.ets' in block_lower or '.ets#' in block_lower:
            lang = "ArkTS"
        elif '.ts#' in block_lower or '.d.ts' in block_lower:
            lang = "ts"
        elif '.cpp' in block_lower or '.cc#' in block_lower or '.h#' in block_lower:
            lang = "cpp"
        elif 'json' in block_lower:
            lang = "json"
        elif 'xml' in block_lower:
            lang = "xml"
        elif 'bash' in block_lower or 'shell' in block_lower:
            lang = "bash"

        code_match = re.search(r'<pre[^>]*>([\s\S]*?)</pre>', block)
        if code_match:
            code = code_match.group(1)
            code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
            code = re.sub(r'</?code[^>]*>', '', code)
            # Strip highlight toolbar noise
            code = re.sub(r'<div[^>]*highlight-div-header[^>]*>[\s\S]*?</div>', '', code)
            code = code.strip()
            md = md.replace(f"\x00CODE{i}\x00", f"\n```{lang}\n{code}\n```\n")
        else:
            md = md.replace(f"\x00CODE{i}\x00", "")

    # 11. Restore notes as callouts
    for i, note_html in enumerate(notes):
        note_type = "NOTE"
        if 'caution' in note_html.lower() or '注意' in note_html or '警告' in note_html or '危险' in note_html:
            note_type = "WARNING"
        if 'tip' in note_html.lower() or '说明' in note_html:
            note_type = "TIP"
        # Extract note content
        inner = re.sub(r'<[^>]+>', ' ', note_html)
        inner = re.sub(r'\s+', ' ', inner).strip()
        # Remove common note prefixes
        inner = re.sub(r'^(注意|说明|警告|危险|提示)[：:]?\s*', '', inner)
        note_md = f"\n> [!{note_type}]\n> {inner}\n"
        md = md.replace(f"\x00NOTE{i}\x00", note_md)

    # 12. Handle images
    for orig_url, local_path in images_map.items():
        encoded = local_path.replace(' ', '%20')
        md = md.replace(orig_url, encoded)

    # Convert remaining img tags
    def replace_img(m):
        src = re.search(r'src="([^"]+)"', m.group(0)) or re.search(r"src='([^']+)'", m.group(0))
        if not src:
            return ''
        s = src.group(1)
        for orig, local in images_map.items():
            if orig in s:
                return f"\n![]({local.replace(' ', '%20')})\n"
        return f"\n![]({s})\n"
    md = re.sub(r'<img[^>]+>', replace_img, md)

    # 13. Strip remaining HTML tags (protect code blocks first!)
    # Re-protect code blocks because restored code may contain < > characters
    code_blocks2 = []
    md = re.sub(r'```[\s\S]*?```',
        lambda m: (code_blocks2.append(m.group(0)) or f"\x00C2{len(code_blocks2)-1}\x00"), md)
    md = re.sub(r'<[^>]+>', '', md)
    for i, block in enumerate(code_blocks2):
        md = md.replace(f"\x00C2{i}\x00", block)

    # 14. Decode entities
    md = md.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    md = md.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')

    # 15. Fix relative links
    md = re.sub(r'\[([^\]]*)\]\((/consumer/cn/doc/[^\)]+)\)',
                r'[\1](https://developer.huawei.com\2)', md)

    # ── Post-processing ──
    # All post-processing must protect code blocks (```) from modification

    # Split into code blocks and non-code sections
    def protect_code_sections(text):
        """Split text into alternating (non_code, code_block) sections."""
        parts = re.split(r'(```[\s\S]*?```)', text)
        return parts  # Even indices: non-code, Odd indices: code blocks

    parts = protect_code_sections(md)

    # Process only non-code sections (even indices)
    for pi in range(0, len(parts), 2):
        # Escape $ and <>
        parts[pi] = re.sub(r'<(pid|bundleName|uri|\w+)>', r'&lt;\1&gt;', parts[pi])
        parts[pi] = re.sub(r'\$r\b', r'\\$r', parts[pi])
        parts[pi] = re.sub(r'\$rawfile\b', r'\\$rawfile', parts[pi])
        parts[pi] = re.sub(r'(%\d+)\$([sd])', r'\1\\$\2', parts[pi])

        # Image references on own lines
        lines = parts[pi].split('\n')
        new_lines = []
        for line in lines:
            if '![' in line and '](' in line and not line.strip().startswith('!['):
                for part in re.split(r'(!\[.*?\]\(.*?\))', line):
                    part = part.strip()
                    if part:
                        new_lines.append(part)
            else:
                new_lines.append(line)
        parts[pi] = '\n'.join(new_lines)

        # Clean leading spaces (non-code, non-special lines only)
        lines = parts[pi].split('\n')
        for j, line in enumerate(lines):
            s = line.lstrip()
            if line.startswith('    ') and not s.startswith(('-', '>', '|', '#', '`')):
                lines[j] = s
        parts[pi] = '\n'.join(lines)

    md = ''.join(parts)

    # API metadata spacing (references) - also in non-code only
    if catalog == "harmonyos-references":
        parts2 = protect_code_sections(md)
        for pi in range(0, len(parts2), 2):
            lines = parts2[pi].split('\n')
            result = []
            prev_was_meta = False
            for line in lines:
                is_meta = bool(re.match(r'\*\*[^*]+[：:]\*\*', line.strip()))
                if is_meta and prev_was_meta:
                    result.append('')
                result.append(line)
                prev_was_meta = is_meta
            parts2[pi] = '\n'.join(result)
        md = ''.join(parts2)

    # Build header
    header = f"# {title}\n\n更新时间：{update_time}\n\n来源：{source_url}\n"
    if device_type:
        header += f"**支持设备：** {device_type}\n"
    header += "\n"

    return header + md.strip() + "\n"


def main():
    updates_file = BASE / "docs_to_update.json"
    with open(updates_file, "r") as f:
        updates = json.load(f)

    total = len(updates)
    print(f"Processing {total} documents (requests-based, no Playwright)...")
    print(f"API: {API_URL}")
    print()

    updated = 0
    errors = 0
    skipped = 0
    start = time.time()

    for i, doc in enumerate(updates):
        try:
            file_path = BASE / doc["file"]
            catalog = doc["catalog"]
            slug = doc["slug"]
            source_url = doc["url"]

            title, update_time, html = fetch_doc(catalog, slug)

            if html is None or (isinstance(html, str) and html.startswith('Error')):
                errors += 1
                continue

            if not html or not title:
                skipped += 1
                continue

            # Map images to existing local assets
            images_map = build_image_map(html, str(file_path))

            # Convert to Markdown
            md = html_to_markdown(html, title, update_time, source_url, catalog, images_map)

            # Write file
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(md, encoding='utf-8')

            updated += 1

            if updated % 100 == 0:
                elapsed = time.time() - start
                rate = updated / elapsed
                eta = (total - i - 1) / rate if rate > 0 else 0
                print(f"  {i+1}/{total} ({rate:.1f}/s, ETA: {eta:.0f}s) updated={updated} errors={errors}")

        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"  ERROR [{doc.get('slug', '?')}]: {e}")

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"FAST REFETCH COMPLETE in {elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"Total: {total}, Updated: {updated}, Skipped: {skipped}, Errors: {errors}")
    print(f"Rate: {total/max(elapsed,1):.1f} docs/s")

if __name__ == "__main__":
    main()
