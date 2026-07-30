# 在TextArea中复制完文字后如何取消文字的选中状态

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1340

#### 问题现象

TextArea组件输入若干内容，长按选择文字并点击“复制”后所选文字仍然是选中状态，如何取消其选中状态？
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct Index {
  @State message: string = '123456';
  controller: TextAreaController = new TextAreaController();
  startIndex: number = -1;
  endIndex: number = -1;

  build() {
    Column() {
      TextArea({ controller: this.controller, text: this.message })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })
        .margin(40)
    }
    .height('100%')
    .width('100%')
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/wOr3S5JJQSGgmTFUDnDO8Q/zh-cn_image_0000002628761404.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041300Z&HW-CC-Expire=86400&HW-CC-Sign=CBE062E19588FD66605E331B65FA1A65F1631C82EF221DAA95EE6D00F1CAEA1F)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/M69avwNuRCSuuQfQ_J7ZPA/zh-cn_image_0000002658960733.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041300Z&HW-CC-Expire=86400&HW-CC-Sign=E246FDDF266363C21B6B3770A6C88D63451C5A3519731621F73BA9E53BB33FF0)

 
 

#### 背景知识

- [onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#ontextselectionchange10)：文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。
- [onCopy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#oncopy8)：进行复制操作时，触发该回调。
- [caretPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#caretposition8)：设置输入光标的位置。

 
 

#### 问题定位

在使用系统提供的复制功能时，复制完成后并未对光标位置进行修改，故文本还是呈现选中状态。
 
 

#### 分析结论

在TextArea的onCopy回调中修改光标位置，即可实现取消文字的选中状态。
 
 

#### 修改建议
1. 选中文字时在[onTextSelectionChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#ontextselectionchange10)回调里记录光标结束位置，
2. 点击“复制”时在[onCopy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#oncopy8)回调里使用[caretPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#caretposition8)将光标定位到所记录的结束位置。
 
```text
@Entry
@Component
struct TextAreaSelectionChangeDemo {
  @State message: string = '123456';
  controller: TextAreaController = new TextAreaController();
  startIndex: number = -1;
  endIndex: number = -1;

  build() {
    Column() {
      TextArea({ controller: this.controller, text: this.message })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
        <em>  // 记录光标起始和结束位置</em>
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })
        .onCopy(() => {
          <em>// 完成复制后将光标定位到记录下来的结束位置</em>
          this.controller.caretPosition(this.endIndex);
        })
        .margin(40)
    }
    .height('100%')
    .width('100%')
  }
}
```
