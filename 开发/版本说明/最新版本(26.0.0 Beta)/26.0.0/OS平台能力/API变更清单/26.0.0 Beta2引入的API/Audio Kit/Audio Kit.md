# Audio Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：audio； API声明：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; 差异内容：201,801 | 类名：audio； API声明：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 权限变更 | 类名：audio； API声明：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; 差异内容：ohos.permission.MICROPHONE | 类名：audio； API声明：function createAudioLoopback(mode: AudioLoopbackMode): Promise&lt;AudioLoopback&gt;; 差异内容：NA | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：type DeviceTypeArray = Array&lt;DeviceType&gt;; 差异内容：type DeviceTypeArray = Array&lt;DeviceType&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager； API声明：getDeviceEnhanceManager(): AudioDeviceEnhanceManager; 差异内容：getDeviceEnhanceManager(): AudioDeviceEnhanceManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager； API声明：getDebuggingManager(): AudioDebuggingManager; 差异内容：getDebuggingManager(): AudioDebuggingManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager； API声明：getRecordingManager(): AudioRecordingManager; 差异内容：getRecordingManager(): AudioRecordingManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager； API声明：declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void; 差异内容：declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionBehaviorFlags； API声明：PAUSE_WHEN_INTERRUPTED = 0x00000004 差异内容：PAUSE_WHEN_INTERRUPTED = 0x00000004 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface SystemRecordControllerConfig 差异内容：interface SystemRecordControllerConfig | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SystemRecordControllerConfig； API声明：sourceType: SourceType; 差异内容：sourceType: SourceType; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioDeviceEnhanceManager 差异内容：interface AudioDeviceEnhanceManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceEnhanceManager； API声明：isEnhancedRoutingSupported(): boolean; 差异内容：isEnhancedRoutingSupported(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceEnhanceManager； API声明：selectOutputDevice(outputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; 差异内容：selectOutputDevice(outputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceEnhanceManager； API声明：selectInputDevice(inputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; 差异内容：selectInputDevice(inputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceEnhanceManager； API声明：selectOutputDeviceForAudioRenderer(renderer: AudioRenderer, outputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; 差异内容：selectOutputDeviceForAudioRenderer(renderer: AudioRenderer, outputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceEnhanceManager； API声明：selectInputDeviceForAudioCapturer(capturer: AudioCapturer, inputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; 差异内容：selectInputDeviceForAudioCapturer(capturer: AudioCapturer, inputDevice: AudioDeviceDescriptor): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioRecordingManager 差异内容：interface AudioRecordingManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRecordingManager； API声明：enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise&lt;void&gt;; 差异内容：enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：interface AudioDebuggingManager 差异内容：interface AudioDebuggingManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDebuggingManager； API声明：printAppInfo(fd: number): void; 差异内容：printAppInfo(fd: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDebuggingManager； API声明：printRendererInfo(renderer: AudioRenderer, fd: number): void; 差异内容：printRendererInfo(renderer: AudioRenderer, fd: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDebuggingManager； API声明：printCapturerInfo(capturer: AudioCapturer, fd: number): void; 差异内容：printCapturerInfo(capturer: AudioCapturer, fd: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDebuggingManager； API声明：printLoopbackInfo(loopback: AudioLoopback, fd: number): void; 差异内容：printLoopbackInfo(loopback: AudioLoopback, fd: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDebuggingManager； API声明：printSessionInfo(session: AudioSessionManager, fd: number): void; 差异内容：printSessionInfo(session: AudioSessionManager, fd: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum AudioPlaybackCaptureMode 差异内容：enum AudioPlaybackCaptureMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPlaybackCaptureMode； API声明：MODE_DEFAULT = 0x0 差异内容：MODE_DEFAULT = 0x0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPlaybackCaptureMode； API声明：MODE_MEDIA = 0x1 差异内容：MODE_MEDIA = 0x1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPlaybackCaptureMode； API声明：MODE_EXCLUDING_SELF = 0x8000 差异内容：MODE_EXCLUDING_SELF = 0x8000 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio； API声明：enum PlaybackCaptureStartState 差异内容：enum PlaybackCaptureStartState | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：PlaybackCaptureStartState； API声明：STATE_SUCCESS = 0 差异内容：STATE_SUCCESS = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：PlaybackCaptureStartState； API声明：STATE_FAILED = 1 差异内容：STATE_FAILED = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：PlaybackCaptureStartState； API声明：STATE_NOT_AUTHORIZED = 2 差异内容：STATE_NOT_AUTHORIZED = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturerOptions； API声明：playbackCaptureMode?: AudioPlaybackCaptureMode; 差异内容：playbackCaptureMode?: AudioPlaybackCaptureMode; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer； API声明：requestPlaybackCaptureStart(callback: Callback&lt;PlaybackCaptureStartState&gt;): void; 差异内容：requestPlaybackCaptureStart(callback: Callback&lt;PlaybackCaptureStartState&gt;): void; | api/@ohos.multimedia.audio.d.ts |
