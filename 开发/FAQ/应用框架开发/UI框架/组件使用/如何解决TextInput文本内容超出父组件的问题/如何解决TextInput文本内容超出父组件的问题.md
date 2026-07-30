# 如何解决TextInput文本内容超出父组件的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1197

#### 问题现象

TextInput组件绑定自定义键盘，如何实现当内容超过父组件宽度时新输入的内容能够全部显示，已输入的内容向左移动，超出父组件部分的内容可以隐藏的效果？
 
问题代码示例参考如下：
 
```text
build() {
 <em> // ...</em>
  RelativeContainer() {
    Text("￥")
      .fontSize(24)
      .fontColor($r('app.color.black'))
      .maxLines(1)
      .padding({ left: 3, right: 3 })
      .id('money_symbol')

    TextInput({ text: this.input, placeholder: "0.00" })
      .placeholderColor($r('app.color.black'))
      .placeholderFont({ size: 24, weight: FontWeight.Regular })
      .fontSize(24)
      .fontWeight(FontWeight.Regular)
      .fontColor($r('app.color.black'))
      .maxLines(1)
      .textAlign(TextAlign.End)
      .enableKeyboardOnFocus(false) <em>// 不弹起系统键盘</em>
      .caretColor(Color.Transparent)<em> // 设置光标透明色</em>
      .backgroundColor(Color.Transparent)
      .margin({ right: 12 })
      .padding(0)
      .id('money')
      .width('auto')
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
        right: { anchor: '__container__', align: HorizontalAlign.End }
      })

  }
  .backgroundImage($r('app.media.bg_keyboard_input_box'))
  .backgroundImageSize(ImageSize.FILL)
  .width(289)

  Row({ space: 10 }) {
    KeyboardButton({ text: this.numbers[7] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[7])
      })
    KeyboardButton({ text: this.numbers[8] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[8])
      })
    KeyboardButton({ text: this.numbers[9] })
      .onClick(() => {
        this.input = this.calculator.input(this.numbers[9])
      })
    KeyboardButton({
      text: this.date,
      fontSize: 15,
      fontWeight: FontWeight.Medium,
      imageWidth: 18,
    })
  }

 <em> // ...</em>

}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Fe9q4jv_RX25XDf8ulwYiQ/zh-cn_image_0000002658952189.png?HW-CC-KV=V1&HW-CC-Date=20260730T072345Z&HW-CC-Expire=86400&HW-CC-Sign=27D85B56BD72D14778B3252EB549DDC855157516A156B4322269821D86FC8B09)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/gMrJc8KNSzOKfUEu3eX9vA/zh-cn_image_0000002628592998.png?HW-CC-KV=V1&HW-CC-Date=20260730T072345Z&HW-CC-Expire=86400&HW-CC-Sign=B531509807D9A53B1D8307C2F9D0CFB45989731F0323F260C88962EA468A10F0)

 
 

#### 背景知识

- [TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)：单行文本输入框组件。
- [textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#textalign9)：设置文本在输入框中的水平对齐方式。仅支持TextAlign.Start、TextAlign.Center和TextAlign.End。
- [requestFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#requestfocus9)：调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。

 
 

#### 解决方案

输入内容时给自定义键盘点击事件添加获焦逻辑，使TextInput组件获取到焦点实现当内容超过组件宽度时自动左滑的功能。
 
- Index页面内容：
```text
import { Calculator } from './Calculator';

@Entry
@Component
struct Index {
  @State input: ResourceStr = '';
  date: string = '日期';
  private calculator: Calculator = new Calculator(100, 100);
  private context: Context = this.getUIContext().getHostContext() as Context;
  private numbers: Array<string> =
    this.context.resourceManager.getStringArrayValueSync($r('app.strarray.accounting_keyboard').id); <em>// 根据具体情况加载资源</em>

