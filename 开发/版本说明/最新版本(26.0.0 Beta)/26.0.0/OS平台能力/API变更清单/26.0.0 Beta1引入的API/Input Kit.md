# Input Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-7001

## Input Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace inputEventClient 差异内容：declare namespace inputEventClient | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient； API声明：interface KeyboardController 差异内容：interface KeyboardController | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyboardController； API声明：pressKey(keyCode: KeyCode): Promise&lt;void&gt;; 差异内容：pressKey(keyCode: KeyCode): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyboardController； API声明：releaseKey(keyCode: KeyCode): Promise&lt;void&gt;; 差异内容：releaseKey(keyCode: KeyCode): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient； API声明：function createKeyboardController(): Promise&lt;KeyboardController&gt;; 差异内容：function createKeyboardController(): Promise&lt;KeyboardController&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient； API声明：interface MouseController 差异内容：interface MouseController | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：moveTo(displayId: number, displayX: number, displayY: number): Promise&lt;void&gt;; 差异内容：moveTo(displayId: number, displayX: number, displayY: number): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：pressButton(button: Button): Promise&lt;void&gt;; 差异内容：pressButton(button: Button): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：releaseButton(button: Button): Promise&lt;void&gt;; 差异内容：releaseButton(button: Button): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：beginAxis(axis: Axis, value: number): Promise&lt;void&gt;; 差异内容：beginAxis(axis: Axis, value: number): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：updateAxis(axis: Axis, value: number): Promise&lt;void&gt;; 差异内容：updateAxis(axis: Axis, value: number): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController； API声明：endAxis(axis: Axis): Promise&lt;void&gt;; 差异内容：endAxis(axis: Axis): Promise&lt;void&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient； API声明：function createMouseController(): Promise&lt;MouseController&gt;; 差异内容：function createMouseController(): Promise&lt;MouseController&gt;; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_MOUSE_ASSISTANT = 2732 差异内容：KEYCODE_MOUSE_ASSISTANT = 2732 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_MOUSE_INTELLIGENCE_SELECTION = 2733 差异内容：KEYCODE_MOUSE_INTELLIGENCE_SELECTION = 2733 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_AOD_SINGLE_CLICK = 2740 差异内容：KEYCODE_AOD_SINGLE_CLICK = 2740 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_XKEY = 3232 差异内容：KEYCODE_XKEY = 3232 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_FINGERPRINT_SLIDE_UP = 3233 差异内容：KEYCODE_FINGERPRINT_SLIDE_UP = 3233 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_FINGERPRINT_SLIDE_DOWN = 3234 差异内容：KEYCODE_FINGERPRINT_SLIDE_DOWN = 3234 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：Action； API声明：PULL_DOWN = 4 差异内容：PULL_DOWN = 4 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增API | NA | 类名：Action； API声明：PULL_MOVE = 5 差异内容：PULL_MOVE = 5 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增API | NA | 类名：Action； API声明：PULL_UP = 6 差异内容：PULL_UP = 6 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.multimodalInput.inputEventClient.d.ts 差异内容：InputKit | api/@ohos.multimodalInput.inputEventClient.d.ts |
