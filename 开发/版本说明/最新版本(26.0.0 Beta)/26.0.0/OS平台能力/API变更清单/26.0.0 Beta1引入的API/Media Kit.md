# Media Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：media； API声明：function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource \| undefined; 差异内容：function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource \| undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource \| undefined; 差异内容：function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource \| undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface AVTimedMetaData 差异内容：interface AVTimedMetaData | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData； API声明：id?: string; 差异内容：id?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData； API声明：classify?: string; 差异内容：classify?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData； API声明：start: number; 差异内容：start: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData； API声明：duration: number; 差异内容：duration: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData； API声明：contents: Record<string, object>; 差异内容：contents: Record<string, object>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor； API声明：fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata \| undefined>; 差异内容：fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata \| undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor； API声明：fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number): Promise<image.PixelMap \| undefined>; 差异内容：fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number): Promise<image.PixelMap \| undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor； API声明：fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number, callback: OnFrameFetched): void; 差异内容：fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number, callback: OnFrameFetched): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadata； API声明：encoder?: string; 差异内容：encoder?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface VideoSize 差异内容：interface VideoSize | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：VideoSize； API声明：width?: number; 差异内容：width?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：VideoSize； API声明：height?: number; 差异内容：height?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：interface TrackSelectionFilter 差异内容：interface TrackSelectionFilter | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：maxVideoBitrate?: number; 差异内容：maxVideoBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：minVideoBitrate?: number; 差异内容：minVideoBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：maxVideoFrameRate?: number; 差异内容：maxVideoFrameRate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：minVideoFrameRate?: number; 差异内容：minVideoFrameRate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：maxVideoResolution?: VideoSize; 差异内容：maxVideoResolution?: VideoSize; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：minVideoResolution?: VideoSize; 差异内容：minVideoResolution?: VideoSize; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：preferredVideoMimeTypes?: Array&lt;string&gt;; 差异内容：preferredVideoMimeTypes?: Array&lt;string&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：maxAudioBitrate?: number; 差异内容：maxAudioBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：minAudioBitrate?: number; 差异内容：minAudioBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：maxAudioChannels?: number; 差异内容：maxAudioChannels?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：preferredAudioMimeTypes?: Array&lt;string&gt;; 差异内容：preferredAudioMimeTypes?: Array&lt;string&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：preferredAudioLanguages?: Array&lt;string&gt;; 差异内容：preferredAudioLanguages?: Array&lt;string&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter； API声明：preferredSubtitleLanguages?: Array&lt;string&gt;; 差异内容：preferredSubtitleLanguages?: Array&lt;string&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getTrackSelectionFilter(): Promise&lt;TrackSelectionFilter&gt;; 差异内容：getTrackSelectionFilter(): Promise&lt;TrackSelectionFilter&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：setTrackSelectionFilter(filter: TrackSelectionFilter): Promise&lt;void&gt;; 差异内容：setTrackSelectionFilter(filter: TrackSelectionFilter): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getLoadedTimeRanges(): Promise<Array&lt;Range&gt;>; 差异内容：getLoadedTimeRanges(): Promise<Array&lt;Range&gt;>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getSeekableTimeRanges(): Promise<Array&lt;Range&gt;>; 差异内容：getSeekableTimeRanges(): Promise<Array&lt;Range&gt;>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：seekToDefaultPosition(): void; 差异内容：seekToDefaultPosition(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：advanceToNextMediaSource(): Promise&lt;void&gt;; 差异内容：advanceToNextMediaSource(): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：advanceToPrevMediaSource(): Promise&lt;void&gt;; 差异内容：advanceToPrevMediaSource(): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getCurrentMediaSource(): MediaSource \| undefined; 差异内容：getCurrentMediaSource(): MediaSource \| undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：addPlaybackMediaSource(src: MediaSource, id?: string): Promise&lt;string&gt;; 差异内容：addPlaybackMediaSource(src: MediaSource, id?: string): Promise&lt;string&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：removePlaybackMediaSource(id: string): Promise&lt;void&gt;; 差异内容：removePlaybackMediaSource(id: string): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：clearPlaybackList(): Promise&lt;void&gt;; 差异内容：clearPlaybackList(): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：advanceToMediaSource(id: string): Promise&lt;void&gt;; 差异内容：advanceToMediaSource(id: string): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：getMediaSources(): Array<MediaSource \| undefined>; 差异内容：getMediaSources(): Array<MediaSource \| undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：playlistLoopMode?: PlaylistLoopMode; 差异内容：playlistLoopMode?: PlaylistLoopMode; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：onPlaybackContentChanged(callback: Callback&lt;string&gt;): void; 差异内容：onPlaybackContentChanged(callback: Callback&lt;string&gt;): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：offPlaybackContentChanged(callback?: Callback&lt;string&gt;): void; 差异内容：offPlaybackContentChanged(callback?: Callback&lt;string&gt;): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：onTimedMetaData(callback: Callback&lt;AVTimedMetaData&gt;): void; 差异内容：onTimedMetaData(callback: Callback&lt;AVTimedMetaData&gt;): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：offTimedMetaData(callback?: Callback&lt;AVTimedMetaData&gt;): void; 差异内容：offTimedMetaData(callback?: Callback&lt;AVTimedMetaData&gt;): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明：enum PlaylistLoopMode 差异内容：enum PlaylistLoopMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode； API声明：PLAYLIST_LOOP_MODE_ALL = 1 差异内容：PLAYLIST_LOOP_MODE_ALL = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode； API声明：PLAYLIST_LOOP_MODE_ONE = 2 差异内容：PLAYLIST_LOOP_MODE_ONE = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode； API声明：PLAYLIST_LOOP_MODE_SHUFFLE = 3 差异内容：PLAYLIST_LOOP_MODE_SHUFFLE = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode； API声明：PLAYLIST_LOOP_MODE_NONE = 4 差异内容：PLAYLIST_LOOP_MODE_NONE = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSource； API声明：getID(): string; 差异内容：getID(): string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorder； API声明：setMetadata(metadata: Record<string, string>): void; 差异内容：setMetadata(metadata: Record<string, string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：APP_ONLY = 3 差异内容：APP_ONLY = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：WINDOW_AND_APP = 4 差异内容：WINDOW_AND_APP = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：SCREEN_AND_APP = 5 差异内容：SCREEN_AND_APP = 5 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode； API声明：SCREEN_WINDOW_AND_APP = 6 差异内容：SCREEN_WINDOW_AND_APP = 6 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode； API声明：SCREENCAPTURE_STATE_PAUSED_BY_USER = 11 差异内容：SCREENCAPTURE_STATE_PAUSED_BY_USER = 11 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode； API声明：SCREENCAPTURE_STATE_RESUMED_BY_USER = 12 差异内容：SCREENCAPTURE_STATE_RESUMED_BY_USER = 12 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode； API声明：SCREENCAPTURE_STATE_PAUSED_BY_APP = 13 差异内容：SCREENCAPTURE_STATE_PAUSED_BY_APP = 13 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode； API声明：SCREENCAPTURE_STATE_RESUMED_BY_APP = 14 差异内容：SCREENCAPTURE_STATE_RESUMED_BY_APP = 14 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStrategy； API声明：enablePause?: boolean; 差异内容：enablePause?: boolean; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：pauseRecording(): Promise&lt;void&gt;; 差异内容：pauseRecording(): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder； API声明：resumeRecording(): Promise&lt;void&gt;; 差异内容：resumeRecording(): Promise&lt;void&gt;; | api/@ohos.multimedia.media.d.ts |
