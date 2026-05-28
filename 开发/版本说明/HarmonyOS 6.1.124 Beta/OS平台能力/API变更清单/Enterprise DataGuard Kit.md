# Enterprise DataGuard Kit

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：fileGuard； API声明：enum AuthenticateKeyType 差异内容：enum AuthenticateKeyType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType； API声明：PUBLIC_KEY = 0 差异内容：PUBLIC_KEY = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType； API声明：PRIVATE_KEY = 1 差异内容：PRIVATE_KEY = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard； API声明：enum AuthenticateDeviceType 差异内容：enum AuthenticateDeviceType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType； API声明：UPPER = 0 差异内容：UPPER = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType； API声明：LOWER = 1 差异内容：LOWER = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：addUnrestrictedApplicationList(appIds: Array&lt;string&gt;, userId?: number): Promise&lt;void&gt;; 差异内容：addUnrestrictedApplicationList(appIds: Array&lt;string&gt;, userId?: number): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：removeUnrestrictedApplicationList(appIds: Array&lt;string&gt;, userId?: number): Promise&lt;void&gt;; 差异内容：removeUnrestrictedApplicationList(appIds: Array&lt;string&gt;, userId?: number): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：getUnrestrictedApplicationList(userId?: number): Promise<Array&lt;string&gt;>; 差异内容：getUnrestrictedApplicationList(userId?: number): Promise<Array&lt;string&gt;>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise&lt;void&gt;; 差异内容：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：onPrintStartup(callback: Callback&lt;void&gt;): void; 差异内容：onPrintStartup(callback: Callback&lt;void&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：offPrintStartup(callback?: Callback&lt;void&gt;): void; 差异内容：offPrintStartup(callback?: Callback&lt;void&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function verifyUserByDialog(userId: number): Promise&lt;void&gt;; 差异内容：function verifyUserByDialog(userId: number): Promise&lt;void&gt;; | api/@hms.pcService.recoveryKeyService.d.ts |
