# AVSession Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：avSession； API声明：enum DecoderType 差异内容：enum DecoderType | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType； API声明：OH_AVCODEC_MIMETYPE_VIDEO_AVC = "video/avc" 差异内容：OH_AVCODEC_MIMETYPE_VIDEO_AVC = "video/avc" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType； API声明：OH_AVCODEC_MIMETYPE_VIDEO_HEVC = "video/hevc" 差异内容：OH_AVCODEC_MIMETYPE_VIDEO_HEVC = "video/hevc" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType； API声明：OH_AVCODEC_MIMETYPE_AUDIO_VIVID = "audio/av3a" 差异内容：OH_AVCODEC_MIMETYPE_AUDIO_VIVID = "audio/av3a" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：enum ResolutionLevel 差异内容：enum ResolutionLevel | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel； API声明：RESOLUTION_480P = 0 差异内容：RESOLUTION_480P = 0 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel； API声明：RESOLUTION_720P = 1 差异内容：RESOLUTION_720P = 1 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel； API声明：RESOLUTION_1080P = 2 差异内容：RESOLUTION_1080P = 2 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel； API声明：RESOLUTION_2K = 3 差异内容：RESOLUTION_2K = 3 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel； API声明：RESOLUTION_4K = 4 差异内容：RESOLUTION_4K = 4 | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVCastController； API声明：getSupportedDecoders(): Promise<Array&lt;DecoderType&gt;>; 差异内容：getSupportedDecoders(): Promise<Array&lt;DecoderType&gt;>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVCastController； API声明：getRecommendedResolutionLevel(decoderType: DecoderType): Promise&lt;ResolutionLevel&gt;; 差异内容：getRecommendedResolutionLevel(decoderType: DecoderType): Promise&lt;ResolutionLevel&gt;; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVCastController； API声明：getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>; 差异内容：getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVCastController； API声明：getSupportedPlaySpeeds(): Promise<Array&lt;number&gt;>; 差异内容：getSupportedPlaySpeeds(): Promise<Array&lt;number&gt;>; | api/@ohos.multimedia.avsession.d.ts |
