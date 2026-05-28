# ArkWeb

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6012

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_NONE = 4 差异内容：THREAT_NONE = 4 | component/web.d.ts |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_UNPROCESSED = 5 差异内容：THREAT_UNPROCESSED = 5 | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback): WebAttribute; 差异内容：onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：webview； API声明：class PrefetchOptions 差异内容：class PrefetchOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PrefetchOptions； API声明：minTimeBetweenPrefetchesMs: number; 差异内容：minTimeBetweenPrefetchesMs: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PrefetchOptions； API声明：ignoreCacheControlNoStore: boolean; 差异内容：ignoreCacheControlNoStore: boolean; | api/@ohos.web.webview.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebviewController； API声明：prefetchPage(url: string, additionalHeaders?: Array&lt;WebHeader&gt;): void; 差异内容：prefetchPage(url: string, additionalHeaders?: Array&lt;WebHeader&gt;): void; | 类名：WebviewController； API声明：prefetchPage(url: string, additionalHeaders?: Array&lt;WebHeader&gt;, prefetchOptions?: PrefetchOptions): void; 差异内容：prefetchPage(url: string, additionalHeaders?: Array&lt;WebHeader&gt;, prefetchOptions?: PrefetchOptions): void; | api/@ohos.web.webview.d.ts |
