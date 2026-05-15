# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global； API声明： declare namespace audio 差异内容：SystemCapability.Multimedia.Audio | 类名：global； API声明： declare namespace audio 差异内容：SystemCapability.Multimedia.Audio.Core | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： enum DeviceUsage 差异内容： enum DeviceUsage | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：MEDIA_OUTPUT_DEVICES = 1 差异内容：MEDIA_OUTPUT_DEVICES = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：MEDIA_INPUT_DEVICES = 2 差异内容：MEDIA_INPUT_DEVICES = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：ALL_MEDIA_DEVICES = 3 差异内容：ALL_MEDIA_DEVICES = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：CALL_OUTPUT_DEVICES = 4 差异内容：CALL_OUTPUT_DEVICES = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：CALL_INPUT_DEVICES = 8 差异内容：CALL_INPUT_DEVICES = 8 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage； API声明：ALL_CALL_DEVICES = 12 差异内容：ALL_CALL_DEVICES = 12 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioScene； API声明：AUDIO_SCENE_RINGING = 1 差异内容：AUDIO_SCENE_RINGING = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioScene； API声明：AUDIO_SCENE_PHONE_CALL = 2 差异内容：AUDIO_SCENE_PHONE_CALL = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager； API声明：getSessionManager(): AudioSessionManager; 差异内容：getSessionManager(): AudioSessionManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors; 差异内容：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void; 差异内容：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void; 差异内容：off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： enum AudioConcurrencyMode 差异内容： enum AudioConcurrencyMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode； API声明：CONCURRENCY_DEFAULT = 0 差异内容：CONCURRENCY_DEFAULT = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode； API声明：CONCURRENCY_MIX_WITH_OTHERS = 1 差异内容：CONCURRENCY_MIX_WITH_OTHERS = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode； API声明：CONCURRENCY_DUCK_OTHERS = 2 差异内容：CONCURRENCY_DUCK_OTHERS = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode； API声明：CONCURRENCY_PAUSE_OTHERS = 3 差异内容：CONCURRENCY_PAUSE_OTHERS = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： enum AudioSessionDeactivatedReason 差异内容： enum AudioSessionDeactivatedReason | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedReason； API声明：DEACTIVATED_LOWER_PRIORITY = 0 差异内容：DEACTIVATED_LOWER_PRIORITY = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedReason； API声明：DEACTIVATED_TIMEOUT = 1 差异内容：DEACTIVATED_TIMEOUT = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： interface AudioSessionStrategy 差异内容： interface AudioSessionStrategy | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStrategy； API声明：concurrencyMode: AudioConcurrencyMode; 差异内容：concurrencyMode: AudioConcurrencyMode; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： interface AudioSessionDeactivatedEvent 差异内容： interface AudioSessionDeactivatedEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedEvent； API声明：reason: AudioSessionDeactivatedReason; 差异内容：reason: AudioSessionDeactivatedReason; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明： interface AudioSessionManager 差异内容： interface AudioSessionManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager； API声明：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>; 差异内容：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager； API声明：deactivateAudioSession(): Promise<void>; 差异内容：deactivateAudioSession(): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager； API声明：isAudioSessionActivated(): boolean; 差异内容：isAudioSessionActivated(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager； API声明：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void; 差异内容：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager； API声明：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void; 差异内容：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer； API声明：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>; 差异内容：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
