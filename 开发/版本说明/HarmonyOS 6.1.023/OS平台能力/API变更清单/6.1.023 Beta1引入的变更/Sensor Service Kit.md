# Sensor Service Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：sensor； API声明：function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void; 差异内容：NA | 类名：sensor； API声明：function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void; 差异内容：401 | api/@ohos.sensor.d.ts |
| 新增错误码 | 类名：sensor； API声明：function off(type: SensorId.FUSION_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void; 差异内容：NA | 类名：sensor； API声明：function off(type: SensorId.FUSION_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void; 差异内容：401 | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：Sensor； API声明：isMockSensor?: boolean; 差异内容：isMockSensor?: boolean; | api/@ohos.sensor.d.ts |
