# ArkWeb

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-hdc

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：WebCookieManager； API声明：static getCookie(url: string): string; 差异内容：NA | 类名：WebCookieManager； API声明：static getCookie(url: string): string; 差异内容：11 | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：WebCookieManager； API声明：static setCookie(url: string, value: string): void; 差异内容：NA | 类名：WebCookieManager； API声明：static setCookie(url: string, value: string): void; 差异内容：11 | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：WebCookieManager； API声明：static deleteEntireCookie(): void; 差异内容：NA | 类名：WebCookieManager； API声明：static deleteEntireCookie(): void; 差异内容：11 | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：WebCookieManager； API声明：static deleteSessionCookie(): void; 差异内容：NA | 类名：WebCookieManager； API声明：static deleteSessionCookie(): void; 差异内容：11 | api/@ohos.web.webview.d.ts |
| API废弃版本变更 | 类名：WebController； API声明：getCookieManager(): WebCookie; 差异内容：NA | 类名：WebController； API声明：getCookieManager(): WebCookie; 差异内容：9 | component/web.d.ts |
| API废弃版本变更 | 类名：WebAttribute； API声明：password(password: boolean): WebAttribute; 差异内容：NA | 类名：WebAttribute； API声明：password(password: boolean): WebAttribute; 差异内容：10 | component/web.d.ts |
| API废弃版本变更 | 类名：WebAttribute； API声明：tableData(tableData: boolean): WebAttribute; 差异内容：NA | 类名：WebAttribute； API声明：tableData(tableData: boolean): WebAttribute; 差异内容：10 | component/web.d.ts |
| API废弃版本变更 | 类名：WebAttribute； API声明：wideViewModeAccess(wideViewModeAccess: boolean): WebAttribute; 差异内容：NA | 类名：WebAttribute； API声明：wideViewModeAccess(wideViewModeAccess: boolean): WebAttribute; 差异内容：10 | component/web.d.ts |
| API废弃版本变更 | 类名：WebAttribute； API声明：userAgent(userAgent: string): WebAttribute; 差异内容：NA | 类名：WebAttribute； API声明：userAgent(userAgent: string): WebAttribute; 差异内容：10 | component/web.d.ts |
| API废弃版本变更 | 类名：WebAttribute； API声明：onUrlLoadIntercept(callback: (event?: {  data: string \| WebResourceRequest;  }) => boolean): WebAttribute; 差异内容：NA | 类名：WebAttribute； API声明：onUrlLoadIntercept(callback: (event?: {  data: string \| WebResourceRequest;  }) => boolean): WebAttribute; 差异内容：10 | component/web.d.ts |
| 错误码变更 | 类名：WebStorage； API声明：static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void; 差异内容：NA | 类名：WebStorage； API声明：static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void; 差异内容：17100012,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebStorage； API声明：static getOriginQuota(origin: string, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：WebStorage； API声明：static getOriginQuota(origin: string, callback: AsyncCallback<number>): void; 差异内容：17100011,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebStorage； API声明：static getOriginUsage(origin: string, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：WebStorage； API声明：static getOriginUsage(origin: string, callback: AsyncCallback<number>): void; 差异内容：17100011,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void; 差异内容：17100011,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(callback: AsyncCallback<Array<string>>): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void; 差异内容：401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebCookieManager； API声明：static saveCookieAsync(callback: AsyncCallback<void>): void; 差异内容：NA | 类名：WebCookieManager； API声明：static saveCookieAsync(callback: AsyncCallback<void>): void; 差异内容：401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void; 差异内容：NA | 类名：WebviewController； API声明：storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void; 差异内容：17100001,17100003,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：runJavaScript(script: string, callback: AsyncCallback<string>): void; 差异内容：NA | 类名：WebviewController； API声明：runJavaScript(script: string, callback: AsyncCallback<string>): void; 差异内容：17100001,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：hasImage(callback: AsyncCallback<boolean>): void; 差异内容：NA | 类名：WebviewController； API声明：hasImage(callback: AsyncCallback<boolean>): void; 差异内容：17100001,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：createWebMessagePorts(): Array<WebMessagePort>; 差异内容：17100001 | 类名：WebviewController； API声明：createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>; 差异内容：17100001,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：static customizeSchemes(schemes: Array<WebCustomScheme>): void; 差异内容：401 | 类名：WebviewController； API声明：static customizeSchemes(schemes: Array<WebCustomScheme>): void; 差异内容：17100020,401 | api/@ohos.web.webview.d.ts |
| 错误码变更 | 类名：WebviewController； API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void; 差异内容：17100001,17100002,401 | 类名：WebviewController； API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void; 差异内容：17100001,401 | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebStorage； API声明：static deleteAllData(): void; 差异内容：NA | 类名：WebStorage； API声明：static deleteAllData(incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static allowGeolocation(origin: string): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static allowGeolocation(origin: string, incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static deleteGeolocation(origin: string): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static deleteGeolocation(origin: string, incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static deleteAllGeolocation(): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static deleteAllGeolocation(incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string): Promise<boolean>; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(): Promise<Array<string>>; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(callback: AsyncCallback<Array<string>>): void; 差异内容：NA | 类名：GeolocationPermissions； API声明：static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebCookieManager； API声明：static existCookie(): boolean; 差异内容：NA | 类名：WebCookieManager； API声明：static existCookie(incognito?: boolean): boolean; 差异内容：incognito?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebviewController； API声明：createWebMessagePorts(): Array<WebMessagePort>; 差异内容：NA | 类名：WebviewController； API声明：createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>; 差异内容：isExtentionType?: boolean | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebviewController； API声明：registerJavaScriptProxy(object: object, name: string, methodList: Array<string>): void; 差异内容：NA | 类名：WebviewController； API声明：registerJavaScriptProxy(object: object, name: string, methodList: Array<string>, asyncMethodList?: Array<string>): void; 差异内容：asyncMethodList?: Array<string> | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：javaScriptProxy(javaScriptProxy: {  object: object;  name: string;  methodList: Array<string>;  controller: WebController \| WebviewController;  }): WebAttribute; 差异内容：javaScriptProxy: {  object: object;  name: string;  methodList: Array<string>;  controller: WebController \| WebviewController;  } | 类名：WebAttribute； API声明：javaScriptProxy(javaScriptProxy: {  object: object;  name: string;  methodList: Array<string>;  controller: WebController \| WebviewController;  asyncMethodList?: Array<string>;  }): WebAttribute; 差异内容：javaScriptProxy: {  object: object;  name: string;  methodList: Array<string>;  controller: WebController \| WebviewController;  asyncMethodList?: Array<string>;  } | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onPageEnd(callback: (event?: {  url: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  url: string;  }) => void | 类名：WebAttribute； API声明：onPageEnd(callback: (event?: {  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onPageBegin(callback: (event?: {  url: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  url: string;  }) => void | 类名：WebAttribute； API声明：onPageBegin(callback: (event?: {  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onProgressChange(callback: (event?: {  newProgress: number;  }) => void): WebAttribute; 差异内容：callback: (event?: {  newProgress: number;  }) => void | 类名：WebAttribute； API声明：onProgressChange(callback: (event?: {  /**  * The new progress of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  newProgress: number;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The new progress of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  newProgress: number;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onTitleReceive(callback: (event?: {  title: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  title: string;  }) => void | 类名：WebAttribute； API声明：onTitleReceive(callback: (event?: {  /**  * The title of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  title: string;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The title of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  title: string;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onGeolocationShow(callback: (event?: {  origin: string;  geolocation: JsGeolocation;  }) => void): WebAttribute; 差异内容：callback: (event?: {  origin: string;  geolocation: JsGeolocation;  }) => void | 类名：WebAttribute； API声明：onGeolocationShow(callback: (event?: {  /**  * Origin of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  origin: string;  /**  * Defines the js geolocation request.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  geolocation: JsGeolocation;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * Origin of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  origin: string;  /**  * Defines the js geolocation request.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  geolocation: JsGeolocation;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onAlert(callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean | 类名：WebAttribute； API声明：onAlert(callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of alert dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of alert dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onBeforeUnload(callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean | 类名：WebAttribute； API声明：onBeforeUnload(callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * The message of confirm dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * The message of confirm dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onConfirm(callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  url: string;  message: string;  result: JsResult;  }) => boolean | 类名：WebAttribute； API声明：onConfirm(callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of confirm dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of confirm dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onPrompt(callback: (event?: {  url: string;  message: string;  value: string;  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  url: string;  message: string;  value: string;  result: JsResult;  }) => boolean | 类名：WebAttribute； API声明：onPrompt(callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of prompt dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * The value of prompt dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  value: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The message of prompt dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: string;  /**  * The value of prompt dialog.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  value: string;  /**  * Handle the user's JavaScript result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: JsResult;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onConsole(callback: (event?: {  message: ConsoleMessage;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  message: ConsoleMessage;  }) => boolean | 类名：WebAttribute； API声明：onConsole(callback: (event?: {  /**  * Console message information of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: ConsoleMessage;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * Console message information of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  message: ConsoleMessage;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onErrorReceive(callback: (event?: {  request: WebResourceRequest;  error: WebResourceError;  }) => void): WebAttribute; 差异内容：callback: (event?: {  request: WebResourceRequest;  error: WebResourceError;  }) => void | 类名：WebAttribute； API声明：onErrorReceive(callback: (event?: {  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: WebResourceRequest;  /**  * The information of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The information of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  error: WebResourceError;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: WebResourceRequest;  /**  * The information of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @since 10  */  /**  * The information of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  error: WebResourceError;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onHttpErrorReceive(callback: (event?: {  request: WebResourceRequest;  response: WebResourceResponse;  }) => void): WebAttribute; 差异内容：callback: (event?: {  request: WebResourceRequest;  response: WebResourceResponse;  }) => void | 类名：WebAttribute； API声明：onHttpErrorReceive(callback: (event?: {  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: WebResourceRequest;  /**  * Web resource response of event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  response: WebResourceResponse;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of error event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: WebResourceRequest;  /**  * Web resource response of event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  response: WebResourceResponse;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onDownloadStart(callback: (event?: {  url: string;  userAgent: string;  contentDisposition: string;  mimetype: string;  contentLength: number;  }) => void): WebAttribute; 差异内容：callback: (event?: {  url: string;  userAgent: string;  contentDisposition: string;  mimetype: string;  contentLength: number;  }) => void | 类名：WebAttribute； API声明：onDownloadStart(callback: (event?: {  /**  * The URL of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The userAgent of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  userAgent: string;  /**  * The contentDisposition of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  contentDisposition: string;  /**  * The mimetype of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  mimetype: string;  /**  * The contentLength of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  contentLength: number;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The URL of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  /**  * The userAgent of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  userAgent: string;  /**  * The contentDisposition of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  contentDisposition: string;  /**  * The mimetype of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  mimetype: string;  /**  * The contentLength of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  contentLength: number;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onRefreshAccessedHistory(callback: (event?: {  url: string;  isRefreshed: boolean;  }) => void): WebAttribute; 差异内容：callback: (event?: {  url: string;  isRefreshed: boolean;  }) => void | 类名：WebAttribute； API声明：onRefreshAccessedHistory(callback: (event?: {  /**  * URL of the visit.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * If true, the page is being reloaded, otherwise, means that the page is newly loaded.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isRefreshed: boolean;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * URL of the visit.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * If true, the page is being reloaded, otherwise, means that the page is newly loaded.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isRefreshed: boolean;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onRenderExited(callback: (event?: {  renderExitReason: RenderExitReason;  }) => void): WebAttribute; 差异内容：callback: (event?: {  renderExitReason: RenderExitReason;  }) => void | 类名：WebAttribute； API声明：onRenderExited(callback: (event?: {  /**  * The specific reason why the rendering process exits abnormally.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  renderExitReason: RenderExitReason;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The specific reason why the rendering process exits abnormally.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  renderExitReason: RenderExitReason;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onShowFileSelector(callback: (event?: {  result: FileSelectorResult;  fileSelector: FileSelectorParam;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  result: FileSelectorResult;  fileSelector: FileSelectorParam;  }) => boolean | 类名：WebAttribute； API声明：onShowFileSelector(callback: (event?: {  /**  * Defines the file selector result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: FileSelectorResult;  /**  * Encompassed message information as parameters to fileSelector.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  fileSelector: FileSelectorParam;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * Defines the file selector result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  result: FileSelectorResult;  /**  * Encompassed message information as parameters to fileSelector.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  fileSelector: FileSelectorParam;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onResourceLoad(callback: (event: {  url: string;  }) => void): WebAttribute; 差异内容：callback: (event: {  url: string;  }) => void | 类名：WebAttribute； API声明：onResourceLoad(callback: (event: {  /**  * The URL of the loaded resource file.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * The URL of the loaded resource file.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onFullScreenEnter(callback: (event: {  handler: FullScreenExitHandler;  }) => void): WebAttribute; 差异内容：callback: (event: {  handler: FullScreenExitHandler;  }) => void | 类名：WebAttribute； API声明：onFullScreenEnter(callback: OnFullScreenEnterCallback): WebAttribute; 差异内容：callback: OnFullScreenEnterCallback | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onScaleChange(callback: (event: {  oldScale: number;  newScale: number;  }) => void): WebAttribute; 差异内容：callback: (event: {  oldScale: number;  newScale: number;  }) => void | 类名：WebAttribute； API声明：onScaleChange(callback: (event: {  /**  * Old scale of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  oldScale: number;  /**  * New scale of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  newScale: number;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * Old scale of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  oldScale: number;  /**  * New scale of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  newScale: number;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onHttpAuthRequest(callback: (event?: {  handler: HttpAuthHandler;  host: string;  realm: string;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  handler: HttpAuthHandler;  host: string;  realm: string;  }) => boolean | 类名：WebAttribute； API声明：onHttpAuthRequest(callback: (event?: {  /**  * Defines the http auth request result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  handler: HttpAuthHandler;  /**  * Host of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  host: string;  /**  * realm of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  realm: string;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * Defines the http auth request result.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  handler: HttpAuthHandler;  /**  * Host of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  host: string;  /**  * realm of the page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  realm: string;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onInterceptRequest(callback: (event?: {  request: WebResourceRequest;  }) => WebResourceResponse): WebAttribute; 差异内容：callback: (event?: {  request: WebResourceRequest;  }) => WebResourceResponse | 类名：WebAttribute； API声明：onInterceptRequest(callback: (event?: {  /**  * The url of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  request: WebResourceRequest;  }) => WebResourceResponse): WebAttribute; 差异内容：callback: (event?: {  /**  * The url of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  request: WebResourceRequest;  }) => WebResourceResponse | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onPermissionRequest(callback: (event?: {  request: PermissionRequest;  }) => void): WebAttribute; 差异内容：callback: (event?: {  request: PermissionRequest;  }) => void | 类名：WebAttribute； API声明：onPermissionRequest(callback: (event?: {  /**  * Defines the onPermissionRequest callback.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: PermissionRequest;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * Defines the onPermissionRequest callback.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  request: PermissionRequest;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onContextMenuShow(callback: (event?: {  param: WebContextMenuParam;  result: WebContextMenuResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  param: WebContextMenuParam;  result: WebContextMenuResult;  }) => boolean | 类名：WebAttribute； API声明：onContextMenuShow(callback: (event?: {  /**  * The menu-related parameters.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  param: WebContextMenuParam;  /**  * The menu corresponding event is passed to the kernel.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  result: WebContextMenuResult;  }) => boolean): WebAttribute; 差异内容：callback: (event?: {  /**  * The menu-related parameters.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  param: WebContextMenuParam;  /**  * The menu corresponding event is passed to the kernel.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  result: WebContextMenuResult;  }) => boolean | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onSearchResultReceive(callback: (event?: {  activeMatchOrdinal: number;  numberOfMatches: number;  isDoneCounting: boolean;  }) => void): WebAttribute; 差异内容：callback: (event?: {  activeMatchOrdinal: number;  numberOfMatches: number;  isDoneCounting: boolean;  }) => void | 类名：WebAttribute； API声明：onSearchResultReceive(callback: (event?: {  /**  * The ordinal number of the currently matched lookup item (starting from 0).  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  activeMatchOrdinal: number;  /**  * The number of all matched keywords.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  numberOfMatches: number;  /**  * Find out whether the operation is completed on the next page. The method may be called back multiple times until isDoneCounting is true.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isDoneCounting: boolean;  }) => void): WebAttribute; 差异内容：callback: (event?: {  /**  * The ordinal number of the currently matched lookup item (starting from 0).  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  activeMatchOrdinal: number;  /**  * The number of all matched keywords.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  numberOfMatches: number;  /**  * Find out whether the operation is completed on the next page. The method may be called back multiple times until isDoneCounting is true.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isDoneCounting: boolean;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onScroll(callback: (event: {  xOffset: number;  yOffset: number;  }) => void): WebAttribute; 差异内容：callback: (event: {  xOffset: number;  yOffset: number;  }) => void | 类名：WebAttribute； API声明：onScroll(callback: (event: {  /**  * The X offset of the scroll.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  xOffset: number;  /**  * The Y offset of the scroll.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  yOffset: number;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * The X offset of the scroll.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  xOffset: number;  /**  * The Y offset of the scroll.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  yOffset: number;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onSslErrorEventReceive(callback: (event: {  handler: SslErrorHandler;  error: SslError;  }) => void): WebAttribute; 差异内容：callback: (event: {  handler: SslErrorHandler;  error: SslError;  }) => void | 类名：WebAttribute； API声明：onSslErrorEventReceive(callback: (event: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: SslErrorHandler;  /**  * Error codes.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  error: SslError;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: SslErrorHandler;  /**  * Error codes.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  error: SslError;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onClientAuthenticationRequest(callback: (event: {  handler: ClientAuthenticationHandler;  host: string;  port: number;  keyTypes: Array<string>;  issuers: Array<string>;  }) => void): WebAttribute; 差异内容：callback: (event: {  handler: ClientAuthenticationHandler;  host: string;  port: number;  keyTypes: Array<string>;  issuers: Array<string>;  }) => void | 类名：WebAttribute； API声明：onClientAuthenticationRequest(callback: (event: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ClientAuthenticationHandler;  /**  * The hostname of the requesting certificate server.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  host: string;  /**  * The port number of the request certificate server.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  port: number;  /**  * Acceptable asymmetric key types.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  keyTypes: Array<string>;  /**  * Certificates that match the private key are acceptable to the issuer.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  issuers: Array<string>;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ClientAuthenticationHandler;  /**  * The hostname of the requesting certificate server.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  host: string;  /**  * The port number of the request certificate server.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  port: number;  /**  * Acceptable asymmetric key types.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  keyTypes: Array<string>;  /**  * Certificates that match the private key are acceptable to the issuer.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  issuers: Array<string>;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onWindowNew(callback: (event: {  isAlert: boolean;  isUserTrigger: boolean;  targetUrl: string;  handler: ControllerHandler;  }) => void): WebAttribute; 差异内容：callback: (event: {  isAlert: boolean;  isUserTrigger: boolean;  targetUrl: string;  handler: ControllerHandler;  }) => void | 类名：WebAttribute； API声明：onWindowNew(callback: (event: {  /**  * true indicates the request to create a dialog and false indicates a new tab.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isAlert: boolean;  /**  * true indicates that it is triggered by the user, and false indicates that it is triggered by a non-user.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isUserTrigger: boolean;  /**  * Destination URL.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  targetUrl: string;  /**  * Lets you set the WebviewController instance for creating a new window.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ControllerHandler;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * true indicates the request to create a dialog and false indicates a new tab.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isAlert: boolean;  /**  * true indicates that it is triggered by the user, and false indicates that it is triggered by a non-user.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  isUserTrigger: boolean;  /**  * Destination URL.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  targetUrl: string;  /**  * Lets you set the WebviewController instance for creating a new window.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ControllerHandler;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onTouchIconUrlReceived(callback: (event: {  url: string;  precomposed: boolean;  }) => void): WebAttribute; 差异内容：callback: (event: {  url: string;  precomposed: boolean;  }) => void | 类名：WebAttribute； API声明：onTouchIconUrlReceived(callback: (event: {  /**  * The apple-touch-icon URL address received.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * Corresponding to whether apple-touch-icon is precomposited.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  precomposed: boolean;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * The apple-touch-icon URL address received.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  url: string;  /**  * Corresponding to whether apple-touch-icon is precomposited.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  precomposed: boolean;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onFaviconReceived(callback: (event: {  favicon: PixelMap;  }) => void): WebAttribute; 差异内容：callback: (event: {  favicon: PixelMap;  }) => void | 类名：WebAttribute； API声明：onFaviconReceived(callback: (event: {  /**  * Received the Favicon icon for the PixelMap object.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  favicon: PixelMap;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * Received the Favicon icon for the PixelMap object.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  favicon: PixelMap;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onPageVisible(callback: (event: {  url: string;  }) => void): WebAttribute; 差异内容：callback: (event: {  url: string;  }) => void | 类名：WebAttribute； API声明：onPageVisible(callback: (event: {  /**  * The URL of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * The URL of page.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  url: string;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebAttribute； API声明：onDataResubmitted(callback: (event: {  handler: DataResubmissionHandler;  }) => void): WebAttribute; 差异内容：callback: (event: {  handler: DataResubmissionHandler;  }) => void | 类名：WebAttribute； API声明：onDataResubmitted(callback: (event: {  /**  * Form data resubmission handle.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: DataResubmissionHandler;  }) => void): WebAttribute; 差异内容：callback: (event: {  /**  * Form data resubmission handle.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: DataResubmissionHandler;  }) => void | component/web.d.ts |
| 函数变更 | 类名：WebResourceResponse； API声明：setResponseData(data: string \| number); 差异内容：data: string \| number | 类名：WebResourceResponse； API声明：setResponseData(data: string \| number \| Resource \| ArrayBuffer); 差异内容：data: string \| number \| Resource \| ArrayBuffer | component/web.d.ts |
| 新增API | NA | 类名：webview； API声明： enum SecureDnsMode 差异内容： enum SecureDnsMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecureDnsMode； API声明：OFF = 0 差异内容：OFF = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecureDnsMode； API声明：AUTO = 1 差异内容：AUTO = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecureDnsMode； API声明：SECURE_ONLY = 2 差异内容：SECURE_ONLY = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum SecurityLevel 差异内容： enum SecurityLevel | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityLevel； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityLevel； API声明：SECURE = 1 差异内容：SECURE = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityLevel； API声明：WARNING = 2 差异内容：WARNING = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SecurityLevel； API声明：DANGEROUS = 3 差异内容：DANGEROUS = 3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum MediaPlaybackState 差异内容： enum MediaPlaybackState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaPlaybackState； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaPlaybackState； API声明：PLAYING = 1 差异内容：PLAYING = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaPlaybackState； API声明：PAUSED = 2 差异内容：PAUSED = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaPlaybackState； API声明：STOPPED = 3 差异内容：STOPPED = 3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isStandard?: boolean; 差异内容：isStandard?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isLocal?: boolean; 差异内容：isLocal?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isDisplayIsolated?: boolean; 差异内容：isDisplayIsolated?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isSecure?: boolean; 差异内容：isSecure?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isCspBypassing?: boolean; 差异内容：isCspBypassing?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCustomScheme； API声明：isCodeCacheSupported?: boolean; 差异内容：isCodeCacheSupported?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface RequestInfo 差异内容： interface RequestInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：RequestInfo； API声明：url: string; 差异内容：url: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：RequestInfo； API声明：method: string; 差异内容：method: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：RequestInfo； API声明：formData: string; 差异内容：formData: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static fetchCookieSync(url: string, incognito?: boolean): string; 差异内容：static fetchCookieSync(url: string, incognito?: boolean): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static fetchCookie(url: string): Promise<string>; 差异内容：static fetchCookie(url: string): Promise<string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static fetchCookie(url: string, callback: AsyncCallback<string>): void; 差异内容：static fetchCookie(url: string, callback: AsyncCallback<string>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static configCookieSync(url: string, value: string, incognito?: boolean): void; 差异内容：static configCookieSync(url: string, value: string, incognito?: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static configCookie(url: string, value: string): Promise<void>; 差异内容：static configCookie(url: string, value: string): Promise<void>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static configCookie(url: string, value: string, callback: AsyncCallback<void>): void; 差异内容：static configCookie(url: string, value: string, callback: AsyncCallback<void>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearAllCookiesSync(incognito?: boolean): void; 差异内容：static clearAllCookiesSync(incognito?: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearAllCookies(): Promise<void>; 差异内容：static clearAllCookies(): Promise<void>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearAllCookies(callback: AsyncCallback<void>): void; 差异内容：static clearAllCookies(callback: AsyncCallback<void>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearSessionCookieSync(): void; 差异内容：static clearSessionCookieSync(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearSessionCookie(): Promise<void>; 差异内容：static clearSessionCookie(): Promise<void>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager； API声明：static clearSessionCookie(callback: AsyncCallback<void>): void; 差异内容：static clearSessionCookie(callback: AsyncCallback<void>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum WebMessageType 差异内容： enum WebMessageType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：NOT_SUPPORT 差异内容：NOT_SUPPORT | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：STRING 差异内容：STRING | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：NUMBER 差异内容：NUMBER | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：BOOLEAN 差异内容：BOOLEAN | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：ARRAY_BUFFER 差异内容：ARRAY_BUFFER | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：ARRAY 差异内容：ARRAY | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageType； API声明：ERROR 差异内容：ERROR | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebMessageExt 差异内容： class WebMessageExt | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getType(): WebMessageType; 差异内容：getType(): WebMessageType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getString(): string; 差异内容：getString(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getNumber(): number; 差异内容：getNumber(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getBoolean(): boolean; 差异内容：getBoolean(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getArrayBuffer(): ArrayBuffer; 差异内容：getArrayBuffer(): ArrayBuffer; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getArray(): Array<string \| number \| boolean>; 差异内容：getArray(): Array<string \| number \| boolean>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：getError(): Error; 差异内容：getError(): Error; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setType(type: WebMessageType): void; 差异内容：setType(type: WebMessageType): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setString(message: string): void; 差异内容：setString(message: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setNumber(message: number): void; 差异内容：setNumber(message: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setBoolean(message: boolean): void; 差异内容：setBoolean(message: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setArrayBuffer(message: ArrayBuffer): void; 差异内容：setArrayBuffer(message: ArrayBuffer): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setArray(message: Array<string \| number \| boolean>): void; 差异内容：setArray(message: Array<string \| number \| boolean>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessageExt； API声明：setError(message: Error): void; 差异内容：setError(message: Error): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessagePort； API声明：isExtentionType?: boolean; 差异内容：isExtentionType?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessagePort； API声明：postMessageEventExt(message: WebMessageExt): void; 差异内容：postMessageEventExt(message: WebMessageExt): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebMessagePort； API声明：onMessageEventExt(callback: (result: WebMessageExt) => void): void; 差异内容：onMessageEventExt(callback: (result: WebMessageExt) => void): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface SnapshotInfo 差异内容： interface SnapshotInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotInfo； API声明：id?: string; 差异内容：id?: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotInfo； API声明：size?: SizeOptions; 差异内容：size?: SizeOptions; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface SnapshotResult 差异内容： interface SnapshotResult | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotResult； API声明：id?: string; 差异内容：id?: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotResult； API声明：status?: boolean; 差异内容：status?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotResult； API声明：size?: SizeOptions; 差异内容：size?: SizeOptions; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SnapshotResult； API声明：imagePixelMap?: image.PixelMap; 差异内容：imagePixelMap?: image.PixelMap; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum JsMessageType 差异内容： enum JsMessageType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：NOT_SUPPORT 差异内容：NOT_SUPPORT | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：STRING 差异内容：STRING | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：NUMBER 差异内容：NUMBER | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：BOOLEAN 差异内容：BOOLEAN | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：ARRAY_BUFFER 差异内容：ARRAY_BUFFER | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageType； API声明：ARRAY 差异内容：ARRAY | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class JsMessageExt 差异内容： class JsMessageExt | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getType(): JsMessageType; 差异内容：getType(): JsMessageType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getString(): string; 差异内容：getString(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getNumber(): number; 差异内容：getNumber(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getBoolean(): boolean; 差异内容：getBoolean(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getArrayBuffer(): ArrayBuffer; 差异内容：getArrayBuffer(): ArrayBuffer; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：JsMessageExt； API声明：getArray(): Array<string \| number \| boolean>; 差异内容：getArray(): Array<string \| number \| boolean>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum RenderProcessMode 差异内容： enum RenderProcessMode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：RenderProcessMode； API声明：SINGLE = 0 差异内容：SINGLE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：RenderProcessMode； API声明：MULTIPLE 差异内容：MULTIPLE | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface CacheOptions 差异内容： interface CacheOptions | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：CacheOptions； API声明：responseHeaders: Array<WebHeader>; 差异内容：responseHeaders: Array<WebHeader>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum OfflineResourceType 差异内容： enum OfflineResourceType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceType； API声明：IMAGE 差异内容：IMAGE | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceType； API声明：CSS 差异内容：CSS | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceType； API声明：CLASSIC_JS 差异内容：CLASSIC_JS | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceType； API声明：MODULE_JS 差异内容：MODULE_JS | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface OfflineResourceMap 差异内容： interface OfflineResourceMap | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceMap； API声明：urlList: Array<string>; 差异内容：urlList: Array<string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceMap； API声明：resource: Uint8Array; 差异内容：resource: Uint8Array; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceMap； API声明：responseHeaders: Array<WebHeader>; 差异内容：responseHeaders: Array<WebHeader>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：OfflineResourceMap； API声明：type: OfflineResourceType; 差异内容：type: OfflineResourceType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void; 差异内容：static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：enableSafeBrowsing(enable: boolean): void; 差异内容：enableSafeBrowsing(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：isSafeBrowsingEnabled(): boolean; 差异内容：isSafeBrowsingEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：runJavaScriptExt(script: string \| ArrayBuffer): Promise<JsMessageExt>; 差异内容：runJavaScriptExt(script: string \| ArrayBuffer): Promise<JsMessageExt>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：runJavaScriptExt(script: string \| ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void; 差异内容：runJavaScriptExt(script: string \| ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getCertificate(): Promise<Array<cert.X509Cert>>; 差异内容：getCertificate(): Promise<Array<cert.X509Cert>>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void; 差异内容：getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setAudioMuted(mute: boolean): void; 差异内容：setAudioMuted(mute: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void; 差异内容：prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void; 差异内容：static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setCustomUserAgent(userAgent: string): void; 差异内容：setCustomUserAgent(userAgent: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getCustomUserAgent(): string; 差异内容：getCustomUserAgent(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static setConnectionTimeout(timeout: number): void; 差异内容：static setConnectionTimeout(timeout: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setDownloadDelegate(delegate: WebDownloadDelegate): void; 差异内容：setDownloadDelegate(delegate: WebDownloadDelegate): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：startDownload(url: string): void; 差异内容：startDownload(url: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：postUrl(url: string, postData: ArrayBuffer): void; 差异内容：postUrl(url: string, postData: ArrayBuffer): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter; 差异内容：createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getSecurityLevel(): SecurityLevel; 差异内容：getSecurityLevel(): SecurityLevel; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：isIncognitoMode(): boolean; 差异内容：isIncognitoMode(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setScrollable(enable: boolean): void; 差异内容：setScrollable(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getScrollable(): boolean; 差异内容：getScrollable(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setPrintBackground(enable: boolean): void; 差异内容：setPrintBackground(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getPrintBackground(): boolean; 差异内容：getPrintBackground(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：startCamera(): void; 差异内容：startCamera(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：stopCamera(): void; 差异内容：stopCamera(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：closeCamera(): void; 差异内容：closeCamera(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static pauseAllTimers(): void; 差异内容：static pauseAllTimers(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static resumeAllTimers(): void; 差异内容：static resumeAllTimers(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getLastJavascriptProxyCallingFrameUrl(): string; 差异内容：getLastJavascriptProxyCallingFrameUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void; 差异内容：setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：clearWebSchemeHandler(): void; 差异内容：clearWebSchemeHandler(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void; 差异内容：static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static clearServiceWorkerWebSchemeHandler(): void; 差异内容：static clearServiceWorkerWebSchemeHandler(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：enableIntelligentTrackingPrevention(enable: boolean): void; 差异内容：enableIntelligentTrackingPrevention(enable: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：isIntelligentTrackingPreventionEnabled(): boolean; 差异内容：isIntelligentTrackingPreventionEnabled(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void; 差异内容：static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void; 差异内容：static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static clearIntelligentTrackingPreventionBypassingList(): void; 差异内容：static clearIntelligentTrackingPreventionBypassingList(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：stopAllMedia(): void; 差异内容：stopAllMedia(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：resumeAllMedia(): void; 差异内容：resumeAllMedia(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：pauseAllMedia(): void; 差异内容：pauseAllMedia(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：closeAllMediaPresentations(): void; 差异内容：closeAllMediaPresentations(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getMediaPlaybackState(): MediaPlaybackState; 差异内容：getMediaPlaybackState(): MediaPlaybackState; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void; 差异内容：onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void; 差异内容：static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string, cacheValidTime?: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static clearPrefetchedResource(cacheKeyList: Array<string>): void; 差异内容：static clearPrefetchedResource(cacheKeyList: Array<string>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static enableWholeWebPageDrawing(): void; 差异内容：static enableWholeWebPageDrawing(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void; 差异内容：webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static setRenderProcessMode(mode: RenderProcessMode): void; 差异内容：static setRenderProcessMode(mode: RenderProcessMode): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static getRenderProcessMode(): RenderProcessMode; 差异内容：static getRenderProcessMode(): RenderProcessMode; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：terminateRenderProcess(): boolean; 差异内容：terminateRenderProcess(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：precompileJavaScript(url: string, script: string \| Uint8Array, cacheOptions: CacheOptions): Promise<number>; 差异内容：precompileJavaScript(url: string, script: string \| Uint8Array, cacheOptions: CacheOptions): Promise<number>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void; 差异内容：injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static setHostIP(hostName: string, address: string, aliveTime: number): void; 差异内容：static setHostIP(hostName: string, address: string, aliveTime: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static clearHostIP(hostName: string): void; 差异内容：static clearHostIP(hostName: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：static warmupServiceWorker(url: string): void; 差异内容：static warmupServiceWorker(url: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController； API声明：getSurfaceId(): string; 差异内容：getSurfaceId(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum WebDownloadState 差异内容： enum WebDownloadState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：IN_PROGRESS = 0 差异内容：IN_PROGRESS = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：COMPLETED 差异内容：COMPLETED | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：CANCELED 差异内容：CANCELED | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：INTERRUPTED 差异内容：INTERRUPTED | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：PENDING 差异内容：PENDING | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：PAUSED 差异内容：PAUSED | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadState； API声明：UNKNOWN 差异内容：UNKNOWN | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum WebDownloadErrorCode 差异内容： enum WebDownloadErrorCode | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：ERROR_UNKNOWN = 0 差异内容：ERROR_UNKNOWN = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_FAILED = 1 差异内容：FILE_FAILED = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_ACCESS_DENIED = 2 差异内容：FILE_ACCESS_DENIED = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_NO_SPACE = 3 差异内容：FILE_NO_SPACE = 3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_NAME_TOO_LONG = 5 差异内容：FILE_NAME_TOO_LONG = 5 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_TOO_LARGE = 6 差异内容：FILE_TOO_LARGE = 6 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_TRANSIENT_ERROR = 10 差异内容：FILE_TRANSIENT_ERROR = 10 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_BLOCKED = 11 差异内容：FILE_BLOCKED = 11 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_TOO_SHORT = 13 差异内容：FILE_TOO_SHORT = 13 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_HASH_MISMATCH = 14 差异内容：FILE_HASH_MISMATCH = 14 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：FILE_SAME_AS_SOURCE = 15 差异内容：FILE_SAME_AS_SOURCE = 15 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：NETWORK_FAILED = 20 差异内容：NETWORK_FAILED = 20 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：NETWORK_TIMEOUT = 21 差异内容：NETWORK_TIMEOUT = 21 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：NETWORK_DISCONNECTED = 22 差异内容：NETWORK_DISCONNECTED = 22 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：NETWORK_SERVER_DOWN = 23 差异内容：NETWORK_SERVER_DOWN = 23 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：NETWORK_INVALID_REQUEST = 24 差异内容：NETWORK_INVALID_REQUEST = 24 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_FAILED = 30 差异内容：SERVER_FAILED = 30 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_NO_RANGE = 31 差异内容：SERVER_NO_RANGE = 31 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_BAD_CONTENT = 33 差异内容：SERVER_BAD_CONTENT = 33 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_UNAUTHORIZED = 34 差异内容：SERVER_UNAUTHORIZED = 34 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_CERT_PROBLEM = 35 差异内容：SERVER_CERT_PROBLEM = 35 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_FORBIDDEN = 36 差异内容：SERVER_FORBIDDEN = 36 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_UNREACHABLE = 37 差异内容：SERVER_UNREACHABLE = 37 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_CONTENT_LENGTH_MISMATCH = 38 差异内容：SERVER_CONTENT_LENGTH_MISMATCH = 38 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：SERVER_CROSS_ORIGIN_REDIRECT = 39 差异内容：SERVER_CROSS_ORIGIN_REDIRECT = 39 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：USER_CANCELED = 40 差异内容：USER_CANCELED = 40 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：USER_SHUTDOWN = 41 差异内容：USER_SHUTDOWN = 41 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadErrorCode； API声明：CRASH = 50 差异内容：CRASH = 50 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebDownloadItem 差异内容： class WebDownloadItem | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getGuid(): string; 差异内容：getGuid(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getCurrentSpeed(): number; 差异内容：getCurrentSpeed(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getPercentComplete(): number; 差异内容：getPercentComplete(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getTotalBytes(): number; 差异内容：getTotalBytes(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getState(): WebDownloadState; 差异内容：getState(): WebDownloadState; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getLastErrorCode(): WebDownloadErrorCode; 差异内容：getLastErrorCode(): WebDownloadErrorCode; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getMethod(): string; 差异内容：getMethod(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getMimeType(): string; 差异内容：getMimeType(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getUrl(): string; 差异内容：getUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getSuggestedFileName(): string; 差异内容：getSuggestedFileName(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：start(downloadPath: string): void; 差异内容：start(downloadPath: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：cancel(): void; 差异内容：cancel(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：pause(): void; 差异内容：pause(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：resume(): void; 差异内容：resume(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getReceivedBytes(): number; 差异内容：getReceivedBytes(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：getFullPath(): string; 差异内容：getFullPath(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：serialize(): Uint8Array; 差异内容：serialize(): Uint8Array; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadItem； API声明：static deserialize(serializedData: Uint8Array): WebDownloadItem; 差异内容：static deserialize(serializedData: Uint8Array): WebDownloadItem; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebDownloadDelegate 差异内容： class WebDownloadDelegate | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadDelegate； API声明：onBeforeDownload(callback: Callback<WebDownloadItem>): void; 差异内容：onBeforeDownload(callback: Callback<WebDownloadItem>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadDelegate； API声明：onDownloadUpdated(callback: Callback<WebDownloadItem>): void; 差异内容：onDownloadUpdated(callback: Callback<WebDownloadItem>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadDelegate； API声明：onDownloadFinish(callback: Callback<WebDownloadItem>): void; 差异内容：onDownloadFinish(callback: Callback<WebDownloadItem>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadDelegate； API声明：onDownloadFailed(callback: Callback<WebDownloadItem>): void; 差异内容：onDownloadFailed(callback: Callback<WebDownloadItem>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebDownloadManager 差异内容： class WebDownloadManager | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadManager； API声明：static setDownloadDelegate(delegate: WebDownloadDelegate): void; 差异内容：static setDownloadDelegate(delegate: WebDownloadDelegate): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebDownloadManager； API声明：static resumeDownload(webDownloadItem: WebDownloadItem): void; 差异内容：static resumeDownload(webDownloadItem: WebDownloadItem): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebHttpBodyStream 差异内容： class WebHttpBodyStream | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：initialize(): Promise<void>; 差异内容：initialize(): Promise<void>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：read(size: number): Promise<ArrayBuffer>; 差异内容：read(size: number): Promise<ArrayBuffer>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：getSize(): number; 差异内容：getSize(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：getPosition(): number; 差异内容：getPosition(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：isChunked(): boolean; 差异内容：isChunked(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：isEof(): boolean; 差异内容：isEof(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebHttpBodyStream； API声明：isInMemory(): boolean; 差异内容：isInMemory(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum WebResourceType 差异内容： enum WebResourceType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：MAIN_FRAME = 0 差异内容：MAIN_FRAME = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：SUB_FRAME = 1 差异内容：SUB_FRAME = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：STYLE_SHEET = 2 差异内容：STYLE_SHEET = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：SCRIPT = 3 差异内容：SCRIPT = 3 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：IMAGE = 4 差异内容：IMAGE = 4 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：FONT_RESOURCE = 5 差异内容：FONT_RESOURCE = 5 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：SUB_RESOURCE = 6 差异内容：SUB_RESOURCE = 6 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：OBJECT = 7 差异内容：OBJECT = 7 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：MEDIA = 8 差异内容：MEDIA = 8 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：WORKER = 9 差异内容：WORKER = 9 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：SHARED_WORKER = 10 差异内容：SHARED_WORKER = 10 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：PREFETCH = 11 差异内容：PREFETCH = 11 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：FAVICON = 12 差异内容：FAVICON = 12 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：XHR = 13 差异内容：XHR = 13 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：PING = 14 差异内容：PING = 14 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：SERVICE_WORKER = 15 差异内容：SERVICE_WORKER = 15 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：CSP_REPORT = 16 差异内容：CSP_REPORT = 16 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：PLUGIN_RESOURCE = 17 差异内容：PLUGIN_RESOURCE = 17 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：NAVIGATION_PRELOAD_MAIN_FRAME = 19 差异内容：NAVIGATION_PRELOAD_MAIN_FRAME = 19 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceType； API声明：NAVIGATION_PRELOAD_SUB_FRAME = 20 差异内容：NAVIGATION_PRELOAD_SUB_FRAME = 20 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebSchemeHandlerRequest 差异内容： class WebSchemeHandlerRequest | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getHeader(): Array<WebHeader>; 差异内容：getHeader(): Array<WebHeader>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getRequestUrl(): string; 差异内容：getRequestUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getRequestMethod(): string; 差异内容：getRequestMethod(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getReferrer(): string; 差异内容：getReferrer(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：isMainFrame(): boolean; 差异内容：isMainFrame(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：hasGesture(): boolean; 差异内容：hasGesture(): boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getHttpBodyStream(): WebHttpBodyStream \| null; 差异内容：getHttpBodyStream(): WebHttpBodyStream \| null; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getRequestResourceType(): WebResourceType; 差异内容：getRequestResourceType(): WebResourceType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerRequest； API声明：getFrameUrl(): string; 差异内容：getFrameUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebSchemeHandlerResponse 差异内容： class WebSchemeHandlerResponse | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setUrl(url: string): void; 差异内容：setUrl(url: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getUrl(): string; 差异内容：getUrl(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setNetErrorCode(code: WebNetErrorList): void; 差异内容：setNetErrorCode(code: WebNetErrorList): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getNetErrorCode(): WebNetErrorList; 差异内容：getNetErrorCode(): WebNetErrorList; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setStatus(code: number): void; 差异内容：setStatus(code: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getStatus(): number; 差异内容：getStatus(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setStatusText(text: string): void; 差异内容：setStatusText(text: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getStatusText(): string; 差异内容：getStatusText(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setMimeType(type: string): void; 差异内容：setMimeType(type: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getMimeType(): string; 差异内容：getMimeType(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setEncoding(encoding: string): void; 差异内容：setEncoding(encoding: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getEncoding(): string; 差异内容：getEncoding(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：setHeaderByName(name: string, value: string, overwrite: boolean): void; 差异内容：setHeaderByName(name: string, value: string, overwrite: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse； API声明：getHeaderByName(name: string): string; 差异内容：getHeaderByName(name: string): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebResourceHandler 差异内容： class WebResourceHandler | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceHandler； API声明：didReceiveResponse(response: WebSchemeHandlerResponse): void; 差异内容：didReceiveResponse(response: WebSchemeHandlerResponse): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceHandler； API声明：didReceiveResponseBody(data: ArrayBuffer): void; 差异内容：didReceiveResponseBody(data: ArrayBuffer): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceHandler； API声明：didFinish(): void; 差异内容：didFinish(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceHandler； API声明：didFail(code: WebNetErrorList): void; 差异内容：didFail(code: WebNetErrorList): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class WebSchemeHandler 差异内容： class WebSchemeHandler | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandler； API声明：onRequestStart(callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void; 差异内容：onRequestStart(callback: (request: WebSchemeHandlerRequest, handler: WebResourceHandler) => boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandler； API声明：onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void; 差异内容：onRequestStop(callback: Callback<WebSchemeHandlerRequest>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum PlaybackStatus 差异内容： enum PlaybackStatus | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PlaybackStatus； API声明：PAUSED = 0 差异内容：PAUSED = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PlaybackStatus； API声明：PLAYING 差异内容：PLAYING | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum NetworkState 差异内容： enum NetworkState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NetworkState； API声明：EMPTY = 0 差异内容：EMPTY = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NetworkState； API声明：IDLE 差异内容：IDLE | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NetworkState； API声明：LOADING 差异内容：LOADING | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NetworkState； API声明：NETWORK_ERROR 差异内容：NETWORK_ERROR | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum ReadyState 差异内容： enum ReadyState | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ReadyState； API声明：HAVE_NOTHING = 0 差异内容：HAVE_NOTHING = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ReadyState； API声明：HAVE_METADATA 差异内容：HAVE_METADATA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ReadyState； API声明：HAVE_CURRENT_DATA 差异内容：HAVE_CURRENT_DATA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ReadyState； API声明：HAVE_FUTURE_DATA 差异内容：HAVE_FUTURE_DATA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ReadyState； API声明：HAVE_ENOUGH_DATA 差异内容：HAVE_ENOUGH_DATA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum MediaError 差异内容： enum MediaError | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaError； API声明：NETWORK_ERROR = 1 差异内容：NETWORK_ERROR = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaError； API声明：FORMAT_ERROR 差异内容：FORMAT_ERROR | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaError； API声明：DECODE_ERROR 差异内容：DECODE_ERROR | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface NativeMediaPlayerHandler 差异内容： interface NativeMediaPlayerHandler | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleStatusChanged(status: PlaybackStatus): void; 差异内容：handleStatusChanged(status: PlaybackStatus): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleVolumeChanged(volume: number): void; 差异内容：handleVolumeChanged(volume: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleMutedChanged(muted: boolean): void; 差异内容：handleMutedChanged(muted: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handlePlaybackRateChanged(playbackRate: number): void; 差异内容：handlePlaybackRateChanged(playbackRate: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleDurationChanged(duration: number): void; 差异内容：handleDurationChanged(duration: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleTimeUpdate(currentPlayTime: number): void; 差异内容：handleTimeUpdate(currentPlayTime: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleBufferedEndTimeChanged(bufferedEndTime: number): void; 差异内容：handleBufferedEndTimeChanged(bufferedEndTime: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleEnded(): void; 差异内容：handleEnded(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleNetworkStateChanged(state: NetworkState): void; 差异内容：handleNetworkStateChanged(state: NetworkState): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleReadyStateChanged(state: ReadyState): void; 差异内容：handleReadyStateChanged(state: ReadyState): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleFullscreenChanged(fullscreen: boolean): void; 差异内容：handleFullscreenChanged(fullscreen: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleSeeking(): void; 差异内容：handleSeeking(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleSeekFinished(): void; 差异内容：handleSeekFinished(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleError(error: MediaError, errorMessage: string): void; 差异内容：handleError(error: MediaError, errorMessage: string): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerHandler； API声明：handleVideoSizeChanged(width: number, height: number): void; 差异内容：handleVideoSizeChanged(width: number, height: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface NativeMediaPlayerBridge 差异内容： interface NativeMediaPlayerBridge | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：updateRect(x: number, y: number, width: number, height: number): void; 差异内容：updateRect(x: number, y: number, width: number, height: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：play(): void; 差异内容：play(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：pause(): void; 差异内容：pause(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：seek(targetTime: number): void; 差异内容：seek(targetTime: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：setVolume(volume: number): void; 差异内容：setVolume(volume: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：setMuted(muted: boolean): void; 差异内容：setMuted(muted: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：setPlaybackRate(playbackRate: number): void; 差异内容：setPlaybackRate(playbackRate: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：release(): void; 差异内容：release(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：enterFullscreen(): void; 差异内容：enterFullscreen(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerBridge； API声明：exitFullscreen(): void; 差异内容：exitFullscreen(): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum MediaType 差异内容： enum MediaType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaType； API声明：VIDEO = 0 差异内容：VIDEO = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaType； API声明：AUDIO 差异内容：AUDIO | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum SourceType 差异内容： enum SourceType | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SourceType； API声明：URL = 0 差异内容：URL = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：SourceType； API声明：MSE 差异内容：MSE | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class MediaSourceInfo 差异内容： class MediaSourceInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaSourceInfo； API声明：type: SourceType; 差异内容：type: SourceType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaSourceInfo； API声明：source: string; 差异内容：source: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaSourceInfo； API声明：format: string; 差异内容：format: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： class NativeMediaPlayerSurfaceInfo 差异内容： class NativeMediaPlayerSurfaceInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerSurfaceInfo； API声明：id: string; 差异内容：id: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：NativeMediaPlayerSurfaceInfo； API声明：rect: {  x: number;  y: number;  width: number;  height: number;  }; 差异内容：rect: {  x: number;  y: number;  width: number;  height: number;  }; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： enum Preload 差异内容： enum Preload | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：Preload； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：Preload； API声明：METADATA 差异内容：METADATA | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：Preload； API声明：AUTO 差异内容：AUTO | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明： interface MediaInfo 差异内容： interface MediaInfo | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：embedID: string; 差异内容：embedID: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：mediaType: MediaType; 差异内容：mediaType: MediaType; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：mediaSrcList: MediaSourceInfo[]; 差异内容：mediaSrcList: MediaSourceInfo[]; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：surfaceInfo: NativeMediaPlayerSurfaceInfo; 差异内容：surfaceInfo: NativeMediaPlayerSurfaceInfo; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：controlsShown: boolean; 差异内容：controlsShown: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：controlList: string[]; 差异内容：controlList: string[]; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：muted: boolean; 差异内容：muted: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：posterUrl: string; 差异内容：posterUrl: string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：preload: Preload; 差异内容：preload: Preload; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：headers: Record<string, string>; 差异内容：headers: Record<string, string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：MediaInfo； API声明：attributes: Record<string, string>; 差异内容：attributes: Record<string, string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview； API声明：type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge; 差异内容：type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ClientAuthenticationHandler； API声明：confirm(authUri: string): void; 差异内容：confirm(authUri: string): void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnNavigationEntryCommittedCallback = (loadCommittedDetails: LoadCommittedDetails) => void; 差异内容：type OnNavigationEntryCommittedCallback = (loadCommittedDetails: LoadCommittedDetails) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void; 差异内容：type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void; 差异内容：type OnLargestContentfulPaintCallback = (largestContentfulPaint: LargestContentfulPaint) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void; 差异内容：type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void; 差异内容：type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean; 差异内容：type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type NativeMediaPlayerConfig = {  /**  * Should playing web media by native application instead of web player.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 12  */  enable: boolean;  /**  * The contents painted by native media player should overlay web page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 12  */  shouldOverlay: boolean; }; 差异内容：type NativeMediaPlayerConfig = {  /**  * Should playing web media by native application instead of web player.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 12  */  enable: boolean;  /**  * The contents painted by native media player should overlay web page.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 12  */  shouldOverlay: boolean; }; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnRenderProcessNotRespondingCallback = (data: RenderProcessNotRespondingData) => void; 差异内容：type OnRenderProcessNotRespondingCallback = (data: RenderProcessNotRespondingData) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnRenderProcessRespondingCallback = () => void; 差异内容：type OnRenderProcessRespondingCallback = () => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void; 差异内容：type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void; 差异内容：type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum OverScrollMode 差异内容： declare enum OverScrollMode | component/web.d.ts |
| 新增API | NA | 类名：OverScrollMode； API声明：NEVER 差异内容：NEVER | component/web.d.ts |
| 新增API | NA | 类名：OverScrollMode； API声明：ALWAYS 差异内容：ALWAYS | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum WebCaptureMode 差异内容： declare enum WebCaptureMode | component/web.d.ts |
| 新增API | NA | 类名：WebCaptureMode； API声明：HOME_SCREEN = 0 差异内容：HOME_SCREEN = 0 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum ThreatType 差异内容： declare enum ThreatType | component/web.d.ts |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_ILLEGAL = 0 差异内容：THREAT_ILLEGAL = 0 | component/web.d.ts |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_FRAUD = 1 差异内容：THREAT_FRAUD = 1 | component/web.d.ts |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_RISK = 2 差异内容：THREAT_RISK = 2 | component/web.d.ts |
| 新增API | NA | 类名：ThreatType； API声明：THREAT_WARNING = 3 差异内容：THREAT_WARNING = 3 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface WebMediaOptions 差异内容： declare interface WebMediaOptions | component/web.d.ts |
| 新增API | NA | 类名：WebMediaOptions； API声明：resumeInterval?: number; 差异内容：resumeInterval?: number; | component/web.d.ts |
| 新增API | NA | 类名：WebMediaOptions； API声明：audioExclusive?: boolean; 差异内容：audioExclusive?: boolean; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface ScreenCaptureConfig 差异内容： declare interface ScreenCaptureConfig | component/web.d.ts |
| 新增API | NA | 类名：ScreenCaptureConfig； API声明：captureMode: WebCaptureMode; 差异内容：captureMode: WebCaptureMode; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface FullScreenEnterEvent 差异内容： declare interface FullScreenEnterEvent | component/web.d.ts |
| 新增API | NA | 类名：FullScreenEnterEvent； API声明：handler: FullScreenExitHandler; 差异内容：handler: FullScreenExitHandler; | component/web.d.ts |
| 新增API | NA | 类名：FullScreenEnterEvent； API声明：videoWidth?: number; 差异内容：videoWidth?: number; | component/web.d.ts |
| 新增API | NA | 类名：FullScreenEnterEvent； API声明：videoHeight?: number; 差异内容：videoHeight?: number; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void; 差异内容：type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明：type OnContextMenuHideCallback = () => void; 差异内容：type OnContextMenuHideCallback = () => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum WebLayoutMode 差异内容： declare enum WebLayoutMode | component/web.d.ts |
| 新增API | NA | 类名：WebLayoutMode； API声明：NONE 差异内容：NONE | component/web.d.ts |
| 新增API | NA | 类名：WebLayoutMode； API声明：FIT_CONTENT 差异内容：FIT_CONTENT | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum RenderProcessNotRespondingReason 差异内容： declare enum RenderProcessNotRespondingReason | component/web.d.ts |
| 新增API | NA | 类名：RenderProcessNotRespondingReason； API声明：INPUT_TIMEOUT 差异内容：INPUT_TIMEOUT | component/web.d.ts |
| 新增API | NA | 类名：RenderProcessNotRespondingReason； API声明：NAVIGATION_COMMIT_TIMEOUT 差异内容：NAVIGATION_COMMIT_TIMEOUT | component/web.d.ts |
| 新增API | NA | 类名：ProtectedResourceType； API声明：VIDEO_CAPTURE = 'TYPE_VIDEO_CAPTURE' 差异内容：VIDEO_CAPTURE = 'TYPE_VIDEO_CAPTURE' | component/web.d.ts |
| 新增API | NA | 类名：ProtectedResourceType； API声明：AUDIO_CAPTURE = 'TYPE_AUDIO_CAPTURE' 差异内容：AUDIO_CAPTURE = 'TYPE_AUDIO_CAPTURE' | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare class ScreenCaptureHandler 差异内容： declare class ScreenCaptureHandler | component/web.d.ts |
| 新增API | NA | 类名：ScreenCaptureHandler； API声明：getOrigin(): string; 差异内容：getOrigin(): string; | component/web.d.ts |
| 新增API | NA | 类名：ScreenCaptureHandler； API声明：grant(config: ScreenCaptureConfig): void; 差异内容：grant(config: ScreenCaptureConfig): void; | component/web.d.ts |
| 新增API | NA | 类名：ScreenCaptureHandler； API声明：deny(): void; 差异内容：deny(): void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum NativeEmbedStatus 差异内容： declare enum NativeEmbedStatus | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus； API声明：CREATE = 0 差异内容：CREATE = 0 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus； API声明：UPDATE = 1 差异内容：UPDATE = 1 | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedStatus； API声明：DESTROY = 2 差异内容：DESTROY = 2 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum WebNavigationType 差异内容： declare enum WebNavigationType | component/web.d.ts |
| 新增API | NA | 类名：WebNavigationType； API声明：UNKNOWN = 0 差异内容：UNKNOWN = 0 | component/web.d.ts |
| 新增API | NA | 类名：WebNavigationType； API声明：MAIN_FRAME_NEW_ENTRY = 1 差异内容：MAIN_FRAME_NEW_ENTRY = 1 | component/web.d.ts |
| 新增API | NA | 类名：WebNavigationType； API声明：MAIN_FRAME_EXISTING_ENTRY = 2 差异内容：MAIN_FRAME_EXISTING_ENTRY = 2 | component/web.d.ts |
| 新增API | NA | 类名：WebNavigationType； API声明：NAVIGATION_TYPE_NEW_SUBFRAME = 4 差异内容：NAVIGATION_TYPE_NEW_SUBFRAME = 4 | component/web.d.ts |
| 新增API | NA | 类名：WebNavigationType； API声明：NAVIGATION_TYPE_AUTO_SUBFRAME = 5 差异内容：NAVIGATION_TYPE_AUTO_SUBFRAME = 5 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum RenderMode 差异内容： declare enum RenderMode | component/web.d.ts |
| 新增API | NA | 类名：RenderMode； API声明：ASYNC_RENDER = 0 差异内容：ASYNC_RENDER = 0 | component/web.d.ts |
| 新增API | NA | 类名：RenderMode； API声明：SYNC_RENDER = 1 差异内容：SYNC_RENDER = 1 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare enum ViewportFit 差异内容： declare enum ViewportFit | component/web.d.ts |
| 新增API | NA | 类名：ViewportFit； API声明：AUTO = 0 差异内容：AUTO = 0 | component/web.d.ts |
| 新增API | NA | 类名：ViewportFit； API声明：CONTAINS = 1 差异内容：CONTAINS = 1 | component/web.d.ts |
| 新增API | NA | 类名：ViewportFit； API声明：COVER = 2 差异内容：COVER = 2 | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare class EventResult 差异内容： declare class EventResult | component/web.d.ts |
| 新增API | NA | 类名：EventResult； API声明：setGestureEventResult(result: boolean): void; 差异内容：setGestureEventResult(result: boolean): void; | component/web.d.ts |
| 新增API | NA | 类名：WebOptions； API声明：renderMode?: RenderMode; 差异内容：renderMode?: RenderMode; | component/web.d.ts |
| 新增API | NA | 类名：WebOptions； API声明：incognitoMode?: boolean; 差异内容：incognitoMode?: boolean; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface ScriptItem 差异内容： declare interface ScriptItem | component/web.d.ts |
| 新增API | NA | 类名：ScriptItem； API声明：script: string; 差异内容：script: string; | component/web.d.ts |
| 新增API | NA | 类名：ScriptItem； API声明：scriptRules: Array<string>; 差异内容：scriptRules: Array<string>; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface LoadCommittedDetails 差异内容： declare interface LoadCommittedDetails | component/web.d.ts |
| 新增API | NA | 类名：LoadCommittedDetails； API声明：isMainFrame: boolean; 差异内容：isMainFrame: boolean; | component/web.d.ts |
| 新增API | NA | 类名：LoadCommittedDetails； API声明：isSameDocument: boolean; 差异内容：isSameDocument: boolean; | component/web.d.ts |
| 新增API | NA | 类名：LoadCommittedDetails； API声明：didReplaceEntry: boolean; 差异内容：didReplaceEntry: boolean; | component/web.d.ts |
| 新增API | NA | 类名：LoadCommittedDetails； API声明：navigationType: WebNavigationType; 差异内容：navigationType: WebNavigationType; | component/web.d.ts |
| 新增API | NA | 类名：LoadCommittedDetails； API声明：url: string; 差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface IntelligentTrackingPreventionDetails 差异内容： declare interface IntelligentTrackingPreventionDetails | component/web.d.ts |
| 新增API | NA | 类名：IntelligentTrackingPreventionDetails； API声明：host: string; 差异内容：host: string; | component/web.d.ts |
| 新增API | NA | 类名：IntelligentTrackingPreventionDetails； API声明：trackerHost: string; 差异内容：trackerHost: string; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface NativeEmbedInfo 差异内容： declare interface NativeEmbedInfo | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：id?: string; 差异内容：id?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：type?: string; 差异内容：type?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：src?: string; 差异内容：src?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：position?: Position; 差异内容：position?: Position; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：width?: number; 差异内容：width?: number; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：height?: number; 差异内容：height?: number; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：url?: string; 差异内容：url?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：tag?: string; 差异内容：tag?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedInfo； API声明：params?: Map<string, string>; 差异内容：params?: Map<string, string>; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface NativeEmbedDataInfo 差异内容： declare interface NativeEmbedDataInfo | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedDataInfo； API声明：status?: NativeEmbedStatus; 差异内容：status?: NativeEmbedStatus; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedDataInfo； API声明：surfaceId?: string; 差异内容：surfaceId?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedDataInfo； API声明：embedId?: string; 差异内容：embedId?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedDataInfo； API声明：info?: NativeEmbedInfo; 差异内容：info?: NativeEmbedInfo; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface NativeEmbedTouchInfo 差异内容： declare interface NativeEmbedTouchInfo | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedTouchInfo； API声明：embedId?: string; 差异内容：embedId?: string; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedTouchInfo； API声明：touchEvent?: TouchEvent; 差异内容：touchEvent?: TouchEvent; | component/web.d.ts |
| 新增API | NA | 类名：NativeEmbedTouchInfo； API声明：result?: EventResult; 差异内容：result?: EventResult; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface FirstMeaningfulPaint 差异内容： declare interface FirstMeaningfulPaint | component/web.d.ts |
| 新增API | NA | 类名：FirstMeaningfulPaint； API声明：navigationStartTime?: number; 差异内容：navigationStartTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：FirstMeaningfulPaint； API声明：firstMeaningfulPaintTime?: number; 差异内容：firstMeaningfulPaintTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface LargestContentfulPaint 差异内容： declare interface LargestContentfulPaint | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：navigationStartTime?: number; 差异内容：navigationStartTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：largestImagePaintTime?: number; 差异内容：largestImagePaintTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：largestTextPaintTime?: number; 差异内容：largestTextPaintTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：imageBPP?: number; 差异内容：imageBPP?: number; | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：largestImageLoadStartTime?: number; 差异内容：largestImageLoadStartTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：LargestContentfulPaint； API声明：largestImageLoadEndTime?: number; 差异内容：largestImageLoadEndTime?: number; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface RenderProcessNotRespondingData 差异内容： declare interface RenderProcessNotRespondingData | component/web.d.ts |
| 新增API | NA | 类名：RenderProcessNotRespondingData； API声明：jsStack: string; 差异内容：jsStack: string; | component/web.d.ts |
| 新增API | NA | 类名：RenderProcessNotRespondingData； API声明：pid: number; 差异内容：pid: number; | component/web.d.ts |
| 新增API | NA | 类名：RenderProcessNotRespondingData； API声明：reason: RenderProcessNotRespondingReason; 差异内容：reason: RenderProcessNotRespondingReason; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：mediaOptions(options: WebMediaOptions): WebAttribute; 差异内容：mediaOptions(options: WebMediaOptions): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：overScrollMode(mode: OverScrollMode): WebAttribute; 差异内容：overScrollMode(mode: OverScrollMode): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：metaViewport(enabled: boolean): WebAttribute; 差异内容：metaViewport(enabled: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onScreenCaptureRequest(callback: (event?: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ScreenCaptureHandler;  }) => void): WebAttribute; 差异内容：onScreenCaptureRequest(callback: (event?: {  /**  * Notifies the user of the operation behavior of the web component.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  handler: ScreenCaptureHandler;  }) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onContextMenuHide(callback: OnContextMenuHideCallback): WebAttribute; 差异内容：onContextMenuHide(callback: OnContextMenuHideCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onSslErrorEvent(callback: OnSslErrorEventCallback): WebAttribute; 差异内容：onSslErrorEvent(callback: OnSslErrorEventCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：defaultTextEncodingFormat(textEncodingFormat: string): WebAttribute; 差异内容：defaultTextEncodingFormat(textEncodingFormat: string): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：allowWindowOpenMethod(flag: boolean): WebAttribute; 差异内容：allowWindowOpenMethod(flag: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onAudioStateChanged(callback: (event: {  /**  * The audio playback status of the current page, true if playing true otherwise false  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  playing: boolean;  }) => void): WebAttribute; 差异内容：onAudioStateChanged(callback: (event: {  /**  * The audio playback status of the current page, true if playing true otherwise false  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  playing: boolean;  }) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onFirstContentfulPaint(callback: (event?: {  /**  * The time at which navigation begins, expressed in microseconds.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  navigationStartTick: number;  /**  * The time it takes to draw content for the first time from navigation, expressed in milliseconds.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  firstContentfulPaintMs: number;  }) => void): WebAttribute; 差异内容：onFirstContentfulPaint(callback: (event?: {  /**  * The time at which navigation begins, expressed in microseconds.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  navigationStartTick: number;  /**  * The time it takes to draw content for the first time from navigation, expressed in milliseconds.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  firstContentfulPaintMs: number;  }) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback): WebAttribute; 差异内容：onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback): WebAttribute; 差异内容：onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onLoadIntercept(callback: (event: {  /**  * The url of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  data: WebResourceRequest;  }) => boolean): WebAttribute; 差异内容：onLoadIntercept(callback: (event: {  /**  * The url of the event.  *  * @syscap SystemCapability.Web.Webview.Core  * @crossplatform  * @atomicservice  * @since 11  */  data: WebResourceRequest;  }) => boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onControllerAttached(callback: () => void): WebAttribute; 差异内容：onControllerAttached(callback: () => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onOverScroll(callback: (event: {  /**  * Based on the leftmost part of the page, the horizontal scroll offset is over.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  xOffset: number;  /**  * Based on the top of the page, the vertical scroll offset is over.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  yOffset: number;  }) => void): WebAttribute; 差异内容：onOverScroll(callback: (event: {  /**  * Based on the leftmost part of the page, the horizontal scroll offset is over.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  xOffset: number;  /**  * Based on the top of the page, the vertical scroll offset is over.  *  * @syscap SystemCapability.Web.Webview.Core  * @atomicservice  * @since 11  */  yOffset: number;  }) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback): WebAttribute; 差异内容：onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback): WebAttribute; 差异内容：onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback): WebAttribute; 差异内容：onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：javaScriptOnDocumentStart(scripts: Array<ScriptItem>): WebAttribute; 差异内容：javaScriptOnDocumentStart(scripts: Array<ScriptItem>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：javaScriptOnDocumentEnd(scripts: Array<ScriptItem>): WebAttribute; 差异内容：javaScriptOnDocumentEnd(scripts: Array<ScriptItem>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：layoutMode(mode: WebLayoutMode): WebAttribute; 差异内容：layoutMode(mode: WebLayoutMode): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：nestedScroll(value: NestedScrollOptions): WebAttribute; 差异内容：nestedScroll(value: NestedScrollOptions): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：enableNativeEmbedMode(mode: boolean): WebAttribute; 差异内容：enableNativeEmbedMode(mode: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：registerNativeEmbedRule(tag: string, type: string): WebAttribute; 差异内容：registerNativeEmbedRule(tag: string, type: string): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void): WebAttribute; 差异内容：onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void): WebAttribute; 差异内容：onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：copyOptions(value: CopyOptions): WebAttribute; 差异内容：copyOptions(value: CopyOptions): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback): WebAttribute; 差异内容：onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：textAutosizing(textAutosizing: boolean): WebAttribute; 差异内容：textAutosizing(textAutosizing: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：enableNativeMediaPlayer(config: NativeMediaPlayerConfig): WebAttribute; 差异内容：enableNativeMediaPlayer(config: NativeMediaPlayerConfig): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback): WebAttribute; 差异内容：onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onRenderProcessResponding(callback: OnRenderProcessRespondingCallback): WebAttribute; 差异内容：onRenderProcessResponding(callback: OnRenderProcessRespondingCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>): WebAttribute; 差异内容：selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute； API声明：onViewportFitChanged(callback: OnViewportFitChangedCallback): WebAttribute; 差异内容：onViewportFitChanged(callback: OnViewportFitChangedCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface SslErrorEvent 差异内容： declare interface SslErrorEvent | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：handler: SslErrorHandler; 差异内容：handler: SslErrorHandler; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：error: SslError; 差异内容：error: SslError; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：url: string; 差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：originalUrl: string; 差异内容：originalUrl: string; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：referrer: string; 差异内容：referrer: string; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：isFatalError: boolean; 差异内容：isFatalError: boolean; | component/web.d.ts |
| 新增API | NA | 类名：SslErrorEvent； API声明：isMainFrame: boolean; 差异内容：isMainFrame: boolean; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： declare interface ExpandedMenuItemOptions 差异内容： declare interface ExpandedMenuItemOptions | component/web.d.ts |
| 新增API | NA | 类名：ExpandedMenuItemOptions； API声明：content: ResourceStr; 差异内容：content: ResourceStr; | component/web.d.ts |
| 新增API | NA | 类名：ExpandedMenuItemOptions； API声明：startIcon?: ResourceStr; 差异内容：startIcon?: ResourceStr; | component/web.d.ts |
| 新增API | NA | 类名：ExpandedMenuItemOptions； API声明：action: (selectedText: {  plainText: string;  }) => void; 差异内容：action: (selectedText: {  plainText: string;  }) => void; | component/web.d.ts |
| 新增API | NA | 类名：global； API声明： export declare enum WebNetErrorList 差异内容： export declare enum WebNetErrorList | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：NET_OK = 0 差异内容：NET_OK = 0 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_IO_PENDING = -1 差异内容：ERR_IO_PENDING = -1 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FAILED = -2 差异内容：ERR_FAILED = -2 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ABORTED = -3 差异内容：ERR_ABORTED = -3 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_ARGUMENT = -4 差异内容：ERR_INVALID_ARGUMENT = -4 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_HANDLE = -5 差异内容：ERR_INVALID_HANDLE = -5 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_NOT_FOUND = -6 差异内容：ERR_FILE_NOT_FOUND = -6 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TIMED_OUT = -7 差异内容：ERR_TIMED_OUT = -7 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_TOO_LARGE = -8 差异内容：ERR_FILE_TOO_LARGE = -8 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNEXPECTED = -9 差异内容：ERR_UNEXPECTED = -9 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ACCESS_DENIED = -10 差异内容：ERR_ACCESS_DENIED = -10 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NOT_IMPLEMENTED = -11 差异内容：ERR_NOT_IMPLEMENTED = -11 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INSUFFICIENT_RESOURCES = -12 差异内容：ERR_INSUFFICIENT_RESOURCES = -12 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_OUT_OF_MEMORY = -13 差异内容：ERR_OUT_OF_MEMORY = -13 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UPLOAD_FILE_CHANGED = -14 差异内容：ERR_UPLOAD_FILE_CHANGED = -14 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_NOT_CONNECTED = -15 差异内容：ERR_SOCKET_NOT_CONNECTED = -15 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_EXISTS = -16 差异内容：ERR_FILE_EXISTS = -16 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_PATH_TOO_LONG = -17 差异内容：ERR_FILE_PATH_TOO_LONG = -17 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_NO_SPACE = -18 差异内容：ERR_FILE_NO_SPACE = -18 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FILE_VIRUS_INFECTED = -19 差异内容：ERR_FILE_VIRUS_INFECTED = -19 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BLOCKED_BY_CLIENT = -20 差异内容：ERR_BLOCKED_BY_CLIENT = -20 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NETWORK_CHANGED = -21 差异内容：ERR_NETWORK_CHANGED = -21 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BLOCKED_BY_ADMINISTRATOR = -22 差异内容：ERR_BLOCKED_BY_ADMINISTRATOR = -22 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_CONNECTED = -23 差异内容：ERR_SOCKET_CONNECTED = -23 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UPLOAD_STREAM_REWIND_NOT_SUPPORTED = -25 差异内容：ERR_UPLOAD_STREAM_REWIND_NOT_SUPPORTED = -25 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONTEXT_SHUT_DOWN = -26 差异内容：ERR_CONTEXT_SHUT_DOWN = -26 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BLOCKED_BY_RESPONSE = -27 差异内容：ERR_BLOCKED_BY_RESPONSE = -27 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CLEARTEXT_NOT_PERMITTED = -29 差异内容：ERR_CLEARTEXT_NOT_PERMITTED = -29 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BLOCKED_BY_CSP = -30 差异内容：ERR_BLOCKED_BY_CSP = -30 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_H2_OR_QUIC_REQUIRED = -31 差异内容：ERR_H2_OR_QUIC_REQUIRED = -31 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BLOCKED_BY_ORB = -32 差异内容：ERR_BLOCKED_BY_ORB = -32 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_CLOSED = -100 差异内容：ERR_CONNECTION_CLOSED = -100 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_RESET = -101 差异内容：ERR_CONNECTION_RESET = -101 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_REFUSED = -102 差异内容：ERR_CONNECTION_REFUSED = -102 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_ABORTED = -103 差异内容：ERR_CONNECTION_ABORTED = -103 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_FAILED = -104 差异内容：ERR_CONNECTION_FAILED = -104 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NAME_NOT_RESOLVED = -105 差异内容：ERR_NAME_NOT_RESOLVED = -105 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INTERNET_DISCONNECTED = -106 差异内容：ERR_INTERNET_DISCONNECTED = -106 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_PROTOCOL_ERROR = -107 差异内容：ERR_SSL_PROTOCOL_ERROR = -107 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ADDRESS_INVALID = -108 差异内容：ERR_ADDRESS_INVALID = -108 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ADDRESS_UNREACHABLE = -109 差异内容：ERR_ADDRESS_UNREACHABLE = -109 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_CERT_NEEDED = -110 差异内容：ERR_SSL_CLIENT_AUTH_CERT_NEEDED = -110 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TUNNEL_CONNECTION_FAILED = -111 差异内容：ERR_TUNNEL_CONNECTION_FAILED = -111 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NO_SSL_VERSIONS_ENABLED = -112 差异内容：ERR_NO_SSL_VERSIONS_ENABLED = -112 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_VERSION_OR_CIPHER_MISMATCH = -113 差异内容：ERR_SSL_VERSION_OR_CIPHER_MISMATCH = -113 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_RENEGOTIATION_REQUESTED = -114 差异内容：ERR_SSL_RENEGOTIATION_REQUESTED = -114 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_AUTH_UNSUPPORTED = -115 差异内容：ERR_PROXY_AUTH_UNSUPPORTED = -115 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_BAD_SSL_CLIENT_AUTH_CERT = -117 差异内容：ERR_BAD_SSL_CLIENT_AUTH_CERT = -117 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONNECTION_TIMED_OUT = -118 差异内容：ERR_CONNECTION_TIMED_OUT = -118 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HOST_RESOLVER_QUEUE_TOO_LARGE = -119 差异内容：ERR_HOST_RESOLVER_QUEUE_TOO_LARGE = -119 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKS_CONNECTION_FAILED = -120 差异内容：ERR_SOCKS_CONNECTION_FAILED = -120 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKS_CONNECTION_HOST_UNREACHABLE = -121 差异内容：ERR_SOCKS_CONNECTION_HOST_UNREACHABLE = -121 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ALPN_NEGOTIATION_FAILED = -122 差异内容：ERR_ALPN_NEGOTIATION_FAILED = -122 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_NO_RENEGOTIATION = -123 差异内容：ERR_SSL_NO_RENEGOTIATION = -123 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_WINSOCK_UNEXPECTED_WRITTEN_BYTES = -124 差异内容：ERR_WINSOCK_UNEXPECTED_WRITTEN_BYTES = -124 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_DECOMPRESSION_FAILURE_ALERT = -125 差异内容：ERR_SSL_DECOMPRESSION_FAILURE_ALERT = -125 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_BAD_RECORD_MAC_ALERT = -126 差异内容：ERR_SSL_BAD_RECORD_MAC_ALERT = -126 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_AUTH_REQUESTED = -127 差异内容：ERR_PROXY_AUTH_REQUESTED = -127 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_CONNECTION_FAILED = -130 差异内容：ERR_PROXY_CONNECTION_FAILED = -130 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_MANDATORY_PROXY_CONFIGURATION_FAILED = -131 差异内容：ERR_MANDATORY_PROXY_CONFIGURATION_FAILED = -131 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PRECONNECT_MAX_SOCKET_LIMIT = -133 差异内容：ERR_PRECONNECT_MAX_SOCKET_LIMIT = -133 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_PRIVATE_KEY_ACCESS_DENIED = -134 差异内容：ERR_SSL_CLIENT_AUTH_PRIVATE_KEY_ACCESS_DENIED = -134 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_CERT_NO_PRIVATE_KEY = -135 差异内容：ERR_SSL_CLIENT_AUTH_CERT_NO_PRIVATE_KEY = -135 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_CERTIFICATE_INVALID = -136 差异内容：ERR_PROXY_CERTIFICATE_INVALID = -136 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NAME_RESOLUTION_FAILED = -137 差异内容：ERR_NAME_RESOLUTION_FAILED = -137 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NETWORK_ACCESS_DENIED = -138 差异内容：ERR_NETWORK_ACCESS_DENIED = -138 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TEMPORARILY_THROTTLED = -139 差异内容：ERR_TEMPORARILY_THROTTLED = -139 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTPS_PROXY_TUNNEL_RESPONSE_REDIRECT = -140 差异内容：ERR_HTTPS_PROXY_TUNNEL_RESPONSE_REDIRECT = -140 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_SIGNATURE_FAILED = -141 差异内容：ERR_SSL_CLIENT_AUTH_SIGNATURE_FAILED = -141 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_MSG_TOO_BIG = -142 差异内容：ERR_MSG_TOO_BIG = -142 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_WS_PROTOCOL_ERROR = -145 差异内容：ERR_WS_PROTOCOL_ERROR = -145 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ADDRESS_IN_USE = -147 差异内容：ERR_ADDRESS_IN_USE = -147 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_HANDSHAKE_NOT_COMPLETED = -148 差异内容：ERR_SSL_HANDSHAKE_NOT_COMPLETED = -148 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_BAD_PEER_PUBLIC_KEY = -149 差异内容：ERR_SSL_BAD_PEER_PUBLIC_KEY = -149 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_PINNED_KEY_NOT_IN_CERT_CHAIN = -150 差异内容：ERR_SSL_PINNED_KEY_NOT_IN_CERT_CHAIN = -150 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CLIENT_AUTH_CERT_TYPE_UNSUPPORTED = -151 差异内容：ERR_CLIENT_AUTH_CERT_TYPE_UNSUPPORTED = -151 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_DECRYPT_ERROR_ALERT = -153 差异内容：ERR_SSL_DECRYPT_ERROR_ALERT = -153 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_WS_THROTTLE_QUEUE_TOO_LARGE = -154 差异内容：ERR_WS_THROTTLE_QUEUE_TOO_LARGE = -154 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_SERVER_CERT_CHANGED = -156 差异内容：ERR_SSL_SERVER_CERT_CHANGED = -156 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_UNRECOGNIZED_NAME_ALERT = -159 差异内容：ERR_SSL_UNRECOGNIZED_NAME_ALERT = -159 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_SET_RECEIVE_BUFFER_SIZE_ERROR = -160 差异内容：ERR_SOCKET_SET_RECEIVE_BUFFER_SIZE_ERROR = -160 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_SET_SEND_BUFFER_SIZE_ERROR = -161 差异内容：ERR_SOCKET_SET_SEND_BUFFER_SIZE_ERROR = -161 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_RECEIVE_BUFFER_SIZE_UNCHANGEABLE = -162 差异内容：ERR_SOCKET_RECEIVE_BUFFER_SIZE_UNCHANGEABLE = -162 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SOCKET_SEND_BUFFER_SIZE_UNCHANGEABLE = -163 差异内容：ERR_SOCKET_SEND_BUFFER_SIZE_UNCHANGEABLE = -163 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_CERT_BAD_FORMAT = -164 差异内容：ERR_SSL_CLIENT_AUTH_CERT_BAD_FORMAT = -164 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ICANN_NAME_COLLISION = -166 差异内容：ERR_ICANN_NAME_COLLISION = -166 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_SERVER_CERT_BAD_FORMAT = -167 差异内容：ERR_SSL_SERVER_CERT_BAD_FORMAT = -167 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CT_STH_PARSING_FAILED = -168 差异内容：ERR_CT_STH_PARSING_FAILED = -168 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CT_STH_INCOMPLETE = -169 差异内容：ERR_CT_STH_INCOMPLETE = -169 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNABLE_TO_REUSE_CONNECTION_FOR_PROXY_AUTH = -170 差异内容：ERR_UNABLE_TO_REUSE_CONNECTION_FOR_PROXY_AUTH = -170 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CT_CONSISTENCY_PROOF_PARSING_FAILED = -171 差异内容：ERR_CT_CONSISTENCY_PROOF_PARSING_FAILED = -171 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_OBSOLETE_CIPHER = -172 差异内容：ERR_SSL_OBSOLETE_CIPHER = -172 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_WS_UPGRADE = -173 差异内容：ERR_WS_UPGRADE = -173 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_READ_IF_READY_NOT_IMPLEMENTED = -174 差异内容：ERR_READ_IF_READY_NOT_IMPLEMENTED = -174 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NO_BUFFER_SPACE = -176 差异内容：ERR_NO_BUFFER_SPACE = -176 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_CLIENT_AUTH_NO_COMMON_ALGORITHMS = -177 差异内容：ERR_SSL_CLIENT_AUTH_NO_COMMON_ALGORITHMS = -177 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_EARLY_DATA_REJECTED = -178 差异内容：ERR_EARLY_DATA_REJECTED = -178 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_WRONG_VERSION_ON_EARLY_DATA = -179 差异内容：ERR_WRONG_VERSION_ON_EARLY_DATA = -179 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TLS13_DOWNGRADE_DETECTED = -180 差异内容：ERR_TLS13_DOWNGRADE_DETECTED = -180 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_KEY_USAGE_INCOMPATIBLE = -181 差异内容：ERR_SSL_KEY_USAGE_INCOMPATIBLE = -181 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_ECH_CONFIG_LIST = -182 差异内容：ERR_INVALID_ECH_CONFIG_LIST = -182 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ECH_NOT_NEGOTIATED = -183 差异内容：ERR_ECH_NOT_NEGOTIATED = -183 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ECH_FALLBACK_CERTIFICATE_INVALID = -184 差异内容：ERR_ECH_FALLBACK_CERTIFICATE_INVALID = -184 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_COMMON_NAME_INVALID = -200 差异内容：ERR_CERT_COMMON_NAME_INVALID = -200 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_DATE_INVALID = -201 差异内容：ERR_CERT_DATE_INVALID = -201 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_AUTHORITY_INVALID = -202 差异内容：ERR_CERT_AUTHORITY_INVALID = -202 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_CONTAINS_ERRORS = -203 差异内容：ERR_CERT_CONTAINS_ERRORS = -203 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_NO_REVOCATION_MECHANISM = -204 差异内容：ERR_CERT_NO_REVOCATION_MECHANISM = -204 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_UNABLE_TO_CHECK_REVOCATION = -205 差异内容：ERR_CERT_UNABLE_TO_CHECK_REVOCATION = -205 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_REVOKED = -206 差异内容：ERR_CERT_REVOKED = -206 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_INVALID = -207 差异内容：ERR_CERT_INVALID = -207 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_WEAK_SIGNATURE_ALGORITHM = -208 差异内容：ERR_CERT_WEAK_SIGNATURE_ALGORITHM = -208 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_NON_UNIQUE_NAME = -210 差异内容：ERR_CERT_NON_UNIQUE_NAME = -210 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_WEAK_KEY = -211 差异内容：ERR_CERT_WEAK_KEY = -211 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_NAME_CONSTRAINT_VIOLATION = -212 差异内容：ERR_CERT_NAME_CONSTRAINT_VIOLATION = -212 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_VALIDITY_TOO_LONG = -213 差异内容：ERR_CERT_VALIDITY_TOO_LONG = -213 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERTIFICATE_TRANSPARENCY_REQUIRED = -214 差异内容：ERR_CERTIFICATE_TRANSPARENCY_REQUIRED = -214 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_SYMANTEC_LEGACY = -215 差异内容：ERR_CERT_SYMANTEC_LEGACY = -215 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_KNOWN_INTERCEPTION_BLOCKED = -217 差异内容：ERR_CERT_KNOWN_INTERCEPTION_BLOCKED = -217 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SSL_OBSOLETE_VERSION_OR_CIPHER = -218 差异内容：ERR_SSL_OBSOLETE_VERSION_OR_CIPHER = -218 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_END = -219 差异内容：ERR_CERT_END = -219 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_URL = -300 差异内容：ERR_INVALID_URL = -300 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DISALLOWED_URL_SCHEME = -301 差异内容：ERR_DISALLOWED_URL_SCHEME = -301 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNKNOWN_URL_SCHEME = -302 差异内容：ERR_UNKNOWN_URL_SCHEME = -302 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_REDIRECT = -303 差异内容：ERR_INVALID_REDIRECT = -303 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TOO_MANY_REDIRECTS = -310 差异内容：ERR_TOO_MANY_REDIRECTS = -310 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNSAFE_REDIRECT = -311 差异内容：ERR_UNSAFE_REDIRECT = -311 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNSAFE_PORT = -312 差异内容：ERR_UNSAFE_PORT = -312 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_RESPONSE = -320 差异内容：ERR_INVALID_RESPONSE = -320 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_CHUNKED_ENCODING = -321 差异内容：ERR_INVALID_CHUNKED_ENCODING = -321 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_METHOD_UNSUPPORTED = -322 差异内容：ERR_METHOD_UNSUPPORTED = -322 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNEXPECTED_PROXY_AUTH = -323 差异内容：ERR_UNEXPECTED_PROXY_AUTH = -323 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_EMPTY_RESPONSE = -324 差异内容：ERR_EMPTY_RESPONSE = -324 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_HEADERS_TOO_BIG = -325 差异内容：ERR_RESPONSE_HEADERS_TOO_BIG = -325 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PAC_SCRIPT_FAILED = -327 差异内容：ERR_PAC_SCRIPT_FAILED = -327 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_REQUEST_RANGE_NOT_SATISFIABLE = -328 差异内容：ERR_REQUEST_RANGE_NOT_SATISFIABLE = -328 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_MALFORMED_IDENTITY = -329 差异内容：ERR_MALFORMED_IDENTITY = -329 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONTENT_DECODING_FAILED = -330 差异内容：ERR_CONTENT_DECODING_FAILED = -330 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NETWORK_IO_SUSPENDED = -331 差异内容：ERR_NETWORK_IO_SUSPENDED = -331 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SYN_REPLY_NOT_RECEIVED = -332 差异内容：ERR_SYN_REPLY_NOT_RECEIVED = -332 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ENCODING_CONVERSION_FAILED = -333 差异内容：ERR_ENCODING_CONVERSION_FAILED = -333 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNRECOGNIZED_FTP_DIRECTORY_LISTING_FORMAT = -334 差异内容：ERR_UNRECOGNIZED_FTP_DIRECTORY_LISTING_FORMAT = -334 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NO_SUPPORTED_PROXIES = -336 差异内容：ERR_NO_SUPPORTED_PROXIES = -336 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_PROTOCOL_ERROR = -337 差异内容：ERR_HTTP2_PROTOCOL_ERROR = -337 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_AUTH_CREDENTIALS = -338 差异内容：ERR_INVALID_AUTH_CREDENTIALS = -338 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNSUPPORTED_AUTH_SCHEME = -339 差异内容：ERR_UNSUPPORTED_AUTH_SCHEME = -339 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ENCODING_DETECTION_FAILED = -340 差异内容：ERR_ENCODING_DETECTION_FAILED = -340 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_MISSING_AUTH_CREDENTIALS = -341 差异内容：ERR_MISSING_AUTH_CREDENTIALS = -341 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNEXPECTED_SECURITY_LIBRARY_STATUS = -342 差异内容：ERR_UNEXPECTED_SECURITY_LIBRARY_STATUS = -342 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_MISCONFIGURED_AUTH_ENVIRONMENT = -343 差异内容：ERR_MISCONFIGURED_AUTH_ENVIRONMENT = -343 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_UNDOCUMENTED_SECURITY_LIBRARY_STATUS = -344 差异内容：ERR_UNDOCUMENTED_SECURITY_LIBRARY_STATUS = -344 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_BODY_TOO_BIG_TO_DRAIN = -345 差异内容：ERR_RESPONSE_BODY_TOO_BIG_TO_DRAIN = -345 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_LENGTH = -346 差异内容：ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_LENGTH = -346 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INCOMPLETE_HTTP2_HEADERS = -347 差异内容：ERR_INCOMPLETE_HTTP2_HEADERS = -347 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PAC_NOT_IN_DHCP = -348 差异内容：ERR_PAC_NOT_IN_DHCP = -348 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION = -349 差异内容：ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION = -349 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_HEADERS_MULTIPLE_LOCATION = -350 差异内容：ERR_RESPONSE_HEADERS_MULTIPLE_LOCATION = -350 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_SERVER_REFUSED_STREAM = -351 差异内容：ERR_HTTP2_SERVER_REFUSED_STREAM = -351 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_PING_FAILED = -352 差异内容：ERR_HTTP2_PING_FAILED = -352 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONTENT_LENGTH_MISMATCH = -354 差异内容：ERR_CONTENT_LENGTH_MISMATCH = -354 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INCOMPLETE_CHUNKED_ENCODING = -355 差异内容：ERR_INCOMPLETE_CHUNKED_ENCODING = -355 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_QUIC_PROTOCOL_ERROR = -356 差异内容：ERR_QUIC_PROTOCOL_ERROR = -356 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_RESPONSE_HEADERS_TRUNCATED = -357 差异内容：ERR_RESPONSE_HEADERS_TRUNCATED = -357 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_QUIC_HANDSHAKE_FAILED = -358 差异内容：ERR_QUIC_HANDSHAKE_FAILED = -358 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_INADEQUATE_TRANSPORT_SECURITY = -360 差异内容：ERR_HTTP2_INADEQUATE_TRANSPORT_SECURITY = -360 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_FLOW_CONTROL_ERROR = -361 差异内容：ERR_HTTP2_FLOW_CONTROL_ERROR = -361 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_FRAME_SIZE_ERROR = -362 差异内容：ERR_HTTP2_FRAME_SIZE_ERROR = -362 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_COMPRESSION_ERROR = -363 差异内容：ERR_HTTP2_COMPRESSION_ERROR = -363 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_AUTH_REQUESTED_WITH_NO_CONNECTION = -364 差异内容：ERR_PROXY_AUTH_REQUESTED_WITH_NO_CONNECTION = -364 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP_1_1_REQUIRED = -365 差异内容：ERR_HTTP_1_1_REQUIRED = -365 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PROXY_HTTP_1_1_REQUIRED = -366 差异内容：ERR_PROXY_HTTP_1_1_REQUIRED = -366 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PAC_SCRIPT_TERMINATED = -367 差异内容：ERR_PAC_SCRIPT_TERMINATED = -367 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_HTTP_RESPONSE = -370 差异内容：ERR_INVALID_HTTP_RESPONSE = -370 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CONTENT_DECODING_INIT_FAILED = -371 差异内容：ERR_CONTENT_DECODING_INIT_FAILED = -371 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_RST_STREAM_NO_ERROR_RECEIVED = -372 差异内容：ERR_HTTP2_RST_STREAM_NO_ERROR_RECEIVED = -372 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_PUSHED_STREAM_NOT_AVAILABLE = -373 差异内容：ERR_HTTP2_PUSHED_STREAM_NOT_AVAILABLE = -373 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_CLAIMED_PUSHED_STREAM_RESET_BY_SERVER = -374 差异内容：ERR_HTTP2_CLAIMED_PUSHED_STREAM_RESET_BY_SERVER = -374 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TOO_MANY_RETRIES = -375 差异内容：ERR_TOO_MANY_RETRIES = -375 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_STREAM_CLOSED = -376 差异内容：ERR_HTTP2_STREAM_CLOSED = -376 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_CLIENT_REFUSED_STREAM = -377 差异内容：ERR_HTTP2_CLIENT_REFUSED_STREAM = -377 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP2_PUSHED_RESPONSE_DOES_NOT_MATCH = -378 差异内容：ERR_HTTP2_PUSHED_RESPONSE_DOES_NOT_MATCH = -378 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_HTTP_RESPONSE_CODE_FAILURE = -379 差异内容：ERR_HTTP_RESPONSE_CODE_FAILURE = -379 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_QUIC_UNKNOWN_CERT_ROOT = -380 差异内容：ERR_QUIC_UNKNOWN_CERT_ROOT = -380 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_QUIC_GOAWAY_REQUEST_CAN_BE_RETRIED = -381 差异内容：ERR_QUIC_GOAWAY_REQUEST_CAN_BE_RETRIED = -381 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TOO_MANY_ACCEPT_CH_RESTARTS = -382 差异内容：ERR_TOO_MANY_ACCEPT_CH_RESTARTS = -382 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INCONSISTENT_IP_ADDRESS_SPACE = -383 差异内容：ERR_INCONSISTENT_IP_ADDRESS_SPACE = -383 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHED_IP_ADDRESS_SPACE_BLOCKED_BY_LOCAL_NETWORK_ACCESS_POLICY = -384 差异内容：ERR_CACHED_IP_ADDRESS_SPACE_BLOCKED_BY_LOCAL_NETWORK_ACCESS_POLICY = -384 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_MISS = -400 差异内容：ERR_CACHE_MISS = -400 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_READ_FAILURE = -401 差异内容：ERR_CACHE_READ_FAILURE = -401 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_WRITE_FAILURE = -402 差异内容：ERR_CACHE_WRITE_FAILURE = -402 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_OPERATION_UNSUPPORTED = -403 差异内容：ERR_CACHE_OPERATION_UNSUPPORTED = -403 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_OPEN_FAILURE = -404 差异内容：ERR_CACHE_OPEN_FAILURE = -404 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_CREATE_FAILURE = -405 差异内容：ERR_CACHE_CREATE_FAILURE = -405 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_RACE = -406 差异内容：ERR_CACHE_RACE = -406 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_CHECKSUM_READ_FAILURE = -407 差异内容：ERR_CACHE_CHECKSUM_READ_FAILURE = -407 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_CHECKSUM_MISMATCH = -408 差异内容：ERR_CACHE_CHECKSUM_MISMATCH = -408 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_LOCK_TIMEOUT = -409 差异内容：ERR_CACHE_LOCK_TIMEOUT = -409 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_AUTH_FAILURE_AFTER_READ = -410 差异内容：ERR_CACHE_AUTH_FAILURE_AFTER_READ = -410 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_ENTRY_NOT_SUITABLE = -411 差异内容：ERR_CACHE_ENTRY_NOT_SUITABLE = -411 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_DOOM_FAILURE = -412 差异内容：ERR_CACHE_DOOM_FAILURE = -412 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CACHE_OPEN_OR_CREATE_FAILURE = -413 差异内容：ERR_CACHE_OPEN_OR_CREATE_FAILURE = -413 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INSECURE_RESPONSE = -501 差异内容：ERR_INSECURE_RESPONSE = -501 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_NO_PRIVATE_KEY_FOR_CERT = -502 差异内容：ERR_NO_PRIVATE_KEY_FOR_CERT = -502 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_ADD_USER_CERT_FAILED = -503 差异内容：ERR_ADD_USER_CERT_FAILED = -503 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_SIGNED_EXCHANGE = -504 差异内容：ERR_INVALID_SIGNED_EXCHANGE = -504 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_INVALID_WEB_BUNDLE = -505 差异内容：ERR_INVALID_WEB_BUNDLE = -505 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TRUST_TOKEN_OPERATION_FAILED = -506 差异内容：ERR_TRUST_TOKEN_OPERATION_FAILED = -506 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_TRUST_TOKEN_OPERATION_SUCCESS_WITHOUT_SENDING_REQUEST = -507 差异内容：ERR_TRUST_TOKEN_OPERATION_SUCCESS_WITHOUT_SENDING_REQUEST = -507 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_FAILED = -601 差异内容：ERR_FTP_FAILED = -601 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_SERVICE_UNAVAILABLE = -602 差异内容：ERR_FTP_SERVICE_UNAVAILABLE = -602 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_TRANSFER_ABORTED = -603 差异内容：ERR_FTP_TRANSFER_ABORTED = -603 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_FILE_BUSY = -604 差异内容：ERR_FTP_FILE_BUSY = -604 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_SYNTAX_ERROR = -605 差异内容：ERR_FTP_SYNTAX_ERROR = -605 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_COMMAND_UNSUPPORTED = -606 差异内容：ERR_FTP_COMMAND_UNSUPPORTED = -606 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_FTP_BAD_COMMAND_SEQUENCE = -607 差异内容：ERR_FTP_BAD_COMMAND_SEQUENCE = -607 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PKCS12_IMPORT_BAD_PASSWORD = -701 差异内容：ERR_PKCS12_IMPORT_BAD_PASSWORD = -701 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PKCS12_IMPORT_FAILED = -702 差异内容：ERR_PKCS12_IMPORT_FAILED = -702 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_IMPORT_CA_CERT_NOT_CA = -703 差异内容：ERR_IMPORT_CA_CERT_NOT_CA = -703 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_IMPORT_CERT_ALREADY_EXISTS = -704 差异内容：ERR_IMPORT_CERT_ALREADY_EXISTS = -704 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_IMPORT_CA_CERT_FAILED = -705 差异内容：ERR_IMPORT_CA_CERT_FAILED = -705 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_IMPORT_SERVER_CERT_FAILED = -706 差异内容：ERR_IMPORT_SERVER_CERT_FAILED = -706 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PKCS12_IMPORT_INVALID_MAC = -707 差异内容：ERR_PKCS12_IMPORT_INVALID_MAC = -707 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PKCS12_IMPORT_INVALID_FILE = -708 差异内容：ERR_PKCS12_IMPORT_INVALID_FILE = -708 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PKCS12_IMPORT_UNSUPPORTED = -709 差异内容：ERR_PKCS12_IMPORT_UNSUPPORTED = -709 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_KEY_GENERATION_FAILED = -710 差异内容：ERR_KEY_GENERATION_FAILED = -710 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_PRIVATE_KEY_EXPORT_FAILED = -712 差异内容：ERR_PRIVATE_KEY_EXPORT_FAILED = -712 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_SELF_SIGNED_CERT_GENERATION_FAILED = -713 差异内容：ERR_SELF_SIGNED_CERT_GENERATION_FAILED = -713 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_DATABASE_CHANGED = -714 差异内容：ERR_CERT_DATABASE_CHANGED = -714 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_CERT_VERIFIER_CHANGED = -716 差异内容：ERR_CERT_VERIFIER_CHANGED = -716 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_MALFORMED_RESPONSE = -800 差异内容：ERR_DNS_MALFORMED_RESPONSE = -800 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_SERVER_REQUIRES_TCP = -801 差异内容：ERR_DNS_SERVER_REQUIRES_TCP = -801 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_SERVER_FAILED = -802 差异内容：ERR_DNS_SERVER_FAILED = -802 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_TIMED_OUT = -803 差异内容：ERR_DNS_TIMED_OUT = -803 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_CACHE_MISS = -804 差异内容：ERR_DNS_CACHE_MISS = -804 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_SEARCH_EMPTY = -805 差异内容：ERR_DNS_SEARCH_EMPTY = -805 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_SORT_ERROR = -806 差异内容：ERR_DNS_SORT_ERROR = -806 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_SECURE_RESOLVER_HOSTNAME_RESOLUTION_FAILED = -808 差异内容：ERR_DNS_SECURE_RESOLVER_HOSTNAME_RESOLUTION_FAILED = -808 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_NAME_HTTPS_ONLY = -809 差异内容：ERR_DNS_NAME_HTTPS_ONLY = -809 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_REQUEST_CANCELED = -810 差异内容：ERR_DNS_REQUEST_CANCELED = -810 | api/@ohos.web.netErrorList.d.ts |
| 新增API | NA | 类名：WebNetErrorList； API声明：ERR_DNS_NO_MATCHING_SUPPORTED_ALPN = -811 差异内容：ERR_DNS_NO_MATCHING_SUPPORTED_ALPN = -811 | api/@ohos.web.netErrorList.d.ts |
