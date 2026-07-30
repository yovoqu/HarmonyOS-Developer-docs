# TextArea拉起键盘的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-767

#### 问题现象

如何在TextArea组件展示时拉起键盘，并通过按钮控制键盘的拉起和关闭？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tVLncV20RIK-IMHL6c_UTg/zh-cn_image_0000002658915019.png?HW-CC-KV=V1&HW-CC-Date=20260701T041250Z&HW-CC-Expire=86400&HW-CC-Sign=C6E20BEA7043C67C91F681BFF35849C98568553493C1D0E0FEA1EC9C199C4ED4)

 
 

#### 背景知识

- [TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)：多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
- [clearFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12)：清除焦点，将焦点强制转移到页面根容器节点，焦点链路上其他节点失焦。
- [requestFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#requestfocus12)：通过组件的id将焦点转移到组件树对应的实体节点。当前帧生效。

 
 

#### 解决方案
1. 设置defaultFocus属性为true来指定TextArea组件为当前页的默认焦点；
2. 创建isFocus变量标识当前键盘是否拉起状态；
3. 根据isFocus值响应对应的点击事件，使用clearFocus、requestFocus接口控制键盘拉起与关闭状态。
```text
import { window } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  @State operate: string = '收起键盘';
  @State isFocus: boolean = false;
  private controller: TextInputController = new TextInputController();

  aboutToAppear() {
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      if (err.code) {
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  build() {
    Column() {
      TextArea({ placeholder: '请输入...', controller: this.controller })
        .padding(12)
        .borderRadius(30)
        .id('myTextArea')
        .defaultFocus(true)
        .margin({ top: 10, bottom: 10 })
        .onFocus(() => {
          this.isFocus = true;
        })
        .onBlur(() => {
          this.isFocus = false;
        })

      Button(this.operate)
        .fontSize(16)
        .type(ButtonType.Normal)
        .borderRadius(25)
        .margin({ top: 50, bottom: 60 })
        .backgroundColor(0x0A59F7)
        .onClick(() => {
          if (this.isFocus) {
            this.getUIContext().getFocusController().clearFocus();
            this.operate = '唤起键盘';
          } else {
            this.getUIContext().getFocusController().requestFocus('myTextArea');
            this.operate = '收起键盘';
          }
        })
    }
    .height('100%')
    .width('100%')
    .padding(16)
    .backgroundColor(0xF1F3F5)
    .justifyContent(FlexAlign.Center)
  }
}
```

 
 

#### 常见FAQ

Q：TextArea中如何点击外部收起软键盘？
 
A：可以通过输入法服务InputMethodController的[stopInputSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#stopinputsession9)接口，控制点击空白区域是否收起键盘。
 
```text
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      TextArea()
    }
    .height('100%')
    .onTouch(() => {
      // 收起键盘
      let inputMethodController = inputMethod.getController();
      inputMethodController.stopInputSession()
    })
  }
}
```
 
Q：TextArea中如何设置成点击不拉起软键盘，仅作为滚动文本展示？
 
A：使用[focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)控制当前组件无法获得焦点。
 
Q：TextArea如何在enterKeyType为send的情况下，点击发送不收起键盘？
 
A：TextArea组件中自定义onsubmit方法，在按下软键盘回车键时，使用SubmitEvent.keepEditableState阻止输入法在失焦情况下关闭。示例代码如下：
 
```text
@Entry
@Component
struct Index {
  build() {
    Column() {
      TextArea().enterKeyType(EnterKeyType.Send)
        .onSubmit((enterKey: EnterKeyType, event?: SubmitEvent) => {
          event?.keepEditableState()
        })
    }
  }
}
```
