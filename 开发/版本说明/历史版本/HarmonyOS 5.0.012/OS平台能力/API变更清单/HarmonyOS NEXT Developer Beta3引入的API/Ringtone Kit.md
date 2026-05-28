# Ringtone Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-ringtonekit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace ringtone 差异内容： declare namespace ringtone | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明： enum RingtoneType 差异内容： enum RingtoneType | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType； API声明：CALL = 0 差异内容：CALL = 0 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType； API声明：MESSAGE = 1 差异内容：MESSAGE = 1 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType； API声明：NOTIFICATION = 2 差异内容：NOTIFICATION = 2 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneType； API声明：ALARM = 3 差异内容：ALARM = 3 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明：function getSupportedRingtoneTypes(): Array&lt;RingtoneType&gt;; 差异内容：function getSupportedRingtoneTypes(): Array&lt;RingtoneType&gt;; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明：function getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>; 差异内容：function getSupportedDataTypes(ringtoneType: RingtoneType): Array<uniformTypeDescriptor.UniformDataType>; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明：function getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number; 差异内容：function getSupportedMaxDuration(ringtoneType: RingtoneType, dataType: uniformTypeDescriptor.UniformDataType): number; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback&lt;RingtoneType&gt;): void; 差异内容：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string, callback: AsyncCallback&lt;RingtoneType&gt;): void; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise&lt;RingtoneType&gt;; 差异内容：function startRingtoneSetting(context: common.UIAbilityContext, path: string, name: string): Promise&lt;RingtoneType&gt;; | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：ringtone； API声明： enum RingtoneErrors 差异内容： enum RingtoneErrors | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_INVALID_PARAM = 401 差异内容：ERROR_INVALID_PARAM = 401 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_USER_CANCELED = 1011600001 差异内容：ERROR_USER_CANCELED = 1011600001 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_FILE_NOT_FOUND = 1011600002 差异内容：ERROR_FILE_NOT_FOUND = 1011600002 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_SHOW_FAILED = 1011600003 差异内容：ERROR_SHOW_FAILED = 1011600003 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_CALL_SYSTEM_API_FAILED = 1011600004 差异内容：ERROR_CALL_SYSTEM_API_FAILED = 1011600004 | api/@hms.core.ringtone.d.ts |
| 新增API | NA | 类名：RingtoneErrors； API声明：ERROR_SYSTEM = 1011699999 差异内容：ERROR_SYSTEM = 1011699999 | api/@hms.core.ringtone.d.ts |
