# ArkWeb

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-7001

## ArkWeb
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：WebviewController； API声明：static prefetchResource(request: RequestInfo, additionalHeaders?: Array&lt;WebHeader&gt;, cacheKey?: string, cacheValidTime?: number): void; 差异内容：NA | 类名：WebviewController； API声明：static prefetchResource(request: RequestInfo, additionalHeaders?: Array&lt;WebHeader&gt;, cacheKey?: string, cacheValidTime?: number): void; 差异内容：401 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController； API声明：injectOfflineResources(resourceMaps: Array&lt;OfflineResourceMap&gt;): void; 差异内容：NA | 类名：WebviewController； API声明：injectOfflineResources(resourceMaps: Array&lt;OfflineResourceMap&gt;): void; 差异内容：401 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ArkWebEngineVersion； API声明：M144 = 3 差异内容：M144 = 3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明：interface SecurityParams 差异内容：interface SecurityParams | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableJITCompilation?: boolean; 差异内容：disableJITCompilation?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableWebAssembly?: boolean; 差异内容：disableWebAssembly?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableWebGL?: boolean; 差异内容：disableWebGL?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disablePDFViewer?: boolean; 差异内容：disablePDFViewer?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableMathML?: boolean; 差异内容：disableMathML?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableServiceWorker?: boolean; 差异内容：disableServiceWorker?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityParams； API声明：disableNonProxyUDP?: boolean; 差异内容：disableNonProxyUDP?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static enableAdvancedSecurityMode(securityParams: SecurityParams): void; 差异内容：static enableAdvancedSecurityMode(securityParams: SecurityParams): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebNativeMessagingExtensionContext； API声明：startAbilityForResult(want: Want, options?: StartOptions): Promise&lt;AbilityResult&gt;; 差异内容：startAbilityForResult(want: Want, options?: StartOptions): Promise&lt;AbilityResult&gt;; | api/@ohos.web.WebNativeMessagingExtensionContext.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum WebKeyboardAppearanceMode 差异内容：declare enum WebKeyboardAppearanceMode | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAppearanceMode； API声明：NONE_IMMERSIVE = 0 差异内容：NONE_IMMERSIVE = 0 | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAppearanceMode； API声明：IMMERSIVE = 1 差异内容：IMMERSIVE = 1 | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAppearanceMode； API声明：LIGHT_IMMERSIVE = 2 差异内容：LIGHT_IMMERSIVE = 2 | component/web.d.ts |
| 新增API | NA | 类名：WebKeyboardAppearanceMode； API声明：DARK_IMMERSIVE = 3 差异内容：DARK_IMMERSIVE = 3 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnInputmethodAttachedCallback = () => void; 差异内容：type OnInputmethodAttachedCallback = () => void; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy): WebAttribute; 差异内容：scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：enableDrag(value: boolean): WebAttribute; 差异内容：enableDrag(value: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：enableScrollDirectionalLock(value: boolean, type: ScrollDirectionalLockType): WebAttribute; 差异内容：enableScrollDirectionalLock(value: boolean, type: ScrollDirectionalLockType): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：aiSessionOptions(aiSessions: Array&lt;AISessionEvent&gt;): WebAttribute; 差异内容：aiSessionOptions(aiSessions: Array&lt;AISessionEvent&gt;): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onInputmethodAttached(callback: OnInputmethodAttachedCallback): WebAttribute; 差异内容：onInputmethodAttached(callback: OnInputmethodAttachedCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：keyboardAppearance(mode: WebKeyboardAppearanceMode): WebAttribute; 差异内容：keyboardAppearance(mode: WebKeyboardAppearanceMode): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum ScrollbarLayoutPolicy 差异内容：declare enum ScrollbarLayoutPolicy | component/web.d.ts |
| 新增API | NA | 类名：ScrollbarLayoutPolicy； API声明：CONTENT = 0 差异内容：CONTENT = 0 | component/web.d.ts |
| 新增API | NA | 类名：ScrollbarLayoutPolicy； API声明：SYSTEM = 1 差异内容：SYSTEM = 1 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum ScrollDirectionalLockType 差异内容：declare enum ScrollDirectionalLockType | component/web.d.ts |
| 新增API | NA | 类名：ScrollDirectionalLockType； API声明：ALL = 0 差异内容：ALL = 0 | component/web.d.ts |
| 新增API | NA | 类名：ScrollDirectionalLockType； API声明：NESTED_SCROLL = 1 差异内容：NESTED_SCROLL = 1 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean; 差异内容：type OnCreateAISession = (id: string, params: string, result: OnAISessionCallback) => boolean; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void; 差异内容：type OnExecuteAIAction = (id: string, params: string, result: OnAISessionCallback) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnDestroyAISession = (id: string) => void; 差异内容：type OnDestroyAISession = (id: string) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：declare interface AISessionEvent 差异内容：declare interface AISessionEvent | component/web.d.ts |
| 新增API | NA | 类名：AISessionEvent； API声明：aiSessionType: AISessionType; 差异内容：aiSessionType: AISessionType; | component/web.d.ts |
| 新增API | NA | 类名：AISessionEvent； API声明：onCreateAISession: OnCreateAISession; 差异内容：onCreateAISession: OnCreateAISession; | component/web.d.ts |
| 新增API | NA | 类名：AISessionEvent； API声明：onExecuteAIAction: OnExecuteAIAction; 差异内容：onExecuteAIAction: OnExecuteAIAction; | component/web.d.ts |
| 新增API | NA | 类名：AISessionEvent； API声明：onDestroyAISession: OnDestroyAISession; 差异内容：onDestroyAISession: OnDestroyAISession; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum AISessionType 差异内容：declare enum AISessionType | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：TRANSLATOR = 1 差异内容：TRANSLATOR = 1 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：LANGUAGE_DETECTOR = 2 差异内容：LANGUAGE_DETECTOR = 2 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：SUMMARIZER = 3 差异内容：SUMMARIZER = 3 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：WRITER = 4 差异内容：WRITER = 4 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：REWRITER = 5 差异内容：REWRITER = 5 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：PROMPT = 6 差异内容：PROMPT = 6 | component/web.d.ts |
| 新增API | NA | 类名：AISessionType； API声明：PROOFREADER = 7 差异内容：PROOFREADER = 7 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum AISessionResultType 差异内容：declare enum AISessionResultType | component/web.d.ts |
| 新增API | NA | 类名：AISessionResultType； API声明：SUCCESS = 0 差异内容：SUCCESS = 0 | component/web.d.ts |
| 新增API | NA | 类名：AISessionResultType； API声明：FAILURE = 1 差异内容：FAILURE = 1 | component/web.d.ts |
| 新增API | NA | 类名：AISessionResultType； API声明：RUNNING = 2 差异内容：RUNNING = 2 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnAISessionCallback = (state: AISessionResultType, content: string) => void; 差异内容：type OnAISessionCallback = (state: AISessionResultType, content: string) => void; | component/web.d.ts |
