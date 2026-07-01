# Basic Services Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-7001

## Basic Services Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：PasteData； API声明：addRecord(mimeType: string, value: ValueType): void; 差异内容：NA | 类名：PasteData； API声明：addRecord(mimeType: string, value: ValueType): void; 差异内容：12900002 | api/@ohos.pasteboard.d.ts |
| 权限变更 | 类名：SystemPasteboard； API声明：getData(callback: AsyncCallback&lt;PasteData&gt;): void; 差异内容：ohos.permission.READ_PASTEBOARD | 类名：SystemPasteboard； API声明：getData(callback: AsyncCallback&lt;PasteData&gt;): void; 差异内容：ohos.permission.READ_PASTEBOARD [since 12] | api/@ohos.pasteboard.d.ts |
| 权限变更 | 类名：SystemPasteboard； API声明：getData(): Promise&lt;PasteData&gt;; 差异内容：ohos.permission.READ_PASTEBOARD | 类名：SystemPasteboard； API声明：getData(): Promise&lt;PasteData&gt;; 差异内容：ohos.permission.READ_PASTEBOARD [since 12] | api/@ohos.pasteboard.d.ts |
| 权限变更 | 类名：SystemPasteboard； API声明：getDataSync(): PasteData; 差异内容：ohos.permission.READ_PASTEBOARD | 类名：SystemPasteboard； API声明：getDataSync(): PasteData; 差异内容：ohos.permission.READ_PASTEBOARD [since 12] | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：settings； API声明：function openMobileNetworkSettingsPage(context: Context): void; 差异内容：function openMobileNetworkSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings； API声明：function openDisplaySettingsPage(context: Context): void; 差异内容：function openDisplaySettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings； API声明：function openScreenRefreshRateSettingsPage(context: Context): void; 差异内容：function openScreenRefreshRateSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings； API声明：function openSoundSettingsPage(context: Context): void; 差异内容：function openSoundSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings； API声明：function openAboutDeviceSettingsPage(context: Context): void; 差异内容：function openAboutDeviceSettingsPage(context: Context): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：settings； API声明：function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: number): void; 差异内容：function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: number): void; | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：osAccount； API声明：function isDomainAccountSupported(): Promise&lt;boolean&gt;; 差异内容：function isDomainAccountSupported(): Promise&lt;boolean&gt;; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：AccountManager； API声明：getOsAccountNameByLocalId(localId: number): Promise&lt;string&gt;; 差异内容：getOsAccountNameByLocalId(localId: number): Promise&lt;string&gt;; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：AccountManager； API声明：getOsAccountLocalIds(): Promise<number[]>; 差异内容：getOsAccountLocalIds(): Promise<number[]>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：DomainAccountInfo； API声明：additionalInfo?: Record<string, Object>; 差异内容：additionalInfo?: Record<string, Object>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：SuppressWarningsType； API声明：PERMISSION = 'permission' 差异内容：PERMISSION = 'permission' | api/@ohos.annotation.d.ets |
| 新增API | NA | 类名：deviceInfo； API声明：const sdkMinorApiVersion: number; 差异内容：const sdkMinorApiVersion: number; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo； API声明：const sdkPatchApiVersion: number; 差异内容：const sdkPatchApiVersion: number; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo； API声明：function apiAvailable(version: string \| number): boolean; 差异内容：function apiAvailable(version: string \| number): boolean; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：deviceInfo； API声明：const deviceColor: string; 差异内容：const deviceColor: string; | api/@ohos.deviceInfo.d.ts |
| 起始版本有变化 | 类名：commonEventManager； API声明：export type CommonEventSubscribeInfo = _CommonEventSubscribeInfo; 差异内容：10 | 类名：commonEventManager； API声明：export type CommonEventSubscribeInfo = _CommonEventSubscribeInfo; 差异内容：11 | api/@ohos.commonEventManager.d.ts |
