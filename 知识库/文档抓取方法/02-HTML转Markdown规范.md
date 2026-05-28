# HTML 转 Markdown 规范

合并自：[[华为文档HTML转Markdown整理方法论]]，并加入实战修复经验

---

## 一、转换顺序（关键！顺序错误会导致内容丢失）

必须严格按以下顺序执行，不可调换：

```
1.  提取 note callout（平衡 div 计数）
2.  剥离 <div> 标签
3.  保护代码块（占位符替换 → 后续恢复）
4.  清除 [h2]/[h3]/[h4] 标记
5.  转换 <table> → Markdown 表格
6.  转换 <h1>-<h4> → 标题
7.  转换 <img> → 图片引用
8.  转换 <ul>/<ol> → 列表（li 内先折叠 p，再转 - text，后替换 ul/ol，最后清前导空格）
9.  替换 <p> → 换行
10. 转换内联元素（strong/a/em）
11. 恢复代码块（替换占位符）
12. 恢复 note callout
13. 清理残留 HTML 标签
14. HTML 实体解码
15. 修复相对链接为绝对链接
16. 后处理（保护代码块的前提下）
```

**违反此顺序的后果**：
- 先处理 `<p>` 再剥离 `<div>` → 内部 `<table>`、`<ul>` 结构被破坏
- 全局 `replace(/<[^>]*>/g, '')` 不在代码块保护之后 → `<=` 等符号被误匹配，跨越数百字符删除代码

## 二、文档头部规范

```markdown
# 文档标题

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/slug
**支持设备：** Phone | PC/2in1 | Tablet | TV | Wearable
```

- **标题**：使用 API 返回的 `title` 字段
- **更新时间**：使用 API 返回的 `displayUpdateTime`（CST 时区）
- **来源**：官网完整 URL
- **支持设备**（仅 API 参考文档）：从 `<h1 device-type="...">` 属性提取

### 设备类型映射

| 代码 | 显示名称 |
|------|----------|
| phone | Phone |
| 2in1 | PC/2in1 |
| tablet | Tablet |
| wearable | Wearable |
| tv | TV |

## 三、文件命名

- **使用 API 返回的 title 作为文件名**，不使用 URL slug
- 非法字符替换：`/`→`／`、`:`→`：`、`*`→`＊`、`?`→`？`、`"`→`＂`、`<`→`＜`、`>`→`＞`、`|`→`｜`
- landing page 不转换为 Markdown

## 四、表格转换

### 4.1 正确做法：表级解析

```python
def convert_table(table_html):
    """逐表解析，避免跨表污染"""
    inner = re.sub(r'</?thead[^>]*>', '', table_html)
    inner = re.sub(r'</?tbody[^>]*>', '', inner)
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', inner, re.DOTALL)
    lines = []
    for row_html in rows:
        is_header = '<th' in row_html
        # ⚠️ 必须用 \b 词边界！<th[^>]*> 会匹配 <thead>
        cells = re.findall(r'<(th|td)\b[^>]*>(.*?)</\1>', row_html, re.DOTALL)
        cell_texts = []
        for tag, content in cells:
            text = re.sub(r'<[^>]+>', '', content).strip()
            text = text.replace('|', '\\|')
            cell_texts.append(text)
        if not cell_texts:
            continue
        if is_header:
            lines.append('| ' + ' | '.join(cell_texts) + ' |')
            lines.append('| ' + ' | '.join(['---'] * len(cell_texts)) + ' |')
        else:
            lines.append('| ' + ' | '.join(cell_texts) + ' |')
    return '\n'.join(lines)
```

### 4.2 常见陷阱

| 陷阱 | 错误做法 | 正确做法 |
|------|----------|----------|
| `<th>` 误匹配 `<thead>` | `<th[^>]*>` | `<th\b[^>]*>` |
| 无分隔线 | 只输出表头行 | 表头行后插入 `\|---\|---\|` |
| 表格被后处理破坏 | 全局应用空格清理 | 保护代码块，表格行以 `\|` 开头应跳过清理 |

### 4.3 后处理

- 删除所有单元格均为空的列（从右向左扫描）
- `rowspan` 处理见 4.5 节

### 4.4 表格内说明（Note in Table Cell）

当 `<div class="note">` 位于 `<td>` 或 `<th>` 内部时，说明内容属于该表格。Markdown 表格单元格内不支持多行块引用，因此必须将说明提取到表格外部。

