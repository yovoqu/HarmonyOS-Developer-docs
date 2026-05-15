# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-5031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AccountManager； API声明：getForegroundOsAccountLocalId(): Promise<number>; 差异内容：getForegroundOsAccountLocalId(): Promise<number>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：AccountManager； API声明：getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>; 差异内容：getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：agent； API声明： interface Notification 差异内容： interface Notification | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Notification； API声明：title?: string; 差异内容：title?: string; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Notification； API声明：text?: string; 差异内容：text?: string; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Config； API声明：notification?: Notification; 差异内容：notification?: Notification; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent； API声明： interface GroupConfig 差异内容： interface GroupConfig | api/@ohos.request.d.ts |
| 新增API | NA | 类名：GroupConfig； API声明：gauge?: boolean; 差异内容：gauge?: boolean; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：GroupConfig； API声明：notification: Notification; 差异内容：notification: Notification; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent； API声明：function createGroup(config: GroupConfig): Promise<string>; 差异内容：function createGroup(config: GroupConfig): Promise<string>; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent； API声明：function attachGroup(gid: string, tids: string[]): Promise<void>; 差异内容：function attachGroup(gid: string, tids: string[]): Promise<void>; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent； API声明：function deleteGroup(gid: string): Promise<void>; 差异内容：function deleteGroup(gid: string): Promise<void>; | api/@ohos.request.d.ts |
