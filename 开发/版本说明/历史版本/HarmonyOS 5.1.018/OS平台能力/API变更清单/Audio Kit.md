# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：AudioStreamManager； API声明：off(type: 'audioRendererChange'): void; 差异内容：NA | 类名：AudioStreamManager； API声明：off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void; 差异内容：callback?: Callback<AudioRendererChangeInfoArray> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager； API声明：off(type: 'audioCapturerChange'): void; 差异内容：NA | 类名：AudioStreamManager； API声明：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void; 差异内容：callback?: Callback<AudioCapturerChangeInfoArray> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer； API声明：off(type: 'markReach'): void; 差异内容：NA | 类名：AudioRenderer； API声明：off(type: 'markReach', callback?: Callback<number>): void; 差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer； API声明：off(type: 'periodReach'): void; 差异内容：NA | 类名：AudioRenderer； API声明：off(type: 'periodReach', callback?: Callback<number>): void; 差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer； API声明：off(type: 'markReach'): void; 差异内容：NA | 类名：AudioCapturer； API声明：off(type: 'markReach', callback?: Callback<number>): void; 差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer； API声明：off(type: 'periodReach'): void; 差异内容：NA | 类名：AudioCapturer； API声明：off(type: 'periodReach', callback?: Callback<number>): void; 差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：USB_DEVICE = 25 差异内容：USB_DEVICE = 25 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：REMOTE_DAUDIO = 29 差异内容：REMOTE_DAUDIO = 29 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioSpatializationManager 差异内容：interface AudioSpatializationManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager； API声明：isSpatializationEnabledForCurrentDevice(): boolean; 差异内容：isSpatializationEnabledForCurrentDevice(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager； API声明：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void; 差异内容：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager； API声明：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void; 差异内容：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioManager； API声明：getSpatializationManager(): AudioSpatializationManager; 差异内容：getSpatializationManager(): AudioSpatializationManager; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioVolumeGroupManager； API声明：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void; 差异内容：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioRenderer； API声明：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void; 差异内容：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioRenderer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：off(type: 'stateChange', callback?: Callback<AudioState>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioCapturer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：off(type: 'stateChange', callback?: Callback<AudioState>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AudioDeviceDescriptor； API声明：readonly spatializationSupported?: boolean; 差异内容：readonly spatializationSupported?: boolean; | api/@ohos.multimedia.audio.d.ts |
