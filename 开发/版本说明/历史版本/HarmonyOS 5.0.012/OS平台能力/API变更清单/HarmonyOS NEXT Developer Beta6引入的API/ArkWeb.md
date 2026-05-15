# ArkWeb

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：WebviewController； API声明：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void; 差异内容：static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setBackForwardCacheOptions(options: BackForwardCacheOptions): void; 差异内容：setBackForwardCacheOptions(options: BackForwardCacheOptions): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum SuspendType 差异内容： enum SuspendType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType； API声明：ENTER_BACK_FORWARD_CACHE = 0 差异内容：ENTER_BACK_FORWARD_CACHE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType； API声明：ENTER_BACKGROUND 差异内容：ENTER_BACKGROUND | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SuspendType； API声明：AUTO_CLEANUP 差异内容：AUTO_CLEANUP | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：resumePlayer?(): void; 差异内容：resumePlayer?(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：suspendPlayer?(type: SuspendType): void; 差异内容：suspendPlayer?(type: SuspendType): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class BackForwardCacheSupportedFeatures 差异内容： class BackForwardCacheSupportedFeatures | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures； API声明：nativeEmbed: boolean; 差异内容：nativeEmbed: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheSupportedFeatures； API声明：mediaTakeOver: boolean; 差异内容：mediaTakeOver: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class BackForwardCacheOptions 差异内容： class BackForwardCacheOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions； API声明：size: number; 差异内容：size: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：BackForwardCacheOptions； API声明：timeToLive: number; 差异内容：timeToLive: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus； API声明：ENTER_BFCACHE = 3 差异内容：ENTER_BFCACHE = 3 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus； API声明：LEAVE_BFCACHE = 4 差异内容：LEAVE_BFCACHE = 4 | component/web.d.ts |
