# IME Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：InputClient； API声明：getAttachOptions(): AttachOptions; 差异内容：801 | 类名：InputClient； API声明：getAttachOptions(): AttachOptions; 差异内容：NA | api/@ohos.inputMethodEngine.d.ts |
| 删除错误码 | 类名：InputClient； API声明：on(type: 'attachOptionsDidChange', callback: Callback&lt;AttachOptions&gt;): void; 差异内容：801 | 类名：InputClient； API声明：on(type: 'attachOptionsDidChange', callback: Callback&lt;AttachOptions&gt;): void; 差异内容：NA | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethod； API声明：function setSimpleKeyboardEnabled(enable: boolean): void; 差异内容：function setSimpleKeyboardEnabled(enable: boolean): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：AttachOptions； API声明：isSimpleKeyboardEnabled?: boolean; 差异内容：isSimpleKeyboardEnabled?: boolean; | api/@ohos.inputMethodEngine.d.ts |
