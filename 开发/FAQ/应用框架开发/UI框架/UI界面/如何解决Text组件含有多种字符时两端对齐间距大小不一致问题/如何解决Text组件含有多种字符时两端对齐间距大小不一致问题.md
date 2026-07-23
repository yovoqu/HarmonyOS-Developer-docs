# 如何解决Text组件含有多种字符时两端对齐间距大小不一致问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-569

#### 问题现象

使用TextAlign.Justify或TextAlign.Start均未实现两端对齐的效果，不同字符间距大小不一。如图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/EEhmsB2DSU29i1cvA2OOhg/zh-cn_image_0000002658911365.png?HW-CC-KV=V1&HW-CC-Date=20260723T013008Z&HW-CC-Expire=86400&HW-CC-Sign=23F3E0CDF0216D20298C29D128C96087DD1C6BCA3655C241D7F64D0A941229B9)

 
 

#### 背景知识

[Text组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)中的[textAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#textalign)与[WordBreak](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#wordbreak11)相关部分。
 
 

#### 解决方案

中文字符必定是全角字符，但数字英文特殊字符等存在全角和半角两种格式，一般情况下数字英文特殊字符等都会简化半角格式，这些字符只有在作为文本处理时会出现会产生格式问题，使用断行规则可以自动将其转成半角。
 
当使用TextAlign.JUSTIFY或TextAlign.Start无法达到两端对齐时，可以搭配设置断行规则wordBreak来实现对应效果。
 
WordBreak.BREAK_ALL与TextAlign.JUSTIFY组合使用可实现英文单词按字母截断，汉字按字截断，方便控制间距。
 
代码示例如下：
 
```text
@Entry
@Component
struct wordDemo {
  build() {
    Column() {
      Text('测试Test测试123456789!@#$%-测试Test测试123456789!@#$%-测试Test测试123456789!@#$%-测试Test测试123456789!@#$%-测试Test测试123456789!@#$%')
        .textAlign(TextAlign.JUSTIFY)
        .backgroundColor('#87ceeb')
        .wordBreak(WordBreak.BREAK_ALL) <em>// 配合TextAlign.JUSTIFY实现两端对齐，解决间距大小不一的问题</em>
        .fontSize(16)
        .borderRadius(16)
        .padding(16);
    }
    .margin({ left: 16, right: 16 })
  }
}
```
 
 

#### 总结

文字对齐，不仅仅可以用单参数实现，有时候可以通过两个参数组合实现一个对齐效果。
