# 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭

更新时间：2026-06-15 08:43:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265

可以通过全局的焦点控制对象FocusController的[clearFocus()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12)方法收起软键盘，示例代码如下：
 
```ArkTS
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
          this.getUIContext().getFocusController().clearFocus();
        })
    }
  }
}
```
 
参考链接：
 
[代码控制收起软键盘](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-keyboard-layout-adapt#section19809195110316)