**规则**：
1. 检测到表格单元格内的 `<div class="note">` → 提取说明标题和正文
2. 说明移至该表格紧上方（所属 `#####` 标题之后）
3. 使用 `> [!NOTE]` 块引用格式
4. 说明与表格第一行之间保留一个空行

**检测方法**：在完整 HTML 中扫描所有 `<div class="note">`，通过比较该位置之前的 `<td>`/`<th>` 开闭标签数量判断是否在单元格内。

```python
def note_in_cell(html, note_pos):
    before = html[:note_pos]
    td_opens = len(re.findall(r'<td\b', before))
    td_closes = len(re.findall(r'</td>', before))
    th_opens = len(re.findall(r'<th\b', before))
    th_closes = len(re.findall(r'</th>', before))
    return (td_opens > td_closes) or (th_opens > th_closes)
```

**提取说明内容**：使用平衡 div 计数找到匹配的 `</div>`，避免嵌套 `<div class="notebody">` 导致提前截断。

```python
# 平衡计数：从 <div class="note"> 开始
depth = 1; p = note_start + 17
while depth > 0 and p < len(html):
    no = html.find('<div', p)
    nc = html.find('</div>', p)
    if nc < 0: break
    if 0 <= no < nc: depth += 1; p = no + 4
    else: depth -= 1; p = nc + 6
note_html = html[note_start:p]  # 完整 note HTML
```

**期望输出**：

```markdown
##### Phone

> [!NOTE] 说明
> Mate 60系列仅供部分可通过开发者渠道定向获得推送的设备使用。

| 设备系列 | 设备型号 | 型号代码 |
| --- | --- | --- |
| Mate 60系列 | Mate 60 | BRA-AL00 |
```

### 4.5 rowspan 处理

HTML 表格的 `rowspan="N"` 属性在 Markdown 中无对应语法。转换为 Markdown 时，将该单元格的值在后续 N-1 行中重复填充。

```python
span_tracker = {}  # col_index -> {'text': str, 'remaining': int}
for row in rows:
    # 1. 先填充上一行遗留的 rowspan 占位
    for col in sorted(span_tracker.keys()):
        output_cells.insert(col, span_tracker[col]['text'])
        span_tracker[col]['remaining'] -= 1
        if span_tracker[col]['remaining'] <= 0:
            del span_tracker[col]
    # 2. 处理当前行单元格，记录新的 rowspan
    for cell in row['cells']:
        if cell['rowspan'] > 1:
            span_tracker[col_index] = {'text': cell['text'], 'remaining': cell['rowspan'] - 1}
```

### 4.6 表格行前导空格

HTML 中 `<thead>` 和 `<tr>` 之间的空白文本节点会保留到 Markdown 表格行首，导致表格 header 行带前导空格，破坏表格对齐：

```markdown
      | 音频容器规格 | 音频解密类型 |   ← 错误：6 个前导空格
| --- | --- |
| mp4 | AAC |
```

**修复**：在处理列表面换行后，同时对表格行清理前导空格。

```python
# 清理列表项前导空格
md = re.sub(r'^[ \t]+(\d+\. | - )', r'\1', md, flags=re.MULTILINE)
# 清理表格行前导空格
md = re.sub(r'^[ \t]+(\|)', r'\1', md, flags=re.MULTILINE)
```

**注意**：此规则也适用于连续两个独立表格（各自被 `<div>` 包裹）的场景。每个表格的表头行都需要独立清理。

## 五、代码块转换

### 5.1 提取与保护

```python
# 第一步：用占位符保护所有代码块
code_blocks = []
def save_code(m):
    code_blocks.append(m.group(0))
    return f"\x00CODE{len(code_blocks)-1}\x00"
md = re.sub(r'<pre[^>]*>[\s\S]*?</pre>', save_code, md)
```

### 5.2 语言检测优先级

1. `pre` 上的 `codehub` 链接文件后缀 → `.ets` = ArkTS, `.ts` = ts, `.cpp` = cpp
2. `pre.className` → language-json, language-xml 等
3. `pre.hw-language`
4. 默认 `text`

### 5.3 恢复代码块

```python
code = code_content
code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
code = re.sub(r'</?code[^>]*>', '', code)
# 清除 highlight-div-header 工具栏噪声
code = re.sub(r'<div[^>]*highlight-div-header[^>]*>[\s\S]*?</div>', '', code)
md = md.replace(f"\x00CODE{i}\x00", f"\n```{lang}\n{code.strip()}\n```\n")
```

### 5.4 缩进保持

