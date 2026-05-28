# 如何使用iconfont

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-216

使用iconfont时，开发者需先获取字体库的ttf文件，再通过 `font.registerFont` 接口注册。在 `Text` 上使用对应的 unicode 编码即可。参考代码如下：
 
```ArkTS
import { Font } from '@kit.ArkUI'
@Entry
@Component
struct UseIconFont {
  // Assuming 0000 is the Unicode for the specified icon, developers actually need to obtain Unicode from the ttf file of the registered iconFont
  @State unicode: string = '\u0000';
  aboutToAppear(): void {
    let font: Font = this.getUIContext().getFont();
    font.registerFont({
      familyName: 'iconfont',
      familySrc: 'xxx.ttf'
    })
  }
  build() {
    Row() {
      Column() {
        Text(this.unicode)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .fontFamily('iconfont')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 
**参考链接**
 
[registerFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)
