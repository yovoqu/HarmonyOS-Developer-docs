# ArkWeb

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：MessageLevel； API声明：Log 差异内容：NA | 类名：MessageLevel； API声明：Log = 5 差异内容：26.0.0 | component/web.d.ts |
| 新增错误码 | 类名：WebviewController； API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void; 差异内容：NA | 类名：WebviewController； API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void; 差异内容：17100002 | api/@ohos.web.webview.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel； API声明：Debug 差异内容：0 | 类名：MessageLevel； API声明：Debug = 1 差异内容：1 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel； API声明：Error 差异内容：1 | 类名：MessageLevel； API声明：Error = 4 差异内容：4 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel； API声明：Log 差异内容：3 | 类名：MessageLevel； API声明：Log = 5 差异内容：5 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel； API声明：Warn 差异内容：4 | 类名：MessageLevel； API声明：Warn = 3 差异内容：3 | component/web.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：executeAIPageCommand(command: string): Promise&lt;string&gt;; 差异内容：executeAIPageCommand(command: string): Promise&lt;string&gt;; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollbarMode； API声明：OVERLAY_VISUAL_SCROLLBAR = 2 差异内容：OVERLAY_VISUAL_SCROLLBAR = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：enableFullscreenVideoOverlay(enabled: boolean): WebAttribute; 差异内容：enableFullscreenVideoOverlay(enabled: boolean): WebAttribute; | component/web.d.ts |
