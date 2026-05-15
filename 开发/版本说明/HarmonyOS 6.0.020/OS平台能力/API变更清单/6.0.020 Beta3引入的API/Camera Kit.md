# Camera Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：camera； API声明：enum SystemPressureLevel 差异内容：enum SystemPressureLevel | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SystemPressureLevel； API声明：SYSTEM_PRESSURE_NORMAL = 0 差异内容：SYSTEM_PRESSURE_NORMAL = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SystemPressureLevel； API声明：SYSTEM_PRESSURE_MILD = 1 差异内容：SYSTEM_PRESSURE_MILD = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SystemPressureLevel； API声明：SYSTEM_PRESSURE_SEVERE = 2 差异内容：SYSTEM_PRESSURE_SEVERE = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SystemPressureLevel； API声明：SYSTEM_PRESSURE_CRITICAL = 3 差异内容：SYSTEM_PRESSURE_CRITICAL = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：SystemPressureLevel； API声明：SYSTEM_PRESSURE_SHUTDOWN = 4 差异内容：SYSTEM_PRESSURE_SHUTDOWN = 4 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ControlCenterStatusInfo 差异内容：interface ControlCenterStatusInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterStatusInfo； API声明：readonly effectType: ControlCenterEffectType; 差异内容：readonly effectType: ControlCenterEffectType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterStatusInfo； API声明：readonly isActive: boolean; 差异内容：readonly isActive: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：enum ControlCenterEffectType 差异内容：enum ControlCenterEffectType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterEffectType； API声明：BEAUTY = 0 差异内容：BEAUTY = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterEffectType； API声明：PORTRAIT = 1 差异内容：PORTRAIT = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ControlCenterQuery 差异内容：interface ControlCenterQuery | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterQuery； API声明：isControlCenterSupported(): boolean; 差异内容：isControlCenterSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenterQuery； API声明：getSupportedEffectTypes(): Array<ControlCenterEffectType>; 差异内容：getSupportedEffectTypes(): Array<ControlCenterEffectType>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera； API声明：interface ControlCenter 差异内容：interface ControlCenter | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ControlCenter； API声明：enableControlCenter(enabled: boolean): void; 差异内容：enableControlCenter(enabled: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：PhotoSession； API声明：on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void; 差异内容：on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：PhotoSession； API声明：off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void; 差异内容：off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：VideoSession； API声明：on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void; 差异内容：on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：VideoSession； API声明：off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void; 差异内容：off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：VideoSession； API声明：on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void; 差异内容：on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：VideoSession； API声明：off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void; 差异内容：off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void; | api/@ohos.multimedia.camera.d.ts |
