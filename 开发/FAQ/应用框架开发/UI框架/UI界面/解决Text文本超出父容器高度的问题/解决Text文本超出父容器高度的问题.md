# 解决Text文本超出父容器高度的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-764

#### 问题现象

父容器的宽高固定，而Text文本内容长度不确定，当文本过长时，会超出父容器的高度。问题代码如下：
 
```text
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' +
        '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111' +
        '11111111111111111111111111111111111111111111111111111111111111111')
        .wordBreak(WordBreak.BREAK_ALL)
    }
    .width('100%')
    .height(80)
    .backgroundColor('#ffb7bdc4')
    .padding({ top: 20, bottom: 20 })
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/c5V7jfBxSImsL2CduNqqcQ/zh-cn_image_0000002628395802.png?HW-CC-KV=V1&HW-CC-Date=20260730T072454Z&HW-CC-Expire=86400&HW-CC-Sign=8A225BF3795DD1DC32CE9ACAAD47212294923D3A97796B5F81DBCACEBB854CCA)

 
 

#### 背景知识

- [Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)是显示一段文本的组件。默认情况下，文本是可自动换行的，通过设置[maxLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#maxlines)属性，指定文本最多不会超过指定的行。如果有多余的文本，可以通过[textOverflow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textoverflow)来指定截断方式。
- [TextArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea)是多行文本输入框组件，高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。
- [measureTextSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretextsize12)是一个用于测量文本尺寸的方法，通常在富文本编辑器、文本渲染库（如Canvas）或任何需要动态调整文本大小的应用中使用。这个方法可以帮助开发者准确地计算文本的实际尺寸，以便进行布局和排版优化。

 
 

#### 解决方案

- **方案一**：通过measureTextSize的height值获取当前文本高度，需要注意获取到的值为px单位，需通过[px2vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12)转换为vp单位后使用，然后通过容器高度/文本高度计算出最多显示几行文本。
```text
import { MeasureUtils } from '@kit.ArkUI';

@Entry
@Component
struct MeasureTextPage {
  uiContext: UIContext = this.getUIContext();
  measureText: MeasureUtils = this.uiContext.getMeasureUtils();
  @State textHeight: number = 40;
  textPadding: number = 8;
  @State lineHeight: number = 0;

  aboutToAppear(): void {
    let textSize: SizeOptions = this.measureText.measureTextSize({
      textContent: 'Hello World',
      fontSize: 16
    });
    this.lineHeight = this.getUIContext().px2vp(Number(textSize.height));
    console.info(this.lineHeight.toString());
  }

  build() {
    Column({ space: 20 }) {
      Text('这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这' +
        '是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段' +
        '很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本')
        .backgroundColor('#f1f3f5')
        .borderRadius('8vp')
        .width(304)
        .padding(this.textPadding)
        .height(this.textHeight)
        .maxLines(Math.floor((this.textHeight - 2 * this.textPadding) / this.lineHeight))
        .textOverflow({ overflow: TextOverflow.Ellipsis })
      Button('点击').onClick(() => {
        this.textHeight += 2;
      })
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ZuPtB43DRFKyMToyJgOkmA/zh-cn_image_0000002658795067.png?HW-CC-KV=V1&HW-CC-Date=20260730T072454Z&HW-CC-Expire=86400&HW-CC-Sign=CB6F97E127AFCB7CD469B7AEF149E3345F27F81148536D52A4CF747C7319757C)

- **方案二**：使用TextArea代替Text组件，当TextArea的文本内容超过组件范围时会自动生成滑动条。

 
 

#### 总结

Text组件默认可折行，从而导致超出父容器高度的现象，有两种方案可以解决：
 
一是需要通过maxLines设置最大换行，有多余文本可通过textOverflow设置截断方式。
 
二是使用TextArea组件，该组件在文本超出范围时自动生成滑动条。
