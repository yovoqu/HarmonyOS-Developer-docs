# AVSession Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：AVSession； API声明：on(type: 'playFromAssetId', callback: (assetId: number) => void): void; 差异内容：NA | 类名：AVSession； API声明：on(type: 'playFromAssetId', callback: (assetId: number) => void): void; 差异内容：20 | api/@ohos.multimedia.avsession.d.ts |
| API废弃版本变更 | 类名：AVSession； API声明：off(type: 'playFromAssetId', callback?: (assetId: number) => void): void; 差异内容：NA | 类名：AVSession； API声明：off(type: 'playFromAssetId', callback?: (assetId: number) => void): void; 差异内容：20 | api/@ohos.multimedia.avsession.d.ts |
| 自定义类型变更 | 类名：avSession； API声明：type AVControlCommandType = 'play' \| 'pause' \| 'stop' \| 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'seek' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite' \| 'playFromAssetId' \| 'answer' \| 'hangUp' \| 'toggleCallMute' \| 'setTargetLoopMode'; 差异内容：'play' \| 'pause' \| 'stop' \| 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'seek' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite' \| 'playFromAssetId' \| 'answer' \| 'hangUp' \| 'toggleCallMute' \| 'setTargetLoopMode' | 类名：avSession； API声明：type AVControlCommandType = 'play' \| 'pause' \| 'stop' \| 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'seek' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite' \| 'playFromAssetId' \| 'playWithAssetId' \| 'answer' \| 'hangUp' \| 'toggleCallMute' \| 'setTargetLoopMode'; 差异内容：'play' \| 'pause' \| 'stop' \| 'playNext' \| 'playPrevious' \| 'fastForward' \| 'rewind' \| 'seek' \| 'setSpeed' \| 'setLoopMode' \| 'toggleFavorite' \| 'playFromAssetId' \| 'playWithAssetId' \| 'answer' \| 'hangUp' \| 'toggleCallMute' \| 'setTargetLoopMode' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：global； API声明：export declare struct AVInputCastPicker 差异内容：export declare struct AVInputCastPicker | api/@ohos.multimedia.avInputCastPicker.d.ets |
| 新增API | NA | 类名：AVInputCastPicker； API声明：@Prop customPicker?: CustomBuilder; 差异内容：@Prop customPicker?: CustomBuilder; | api/@ohos.multimedia.avInputCastPicker.d.ets |
| 新增API | NA | 类名：AVInputCastPicker； API声明：onStateChange?: OnPickerStateCallback; 差异内容：onStateChange?: OnPickerStateCallback; | api/@ohos.multimedia.avInputCastPicker.d.ets |
| 新增API | NA | 类名：global； API声明：export type OnPickerStateCallback = (state: AVCastPickerState) => void; 差异内容：export type OnPickerStateCallback = (state: AVCastPickerState) => void; | api/@ohos.multimedia.avInputCastPicker.d.ets |
| 新增API | NA | 类名：ProtocolType； API声明：TYPE_CAST_PLUS_AUDIO = 8 差异内容：TYPE_CAST_PLUS_AUDIO = 8 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：interface AudioCapabilities 差异内容：interface AudioCapabilities | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AudioCapabilities； API声明：readonly streamInfos: Array<audio.AudioStreamInfo>; 差异内容：readonly streamInfos: Array<audio.AudioStreamInfo>; | api/@ohos.multimedia.avsession.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.multimedia.avInputCastPicker.d.ets 差异内容：AVSessionKit | api/@ohos.multimedia.avInputCastPicker.d.ets |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVSession； API声明：on(type: 'playWithAssetId', callback: Callback&lt;string&gt;): void; 差异内容：on(type: 'playWithAssetId', callback: Callback&lt;string&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AVSession； API声明：off(type: 'playWithAssetId', callback?: Callback&lt;string&gt;): void; 差异内容：off(type: 'playWithAssetId', callback?: Callback&lt;string&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AVMediaDescription； API声明：pcmSrc?: boolean; 差异内容：pcmSrc?: boolean; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：DeviceInfo； API声明：audioCapabilities?: AudioCapabilities; 差异内容：audioCapabilities?: AudioCapabilities; | api/@ohos.multimedia.avsession.d.ts |
