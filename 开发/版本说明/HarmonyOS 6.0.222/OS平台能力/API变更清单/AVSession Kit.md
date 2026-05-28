# AVSession Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：avSession； API声明：type AVSessionType = 'audio' \| 'video' \| 'voice_call' \| 'video_call'; 差异内容：'audio' \| 'video' \| 'voice_call' \| 'video_call' | 类名：avSession； API声明：type AVSessionType = 'audio' \| 'video' \| 'voice_call' \| 'video_call' \| 'photo'; 差异内容：'audio' \| 'video' \| 'voice_call' \| 'video_call' \| 'photo' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：function getAVSession(context: Context): Promise&lt;AVSession&gt;; 差异内容：function getAVSession(context: Context): Promise&lt;AVSession&gt;; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：type NoParamCallback = () => void; 差异内容：type NoParamCallback = () => void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：type TwoParamCallback<T, G> = (data1: T, data2: G) => void; 差异内容：type TwoParamCallback<T, G> = (data1: T, data2: G) => void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：readonly sessionTag: string; 差异内容：readonly sessionTag: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：onPlay(callback: Callback&lt;CommandInfo&gt;): void; 差异内容：onPlay(callback: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：onPlayNext(callback: Callback&lt;CommandInfo&gt;): void; 差异内容：onPlayNext(callback: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：onPlayPrevious(callback: Callback&lt;CommandInfo&gt;): void; 差异内容：onPlayPrevious(callback: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：onFastForward(callback: TwoParamCallback<number, CommandInfo>): void; 差异内容：onFastForward(callback: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：onRewind(callback: TwoParamCallback<number, CommandInfo>): void; 差异内容：onRewind(callback: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：offPlay(callback?: Callback&lt;CommandInfo&gt;): void; 差异内容：offPlay(callback?: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：offPlayNext(callback?: Callback&lt;CommandInfo&gt;): void; 差异内容：offPlayNext(callback?: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：offPlayPrevious(callback?: Callback&lt;CommandInfo&gt;): void; 差异内容：offPlayPrevious(callback?: Callback&lt;CommandInfo&gt;): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void; 差异内容：offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession； API声明：offRewind(callback?: TwoParamCallback<number, CommandInfo>): void; 差异内容：offRewind(callback?: TwoParamCallback<number, CommandInfo>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：interface MenuPosition 差异内容：interface MenuPosition | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition； API声明：x: number; 差异内容：x: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition； API声明：y: number; 差异内容：y: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition； API声明：width: number; 差异内容：width: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：MenuPosition； API声明：height: number; 差异内容：height: number; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVCastPickerOptions； API声明：pickerStyle?: AVCastPickerStyle; 差异内容：pickerStyle?: AVCastPickerStyle; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVCastPickerOptions； API声明：menuPosition?: MenuPosition; 差异内容：menuPosition?: MenuPosition; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVControlCommand； API声明：commandInfo?: CommandInfo; 差异内容：commandInfo?: CommandInfo; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：interface CommandInfo 差异内容：interface CommandInfo | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo； API声明：callerBundleName?: string; 差异内容：callerBundleName?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo； API声明：callerModuleName?: string; 差异内容：callerModuleName?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo； API声明：callerDeviceId?: string; 差异内容：callerDeviceId?: string; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CommandInfo； API声明：callerType?: CallerType; 差异内容：callerType?: CallerType; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession； API声明：enum CallerType 差异内容：enum CallerType | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType； API声明：TYPE_CAST = 'cast' 差异内容：TYPE_CAST = 'cast' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType； API声明：TYPE_BLUETOOTH = 'bluetooth' 差异内容：TYPE_BLUETOOTH = 'bluetooth' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType； API声明：TYPE_NEARLINK = 'nearlink' 差异内容：TYPE_NEARLINK = 'nearlink' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：CallerType； API声明：TYPE_APP = 'app' 差异内容：TYPE_APP = 'app' | api/@ohos.multimedia.avsession.d.ts |
