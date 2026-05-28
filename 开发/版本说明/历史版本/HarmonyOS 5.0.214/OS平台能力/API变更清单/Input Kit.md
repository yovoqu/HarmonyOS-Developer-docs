# Input Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace inputConsumer 差异内容： declare namespace inputConsumer | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer； API声明： interface HotkeyOptions 差异内容： interface HotkeyOptions | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions； API声明：preKeys: Array&lt;number&gt;; 差异内容：preKeys: Array&lt;number&gt;; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions； API声明：finalKey: number; 差异内容：finalKey: number; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions； API声明：isRepeat?: boolean; 差异内容：isRepeat?: boolean; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer； API声明：function getAllSystemHotkeys(): Promise<Array&lt;HotkeyOptions&gt;>; 差异内容：function getAllSystemHotkeys(): Promise<Array&lt;HotkeyOptions&gt;>; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer； API声明：function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback&lt;HotkeyOptions&gt;): void; 差异内容：function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback&lt;HotkeyOptions&gt;): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer； API声明：function off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback&lt;HotkeyOptions&gt;): void; 差异内容：function off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback&lt;HotkeyOptions&gt;): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputDevice； API声明：function getIntervalSinceLastInput(): Promise&lt;number&gt;; 差异内容：function getIntervalSinceLastInput(): Promise&lt;number&gt;; | api/@ohos.multimodalInput.inputDevice.d.ts |
