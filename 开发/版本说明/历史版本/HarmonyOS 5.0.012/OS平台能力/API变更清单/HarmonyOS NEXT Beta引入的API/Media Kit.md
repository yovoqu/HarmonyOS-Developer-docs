# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：AudioRecorder； API声明：prepare(config: AudioRecorderConfig): void; 差异内容：NA | 类名：AudioRecorder； API声明：prepare(config: AudioRecorderConfig): void; 差异内容：201 | api/@ohos.multimedia.media.d.ts |
| 错误码变更 | 类名：AVScreenCaptureRecorder； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：5400103,5400105 | 类名：AVScreenCaptureRecorder； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：201,5400103,5400105 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：function createAVTranscoder(): Promise<AVTranscoder>; 差异内容：function createAVTranscoder(): Promise<AVTranscoder>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVImageQueryOptions； API声明：AV_IMAGE_QUERY_CLOSEST 差异内容：AV_IMAGE_QUERY_CLOSEST | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type OnTrackChangeHandler = (index: number, isSelected: boolean) => void; 差异内容：type OnTrackChangeHandler = (index: number, isSelected: boolean) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getSelectedTracks(): Promise<Array<number>>; 差异内容：getSelectedTracks(): Promise<Array<number>>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：selectTrack(index: number, mode?: SwitchMode): Promise<void>; 差异内容：selectTrack(index: number, mode?: SwitchMode): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：deselectTrack(index: number): Promise<void>; 差异内容：deselectTrack(index: number): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>; 差异内容：setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>; 差异内容：setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getPlaybackInfo(): Promise<PlaybackInfo>; 差异内容：getPlaybackInfo(): Promise<PlaybackInfo>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：on(type: 'trackChange', callback: OnTrackChangeHandler): void; 差异内容：on(type: 'trackChange', callback: OnTrackChangeHandler): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：off(type: 'trackChange', callback?: OnTrackChangeHandler): void; 差异内容：off(type: 'trackChange', callback?: OnTrackChangeHandler): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void; 差异内容：on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void; 差异内容：off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： interface PlaybackInfo 差异内容： interface PlaybackInfo | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： enum PlaybackInfoKey 差异内容： enum PlaybackInfoKey | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackInfoKey； API声明：SERVER_IP_ADDRESS = 'server_ip_address' 差异内容：SERVER_IP_ADDRESS = 'server_ip_address' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackInfoKey； API声明：AVG_DOWNLOAD_RATE = 'average_download_rate' 差异内容：AVG_DOWNLOAD_RATE = 'average_download_rate' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackInfoKey； API声明：DOWNLOAD_RATE = 'download_rate' 差异内容：DOWNLOAD_RATE = 'download_rate' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackInfoKey； API声明：IS_DOWNLOADING = 'is_downloading' 差异内容：IS_DOWNLOADING = 'is_downloading' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackInfoKey； API声明：BUFFER_DURATION = 'buffer_duration' 差异内容：BUFFER_DURATION = 'buffer_duration' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackStrategy； API声明：mutedMediaType?: MediaType; 差异内容：mutedMediaType?: MediaType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorder； API声明：on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void; 差异内容：on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorder； API声明：off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void; 差异内容：off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：ContainerFormatType； API声明：CFT_WAV = 'wav' 差异内容：CFT_WAV = 'wav' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey； API声明：MD_KEY_TRACK_NAME = 'track_name' 差异内容：MD_KEY_TRACK_NAME = 'track_name' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey； API声明：MD_KEY_HDR_TYPE = 'hdr_type' 差异内容：MD_KEY_HDR_TYPE = 'hdr_type' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AudioSourceType； API声明：AUDIO_SOURCE_TYPE_VOICE_RECOGNITION = 2 差异内容：AUDIO_SOURCE_TYPE_VOICE_RECOGNITION = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AudioSourceType； API声明：AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION = 7 差异内容：AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION = 7 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AudioSourceType； API声明：AUDIO_SOURCE_TYPE_VOICE_MESSAGE = 10 差异内容：AUDIO_SOURCE_TYPE_VOICE_MESSAGE = 10 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AudioSourceType； API声明：AUDIO_SOURCE_TYPE_CAMCORDER = 13 差异内容：AUDIO_SOURCE_TYPE_CAMCORDER = 13 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： enum FileGenerationMode 差异内容： enum FileGenerationMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FileGenerationMode； API声明：APP_CREATE = 0 差异内容：APP_CREATE = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FileGenerationMode； API声明：AUTO_CREATE_CAMERA_SCENE = 1 差异内容：AUTO_CREATE_CAMERA_SCENE = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorderConfig； API声明：fileGenerationMode?: FileGenerationMode; 差异内容：fileGenerationMode?: FileGenerationMode; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： enum SwitchMode 差异内容： enum SwitchMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SwitchMode； API声明：SMOOTH = 0 差异内容：SMOOTH = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SwitchMode； API声明：SEGMENT = 1 差异内容：SEGMENT = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SwitchMode； API声明：CLOSEST = 2 差异内容：CLOSEST = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：CodecMimeType； API声明：AUDIO_G711MU = 'audio/g711mu' 差异内容：AUDIO_G711MU = 'audio/g711mu' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode； API声明：SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10 差异内容：SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：skipPrivacyMode(windowIDs: Array<number>): Promise<void>; 差异内容：skipPrivacyMode(windowIDs: Array<number>): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： interface AVTranscoderConfig 差异内容： interface AVTranscoderConfig | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：audioBitrate?: number; 差异内容：audioBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：audioCodec?: CodecMimeType; 差异内容：audioCodec?: CodecMimeType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：fileFormat: ContainerFormatType; 差异内容：fileFormat: ContainerFormatType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：videoBitrate?: number; 差异内容：videoBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：videoCodec?: CodecMimeType; 差异内容：videoCodec?: CodecMimeType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：videoFrameWidth?: number; 差异内容：videoFrameWidth?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig； API声明：videoFrameHeight?: number; 差异内容：videoFrameHeight?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： interface AVTranscoder 差异内容： interface AVTranscoder | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：fdSrc: AVFileDescriptor; 差异内容：fdSrc: AVFileDescriptor; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：fdDst: number; 差异内容：fdDst: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：prepare(config: AVTranscoderConfig): Promise<void>; 差异内容：prepare(config: AVTranscoderConfig): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：start(): Promise<void>; 差异内容：start(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：pause(): Promise<void>; 差异内容：pause(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：resume(): Promise<void>; 差异内容：resume(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：cancel(): Promise<void>; 差异内容：cancel(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：release(): Promise<void>; 差异内容：release(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：on(type: 'complete', callback: Callback<void>): void; 差异内容：on(type: 'complete', callback: Callback<void>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：on(type: 'progressUpdate', callback: Callback<number>): void; 差异内容：on(type: 'progressUpdate', callback: Callback<number>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：off(type: 'complete', callback?: Callback<void>): void; 差异内容：off(type: 'complete', callback?: Callback<void>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder； API声明：off(type: 'progressUpdate', callback?: Callback<number>): void; 差异内容：off(type: 'progressUpdate', callback?: Callback<number>): void; | api/@ohos.multimedia.media.d.ts |
