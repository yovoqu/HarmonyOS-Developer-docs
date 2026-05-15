# Media Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AVPlayer； API声明：addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>; 差异内容：addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：addSubtitleFromUrl(url: string): Promise<void>; 差异内容：addSubtitleFromUrl(url: string): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void; 差异内容：on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer； API声明：off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void; 差异内容：off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media； API声明： interface SubtitleInfo 差异内容： interface SubtitleInfo | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo； API声明：duration?: number; 差异内容：duration?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo； API声明：startTime?: number; 差异内容：startTime?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SubtitleInfo； API声明：text?: string; 差异内容：text?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaType； API声明：MEDIA_TYPE_SUBTITLE = 2 差异内容：MEDIA_TYPE_SUBTITLE = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey； API声明：MD_KEY_LANGUAGE = 'language' 差异内容：MD_KEY_LANGUAGE = 'language' | api/@ohos.multimedia.media.d.ts |