代码块内容**禁止**被后处理阶段修改。所有空格清理/压缩操作必须先保护代码块：

```python
parts = re.split(r'(```[\s\S]*?```)', md)
for pi in range(0, len(parts), 2):  # 只处理非代码块部分
    parts[pi] = apply_cleanup(parts[pi])
md = ''.join(parts)
```

### 5.5 必须删除的代码块噪声

- `<div class="highlight-div-header">` 及其全部子内容
- 复制/收起/自动换行/深色代码主题按钮
- 行号容器
- 锚点图标

## 六、标题转换

```python
# 清除 [h2]/[h3]/[h4] 标记（API 返回的 HTML 标题文本含这些前缀）
def clean_h(text):
    return re.sub(r'\[h[234]\]\s*', '', text)

# h1→##, h2→###, h3→####, h4→#####（因 # 已用于文档标题）
# 跳过与文档标题重复的第一个 h1
md = re.sub(r'<h1[^>]*>\s*' + re.escape(doc_title) + r'\s*</h1>', '', md)
md = re.sub(r'<h1[^>]*>(.*?)</h1>', lambda m: f'## {clean_h(m.group(1))}\n', md)
md = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda m: f'### {clean_h(m.group(1))}\n', md)
md = re.sub(r'<h3[^>]*>(.*?)</h3>', lambda m: f'#### {clean_h(m.group(1))}\n', md)
md = re.sub(r'<h4[^>]*>(.*?)</h4>', lambda m: f'##### {clean_h(m.group(1))}\n', md)
```

## 七、Note Callout 转换

```python
# <div class="note"> → Obsidian callout
# 必须用平衡计数法匹配 <div>，不能用非贪婪 [\s\S]*?
# 因为 note 内部可能嵌套子 div

def extract_notes(html):
    """从 <div class="note" 开始，对 </div> 做平衡计数"""
    pattern = re.compile(r'<div[^>]*class="[^"]*note[^"]*"[^>]*>')
    # 从匹配位置开始，逐字符计数 <div 和 </div>
    # 找到平衡的 </div> 闭合标签
    ...
    return note_content

# 转换格式
note_type = "NOTE"    # 默认
# "注意"/"警告"/"危险" → WARNING
# "说明"/"提示" → TIP

md_output = f"\n> [!{note_type}]\n> {content}\n"
```

## 七点五、列表转换

### 问题根因

华为 API 返回的 HTML 中，`<li>` 内部使用 `<p>` 包裹内容：

```html
<ul>
  <li><p>列表项文本</p></li>
  <li><p><strong>标题</strong></p><p>描述段落1</p><p>描述段落2</p></li>
</ul>
```

如果按常规顺序先转 `<p>` 再转 `<li>`，会导致 `-` 和列表文本被 `<p>` 转换成的换行符断开。

### 正确转换顺序

1. 在 `<li>` 内部先处理 `<p>`：去掉 `<p>` 开头标签，`</p>` 替换为换行
2. 将 `<li>` 转换为 `- text`
3. 先替换 `<ul>/<ol>` 为换行，再清理列表项前导空格（否则第一项不在行首，正则无法匹配）

### 实现

```python
def fix_list_item(m):
    inner = m.group(1)
    # 折叠 <p> 标签：去掉开头，</p> 变 \n
    inner = re.sub(r'<p[^>]*>', '', inner)
    inner = re.sub(r'</p>', '\n', inner)
    inner = re.sub(r'\n{3,}', '\n\n', inner)
    inner = inner.strip()
    lines = inner.split('\n')
    if len(lines) > 1:
        # 多段落列表项：续行前加空行，2 空格缩进
        result = '- ' + lines[0].strip() + '\n'
        for l in lines[1:]:
            if l.strip():
                result += '\n  ' + l.strip() + '\n'
        return result
    return '- ' + inner + '\n'

md = re.sub(r'<li[^>]*>(.*?)</li>', fix_list_item, md, flags=re.DOTALL)
# 关键：先替换 ul/ol，再清理前导空格
md = re.sub(r'</?[ou]l[^>]*>', '\n', md)
md = re.sub(r'^[ \t]+(- )', r'\1', md, flags=re.MULTILINE)
```

### 期望输出

**简单列表**：
```markdown
- 提供音视频统一管控能力，音视频类应用接入AVSession后...
- 提供音频后台约束能力，音频接入AVSession后...
```

**多段落列表项**（续行用空行 + 2 空格缩进）：
```markdown
- **投播体验一致**

  提供音视频统一管控能力...

  用户可以通过系统播控中心...
```

