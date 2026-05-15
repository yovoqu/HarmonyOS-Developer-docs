# IME Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5051

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：inputMethod； API声明：export type SetPreviewTextCallback = (text: string, range: Range) => void; 差异内容：export type SetPreviewTextCallback = (text: string, range: Range) => void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodController； API声明：on(type: 'setPreviewText', callback: SetPreviewTextCallback): void; 差异内容：on(type: 'setPreviewText', callback: SetPreviewTextCallback): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodController； API声明：off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void; 差异内容：off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodController； API声明：on(type: 'finishTextPreview', callback: Callback<void>): void; 差异内容：on(type: 'finishTextPreview', callback: Callback<void>): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：InputMethodController； API声明：off(type: 'finishTextPreview', callback?: Callback<void>): void; 差异内容：off(type: 'finishTextPreview', callback?: Callback<void>): void; | api/@ohos.inputMethod.d.ts |
