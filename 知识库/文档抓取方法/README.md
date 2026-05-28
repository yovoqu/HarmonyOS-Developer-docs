# 华为开发者文档抓取规范

## 文档索引

| 文档 | 内容 | 何时阅读 |
|------|------|----------|
| [01-文档抓取流程](01-文档抓取流程.md) | 端到端抓取流程、API 使用、manifest 规范 | 开始任何抓取任务前 |
| [02-HTML转Markdown规范](02-HTML转Markdown规范.md) | HTML→MD 转换规则、后处理、常见陷阱 | 转换阶段开始前 |
| [03-图片资源规范](03-图片资源规范.md) | 图片下载、命名、引用规范 | 处理含图片的文档时 |
| [04-动态页面处理](04-动态页面处理.md) | Playwright 实时阅读动态页面 | API 不可用时 |

## 整体流程

```
Phase 0: 范围确认 ──→ Phase 1: 获取导航 ──→ Phase 2: 差异对比
                                                   │
                                          ┌────────┘
                                          ▼
Phase 3: 拉取正文 ──→ Phase 4: HTML→MD ──→ Phase 5: 后处理 ──→ Phase 6: 质量检查
```

## 核心 API

所有 API 端点基础路径：`https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/`

### getDocumentById — 获取文档正文

```
POST /getDocumentById
Body: {"objectId":"<slug>","version":"","catalogName":"<catalog>","language":"cn"}
Response: {code:0, value:{title, displayUpdateTime, content:{content:"<html>"}}}
```

### getCatalogTree — 获取导航目录树

```
POST /getCatalogTree
Body: {"language":"cn","catalogName":"<catalog>"}
Response: {code:0, value:{catalogTreeList:[{children, nodeName, isLeaf, relateDocument}]}}
```

### Catalog 名称映射

| 官网 URL 路径 | catalogName | 说明 |
|---------------|-------------|------|
| `/harmonyos-guides/` | `harmonyos-guides` | 开发指南 |
| `/harmonyos-references/` | `harmonyos-references` | API 参考 |
| `/design-guides/` | `design-guides` | 设计指南 |
| `/best-practices/` | `best-practices` | 最佳实践 |
| `/harmonyos-faqs/` | `harmonyos-faqs` | FAQ |
| `/harmonyos-releases/` | `harmonyos-releases` | 版本说明 |
| `/harmonyos-roadmap/` | `harmonyos-roadmap` | 变更路线 |

### 请求头配置

```python
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://developer.huawei.com",
    "Referer": "https://developer.huawei.com/consumer/cn/doc/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}
```

## 关键注意事项

1. **优先使用 API，不优先使用 Playwright**。`requests` + 正确的 Headers 即可调用所有 API，无需浏览器。
2. **表格转换必须用 `\b` 词边界**。`<th[^>]*>` 会误匹配 `<thead>`，正确写法是 `<th\b[^>]*>`。
3. **所有后处理必须保护代码块**。空格清理、`$` 转义等操作前，先用 ` ```[\s\S]*?``` ` 分割保护。
4. **API 返回的标题含 `[h2]` 标记**，转换时必须清除。
5. **时间戳对比需注意时区**。API 返回 CST (UTC+8)，部分旧文档存的是 UTC。
