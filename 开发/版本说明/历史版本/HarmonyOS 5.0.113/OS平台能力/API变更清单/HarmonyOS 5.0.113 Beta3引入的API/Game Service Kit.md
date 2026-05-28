# Game Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：gamePerformance； API声明：function on(type: 'deviceStateChanged', callback: Callback&lt;DeviceInfo&gt;, scope: Array&lt;DeviceInfoType&gt;): void; 差异内容：function on(type: 'deviceStateChanged', callback: Callback&lt;DeviceInfo&gt;, scope: Array&lt;DeviceInfoType&gt;): void; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance； API声明： interface ThermalInfo 差异内容： interface ThermalInfo | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：ThermalInfo； API声明：thermalMargin?: number; 差异内容：thermalMargin?: number; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：ThermalInfo； API声明：thermalTrend?: number; 差异内容：thermalTrend?: number; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfo； API声明：thermalInfo?: ThermalInfo; 差异内容：thermalInfo?: ThermalInfo; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance； API声明： enum DeviceInfoType 差异内容： enum DeviceInfoType | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoType； API声明：THERMAL = 1 差异内容：THERMAL = 1 | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoType； API声明：GPU = 2 差异内容：GPU = 2 | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance； API声明： interface DeviceInfoParameter 差异内容： interface DeviceInfoParameter | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameter； API声明：deviceInfoType: DeviceInfoType; 差异内容：deviceInfoType: DeviceInfoType; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameter； API声明：parameters?: Record<string, string>; 差异内容：parameters?: Record<string, string>; | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance； API声明： enum DeviceInfoParameterKey 差异内容： enum DeviceInfoParameterKey | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：DeviceInfoParameterKey； API声明：THERMAL_TEMP_LEVEL = 'tempLevel' 差异内容：THERMAL_TEMP_LEVEL = 'tempLevel' | api/@hms.core.gameservice.gameperformance.d.ts |
| 新增API | NA | 类名：gamePerformance； API声明：function getDeviceInfoByScope(scope: Array&lt;DeviceInfoParameter&gt;): Promise&lt;DeviceInfo&gt;; 差异内容：function getDeviceInfoByScope(scope: Array&lt;DeviceInfoParameter&gt;): Promise&lt;DeviceInfo&gt;; | api/@hms.core.gameservice.gameperformance.d.ts |
