# TextInput设置手机号格式输入-如何解决修改数据后光标位置错乱的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-719

#### 问题现象

HarmonyOS系统使用TextInput输入手机号，通过onChange函数实现手机号格式344划分，但在实际使用过程中，存在两个问题：
 
- 空格可以删除。
- 执行删除或者插入数字操作，光标位置会重置到末尾位置。

 
当前效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/X9F05EM9R7Wi2xT7xq7bMg/zh-cn_image_0000002658794575.png?HW-CC-KV=V1&HW-CC-Date=20260701T041251Z&HW-CC-Expire=86400&HW-CC-Sign=6BD235D98A74D0F915936B46001AA95E9381A3ECEF44977C3F0AB20D9968FDC7)

 
针对号码123/4567/8910，删除了7和8之间的空格，TextInput空格先被删除，之后value值刷新，展示：123/4567/8910，光标位于末尾。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/rjp-5Xc7SHmvDZzYrXsUUg/zh-cn_image_0000002628555208.png?HW-CC-KV=V1&HW-CC-Date=20260701T041251Z&HW-CC-Expire=86400&HW-CC-Sign=637C04EEE82574CAFBA4C7AA7A179FD9847573BA44E2256103D8729C9F5D8A6A)

 
预期效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/VRVn8rm4Ste9DzqRjaRpdw/zh-cn_image_0000002658914529.png?HW-CC-KV=V1&HW-CC-Date=20260701T041251Z&HW-CC-Expire=86400&HW-CC-Sign=9A63E9087394534FB3F6BC774C5E78FB6547517869CBFABE0CED56A3AC53C238)

 
针对号码123/4567/8910，删除了7和8之间的空格，实际删除数字7，展示：123/4568/910，光标在数字6后面。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/kGsL-WIATLCHVY37itlqIg/zh-cn_image_0000002628395304.png?HW-CC-KV=V1&HW-CC-Date=20260701T041251Z&HW-CC-Expire=86400&HW-CC-Sign=254FBDA69519CFF34FE652E5B462CA23956CE46AE26E6BC26AC66C8CB3B69CCA)

 
删除数字6，展示123/4578/910，光标位于数字5后面。
 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)是一种单行文本输入框组件。当输入内容发生变化时，会触发该组件的[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#onchange)回调函数，当输入完成时，会触发[onDidInsert](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondidinsert12)回调函数，当删除完成时，会触发[onDidDelete](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#ondiddelete12)回调函数。
- [RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)是一种支持图文混排和文本交互式编辑的组件。

 
 

#### 问题定位

onChange函数的规格为value值变化后执行，所以删除空格、删除数字或者添加数字等编辑操作改变value值，导致数据需要重新格式化，也就是重新赋值，此时光标会位于输入值的末尾。
 
 

#### 分析结论

在value值变化前就将展示结果和光标位置获取到，之后再进行赋值以及光标位置定位就可以了。
 
 

#### 修改建议

按照定位思路，在value值变化前通过onDidInsert和onDidDelete回调函数计算出预期展示结果以及光标位置进行赋值。
 
```text
insertNumber(value: RichEditorInsertValue) {
  this.controller.deleteSpans({ start: 0 });
  let realOffset = this.getRealOffset(value.insertOffset, true);
  this.originalPhoneNumber = this.originalPhoneNumber.substring(0, realOffset) + value.insertValue +
  this.originalPhoneNumber.substring(realOffset);
  // 最长11位
  this.originalPhoneNumber = this.originalPhoneNumber.substring(0, 11);
  this.controller.addTextSpan(this.getSpacePhoneNumber(), { style: this.phoneNumberStyle });
  let caretOffset = this.getCaretOffset(realOffset, true);
  this.controller.setCaretOffset(caretOffset);
}

deleteNumber(value: RichEditorDeleteValue) {
  if (this.controller.getCaretOffset() == 0) {
    return;
  }
  this.controller.deleteSpans({ start: 0 });
  let realOffset = this.getRealOffset(value.offset, false);
  this.originalPhoneNumber =
    this.originalPhoneNumber.substring(0, realOffset) + this.originalPhoneNumber.substring(realOffset + 1);
  this.controller.addTextSpan(this.getSpacePhoneNumber(), { style: this.phoneNumberStyle });

  let caretOffset = this.getCaretOffset(realOffset, false);
  this.controller.setCaretOffset(caretOffset);
}
```
 
验证发现已实现上述期望效果，但美中不足的是，删除时光标重置位置时会有闪动效果，因此找到了同样的文本输入组件RichEditor，RichEditor是支持图文混排和文本交互式编辑的组件，具有更灵活的编辑输入能力。
 
使用RichEditor组件达成预期效果，完整示例参考如下：
 
```text
@Entry
@Component
struct Index {
  private controller: RichEditorController = new RichEditorController();
  private originalPhoneNumber: string = '';
  private phoneNumberStyle: RichEditorTextStyle = {
    fontColor: Color.Black,
    fontWeight: FontWeight.Bold
  };

  insertNumber(value: RichEditorInsertValue) {
    this.controller.deleteSpans({ start: 0 });
    let realOffset = this.getRealOffset(value.insertOffset, true);
    this.originalPhoneNumber = this.originalPhoneNumber.substring(0, realOffset) + value.insertValue +
    this.originalPhoneNumber.substring(realOffset);
    // 最长11位
    this.originalPhoneNumber = this.originalPhoneNumber.substring(0, 11);
    this.controller.addTextSpan(this.getSpacePhoneNumber(), { style: this.phoneNumberStyle });
    let caretOffset = this.getCaretOffset(realOffset, true);
    this.controller.setCaretOffset(caretOffset);
  }

  deleteNumber(value: RichEditorDeleteValue) {
    if (this.controller.getCaretOffset() == 0) {
      return;
    }
    this.controller.deleteSpans({ start: 0 });
    let realOffset = this.getRealOffset(value.offset, false);
    this.originalPhoneNumber =
      this.originalPhoneNumber.substring(0, realOffset) + this.originalPhoneNumber.substring(realOffset + 1);
    this.controller.addTextSpan(this.getSpacePhoneNumber(), { style: this.phoneNumberStyle });

    let caretOffset = this.getCaretOffset(realOffset, false);
    this.controller.setCaretOffset(caretOffset);
  }

  getRealOffset(offset: number, isInsert: boolean) {
    let realOffset = offset;
    if (realOffset >= (isInsert ? 9 : 8)) {
      realOffset -= 2;
    } else if (realOffset >= (isInsert ? 4 : 3)) {
      realOffset -= 1;
    }
    return realOffset;
  }

  getCaretOffset(realOffset: number, isInsert: boolean): number {
    let caretOffset = isInsert ? realOffset + 1 : realOffset;
    if (caretOffset >= 7) {
      caretOffset += 2;
    } else if (caretOffset >= 3) {
      caretOffset += 1;
    }
    return caretOffset;
  }

  getSpacePhoneNumber(): string {
    let res = this.originalPhoneNumber;
    if (res.length >= 4) {
      res = res.substring(0, 3) + ' ' + res.substring(3);
    }
    if (res.length >= 9) {
      res = res.substring(0, 8) + ' ' + res.substring(8);
    }
    return res;
  }

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .align(Alignment.Center)
        .id('PhoneNumberInputTestHelloWorld')
        .width('100%')
        .height(60)
        .backgroundColor(0xFFE3ECE3)
        .borderRadius(30)
        .aboutToIMEInput((value: RichEditorInsertValue) => {
          if (isNaN(Number(value.insertValue))) {
            return false;
          }
          this.insertNumber(value);
          return false;
        })
        .enablePreviewText(false)
        .aboutToDelete((value: RichEditorDeleteValue) => {
          this.deleteNumber(value);
          return false;
        });
    }
    .height('100%')
    .width('100%')
    .padding(16);
  }
}
```
 
 

#### 总结

上述场景主要关键点在于重新赋值后光标位置处理以及展示效果，针对常规输入删除场景，使用TextInput就可以满足大部分输入框需求，但也存在一些特殊格式要求的输入场景，会对展示内容进行UI重组，那么推荐使用RichEditor具有更高的灵活性。
