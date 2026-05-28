# Telephony Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-504

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：data； API声明：function queryAllApns(): Promise<Array&lt;ApnInfo&gt;>; 差异内容：function queryAllApns(): Promise<Array&lt;ApnInfo&gt;>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data； API声明：function queryApnIds(apnInfo: ApnInfo): Promise<Array&lt;number&gt;>; 差异内容：function queryApnIds(apnInfo: ApnInfo): Promise<Array&lt;number&gt;>; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data； API声明：function setPreferredApn(apnId: number): Promise&lt;boolean&gt;; 差异内容：function setPreferredApn(apnId: number): Promise&lt;boolean&gt;; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：data； API声明： interface ApnInfo 差异内容： interface ApnInfo | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：apnName: string; 差异内容：apnName: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：apn: string; 差异内容：apn: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：mcc: string; 差异内容：mcc: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：mnc: string; 差异内容：mnc: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：user?: string; 差异内容：user?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：type?: string; 差异内容：type?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：proxy?: string; 差异内容：proxy?: string; | api/@ohos.telephony.data.d.ts |
| 新增API | NA | 类名：ApnInfo； API声明：mmsproxy?: string; 差异内容：mmsproxy?: string; | api/@ohos.telephony.data.d.ts |
| 删除API | 类名：global； API声明： declare namespace eSIM 差异内容： declare namespace eSIM | NA | api/@ohos.telephony.esim.d.ts |
| 删除API | 类名：eSIM； API声明：function isSupported(slotId: number): boolean; 差异内容：function isSupported(slotId: number): boolean; | NA | api/@ohos.telephony.esim.d.ts |
| 删除API | 类名：eSIM； API声明：function addProfile(profile: DownloadableProfile): Promise&lt;boolean&gt;; 差异内容：function addProfile(profile: DownloadableProfile): Promise&lt;boolean&gt;; | NA | api/@ohos.telephony.esim.d.ts |
| kit变更 | TelephonyKit | NA | api/@ohos.telephony.esim.d.ts |