  build() {

    Column({ space: 5 }) {
      Row() {
        Text('￥')
          .fontSize(24)
          .fontColor($r('app.color.black')) <em>// 根据具体情况加载资源</em>
          .maxLines(1)
          .padding({ left: 3, right: 0 })
          .id('money_symbol')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            right: { anchor: 'money', align: HorizontalAlign.Start }
          });

        RelativeContainer() {
          TextInput({ text: this.input, placeholder: '0.00' })
            .placeholderColor($r('app.color.black')) <em>// 根据具体情况加载资源</em>
            .placeholderFont({ size: 24, weight: FontWeight.Regular })
            .fontSize(24)
            .fontWeight(FontWeight.Regular)
            .fontColor($r('app.color.black'))<em> // 根据具体情况加载资源</em>
            .maxLines(1)
            .textAlign(TextAlign.End)
            .enableKeyboardOnFocus(false) <em>// 不弹起系统键盘</em>
            .caretColor(Color.Transparent)<em> // 不希望有光标</em>
            .backgroundColor(Color.Transparent)
            .margin({ right: 12 })
            .padding(0)
            .id('money')
            .width('auto')
            .alignRules({
              top: { anchor: '__container__', align: VerticalAlign.Top },
              bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
              right: { anchor: '__container__', align: HorizontalAlign.End }
            });
        }
        .width(289);
      }
      .height(52)
      .border({ width: 2 })
      .borderRadius(12)
      .margin({ top: 16 });

      Column() {
        Row({ space: 10 }) {
         <em> // 给自定义键盘点击事件添加获焦操作。以按键数字“7”为例</em>
          KeyboardButton({ text: this.numbers[7] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[7]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[8] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[8]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[9] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[9]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({
            text: this.date,
            fontSize: 18,
            fontWeight: FontWeight.Medium,
            imageWidth: 18,
          });
        };

        Row({ space: 10 }) {
          KeyboardButton({ text: this.numbers[4] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[4]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[5] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[5]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[6] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[6]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[12], fontSize: 27 })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[12]);
            });
        };

        Row({ space: 10 }) {
          KeyboardButton({ text: this.numbers[1] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[1]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[2] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[2]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[3] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[3]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ text: this.numbers[11], fontSize: 27 })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[11]);
            });
        };

        Row({ space: 10 }) {
          KeyboardButton({ text: this.numbers[10] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[10]);
            });
          KeyboardButton({ text: this.numbers[0] })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[0]);
              this.getUIContext().getFocusController().requestFocus('money');
            });
          KeyboardButton({ icon: $r('app.media.ic_keyboard_del') }) <em>// 根据具体情况加载资源</em>
            .onClick(() => {
              this.input = this.calculator.delete();
            });
          KeyboardButton({
            text: '完成',
            fontSize: 18,
            fonColor: $r('app.color.white'),<em> // 根据具体情况加载资源</em>
            fontWeight: FontWeight.Medium
          })
            .onClick(() => {
              this.input = this.calculator.input(this.numbers[13]);
            });
        };
      }
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .height('30%')
      .backgroundColor('#DEE0E6')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceBetween)
    .alignItems(HorizontalAlign.Center)
    .padding({ bottom: 0 });
  }
}

@Preview
@Component
export struct KeyboardButton {
  @State isClick: boolean = false;
  text?: ResourceStr;
  icon?: ResourceStr;
  buttonWidth: number = 80;
  imageWidth: number = 29.5;
  fontSize: number = 24;
  fonColor: ResourceStr = $r('app.color.black'); <em>// 根据具体情况加载资源</em>
  fontWeight: FontWeight = FontWeight.Regular;
  btnBackground: ResourceStr = '';
  btnBackgroundPress: ResourceStr = '';

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Image(this.isClick ? this.btnBackgroundPress : this.btnBackground)
        .draggable(false)
        .width(this.buttonWidth);

