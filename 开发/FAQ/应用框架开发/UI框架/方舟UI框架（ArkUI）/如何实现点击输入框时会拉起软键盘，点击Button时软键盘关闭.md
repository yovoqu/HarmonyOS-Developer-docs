# 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265

可以通过调用输入法服务 @kit.IMEKit 的 stopInputSession()方法来隐藏软键盘。示例代码如下：

```ts
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct ClickBlankHideKeyboard {
build() {
Column({ space: 12 }) {
TextInput({ placeholder: 'Please enter your account' })
.height(40)
TextInput({ placeholder: 'Please input a password' })
.height(40)
Button('log on').width('100%')
.onClick(() => {
// Exit text editing mode
try {
this.inputRef.blur();
// Close the current input session and hide the soft keyboard.
inputMethod.getController().stopInputSession();
} catch (err) {
console.error('Failed to hide keyboard: ' + err);
}
})
}
}
}
```

参考链接：

@ohos.inputMethod (输入法框架)
