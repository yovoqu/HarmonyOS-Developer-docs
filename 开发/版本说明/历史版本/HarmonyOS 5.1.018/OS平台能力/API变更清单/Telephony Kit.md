# Telephony Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace eSIM 差异内容：declare namespace eSIM | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM； API声明：function isSupported(slotId: number): boolean; 差异内容：function isSupported(slotId: number): boolean; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM； API声明：function addProfile(profile: DownloadableProfile): Promise<boolean>; 差异内容：function addProfile(profile: DownloadableProfile): Promise<boolean>; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：eSIM； API声明：export interface DownloadableProfile 差异内容：export interface DownloadableProfile | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile； API声明：activationCode: string; 差异内容：activationCode: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile； API声明：confirmationCode?: string; 差异内容：confirmationCode?: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile； API声明：carrierName?: string; 差异内容：carrierName?: string; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：DownloadableProfile； API声明：accessRules?: Array<AccessRule>; 差异内容：accessRules?: Array<AccessRule>; | api/@ohos.telephony.esim.d.ts |
| 新增API | NA | 类名：radio； API声明：function getRadioTechSync(slotId: number): NetworkRadioTech; 差异内容：function getRadioTechSync(slotId: number): NetworkRadioTech; | api/@ohos.telephony.radio.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.telephony.esim.d.ts 差异内容：TelephonyKit | api/@ohos.telephony.esim.d.ts |
