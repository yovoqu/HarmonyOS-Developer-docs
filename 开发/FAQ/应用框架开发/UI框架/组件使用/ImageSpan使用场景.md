# ImageSpan使用场景

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-575

## ImageSpan使用场景
 


##### 问题现象

如何实现下图中的追加评论效果？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/q-rZSLXGR0-dZgSnfG2Tpg/zh-cn_image_0000002658791437.png?HW-CC-KV=V1&HW-CC-Date=20260701T025536Z&HW-CC-Expire=86400&HW-CC-Sign=7E2C71AAD4C51611FC8479BE16D12665422A7AEEB683CCF18598CCB334912D94)

 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/GdwJ2MLkSPaoVqW41lMWew/zh-cn_image_0000002628552050.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025536Z&HW-CC-Expire=86400&HW-CC-Sign=7D9E6569E28A9829EEE70D035CE26AAECA42C3A22209D68E34C72D50E3CE9057)

 
 

##### 背景知识

- [Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。
- [ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)：Text、ContainerSpan组件的子组件，用于显示行内图片。

 
 

##### 解决方案

将图片换成镂空图，ImageSpan使用margin属性调整位置。
 
```text
@Entry
@Component
struct ImageSpanExample {
  content: string = '到了绿湖底部，面上神色一动。';

  build() {
    Column() {
      Text() {
        Span("\n" + this.content)
          .fontSize(20)
        Span('  11  ')
        ImageSpan($r('app.media.startIcon'))  // 需开发者换成镂空的图
          .width('26vp')
          .height('26vp')
          .margin({ left: -27, bottom: -2 })
      }
    }
    .width('100%')
    .height('100%')
  }
}
```
