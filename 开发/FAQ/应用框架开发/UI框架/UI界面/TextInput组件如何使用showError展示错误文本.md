# TextInput组件如何使用showError展示错误文本

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1062

#### 问题现象

如何实现TextInput在用户输入错误时自动显示错误信息和调整UI布局？
 
问题截图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/lBVkJstLTya82M18aGx-kQ/zh-cn_image_0000002658806473.png?HW-CC-KV=V1&HW-CC-Date=20260701T041146Z&HW-CC-Expire=86400&HW-CC-Sign=7D2764DBC7AFFFA07A01332B076C808E057BBCDE0A6DE69E4E8AEB03D63E7746)

 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)单行文本输入框组件。
- [showError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#showerror10)设置错误状态下提示的错误文本或者不显示错误状态。当参数类型为ResourceStr并且输入内容不符合定义规范时，提示错误文本，当提示错误单行文本超长时，末尾以省略号显示。当参数类型为undefined时，不显示错误状态。

 
 

#### 解决方案

1.使用状态变量修饰error，在onChange()回调里将需提示的错误文本赋值error，即可实现自动显示错误信息。
 
2.文本组件设置alignSelf(ItemAlign.Start)，实现提示错误文本时，UI跟随调整。
 
```text
@Entry
@Component
struct ShowError {
  @State password: string = '';
  @State error: string = '';
  controller: TextInputController = new TextInputController();

  build() {
    Column() {
      Row() {
        Text('密码:')
          .fontSize(18)
          .textAlign(TextAlign.Center)
          .alignSelf(ItemAlign.Start)
          .height(50);

        TextInput({ placeholder: '请输入密码', text: $$this.password, controller: this.controller })
          .height(50)
          .showError(this.error)
          .newExtend()
          .borderRadius(20)
          .onChange((value: string) => {
            this.error = value;
            this.password = value;
          });
      }
      .margin(10);
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor('#F1F3F5');
  }
}


// 自定义属性
@Extend(TextInput)
function newExtend() {
  .layoutWeight(1)
  .placeholderColor('#99182431')
  .backgroundColor('#F1F3F5')
  .width('100%')
  .fontSize(14)
  .copyOption(CopyOptions.InApp)
  .borderWidth(1);
}
```
