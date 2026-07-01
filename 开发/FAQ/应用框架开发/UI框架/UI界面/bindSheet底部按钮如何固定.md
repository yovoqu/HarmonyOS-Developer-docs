# bindSheet底部按钮如何固定

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1289

## bindSheet底部按钮如何固定
 


##### 问题现象

展开、收起bindSheet时，底部按钮位置都会发生变动，该如何固定？
 
问题效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/cI_pzSn2Q_KZv9jJgikfVg/zh-cn_image_0000002628757878.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025659Z&HW-CC-Expire=86400&HW-CC-Sign=A5C099CC6E4F5054E3FC3532C3B056E733D3C6B289D7D8758021C3960A7F16AC)

 
 

##### 背景知识

- [bindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
- [constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)：设置约束尺寸，组件布局时，进行尺寸范围限制。
- [position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)绝对定位，确定子组件相对父组件内容区的位置，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。

 
 

##### 解决方案

给bindSheet所绑定的自定义构建函数[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)内部的根容器组件设置constraintSize({minHeight:300,maxHeight:300})属性即可解决，高度值根据实际开发场景需要进行设置。示例代码如下：
 
```text
@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;

  @Builder
  myBuilder() {
    Row() {
      Button('content1')
        .margin(10)
        .fontSize(20)

      Button('content2')
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Bottom)
    .justifyContent(FlexAlign.Center)
    .constraintSize({ minHeight: 300, maxHeight: 300 })
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet($$this.isShow, this.myBuilder(), {
          detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
          backgroundColor: Color.White,
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: 'title', subtitle: 'subtitle' },
        })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}
```
 
效果如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ZzvwQCj5SWyYOe39xG9Xhw/zh-cn_image_0000002658957195.png?HW-CC-KV=V1&HW-CC-Date=20260701T025659Z&HW-CC-Expire=86400&HW-CC-Sign=453765D1641F9EF15E143809AC3AF0BB1BA049BAEAF7FE4D139E1E97D067B897)

 
 

##### 常见FAQ

Q：为什么bindSheet高度改变的时候固定在底部的按钮出现跳动？
 
A：在上下布局中bindSheet高度改变时，模态框重新渲染，底部按钮重新渲染，底部按钮相对于原来位置发生改变，会出现跳动一下的效果，这是正常现象。
 
Q：正文中提供了底部按钮位于半模态窗的相对位置固定的解决方案，如何保证底部按钮的绝对位置一直不变呢？
 
A：给需要保持固定不变的组件设置position({bottom:0})属性即可。
