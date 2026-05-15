# Enterprise DataGuard Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：fileGuard； API声明：enum AuthenticateKeyType 差异内容：enum AuthenticateKeyType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType； API声明：PUBLIC_KEY = 0 差异内容：PUBLIC_KEY = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType； API声明：PRIVATE_KEY = 1 差异内容：PRIVATE_KEY = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard； API声明：enum AuthenticateDeviceType 差异内容：enum AuthenticateDeviceType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType； API声明：UPPER = 0 差异内容：UPPER = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType； API声明：LOWER = 1 差异内容：LOWER = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; 差异内容：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; 差异内容：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>; 差异内容：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>; 差异内容：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：onPrintStartup(callback: Callback<void>): void; 差异内容：onPrintStartup(callback: Callback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard； API声明：offPrintStartup(callback?: Callback<void>): void; 差异内容：offPrintStartup(callback?: Callback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：recoveryKey； API声明：function verifyUserByDialog(userId: number): Promise<void>; 差异内容：function verifyUserByDialog(userId: number): Promise<void>; | api/@hms.pcService.recoveryKeyService.d.ts |
