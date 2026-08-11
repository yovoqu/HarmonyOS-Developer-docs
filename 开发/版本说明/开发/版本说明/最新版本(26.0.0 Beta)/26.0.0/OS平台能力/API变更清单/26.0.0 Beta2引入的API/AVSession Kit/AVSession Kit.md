# AVSession Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AVSession； API声明：setSupportedPlaySpeeds(speeds: Array&lt;number&gt;): Promise&lt;void&gt;; 差异内容：setSupportedPlaySpeeds(speeds: Array&lt;number&gt;): Promise&lt;void&gt;; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：setSupportedLoopModes(loopModes: Array&lt;LoopMode&gt;): Promise&lt;void&gt;; 差异内容：setSupportedLoopModes(loopModes: Array&lt;LoopMode&gt;): Promise&lt;void&gt;; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：setMediaCenterControlType(type: Array&lt;AVMediaCenterControlType&gt;): Promise&lt;void&gt;; 差异内容：setMediaCenterControlType(type: Array&lt;AVMediaCenterControlType&gt;): Promise&lt;void&gt;; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ExtraKey； API声明：REQUIRE_ABILITY_LIST = 'requireAbilityList' 差异内容：REQUIRE_ABILITY_LIST = 'requireAbilityList' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ExtraKey； API声明：SUPPORT_URL_CASTING = 'url-cast' 差异内容：SUPPORT_URL_CASTING = 'url-cast' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：DEVICE_TYPE_CAR = 4 差异内容：DEVICE_TYPE_CAR = 4 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：DEVICE_TYPE_PAD = 6 差异内容：DEVICE_TYPE_PAD = 6 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：DEVICE_TYPE_DEFAULT_CAST_PLUS_STREAM = 7 差异内容：DEVICE_TYPE_DEFAULT_CAST_PLUS_STREAM = 7 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：DEVICE_TYPE_2IN1 = 8 差异内容：DEVICE_TYPE_2IN1 = 8 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType； API声明：DEVICE_TYPE_HIPLAY = 15 差异内容：DEVICE_TYPE_HIPLAY = 15 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：getSupportedPlaySpeeds(): Promise<Array&lt;number&gt;>; 差异内容：getSupportedPlaySpeeds(): Promise<Array&lt;number&gt;>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：getSupportedLoopModes(): Promise<Array&lt;LoopMode&gt;>; 差异内容：getSupportedLoopModes(): Promise<Array&lt;LoopMode&gt;>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：getMediaCenterControlType(): Promise<Array&lt;AVMediaCenterControlType&gt;>; 差异内容：getMediaCenterControlType(): Promise<Array&lt;AVMediaCenterControlType&gt;>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：onMediaCenterControlTypeChanged(callback: Callback<Array&lt;AVMediaCenterControlType&gt;>): void; 差异内容：onMediaCenterControlTypeChanged(callback: Callback<Array&lt;AVMediaCenterControlType&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：offMediaCenterControlTypeChanged(callback?: Callback<Array&lt;AVMediaCenterControlType&gt;>): void; 差异内容：offMediaCenterControlTypeChanged(callback?: Callback<Array&lt;AVMediaCenterControlType&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：onSupportedPlaySpeedsChange(callback: Callback<Array&lt;number&gt;>): void; 差异内容：onSupportedPlaySpeedsChange(callback: Callback<Array&lt;number&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：offSupportedPlaySpeedsChange(callback?: Callback<Array&lt;number&gt;>): void; 差异内容：offSupportedPlaySpeedsChange(callback?: Callback<Array&lt;number&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：onSupportedLoopModesChange(callback: Callback<Array&lt;LoopMode&gt;>): void; 差异内容：onSupportedLoopModesChange(callback: Callback<Array&lt;LoopMode&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController； API声明：offSupportedLoopModesChange(callback?: Callback<Array&lt;LoopMode&gt;>): void; 差异内容：offSupportedLoopModesChange(callback?: Callback<Array&lt;LoopMode&gt;>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：type AVMediaCenterControlType = 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite'; 差异内容：type AVMediaCenterControlType = 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite'; | api/@ohos.multimedia.avsession.d.ts |
