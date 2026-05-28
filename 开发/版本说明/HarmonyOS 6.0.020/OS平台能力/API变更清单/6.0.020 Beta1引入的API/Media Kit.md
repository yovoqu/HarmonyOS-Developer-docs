# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：media； API声明：type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void; 差异内容：SystemCapability.Multimedia.Media.AVPlayer | 类名：media； API声明：type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void; 差异内容：SystemCapability.Multimedia.Media.AVRecorder | api/@ohos.multimedia.media.d.ts |
| 新增错误码 | 类名：AVTranscoder； API声明：prepare(config: AVTranscoderConfig): Promise&lt;void&gt;; 差异内容：NA | 类名：AVTranscoder； API声明：prepare(config: AVTranscoderConfig): Promise&lt;void&gt;; 差异内容：5400103 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：declare interface OutputSize 差异内容：declare interface OutputSize | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：OutputSize； API声明：width?: number; 差异内容：width?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：OutputSize； API声明：height?: number; 差异内容：height?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type OnPlaybackRateDone = (rate: number) => void; 差异内容：type OnPlaybackRateDone = (rate: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：ContainerFormatType； API声明：CFT_AAC = 'aac' 差异内容：CFT_AAC = 'aac' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface AVScreenCaptureStrategy 差异内容：interface AVScreenCaptureStrategy | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStrategy； API声明：keepCaptureDuringCall?: boolean; 差异内容：keepCaptureDuringCall?: boolean; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVImageGenerator； API声明：fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize): Promise<image.PixelMap>; 差异内容：fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize): Promise<image.PixelMap>; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：setPlaybackRate(rate: number): void; 差异内容：setPlaybackRate(rate: number): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void; 差异内容：on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void; 差异内容：off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVRecorder； API声明：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise&lt;void&gt;; 差异内容：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AVScreenCaptureRecordConfig； API声明：strategy?: AVScreenCaptureStrategy; 差异内容：strategy?: AVScreenCaptureStrategy; | api/@ohos.multimedia.media.d.ts |
