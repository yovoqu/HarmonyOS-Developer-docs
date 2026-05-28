# Audio Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：InterruptHint； API声明：INTERRUPT_HINT_MUTE = 6 差异内容：INTERRUPT_HINT_MUTE = 6 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：InterruptHint； API声明：INTERRUPT_HINT_UNMUTE = 7 差异内容：INTERRUPT_HINT_UNMUTE = 7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType； API声明：SOURCE_TYPE_LIVE = 17 差异内容：SOURCE_TYPE_LIVE = 17 | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioManager； API声明：on(type: 'audioSceneChange', callback: Callback&lt;AudioScene&gt;): void; 差异内容：on(type: 'audioSceneChange', callback: Callback&lt;AudioScene&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioManager； API声明：off(type: 'audioSceneChange', callback?: Callback&lt;AudioScene&gt;): void; 差异内容：off(type: 'audioSceneChange', callback?: Callback&lt;AudioScene&gt;): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioStreamManager； API声明：isAcousticEchoCancelerSupported(sourceType: SourceType): boolean; 差异内容：isAcousticEchoCancelerSupported(sourceType: SourceType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：AudioCapturer； API声明：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise&lt;void&gt;; 差异内容：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise&lt;void&gt;; | api/@ohos.multimedia.audio.d.ts |
