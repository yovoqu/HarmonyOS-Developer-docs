# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global； API声明： declare namespace media 差异内容：SystemCapability.Multimedia.Media | 类名：global； API声明： declare namespace media 差异内容：SystemCapability.Multimedia.Media.Core | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：on(type: 'amplitudeUpdate', callback: Callback<Array<Number>>): void; 差异内容：on(type: 'amplitudeUpdate', callback: Callback<Array<Number>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：off(type: 'amplitudeUpdate', callback?: Callback<Array<Number>>): void; 差异内容：off(type: 'amplitudeUpdate', callback?: Callback<Array<Number>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackStrategy； API声明：preferredAudioLanguage?: string; 差异内容：preferredAudioLanguage?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackStrategy； API声明：preferredSubtitleLanguage?: string; 差异内容：preferredSubtitleLanguage?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackSpeed； API声明：SPEED_FORWARD_3_00_X = 7 差异内容：SPEED_FORWARD_3_00_X = 7 | api/@ohos.multimedia.media.d.ts |
