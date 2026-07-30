# Telephony Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：call； API声明：function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise&lt;string&gt;; 差异内容：function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise&lt;string&gt;; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call； API声明：export enum CallTransferType 差异内容：export enum CallTransferType | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType； API声明：TRANSFER_TYPE_UNCONDITIONAL = 0 差异内容：TRANSFER_TYPE_UNCONDITIONAL = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType； API声明：TRANSFER_TYPE_BUSY = 1 差异内容：TRANSFER_TYPE_BUSY = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType； API声明：TRANSFER_TYPE_NO_REPLY = 2 差异内容：TRANSFER_TYPE_NO_REPLY = 2 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferType； API声明：TRANSFER_TYPE_NOT_REACHABLE = 3 差异内容：TRANSFER_TYPE_NOT_REACHABLE = 3 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：MakeCallOptions； API声明：isCustomAccessibility?: boolean; 差异内容：isCustomAccessibility?: boolean; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call； API声明：export interface CallTransferResult 差异内容：export interface CallTransferResult | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult； API声明：status: TransferStatus; 差异内容：status: TransferStatus; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult； API声明：startHour: number; 差异内容：startHour: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult； API声明：startMinute: number; 差异内容：startMinute: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult； API声明：endHour: number; 差异内容：endHour: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：CallTransferResult； API声明：endMinute: number; 差异内容：endMinute: number; | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：call； API声明：export enum TransferStatus 差异内容：export enum TransferStatus | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TransferStatus； API声明：TRANSFER_DISABLE = 0 差异内容：TRANSFER_DISABLE = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TransferStatus； API声明：TRANSFER_ENABLE = 1 差异内容：TRANSFER_ENABLE = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：data； API声明：function showSystemApnSettings(context: Context): Promise&lt;void&gt;; 差异内容：function showSystemApnSettings(context: Context): Promise&lt;void&gt;; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：observer； API声明：function onCommunicationStateChange(callback: Callback&lt;boolean&gt;, options?: ObserverOptions): void; 差异内容：function onCommunicationStateChange(callback: Callback&lt;boolean&gt;, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer； API声明：function offCommunicationStateChange(callback: Callback&lt;boolean&gt;, options?: ObserverOptions): void; 差异内容：function offCommunicationStateChange(callback: Callback&lt;boolean&gt;, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
