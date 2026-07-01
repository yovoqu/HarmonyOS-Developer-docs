# 如何实现TextInput获焦失焦时的文本显示效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1259

## 如何实现TextInput获焦失焦时的文本显示效果
 


##### 问题现象

如何实现不限字数的单行输入框，且TextInput获取焦点时，光标应正常显示在文本末尾；失去焦点时，超出宽度的文本应该以省略号结尾？
 
 

##### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)：单行文本输入框组件，该组件仅支持单文本样式。
- [style](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#style9)：设置输入框为默认风格或内联输入风格，内联输入风格只支持InputType.Normal类型。
- [textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textoverflow12)：设置文本超长时的显示方式。

 
 

##### 解决方案

- **方案一**：
textOverflow仅在内联模式的编辑态、非编辑态下支持，需设置style属性。
- 设置状态变量观测textOverflow、style的类型，在TextInput获焦、失焦时，展示不同的文本形式。
- 获焦时，判断当前类型是否为Inline，是则将style设置为Default，textOverflow设置为MARQUEE；失焦时，style设置为Inline，textOverflow设置为Ellipsis。
- 在Column上添加onClick事件，点击时，使用[clearFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12)清除TextInput焦点。

 
```text
@Entry
@Component
struct Index {
  @State queryContent: string = '';
  @State textInputStyleType: TextInputStyle = TextInputStyle.Default;
  @State textOverflowType: TextOverflow = TextOverflow.Clip;
  private controller: TextInputController = new TextInputController();

  build() {
    Column() {
      TextInput({ text: this.queryContent, placeholder: '搜索感兴趣的内容', controller: this.controller })
        .borderRadius(25)
        .height(50)
        .fontSize(14)
        .fontColor('#66000000')
        .placeholderFont({ size: 14, weight: FontWeight.Medium })
        .style(this.textInputStyleType)
        .maxLines(1)
        .textOverflow(this.textOverflowType)
        .backgroundColor('#f1f3f5')
        .padding({ left: 20, right: 20 })
        .outline({ width: 0 })
        .lineBreakStrategy(LineBreakStrategy.BALANCED)
        .onFocus(() => {
          if (this.textInputStyleType === TextInputStyle.Inline) {
            this.textInputStyleType = TextInputStyle.Default;
            this.textOverflowType = TextOverflow.MARQUEE;
          }
          this.controller.caretPosition(this.queryContent.length);
        })
        .onBlur(() => {
          this.textInputStyleType = TextInputStyle.Inline;
          this.textOverflowType = TextOverflow.Ellipsis;
        })
        .onChange((value: string) => {
          this.queryContent = value;
        });
    }
    .padding(24)
    .height('100%')
    .width('100%')
    .onClick(() => {
      this.getUIContext().getFocusController().clearFocus();
    });
  }
}
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Rt_nIWc1TlihZqH5b08B7w/zh-cn_image_0000002628596026.png?HW-CC-KV=V1&HW-CC-Date=20260701T025646Z&HW-CC-Expire=86400&HW-CC-Sign=BDC17C47B51E328770189C27A5DBC892FBBAA5DDABEA445CCC7F5BE40C0FC082)

 
 
- **方案二**：
失焦时，使用Text覆盖TextInput，textOverflow设置为Ellipsis，超出正常文本宽度显示省略号。
- 获焦时，Text隐藏，显示TextInput，不需要设置textOverflow，光标正常展示在文本最后面。
- 设置状态变量观测失焦和获焦状态，通过[visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility#visibility)来控制Text组件的隐现。

 
```text
@Entry
@Component
struct InputTextDemo {
  @State text: string =
    '这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试这是一个超长文本测试';
  @State isFocus: boolean = false;

  build() {
    Column() {
      Text('今天星期二')
        .fontSize(50)
        .margin(16);
      Stack() {
        Text(this.text)
          .width('90%')
          .height(70)
          .fontSize(16)
          .fontWeight(FontWeight.Medium)
          .fontColor('#000000')
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .visibility(this.isFocus ? Visibility.None : Visibility.Visible)
          .onClick(() => {
            focusControl.requestFocus('TextInput');
            this.isFocus = true;
          });

        TextInput()
          .id('TextInput')
          .width('100%')
          .height(50)
          .fontSize(16)
          .borderRadius(16)
          .fontColor('#66000000')
          .defaultFocus(false)
          .border({
            width: 1,
            color: this.isFocus ? '#f1f3f5' : Color.Transparent
          })
          .visibility(this.isFocus ? Visibility.Visible : Visibility.None)
          .onFocus(() => {
            this.isFocus = true;
          })
          .onBlur(() => {
            this.isFocus = false;
          })
          .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
            if (event.text === '') {
              console.info(`enterKey: ${enterKey}`);
              this.isFocus = false;
            } else {
              this.text = event.text;
              this.isFocus = false;
            }
          });
      };
    }.padding(16);
  }
}
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/OWqv5kGcTeeDjDfP_Ib8vQ/zh-cn_image_0000002658835371.png?HW-CC-KV=V1&HW-CC-Date=20260701T025646Z&HW-CC-Expire=86400&HW-CC-Sign=5C432A7C581823563994A7FB7D9CB9FDF8E3E066EB5812EBC035E8A01FD82F57)
