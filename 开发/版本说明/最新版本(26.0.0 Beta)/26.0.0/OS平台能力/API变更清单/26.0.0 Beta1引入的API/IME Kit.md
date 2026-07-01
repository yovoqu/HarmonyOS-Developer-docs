# IME Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-7001

## IME Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty): Promise&lt;boolean&gt;; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：InputClient； API声明：getAttachOptions(): AttachOptions; 差异内容：NA | 类名：InputClient； API声明：getAttachOptions(): AttachOptions; 差异内容：801 | api/@ohos.inputMethodEngine.d.ts |
| 新增错误码 | 类名：InputClient； API声明：on(type: 'attachOptionsDidChange', callback: Callback&lt;AttachOptions&gt;): void; 差异内容：NA | 类名：InputClient； API声明：on(type: 'attachOptionsDidChange', callback: Callback&lt;AttachOptions&gt;): void; 差异内容：801 | api/@ohos.inputMethodEngine.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchInputMethod(target: InputMethodProperty): Promise&lt;boolean&gt;; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：NA | 类名：inputMethod； API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise&lt;boolean&gt;; 差异内容：ohos.permission.CONNECT_IME_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo； API声明：displayId?: number; 差异内容：displayId?: number; | api/@ohos.inputMethod.d.ts |
