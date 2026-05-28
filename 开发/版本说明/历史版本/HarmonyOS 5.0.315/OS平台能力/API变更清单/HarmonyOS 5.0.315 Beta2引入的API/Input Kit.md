# Input Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pointer； API声明：function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise&lt;void&gt;; 差异内容：function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise&lt;void&gt;; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer； API声明： interface CustomCursor 差异内容： interface CustomCursor | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor； API声明：pixelMap: image.PixelMap; 差异内容：pixelMap: image.PixelMap; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor； API声明：focusX?: number; 差异内容：focusX?: number; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor； API声明：focusY?: number; 差异内容：focusY?: number; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer； API声明： interface CursorConfig 差异内容： interface CursorConfig | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CursorConfig； API声明：followSystem: boolean; 差异内容：followSystem: boolean; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：infraredEmitter； API声明： interface InfraredFrequency 差异内容： interface InfraredFrequency | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：InfraredFrequency； API声明：max: number; 差异内容：max: number; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：InfraredFrequency； API声明：min: number; 差异内容：min: number; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：infraredEmitter； API声明：function transmitInfrared(infraredFrequency: number, pattern: Array&lt;number&gt;): void; 差异内容：function transmitInfrared(infraredFrequency: number, pattern: Array&lt;number&gt;): void; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：infraredEmitter； API声明：function getInfraredFrequencies(): Array&lt;InfraredFrequency&gt;; 差异内容：function getInfraredFrequencies(): Array&lt;InfraredFrequency&gt;; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：inputDevice； API声明： enum FunctionKey 差异内容： enum FunctionKey | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：FunctionKey； API声明：CAPS_LOCK = 1 差异内容：CAPS_LOCK = 1 | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice； API声明：function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise&lt;void&gt;; 差异内容：function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice； API声明：function isFunctionKeyEnabled(functionKey: FunctionKey): Promise&lt;boolean&gt;; 差异内容：function isFunctionKeyEnabled(functionKey: FunctionKey): Promise&lt;boolean&gt;; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_A = 2301 差异内容：KEYCODE_BUTTON_A = 2301 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_B = 2302 差异内容：KEYCODE_BUTTON_B = 2302 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_X = 2304 差异内容：KEYCODE_BUTTON_X = 2304 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_Y = 2305 差异内容：KEYCODE_BUTTON_Y = 2305 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_L1 = 2307 差异内容：KEYCODE_BUTTON_L1 = 2307 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_R1 = 2308 差异内容：KEYCODE_BUTTON_R1 = 2308 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_L2 = 2309 差异内容：KEYCODE_BUTTON_L2 = 2309 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_R2 = 2310 差异内容：KEYCODE_BUTTON_R2 = 2310 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_SELECT = 2311 差异内容：KEYCODE_BUTTON_SELECT = 2311 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_START = 2312 差异内容：KEYCODE_BUTTON_START = 2312 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_MODE = 2313 差异内容：KEYCODE_BUTTON_MODE = 2313 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_THUMBL = 2314 差异内容：KEYCODE_BUTTON_THUMBL = 2314 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_BUTTON_THUMBR = 2315 差异内容：KEYCODE_BUTTON_THUMBR = 2315 | api/@ohos.multimodalInput.keyCode.d.ts |