### 后处理保护

列表续行使用 2 空格缩进，后处理的行首空格清理阈值从 2 空格改为 4 空格，避免误删续行缩进。

## 八、后处理规则

所有后处理必须保护代码块：

```python
parts = re.split(r'(```[\s\S]*?```)', md)
# parts[0]=文本, parts[1]=代码块, parts[2]=文本, ...
for pi in range(0, len(parts), 2):
    # 以下所有规则只应用于 parts[pi]（非代码块部分）
```

### 8.1 图片引用独立成行

```python
# 错误：![](a.png) **说明：** 正文
# 正确：![](a.png)\n\n**说明：** 正文
```

### 8.2 行首空格清除

段落行首 2+ 空格 → 去除。例外：列表项（`- `）、块引用（`> `）、表格行（`|`）、标题（`#`）、代码围栏（`` ``` ``）。

### 8.3 段落内空格压缩

4+ 连续空格 → 单空格。例外：表格行、代码块不处理。

### 8.4 特殊字符转义

| 模式 | 转义为 | 原因 |
|------|--------|------|
| `<pid>`, `<bundleName>`, `<uri>` | `&lt;pid&gt;` 等 | Obsidian 会当成 HTML 标签 |
| `$r(`, `$rawfile(` | `\$r(`, `\$rawfile(` | Obsidian 会当成 LaTeX 公式 |
| `%1$s`, `%2$d` | `%1\$s`, `%2\$d` | 同上 |

### 8.5 相对链接规范化

`/consumer/cn/doc/...` → `https://developer.huawei.com/consumer/cn/doc/...`

### 8.6 图片路径空格编码

`![](assets/doc name/file.png)` → `![](assets/doc%20name/file.png)`

### 8.7 API 元数据间距（仅 references）

连续的 `**xxx：**` 行之间插入空行：
```markdown
**元服务API：** 从API version 12开始支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
```

## 九、note 提取必须用 div 深度计数

Note 内部可能嵌套 `<div class="notebody">` 等子 div：

```html
<div class="note">
  <div class="notebody">
    <p>说明内容</p>
  </div>
</div>
```

用非贪婪 `([\s\S]*?)` 会在第一个 `</div>` 处截断 → note 内容不完整。
用贪婪 `([\s\S]*)` → 多段 note 之间的正文被吞掉。

**正确做法**：从 `<div class="note"` 开始，对 `</div>` 做平衡计数。

## 十、检查清单（26 项）

- [ ] 是否只保留正文页，没有 landing page
- [ ] 文件名是否是官方文档名
- [ ] 头部是否包含真实更新时间
- [ ] 图片是否已经本地化
- [ ] 图片路径是否符合 `assets/{docName}/` 规则
- [ ] 是否残留 HTML 表格
- [ ] 代码块是否使用标准三反引号
- [ ] 代码块语言是否正确
- [ ] 是否混入 `收起 / 复制 / 自动换行 / 深色代码主题`
- [ ] manifest 是否记录转换结果
- [ ] `<pid>`、`<uri>` 等占位符是否转义
- [ ] 是否残留 `/consumer/...` 相对链接
- [ ] 列表项 `-` 和文本是否在同一行（未断裂）
- [ ] 多段落列表项续行是否有 2 空格缩进
- [ ] 列表项是否有残留 HTML 前导空格
- [ ] callout、列表、段落中的链接是否错误拆行
- [ ] 代码块内部是否仍存在未缩进代码
- [ ] JSON / JSON5 / 配置示例是否整理成标准层级
- [ ] shell / 日志 / 工具输出是否被错误"美化"
- [ ] `$r`、`$rawfile`、`%1$s` 等是否转义为 `\$`
- [ ] 图片引用是否独立成行
- [ ] 段落是否有残留行首空格
- [ ] 段落内是否有大量连续空格未压缩
- [ ] 图片路径中的空格是否 URL 编码为 `%20`
- [ ] 表格是否有空列需要删除
- [ ] 表格内说明是否提取到表格外部（`#####` 标题之后，表格之前，空行隔开）
- [ ] 表格行是否有残留 HTML 前导空格（`^[ \t]+\|`）
- [ ] 表格 rowspan 单元格值是否在跨行中重复填充
- [ ] note callout 提取有无导致章节内容丢失
- [ ] API 参考文档头部是否包含 `支持设备：`
- [ ] API 元数据项之间是否有空行分隔
