# Call Service Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callservicekit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace numberIdentify 差异内容：declare namespace numberIdentify | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify； API声明：function isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>; 差异内容：function isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify； API声明：function queryNumberIdentifySwitchState(context: Context): SwitchState; 差异内容：function queryNumberIdentifySwitchState(context: Context): SwitchState; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：numberIdentify； API声明：interface SwitchState 差异内容：interface SwitchState | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：SwitchState； API声明：isNumberIdentifyEnabled: boolean; 差异内容：isNumberIdentifyEnabled: boolean; | api/@hms.telephony.numberIdentify.d.ts |
| 新增API | NA | 类名：SwitchState； API声明：isApplicationNumberIdentifyEnabled: boolean; 差异内容：isApplicationNumberIdentifyEnabled: boolean; | api/@hms.telephony.numberIdentify.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.telephony.numberIdentify.d.ts 差异内容：CallServiceKit | api/@hms.telephony.numberIdentify.d.ts |
