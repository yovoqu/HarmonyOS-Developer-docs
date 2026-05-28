# Text组件如何加载Unicode字符

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-46

在Text组件的content参数中使用字符串，并在字符串中转义Unicode编码。示例代码如下：
 
```ArkTS
@Entry
@Component
struct TextView {
  build() {
    Column() {
      Text("\u{1F468}\u200D\u{1F469}\u200D\u{1F467}\u200D\u{1F466}")
        .width(100)
        .height(100)
        .fontSize(50)
    }
  }
}
```
 
字符串转Unicode编码：
 
```ArkTS
let chineseStr: string = "中文";
const encodedStr = Array.from(chineseStr).map(char =>`\\u${char.codePointAt(0)!.toString(16).padStart(4, '0')}`).join("");
```
 
Unicode编码转字符串：
 
```ArkTS
let unicodeStr: string = "\\u4e2d\\u6587";
const decodedStr = unicodeStr.replace(/\\u([\dA-Fa-f]{4})/g,(_,p1:string) => String.fromCodePoint(parseInt(p1, 16)));
```