      Row({ space: 4 }) {
        if (this.icon) {
          Image(this.icon)
            .width(this.imageWidth);
        }
        if (this.text) {
          Text(this.text)
            .fontSize(this.fontSize)
            .fontColor(this.fonColor)
            .fontWeight(this.fontWeight);
        }
      };
    }
    .height('18%')
    .backgroundColor(Color.White)
    .borderRadius(24)
    .onTouch((event?: TouchEvent) => {
      if (event) {
        if (event.type == TouchType.Down) {
          this.isClick = true;
        }
        if (event.type == TouchType.Up) {
          this.isClick = false;
        }
      }
    });
  }
}
```

- Calculator页面内容：
```text
<em>/**</em>
<em> */</em>
export class Calculator {
  <em>/**</em>
<em>   * 整数位数</em>
<em>   */</em>
  private digit: number = 10;
 <em> /**</em>
<em>   * 小数点的位数</em>
<em>   */</em>
  private accuracy: number = 2;
<em>  /**</em>
<em>   * 匹配的正则表达式</em>
<em>   */</em>
  private regExp: RegExp;
<em>  /**</em>
<em>   * 当前数字的字符串</em>
<em>   */</em>
  private currentStr: string = '';
 <em> /**</em>
<em>   * 前一个数字的字符串</em>
<em>   */</em>
  private lastStr: string = '';
 <em> /**</em>
<em>   * 符号</em>
<em>   */</em>
  private symbol: string = '';

  constructor(digit: number = 10, accuracy: number = 2) {
    if (digit >= 2) {
      this.digit = digit;
    }
    if (accuracy >= 0) {
      this.accuracy = accuracy;
    }
    this.regExp = new RegExp(`^-?\\\d{1,${this.digit}}(\\\.\\\d{1,${this.accuracy}})?$`);
  }

  <em>/**</em>
<em>   * 输入内容</em>
<em>   */</em>
  input(str: string): string {
    if (str === '+' || str === '-') {
      if (this.symbol.length > 0) {
        if (this.currentStr.length > 0) {
          if (!this.calculate()) {
            return this.lastStr + this.symbol + this.currentStr;
          }
        }
      } else if (this.lastStr.length <= 0) {
        return this.lastStr;
      } else if (this.lastStr.endsWith('.')) {
        this.lastStr += '0';
      }
      this.symbol = str;
      return this.lastStr + this.symbol + this.currentStr;
    } else if (str === '=') {
      this.calculate();
      return this.lastStr + this.symbol + this.currentStr;
    } else if (str === '.') {
      if (this.accuracy <= 0) {
        return this.lastStr + this.symbol + this.currentStr;
      }
      if (this.symbol.length > 0) {
        if (this.currentStr.length <= 0) {
          this.currentStr = '0.';
        } else if (this.currentStr.indexOf(str) < 0) {
          this.currentStr += str;
        }
      } else {
        if (this.lastStr.length <= 0) {
          this.lastStr = '0.';
        } else if (this.lastStr.indexOf(str) < 0) {
          this.lastStr += str;
        }
      }
      return this.lastStr + this.symbol + this.currentStr;
    } else {
      let result: string;
      if (this.symbol.length > 0) {
        result = this.currentStr + str;
      } else {
        result = this.lastStr + str;
      }
      if (this.regExp.test(result)) {
        if (this.symbol.length > 0) {
          this.currentStr = result;
        } else {
          this.lastStr = result;
        }
      }
      return this.lastStr + this.symbol + this.currentStr;
    }
  }

 <em> /**</em>
<em>   * 删除内容</em>
<em>   */</em>
  delete(): string {
    if (this.currentStr.length > 0) {
      this.currentStr = this.currentStr.slice(0, -1);
      return this.lastStr + this.symbol + this.currentStr;
    } else if (this.symbol.length > 0) {
      this.symbol = this.symbol.slice(0, -1);
      return this.lastStr + this.symbol;
    } else if (this.lastStr.length > 0) {
      this.lastStr = this.lastStr.slice(0, -1);
      return this.lastStr;
    }
    return '';
  }

 <em> /**</em>
<em>   * 计算</em>
<em>   */</em>
  private calculate(): boolean {
    if (this.currentStr && this.lastStr) {
      const a: number = parseFloat(this.lastStr);
      const b: number = parseFloat(this.currentStr);
      let result: number = 0;
      switch (this.symbol) {
        case '+':
          result = a + b;
          break;
        case '-':
          result = a - b;
          break;
        default:
          return false;
      }
      this.lastStr = result.toString();
      this.currentStr = '';
      this.symbol = '';
      return true;
    }
    return false;
  }
}
```
