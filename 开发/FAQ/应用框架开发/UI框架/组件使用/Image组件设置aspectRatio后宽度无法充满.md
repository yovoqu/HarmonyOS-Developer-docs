# Image组件设置aspectRatio后宽度无法充满

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-511

## Image组件设置aspectRatio后宽度无法充满
 


##### 问题现象

在Column内放置Image组件，给Image组件同时设置aspectRatio、margin、width属性，但图片设置的width属性不生效。
 
问题代码如下：
 
```text
@Entry
@Component
struct Index {


  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .width('100%')
        .aspectRatio(2)
        .objectFit(ImageFit.Cover)
        .margin({ top: 100 })
    }.width('100%').height(300)
  }
}
```
 
 

##### 解决方案

线性布局在给子组件设置[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)值时，子组件的高度就是本身的高度加上margin的高度，指定了[aspectRatio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints#aspectratio)后，为了保持宽高比，Column的宽度会根据aspectRatio宽高比重新计算。
 
- 方案一：如果要给Image设置宽度100%的话，移除margin属性的设置。
- 方案二：如果要给Image组件设置margin属性的话，不显式设置width属性。
