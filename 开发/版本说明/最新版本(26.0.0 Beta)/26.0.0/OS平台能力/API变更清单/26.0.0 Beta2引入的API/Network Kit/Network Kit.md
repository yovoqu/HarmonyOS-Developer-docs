# Network Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;HttpResponse&gt;): void; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：NA | 类名：HttpRequest； API声明：request(url: string, options?: HttpRequestOptions): Promise&lt;HttpResponse&gt;; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestSync(url: string, options?: HttpRequestOptions): HttpResponse; 差异内容：NA | 类名：HttpRequest； API声明：requestSync(url: string, options?: HttpRequestOptions): HttpResponse; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback&lt;number&gt;): void; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：HttpRequest； API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise&lt;number&gt;; 差异内容：NA | 类名：HttpRequest； API声明：requestInStream(url: string, options?: HttpRequestOptions): Promise&lt;number&gt;; 差异内容：2300996 | api/@ohos.net.http.d.ts |
| 新增错误码 | 类名：statistics； API声明：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：statistics； API声明：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics； API声明：function getUidRxBytes(uid: number): Promise&lt;number&gt;; 差异内容：NA | 类名：statistics； API声明：function getUidRxBytes(uid: number): Promise&lt;number&gt;; 差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics； API声明：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：statistics； API声明：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：201 | api/@ohos.net.statistics.d.ts |
| 新增错误码 | 类名：statistics； API声明：function getUidTxBytes(uid: number): Promise&lt;number&gt;; 差异内容：NA | 类名：statistics； API声明：function getUidTxBytes(uid: number): Promise&lt;number&gt;; 差异内容：201 | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics； API声明：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：statistics； API声明：function getUidRxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.GET_NETWORK_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics； API声明：function getUidRxBytes(uid: number): Promise&lt;number&gt;; 差异内容：NA | 类名：statistics； API声明：function getUidRxBytes(uid: number): Promise&lt;number&gt;; 差异内容：ohos.permission.GET_NETWORK_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics； API声明：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：statistics； API声明：function getUidTxBytes(uid: number, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.GET_NETWORK_STATS | api/@ohos.net.statistics.d.ts |
| 权限变更 | 类名：statistics； API声明：function getUidTxBytes(uid: number): Promise&lt;number&gt;; 差异内容：NA | 类名：statistics； API声明：function getUidTxBytes(uid: number): Promise&lt;number&gt;; 差异内容：ohos.permission.GET_NETWORK_STATS | api/@ohos.net.statistics.d.ts |
| 新增API | NA | 类名：http； API声明：export type X509Cert = cert.X509Cert; 差异内容：export type X509Cert = cert.X509Cert; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export interface ValidationContext 差异内容：export interface ValidationContext | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext； API声明：pemCerts: string[]; 差异内容：pemCerts: string[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext； API声明：x509Certs: X509Cert[]; 差异内容：x509Certs: X509Cert[]; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext； API声明：host: string; 差异内容：host: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：ValidationContext； API声明：ip: string; 差异内容：ip: string; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：http； API声明：export type ValidationCallback = (context: ValidationContext) => boolean \| Promise&lt;boolean&gt;; 差异内容：export type ValidationCallback = (context: ValidationContext) => boolean \| Promise&lt;boolean&gt;; | api/@ohos.net.http.d.ts |
| 新增API | NA | 类名：connection； API声明：function refreshGlobalHttpProxy(): Promise&lt;HttpProxy&gt;; 差异内容：function refreshGlobalHttpProxy(): Promise&lt;HttpProxy&gt;; | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetFirewallRule； API声明：interface?: string; 差异内容：interface?: string; | api/@ohos.net.netFirewall.d.ts |
| 新增API | NA | 类名：networkSecurity； API声明：export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>; 差异内容：export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>; | api/@ohos.net.networkSecurity.d.ts |
| 新增API | NA | 类名：WebSocketRequestOptions； API声明：supportOriginPort?: boolean; 差异内容：supportOriginPort?: boolean; | api/@ohos.net.webSocket.d.ts |
