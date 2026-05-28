# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：audio； API声明：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; 差异内容：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum AudioLoopbackMode 差异内容：enum AudioLoopbackMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackMode； API声明：HARDWARE = 0 差异内容：HARDWARE = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum AudioLoopbackStatus 差异内容：enum AudioLoopbackStatus | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackStatus； API声明：UNAVAILABLE_DEVICE = -2 差异内容：UNAVAILABLE_DEVICE = -2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackStatus； API声明：UNAVAILABLE_SCENE = -1 差异内容：UNAVAILABLE_SCENE = -1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackStatus； API声明：AVAILABLE_IDLE = 0 差异内容：AVAILABLE_IDLE = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopbackStatus； API声明：AVAILABLE_RUNNING = 1 差异内容：AVAILABLE_RUNNING = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：NEARLINK = 31 差异内容：NEARLINK = 31 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioLoopback 差异内容：interface AudioLoopback | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback； API声明：getStatus(): Promise&lt;AudioLoopbackStatus&gt;; 差异内容：getStatus(): Promise&lt;AudioLoopbackStatus&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback； API声明：setVolume(volume: number): Promise&lt;void&gt;; 差异内容：setVolume(volume: number): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback； API声明：on(type: 'statusChange', callback: Callback&lt;AudioLoopbackStatus&gt;): void; 差异内容：on(type: 'statusChange', callback: Callback&lt;AudioLoopbackStatus&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback； API声明：off(type: 'statusChange', callback?: Callback&lt;AudioLoopbackStatus&gt;): void; 差异内容：off(type: 'statusChange', callback?: Callback&lt;AudioLoopbackStatus&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback； API声明：enable(enable: boolean): Promise&lt;boolean&gt;; 差异内容：enable(enable: boolean): Promise&lt;boolean&gt;; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioStreamManager； API声明：isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean; 差异内容：isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioStreamManager； API声明：isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean; 差异内容：isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean; | api/@ohos.multimedia.audio.d.ts |
