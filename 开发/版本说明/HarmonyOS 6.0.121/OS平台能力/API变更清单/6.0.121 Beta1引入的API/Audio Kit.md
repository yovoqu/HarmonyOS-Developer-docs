# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：audio； API声明：enum AudioLoopbackReverbPreset 差异内容：enum AudioLoopbackReverbPreset | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackReverbPreset； API声明：ORIGINAL = 1 差异内容：ORIGINAL = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackReverbPreset； API声明：KTV = 2 差异内容：KTV = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackReverbPreset； API声明：THEATER = 3 差异内容：THEATER = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackReverbPreset； API声明：CONCERT = 4 差异内容：CONCERT = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum AudioLoopbackEqualizerPreset 差异内容：enum AudioLoopbackEqualizerPreset | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackEqualizerPreset； API声明：FLAT = 1 差异内容：FLAT = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackEqualizerPreset； API声明：FULL = 2 差异内容：FULL = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackEqualizerPreset； API声明：BRIGHT = 3 差异内容：BRIGHT = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPrivacyType； API声明：PRIVACY_TYPE_SHARED = 2 差异内容：PRIVACY_TYPE_SHARED = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum BluetoothAndNearlinkPreferredRecordCategory 差异内容：enum BluetoothAndNearlinkPreferredRecordCategory | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：BluetoothAndNearlinkPreferredRecordCategory； API声明：PREFERRED_NONE = 0 差异内容：PREFERRED_NONE = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：BluetoothAndNearlinkPreferredRecordCategory； API声明：PREFERRED_DEFAULT = 1 差异内容：PREFERRED_DEFAULT = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：BluetoothAndNearlinkPreferredRecordCategory； API声明：PREFERRED_LOW_LATENCY = 2 差异内容：PREFERRED_LOW_LATENCY = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：BluetoothAndNearlinkPreferredRecordCategory； API声明：PREFERRED_HIGH_QUALITY = 3 差异内容：PREFERRED_HIGH_QUALITY = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface CurrentInputDeviceChangedEvent 差异内容：interface CurrentInputDeviceChangedEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentInputDeviceChangedEvent； API声明：devices: AudioDeviceDescriptors; 差异内容：devices: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentInputDeviceChangedEvent； API声明：changeReason: AudioStreamDeviceChangeReason; 差异内容：changeReason: AudioStreamDeviceChangeReason; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioStreamManager； API声明：isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean; 差异内容：isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors; 差异内容：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback&lt;DeviceChangeAction&gt;): void; 差异内容：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback&lt;DeviceChangeAction&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：off(type: 'availableDeviceChange', callback?: Callback&lt;DeviceChangeAction&gt;): void; 差异内容：off(type: 'availableDeviceChange', callback?: Callback&lt;DeviceChangeAction&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; 差异内容：selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：getSelectedMediaInputDevice(): AudioDeviceDescriptor; 差异内容：getSelectedMediaInputDevice(): AudioDeviceDescriptor; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：clearSelectedMediaInputDevice(): Promise&lt;void&gt;; 差异内容：clearSelectedMediaInputDevice(): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise&lt;void&gt;; 差异内容：setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory; 差异内容：getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;): void; 差异内容：on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioSessionManager； API声明：off(type: 'currentInputDeviceChanged', callback?: Callback&lt;CurrentInputDeviceChangedEvent&gt;): void; 差异内容：off(type: 'currentInputDeviceChanged', callback?: Callback&lt;CurrentInputDeviceChangedEvent&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioLoopback； API声明：setReverbPreset(preset: AudioLoopbackReverbPreset): boolean; 差异内容：setReverbPreset(preset: AudioLoopbackReverbPreset): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioLoopback； API声明：getReverbPreset(): AudioLoopbackReverbPreset; 差异内容：getReverbPreset(): AudioLoopbackReverbPreset; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioLoopback； API声明：setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean; 差异内容：setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioLoopback； API声明：getEqualizerPreset(): AudioLoopbackEqualizerPreset; 差异内容：getEqualizerPreset(): AudioLoopbackEqualizerPreset; | api/@ohos.multimedia.audio.d.ts |
