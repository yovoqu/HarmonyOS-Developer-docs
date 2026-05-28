# Sensor Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SensorId； API声明：FUSION_PRESSURE = 283 差异内容：FUSION_PRESSURE = 283 | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor； API声明：function on(type: SensorId.FUSION_PRESSURE, callback: Callback&lt;FusionPressureResponse&gt;, options?: Options): void; 差异内容：function on(type: SensorId.FUSION_PRESSURE, callback: Callback&lt;FusionPressureResponse&gt;, options?: Options): void; | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor； API声明：function off(type: SensorId.FUSION_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback&lt;FusionPressureResponse&gt;): void; 差异内容：function off(type: SensorId.FUSION_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback&lt;FusionPressureResponse&gt;): void; | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor； API声明：interface FusionPressureResponse 差异内容：interface FusionPressureResponse | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：FusionPressureResponse； API声明：fusionPressure: number; 差异内容：fusionPressure: number; | api/@ohos.sensor.d.ts |
