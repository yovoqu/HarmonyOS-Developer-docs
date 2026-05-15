# Network Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：networkSecurity； API声明：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>; 差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305023,2305024,2305027,401 | 类名：networkSecurity； API声明：export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>; 差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305018,2305023,2305024,2305027,2305069,401 | api/@ohos.net.networkSecurity.d.ts |
| 错误码变更 | 类名：networkSecurity； API声明：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number; 差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305023,2305024,2305027,401 | 类名：networkSecurity； API声明：export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number; 差异内容：2305001,2305002,2305003,2305004,2305005,2305006,2305007,2305008,2305009,2305010,2305011,2305012,2305018,2305023,2305024,2305027,2305069,401 | api/@ohos.net.networkSecurity.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：connect(url: string, callback: AsyncCallback<boolean>): void; 差异内容：201,401 | 类名：WebSocket； API声明：connect(url: string, callback: AsyncCallback<boolean>): void; 差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void; 差异内容：201,401 | 类名：WebSocket； API声明：connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void; 差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 错误码变更 | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>; 差异内容：201,401 | 类名：WebSocket； API声明：connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>; 差异内容：201,2302001,2302002,2302003,2302999,401 | api/@ohos.net.webSocket.d.ts |
| 新增API | NA | 类名：NetCap； API声明：NET_CAPABILITY_CHECKING_CONNECTIVITY = 31 差异内容：NET_CAPABILITY_CHECKING_CONNECTIVITY = 31 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：NetBearType； API声明：BEARER_BLUETOOTH = 2 差异内容：BEARER_BLUETOOTH = 2 | api/@ohos.net.connection.d.ts |
| 新增API | NA | 类名：TLSSecureOptions； API声明：isBidirectionalAuthentication?: boolean; 差异内容：isBidirectionalAuthentication?: boolean; | api/@ohos.net.socket.d.ts |
| 新增API | NA | 类名：TLSConnectOptions； API声明：skipRemoteValidation?: boolean; 差异内容：skipRemoteValidation?: boolean; | api/@ohos.net.socket.d.ts |
