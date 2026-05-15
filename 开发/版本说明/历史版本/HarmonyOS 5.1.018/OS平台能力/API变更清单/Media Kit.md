# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AVErrorCode； API声明：AVERR_SEEK_CONTINUOUS_UNSUPPORTED = 5410002 差异内容：AVERR_SEEK_CONTINUOUS_UNSUPPORTED = 5410002 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVErrorCode； API声明：AVERR_SUPER_RESOLUTION_UNSUPPORTED = 5410003 差异内容：AVERR_SUPER_RESOLUTION_UNSUPPORTED = 5410003 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVErrorCode； API声明：AVERR_SUPER_RESOLUTION_NOT_ENABLED = 5410004 差异内容：AVERR_SUPER_RESOLUTION_NOT_ENABLED = 5410004 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type OnSuperResolutionChanged = (enabled: boolean) => void; 差异内容：type OnSuperResolutionChanged = (enabled: boolean) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface SeiMessage 差异内容：interface SeiMessage | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SeiMessage； API声明：payloadType: number; 差异内容：payloadType: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SeiMessage； API声明：payload: ArrayBuffer; 差异内容：payload: ArrayBuffer; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: number) => void; 差异内容：type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number; 差异内容：type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void; 差异内容：type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：type SourceCloseCallback = (uuid: number) => void; 差异内容：type SourceCloseCallback = (uuid: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface MediaSourceLoader 差异内容：interface MediaSourceLoader | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoader； API声明：open: SourceOpenCallback; 差异内容：open: SourceOpenCallback; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoader； API声明：read: SourceReadCallback; 差异内容：read: SourceReadCallback; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoader； API声明：close: SourceCloseCallback; 差异内容：close: SourceCloseCallback; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：enum LoadingRequestError 差异内容：enum LoadingRequestError | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_SUCCESS = 0 差异内容：LOADING_ERROR_SUCCESS = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_NOT_READY = 1 差异内容：LOADING_ERROR_NOT_READY = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_NO_RESOURCE = 2 差异内容：LOADING_ERROR_NO_RESOURCE = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_INVAID_HANDLE = 3 差异内容：LOADING_ERROR_INVAID_HANDLE = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_ACCESS_DENIED = 4 差异内容：LOADING_ERROR_ACCESS_DENIED = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_ACCESS_TIMEOUT = 5 差异内容：LOADING_ERROR_ACCESS_TIMEOUT = 5 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：LoadingRequestError； API声明：LOADING_ERROR_AUTHORIZE_FAILED = 6 差异内容：LOADING_ERROR_AUTHORIZE_FAILED = 6 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface MediaSourceLoadingRequest 差异内容：interface MediaSourceLoadingRequest | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoadingRequest； API声明：url: string; 差异内容：url: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoadingRequest； API声明：header?: Record<string, string>; 差异内容：header?: Record<string, string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoadingRequest； API声明：respondData(uuid: number, offset: number, buffer: ArrayBuffer): number; 差异内容：respondData(uuid: number, offset: number, buffer: ArrayBuffer): number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoadingRequest； API声明：respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void; 差异内容：respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSourceLoadingRequest； API声明：finishLoading(uuid: number, state: LoadingRequestError): void; 差异内容：finishLoading(uuid: number, state: LoadingRequestError): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：ContainerFormatType； API声明：CFT_AMR = 'amr' 差异内容：CFT_AMR = 'amr' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SeekMode； API声明：SEEK_CONTINUOUS = 3 差异内容：SEEK_CONTINUOUS = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：CodecMimeType； API声明：AUDIO_AMR_NB = 'audio/3gpp' 差异内容：AUDIO_AMR_NB = 'audio/3gpp' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：CodecMimeType； API声明：AUDIO_AMR_WB = 'audio/amr-wb' 差异内容：AUDIO_AMR_WB = 'audio/amr-wb' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：enum AVScreenCaptureFillMode 差异内容：enum AVScreenCaptureFillMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureFillMode； API声明：PRESERVE_ASPECT_RATIO = 0 差异内容：PRESERVE_ASPECT_RATIO = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureFillMode； API声明：SCALE_TO_FILL = 1 差异内容：SCALE_TO_FILL = 1 | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode): Promise<void>; 差异内容：setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：isSeekContinuousSupported(): boolean; 差异内容：isSeekContinuousSupported(): boolean; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：getPlaybackPosition(): number; 差异内容：getPlaybackPosition(): number; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：setSuperResolution(enabled: boolean): Promise<void>; 差异内容：setSuperResolution(enabled: boolean): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：setVideoWindowSize(width: number, height: number): Promise<void>; 差异内容：setVideoWindowSize(width: number, height: number): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: OnSeiMessageHandle): void; 差异内容：on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: OnSeiMessageHandle): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: OnSeiMessageHandle): void; 差异内容：off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: OnSeiMessageHandle): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：on(type: 'superResolutionChanged', callback: OnSuperResolutionChanged): void; 差异内容：on(type: 'superResolutionChanged', callback: OnSuperResolutionChanged): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVPlayer； API声明：off(type: 'superResolutionChanged', callback?: OnSuperResolutionChanged): void; 差异内容：off(type: 'superResolutionChanged', callback?: OnSuperResolutionChanged): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：MediaSource； API声明：setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void; 差异内容：setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：SoundPool； API声明：on(type: 'playFinishedWithStreamId', callback: Callback<number>): void; 差异内容：on(type: 'playFinishedWithStreamId', callback: Callback<number>): void; | api/multimedia/soundPool.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：SoundPool； API声明：off(type: 'playFinishedWithStreamId'): void; 差异内容：off(type: 'playFinishedWithStreamId'): void; | api/multimedia/soundPool.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PlaybackStrategy； API声明：preferredBufferDurationForPlaying?: number; 差异内容：preferredBufferDurationForPlaying?: number; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PlaybackStrategy； API声明：enableSuperResolution?: boolean; 差异内容：enableSuperResolution?: boolean; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PlaybackStrategy； API声明：thresholdForAutoQuickPlay?: number; 差异内容：thresholdForAutoQuickPlay?: number; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AVRecorderConfig； API声明：maxDuration?: number; 差异内容：maxDuration?: number; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AVScreenCaptureRecordConfig； API声明：fillMode?: AVScreenCaptureFillMode; 差异内容：fillMode?: AVScreenCaptureFillMode; | api/@ohos.multimedia.media.d.ts |
