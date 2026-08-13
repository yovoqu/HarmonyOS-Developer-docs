#!/usr/bin/env python3
"""Check for official documentation updates by comparing local update times with API.

Reads all manifest.json files, for each entry:
  1. Extracts the local update time from the Markdown file header
  2. Queries the getDocumentById API for the official update time
  3. If they differ, adds the doc to docs_to_update.json

Usage: python3 check_updates.py [--limit N] [--fast] [--resume]
"""

import requests
import json, os, re, sys, time
from pathlib import Path
from collections import defaultdict

BASE = Path("/home/yohurm/yovo-harmonyos-docs")
API_URL = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/getDocumentById"
OUTPUT_FILE = BASE / "docs_to_update.json"
PROGRESS_FILE = BASE / "知识库/抓取脚本库/.check_progress.json"

# Map manifest location to catalog name
# ⚠️ 必须最长匹配优先！"设计指南" 必须先于 "指南"，
#    否则 设计/设计指南 的 manifest 会被误判为 harmonyos-guides。
#    同样 "设计指南" 必须先于 "最佳实践"（应用设计最佳实践）。
def catalog_for_manifest(manifest_path):
    rel = str(manifest_path.relative_to(BASE))
    if "设计指南" in rel:
        return "design-guides"
    if "指南" in rel:
        return "harmonyos-guides"
    if "API参考" in rel:
        return "harmonyos-references"
    if "FAQ" in rel:
        return "harmonyos-faqs"
    if "最佳实践" in rel:
        return "best-practices"
    if "版本说明" in rel:
        return "harmonyos-releases"
    return "unknown"

def get_session():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://developer.huawei.com",
        "Referer": "https://developer.huawei.com/consumer/cn/doc/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
    })
    return session

def extract_local_time(md_path):
    """Extract 更新时间 from the markdown file header."""
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"更新时间：(.+)", line)
                if m:
                    return m.group(1).strip()
    except FileNotFoundError:
        return None
    except Exception:
        return None
    return None

def fetch_official_time(session, catalog, slug):
    """Query API and return (title, update_time) or (None, None)."""
    payload = {"objectId": slug, "version": "", "catalogName": catalog, "language": "cn"}
    try:
        resp = session.post(API_URL, json=payload, timeout=15)
        data = resp.json()
        val = data.get("value", data.get("data", {}))
        title = val.get("title", "")
        update_time = val.get("displayUpdateTime", "")
        return title, update_time
    except Exception:
        return None, None

def normalize_time(t):
    """Normalize time strings for comparison (handle different formats)."""
    if not t:
        return ""
    # Remove timezone suffixes, normalize spaces
    t = t.strip()
    # "2026-05-26 06:48:54" vs "2026-05-26 06:48:54 CST" → keep only the datetime part
    return t[:19] if len(t) >= 19 else t

def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"processed": [], "total_checked": 0}

def save_progress(progress):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

def collect_all_entries():
    """Collect all manifest entries with metadata. File paths resolved relative to manifest parent."""
    entries = []
    for mf in sorted(BASE.rglob("manifest.json")):
        catalog = catalog_for_manifest(mf)
        manifest_dir = mf.parent
        with open(mf, "r") as f:
            try:
                data = json.load(f)
            except Exception:
                continue
        for item in data:
            slug = item.get("slug", "")
            local_name = item.get("name", item.get("title", ""))
            file_rel = item.get("file", "")
            url = item.get("url", "")
            if not slug or not file_rel:
                continue
            # Resolve file path relative to manifest directory
            abs_file = (manifest_dir / file_rel).resolve()
            entries.append({
                "manifest": str(mf.relative_to(BASE)),
                "catalog": catalog,
                "slug": slug,
                "file": str(abs_file.relative_to(BASE)),
                "url": url,
                "name": local_name,
            })
    return entries

def main():
    fast = "--fast" in sys.argv
    resume = "--resume" in sys.argv
    limit = None
    for a in sys.argv:
        if a.startswith("--limit="):
            limit = int(a.split("=")[1])

    entries = collect_all_entries()
    print(f"Found {len(entries)} entries in {len(set(e['manifest'] for e in entries))} manifests")

    # Dedupe by slug (cross-catalog same slug is valid, keep all)
    # But some might be same slug, same file - dedupe those
    seen = set()
    unique = []
    for e in entries:
        key = (e["catalog"], e["slug"])
        if key not in seen:
            seen.add(key)
            unique.append(e)
    print(f"Unique (catalog+slug): {len(unique)}")

    progress = load_progress() if resume else {"processed": [], "total_checked": 0}
    processed_set = set(progress["processed"])

    session = get_session()
    to_update = []
    total = len(unique)
    checked = progress["total_checked"]

    start = time.time()
    errors = 0
    not_found = 0

    for i, entry in enumerate(unique):
        if limit and i >= limit:
            break

        slug = entry["slug"]
        catalog = entry["catalog"]
        key = f"{catalog}::{slug}"

        if key in processed_set:
            checked += 1
            continue

        file_path = BASE / entry["file"]
        local_time = extract_local_time(file_path)

        # Query API
        title, official_time = fetch_official_time(session, catalog, slug)

        if title is None and official_time is None:
            errors += 1
            if errors <= 5:
                print(f"  API ERROR [{catalog}] {slug}")
            continue

        if not title or title == "404" or "not found" in official_time.lower() if official_time else False:
            # Some old manifests may reference 404 pages from the last update
            # Don't skip them entirely, just note
            not_found += 1
            if not_found <= 10:
                print(f"  NOT FOUND [{catalog}] {slug} → {title!r}")

        local_norm = normalize_time(local_time)
        official_norm = normalize_time(official_time)

        if local_norm != official_norm:
            status = "NEW" if local_time is None else "UPDATE"
            to_update.append({
                "file": entry["file"],
                "url": entry["url"],
                "slug": slug,
                "catalog": catalog,
                "local_time": local_time or "(new file)",
                "official_time": official_time,
                "status": status,
            })

        checked += 1
        progress["total_checked"] = checked
        progress["processed"].append(key)

        # Progress reporting
        if checked % 500 == 0:
            elapsed = time.time() - start
            rate = checked / max(elapsed, 1)
            eta = (total - checked) / max(rate, 0.01)
            print(f"  [{checked}/{total}] rate={rate:.1f}/s ETA={eta:.0f}s "
                  f"updates={len(to_update)} err={errors} nf={not_found}")
            save_progress(progress)

        # Save progress every 100 docs
        if checked % 100 == 0:
            save_progress(progress)

    save_progress(progress)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"Check complete in {elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"Total checked: {checked}, Updates found: {len(to_update)}")
    print(f"API errors: {errors}, Not found: {not_found}")

    # Write output
    if to_update:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(to_update, f, ensure_ascii=False, indent=2)
        print(f"\nWritten {len(to_update)} entries to {OUTPUT_FILE}")
        print("Run: python3 知识库/抓取脚本库/fetch_docs.py")
    else:
        # Remove empty output file if exists
        if OUTPUT_FILE.exists():
            OUTPUT_FILE.unlink()
        print("\nNo updates needed. All documents are current.")
        # Clean up progress file
        if PROGRESS_FILE.exists():
            PROGRESS_FILE.unlink()

if __name__ == "__main__":
    main()
