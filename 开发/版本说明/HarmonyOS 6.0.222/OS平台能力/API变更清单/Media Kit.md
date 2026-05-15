# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：media； API声明：enum PickerMode 差异内容：enum PickerMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：WINDOW_ONLY = 0 差异内容：WINDOW_ONLY = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：SCREEN_ONLY = 1 差异内容：SCREEN_ONLY = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：SCREEN_AND_WINDOW = 2 差异内容：SCREEN_AND_WINDOW = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：enum AacProfile 差异内容：enum AacProfile | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile； API声明：AAC_LC = 0 差异内容：AAC_LC = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile； API声明：AAC_HE = 1 差异内容：AAC_HE = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile； API声明：AAC_HE_V2 = 2 差异内容：AAC_HE_V2 = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorderProfile； API声明：aacProfile?: AacProfile; 差异内容：aacProfile?: AacProfile; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：setPickerMode(pickerMode: PickerMode): Promise<void>; 差异内容：setPickerMode(pickerMode: PickerMode): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：excludePickerWindows(excludedWindows: Array<number>): Promise<void>; 差异内容：excludePickerWindows(excludedWindows: Array<number>): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：presentPicker(): Promise<void>; 差异内容：presentPicker(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media； API声明：function createAVTranscoder(): Promise<AVTranscoder>; 差异内容：NA | 类名：media； API声明：function createAVTranscoder(): Promise<AVTranscoder>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContainerFormatType； API声明：CFT_MPEG_4 = 'mp4' 差异内容：NA | 类名：ContainerFormatType； API声明：CFT_MPEG_4 = 'mp4' 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：CodecMimeType； API声明：VIDEO_AVC = 'video/avc' 差异内容：NA | 类名：CodecMimeType； API声明：VIDEO_AVC = 'video/avc' 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：CodecMimeType； API声明：VIDEO_HEVC = 'video/hevc' 差异内容：NA | 类名：CodecMimeType； API声明：VIDEO_HEVC = 'video/hevc' 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media； API声明：interface AVTranscoderConfig 差异内容：NA | 类名：media； API声明：interface AVTranscoderConfig 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：audioBitrate?: number; 差异内容：NA | 类名：AVTranscoderConfig； API声明：audioBitrate?: number; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：audioCodec?: CodecMimeType; 差异内容：NA | 类名：AVTranscoderConfig； API声明：audioCodec?: CodecMimeType; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：fileFormat: ContainerFormatType; 差异内容：NA | 类名：AVTranscoderConfig； API声明：fileFormat: ContainerFormatType; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：videoBitrate?: number; 差异内容：NA | 类名：AVTranscoderConfig； API声明：videoBitrate?: number; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：videoCodec?: CodecMimeType; 差异内容：NA | 类名：AVTranscoderConfig； API声明：videoCodec?: CodecMimeType; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：videoFrameWidth?: number; 差异内容：NA | 类名：AVTranscoderConfig； API声明：videoFrameWidth?: number; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：videoFrameHeight?: number; 差异内容：NA | 类名：AVTranscoderConfig； API声明：videoFrameHeight?: number; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig； API声明：enableBFrame?: boolean; 差异内容：NA | 类名：AVTranscoderConfig； API声明：enableBFrame?: boolean; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media； API声明：interface AVTranscoder 差异内容：NA | 类名：media； API声明：interface AVTranscoder 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：fdSrc: AVFileDescriptor; 差异内容：NA | 类名：AVTranscoder； API声明：fdSrc: AVFileDescriptor; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：fdDst: number; 差异内容：NA | 类名：AVTranscoder； API声明：fdDst: number; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：prepare(config: AVTranscoderConfig): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：prepare(config: AVTranscoderConfig): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：start(): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：start(): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：pause(): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：pause(): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：resume(): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：resume(): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：cancel(): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：cancel(): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：release(): Promise<void>; 差异内容：NA | 类名：AVTranscoder； API声明：release(): Promise<void>; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：on(type: 'complete', callback: Callback<void>): void; 差异内容：NA | 类名：AVTranscoder； API声明：on(type: 'complete', callback: Callback<void>): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：NA | 类名：AVTranscoder； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：on(type: 'progressUpdate', callback: Callback<number>): void; 差异内容：NA | 类名：AVTranscoder； API声明：on(type: 'progressUpdate', callback: Callback<number>): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：off(type: 'complete', callback?: Callback<void>): void; 差异内容：NA | 类名：AVTranscoder； API声明：off(type: 'complete', callback?: Callback<void>): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：NA | 类名：AVTranscoder； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder； API声明：off(type: 'progressUpdate', callback?: Callback<number>): void; 差异内容：NA | 类名：AVTranscoder； API声明：off(type: 'progressUpdate', callback?: Callback<number>): void; 差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
