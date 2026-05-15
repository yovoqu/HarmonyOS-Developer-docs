# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-b112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：audio； API声明： enum DeviceBlockStatus 差异内容： enum DeviceBlockStatus | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatus； API声明：UNBLOCKED = 0 差异内容：UNBLOCKED = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatus； API声明：BLOCKED = 1 差异内容：BLOCKED = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： interface DeviceBlockStatusInfo 差异内容： interface DeviceBlockStatusInfo | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatusInfo； API声明：blockStatus: DeviceBlockStatus; 差异内容：blockStatus: DeviceBlockStatus; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatusInfo； API声明：devices: AudioDeviceDescriptors; 差异内容：devices: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：isMicBlockDetectionSupported(): Promise<boolean>; 差异内容：isMicBlockDetectionSupported(): Promise<boolean>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void; 差异内容：on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void; 差异内容：off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType； API声明：SOURCE_TYPE_CAMCORDER = 13 差异内容：SOURCE_TYPE_CAMCORDER = 13 | api/@ohos.multimedia.audio.d.ts |
