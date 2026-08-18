# Image组件宽高等比例放大后图片出现锯齿如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1559

#### 问题现象

使用Image组件时，若对图片进行尺寸放大（尤其是等比例放大），应如何解决由此导致的图片模糊和边缘锯齿问题？
 
效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/MA1U6KZvT5WL5ELzUq1fIg/zh-cn_image_0000002658849111.png?HW-CC-KV=V1&HW-CC-Date=20260811T005642Z&HW-CC-Expire=86400&HW-CC-Sign=64CAB10C1548281822A0F24B475B69E9EDF0FA8D31C18A2770547E036F16F3CE)

 
 

#### 背景知识

- 图片插值是指在缩放图片时，系统所采用的一种用于计算新像素颜色的数学算法。主要目的是缓解因缩放导致的图像边缘锯齿问题，使放大后的图片看起来更平滑。
- Image组件可通过[interpolation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#interpolation)属性设置图片的插值效果，SVG类型图源不支持该属性。该属性的具体行为可由[ImageInterpolation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageinterpolation)枚举值定义，不同的设置采用了不同的插值算法。其中None对应最近邻插值，是一种高效的算法；High是Cubic插值，插值质量最高，但计算开销相对较大。

 
 

#### 解决方案

要缓解图片放大时的锯齿问题，可将Image组件的interpolation属性设置为ImageInterpolation.High，以启用高质量的插值算法。
 
代码如下：
 
```text
@Entry
@Component
struct ImageScalingDemo {
  @State picWidth: number = 100; // Image组件的宽度


  build() {
    Column({ space: 10 }) {
      // 可更换为其他图片资源
      Image($r('app.media.startIcon'))
        .width(this.picWidth)
        .objectFit(ImageFit.Contain) // 设置图片缩放时保持宽高比，且不超出组件边界
        .interpolation(ImageInterpolation.High) // 设置图片的插值效果为Cubic插值
        .autoResize(false); // 关闭图源自动缩放
      Button('点击图片放大').onClick(() => this.picWidth += 50);
      Button('点击图片缩小').onClick(() => this.picWidth -= 50);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
 
效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/a19wmy04T9C-XCF94w2krA/zh-cn_image_0000002628609852.png?HW-CC-KV=V1&HW-CC-Date=20260811T005642Z&HW-CC-Expire=86400&HW-CC-Sign=A83AFF4E70EC9C99D3BED340E82E70E5250D62F8DAA6563B0CA811DF8DC948F9)

 
 

#### 常见FAQ

Q：如何实现图片自适应不失真？
 
A：[autoResize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#autoresize)属性可以设置图片解码过程中是否对图源自动缩放。autoResize设为false时，按原图尺寸解码，提升显示效果，但会增加内存占用。当autoResize设为true，且原图在显示时被进行了缩放，图片都会出现些许的失真、模糊。最佳清晰度配置建议如下：
 
- 图片缩小显示时：.autoResize(false) + .interpolation(.Medium)
- 图片放大显示时：.interpolation(.High)
