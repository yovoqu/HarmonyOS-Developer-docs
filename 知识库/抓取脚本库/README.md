# 抓取脚本库

## fetch_docs.py

主拉取脚本。功能：

1. **差异对比** — 读取 `docs_to_update.json`，调用 API 获取最新更新时间
2. **正文拉取** — 通过 `getDocumentById` API 获取 HTML 正文
3. **HTML→Markdown 转换** — 按 [[02-HTML转Markdown规范]] 全部规则转换
4. **图片映射** — 将 HTML 图片 URL 映射到本地 `assets/` 目录已有资源
5. **后处理** — 清除 `[h2]` 标记、图片分行、空格清理、API 元数据间距

### 用法

```bash
# 处理 docs_to_update.json 中的全部文档
python3 fetch_docs.py

# 只处理前 N 篇（测试用）
python3 fetch_docs.py 10
```

### 输入

`docs_to_update.json` — 格式：
```json
[
  {
    "file": "开发/指南/入门/资源分类与访问.md",
    "url": "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access",
    "slug": "resource-categories-and-access",
    "catalog": "harmonyos-guides",
    "local_time": "2026-04-30 02:41:24",
    "official_time": "2026-05-26 06:48:54",
    "status": "UPDATE"
  }
]
```

### 依赖

```bash
pip3 install requests
```

无 Playwright 依赖。API 直接通过 HTTP 调用。

### 核心 API 端点

- `POST https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/getDocumentById`
- Headers 中必须包含 `Sec-Fetch-Dest: empty`, `Sec-Fetch-Mode: cors`, `Sec-Fetch-Site: same-site`
