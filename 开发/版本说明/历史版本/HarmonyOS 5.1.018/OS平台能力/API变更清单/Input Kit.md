# Input Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：pointer； API声明：function setPointerVisible(visible: boolean, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：pointer； API声明：function setPointerVisible(visible: boolean, callback: AsyncCallback&lt;void&gt;): void; 差异内容：801 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增错误码 | 类名：pointer； API声明：function setPointerVisible(visible: boolean): Promise&lt;void&gt;; 差异内容：NA | 类名：pointer； API声明：function setPointerVisible(visible: boolean): Promise&lt;void&gt;; 差异内容：801 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle； API声明：MIDDLE_BTN_EAST_WEST 差异内容：MIDDLE_BTN_EAST_WEST | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_DAGGER_CLICK = 3211 差异内容：KEYCODE_DAGGER_CLICK = 3211 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_DAGGER_DOUBLE_CLICK = 3212 差异内容：KEYCODE_DAGGER_DOUBLE_CLICK = 3212 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode； API声明：KEYCODE_DAGGER_LONG_PRESS = 3213 差异内容：KEYCODE_DAGGER_LONG_PRESS = 3213 | api/@ohos.multimodalInput.keyCode.d.ts |
| 起始版本有变化 | 类名：infraredEmitter； API声明：interface InfraredFrequency 差异内容：12 | 类名：infraredEmitter； API声明：interface InfraredFrequency 差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：InfraredFrequency； API声明：max: number; 差异内容：12 | 类名：InfraredFrequency； API声明：max: number; 差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：InfraredFrequency； API声明：min: number; 差异内容：12 | 类名：InfraredFrequency； API声明：min: number; 差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：infraredEmitter； API声明：function transmitInfrared(infraredFrequency: number, pattern: Array&lt;number&gt;): void; 差异内容：12 | 类名：infraredEmitter； API声明：function transmitInfrared(infraredFrequency: number, pattern: Array&lt;number&gt;): void; 差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：infraredEmitter； API声明：function getInfraredFrequencies(): Array&lt;InfraredFrequency&gt;; 差异内容：12 | 类名：infraredEmitter； API声明：function getInfraredFrequencies(): Array&lt;InfraredFrequency&gt;; 差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
