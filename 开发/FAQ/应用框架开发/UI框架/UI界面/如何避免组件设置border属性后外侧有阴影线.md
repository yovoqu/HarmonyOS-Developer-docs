# 如何避免组件设置border属性后外侧有阴影线

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1335

#### 问题现象

组件设置边框属性border后，边框外侧出现阴影线。
 
问题代码示例参考如下：
 
```text
@Entry
@Component
struct NavigationPage {

  build() {
    Column() {
      Row()
        .height(300)
        .width(300)
        .backgroundColor('#0a59f7')
        .border({
          color: Color.White,
          radius: 100,
          width: 10
        })
    }
    .width('100%')
    .height('100%')
    .padding(24)
  }
}
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vu-bRrwDR8GDOphpxUq4Wg/zh-cn_image_0000002658959239.png?HW-CC-KV=V1&HW-CC-Date=20260701T041214Z&HW-CC-Expire=86400&HW-CC-Sign=6C24BFD9643D5DD86764D7E6F3C6C46099858F96FABC12AABB6E3FFB8429300E)

 
 

#### 背景知识

- [border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)用于设置组件的边框样式，包括边框宽度、颜色、圆角半径等。border的规格生效范围是组件内，与背景颜色重叠，属于双层绘制，当设置圆角半径较大，且设置了边框宽度时，由于抗锯齿像素是半透明像素的原因，无法遮挡下方内容，可能会出现背景颜色露出，外侧出现与背景色同色的线。
- [outline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline#outline)用于设置组件的外描边样式。outline的规格生效范围在组件外，与组件的背景颜色分别绘制，不重叠。
- [clipShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clipshape12)可以按指定形状裁剪组件，被裁剪的区域可以响应手势事件。

 
 

#### 解决方案

- **方案一**：取消设置边框宽度，增加outline属性，以代替边框。由于outline规则在组件外，需要注意组件位置是否满足布局需要，可以通过外边距margin调整。
- **方案二**：通过clipShape属性，将组件裁剪为期望的圆角样式。
```text
import { RectShape } from '@kit.ArkUI';
const outLineWidth: number = 10;

@Entry
@Component
struct BottomWithBar {

  build() {
    Column() {
      Row() {
        Text(`方案一`);
      }
      // 边框宽度10vp，取消后减少对应宽高
      .height(250)
      .width(250)
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#0a59f7')
      .border({
        color: Color.White,
        radius: 100,
        // width:10，取消边框宽度设置。即无边框
      })
      // 新增outline属性
      .outline({
        width: outLineWidth,
        color: Color.White,
        radius: 100,
        style: OutlineStyle.SOLID
      })
      // 设置外边框，与outline宽度一致
      .margin(outLineWidth);


      Row() {
        Text(`方案二`);
      }
      .height(250)
      .width(250)
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#0a59f7')
      .clipShape(
        new RectShape({
          radius: [80, 80, 80, 20] // 圆角尺寸，分别对应组件左上角、右上角、右下角、左下角
        })
          .height(200)
          .width(200));
    }
    .width('100%')
    .height('100%')
    .padding(24)
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```
 效果预览:

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/V2r79OxBSJewWN3Dh44vfw/zh-cn_image_0000002658839287.png?HW-CC-KV=V1&HW-CC-Date=20260701T041214Z&HW-CC-Expire=86400&HW-CC-Sign=A835378FD16A424BAB7854BCC4419F4683EBB8D9DA1EBF0D9767D042C9F4C231)


 
- **方案三**：调整圆角半径，当圆角半径较小时，可以减轻外侧线的显示。

 
 

#### 常见FAQ

Q：设置border边框宽度之后出现的外侧阴影线是否属于Bug。
 
A：不属于Bug。对于两层绘制且拥有相同圆角时，由于抗锯齿像素是半透明像素的原因无法遮挡下层内容，这是GPU绘制正常原理，且在其他平台均有相同情况。
