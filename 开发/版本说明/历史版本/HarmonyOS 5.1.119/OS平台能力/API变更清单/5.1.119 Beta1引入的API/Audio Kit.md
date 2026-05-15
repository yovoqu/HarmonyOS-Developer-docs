# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：AudioStreamManager； API声明：off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void; 差异内容：401 | 类名：AudioStreamManager； API声明：off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioStreamManager； API声明：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void; 差异内容：401 | 类名：AudioStreamManager； API声明：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioVolumeGroupManager； API声明：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void; 差异内容：401 | 类名：AudioVolumeGroupManager； API声明：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioSpatializationManager； API声明：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void; 差异内容：401 | 类名：AudioSpatializationManager； API声明：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioSpatializationManager； API声明：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void; 差异内容：401 | 类名：AudioSpatializationManager； API声明：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioRenderer； API声明：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void; 差异内容：401 | 类名：AudioRenderer； API声明：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioRenderer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：401 | 类名：AudioRenderer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 删除错误码 | 类名：AudioCapturer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：401 | 类名：AudioCapturer； API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：HDMI = 27 差异内容：HDMI = 27 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：LINE_DIGITAL = 28 差异内容：LINE_DIGITAL = 28 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum AudioVolumeMode 差异内容：enum AudioVolumeMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeMode； API声明：SYSTEM_GLOBAL = 0 差异内容：SYSTEM_GLOBAL = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeMode； API声明：APP_INDIVIDUAL = 1 差异内容：APP_INDIVIDUAL = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioTimestampInfo 差异内容：interface AudioTimestampInfo | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioTimestampInfo； API声明：readonly framePos: number; 差异内容：readonly framePos: number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioTimestampInfo； API声明：readonly timestamp: number; 差异内容：readonly timestamp: number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioVolumeManager； API声明：getAppVolumePercentage(): Promise<number>; 差异内容：getAppVolumePercentage(): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioVolumeManager； API声明：setAppVolumePercentage(volume: number): Promise<void>; 差异内容：setAppVolumePercentage(volume: number): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioVolumeManager； API声明：on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void; 差异内容：on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioVolumeManager； API声明：off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void; 差异内容：off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioRenderer； API声明：getAudioTimestampInfo(): Promise<AudioTimestampInfo>; 差异内容：getAudioTimestampInfo(): Promise<AudioTimestampInfo>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioRenderer； API声明：getAudioTimestampInfoSync(): AudioTimestampInfo; 差异内容：getAudioTimestampInfoSync(): AudioTimestampInfo; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioCapturer； API声明：getAudioTimestampInfo(): Promise<AudioTimestampInfo>; 差异内容：getAudioTimestampInfo(): Promise<AudioTimestampInfo>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioCapturer； API声明：getAudioTimestampInfoSync(): AudioTimestampInfo; 差异内容：getAudioTimestampInfoSync(): AudioTimestampInfo; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AudioRendererInfo； API声明：volumeMode?: AudioVolumeMode; 差异内容：volumeMode?: AudioVolumeMode; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：VolumeEvent； API声明：volumeMode?: AudioVolumeMode; 差异内容：volumeMode?: AudioVolumeMode; | api/@ohos.multimedia.audio.d.ts |
