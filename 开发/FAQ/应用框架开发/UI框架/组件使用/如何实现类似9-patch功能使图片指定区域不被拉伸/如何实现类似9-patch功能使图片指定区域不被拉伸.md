# 如何实现类似9-patch功能使图片指定区域不被拉伸

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-694

#### 问题现象

如何实现一个带箭头的聊天气泡背景，在拉伸时气泡四角和箭头都不变形，类似9-patch图。
 
 

#### 背景知识

- 9-patch图：是一种特殊的PNG格式图片，分为伸缩区（下图灰色，可拉伸区域）和安全区（下图黑色，固定区域），当图片拉伸时，仅对可拉伸区域进行拉伸，固定区域保持原始尺寸与形态不变。

| 水平拉伸（灰色为可拉伸区域） | 垂直拉伸（灰色为可拉伸区域） |

| --- | --- |

|  |  |
- Image组件的[resizable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#resizable11)属性，可精准指定图片的可拉伸区域与固定区域，从而确保图片在不同尺寸的容器中都能保持良好的视觉效果。
[slice](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implementing-image-resizable#section192433524230)参数可以通过上、下、左、右四个偏移量定义四个角的区域为固定区域。
- [lattice](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implementing-image-resizable#section0797147172420)参数支持将图像划分为矩形网格，同时处于偶数列和偶数行（从0开始计算）上的网格图像是固定的，不会被拉伸。

 - 矩形网格对象通过[createImageLattice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice#createimagelattice12)方法创建，使用屏幕物理像素单位px。可以将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的。如果目标网格足够大，则这些固定网格以其原始大小进行绘制；如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。其余网格将进行缩放，来适应剩余的空间。

 
 

#### 解决方案

- **方案一**、对于样式简单的气泡图，通过配置ResizableOptions类型的slice参数，设置统一的上下左右拉伸距离，即可实现类似9-patch图的拉伸效果。拉伸示例图如下（灰色为可拉伸区域）：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/LI_ReM1NQPqHvQRiZolRBQ/zh-cn_image_0000002658794125.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=810165704FB528A3E6A0E67E592FBD75DF5CE35A0E30EF7655427878A68969B5)


1. 通过为slice参数指定上、下、左、右四个方向的像素偏移值，将一张图片划分为九宫格布局。

2. 此时四个角的区域为固定区域，其余为可拉伸区域。

  
> [!NOTE]
> slice除了在resizable属性中使用，还支持在 backgroundImageResizable 属性中使用。


  
```text
@Entry
@Component
struct Page {
  build() {
    Column({ space: 20 }) {
      Stack() {
      <em>  // 加载原始图片资源（不改变大小，不进行任何拉伸处理）</em>
        Image($r('app.media.bubble'))
          .objectFit(ImageFit.None);
        Column() {
          Text('初始图片')
            .fontColor(Color.White);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('calc(100% - 10px)');
      }
      .height(100);

    <em>  // 第二个Stack：显示应用九宫格拉伸的图片</em>
      Stack() {
    <em>    // 加载相同图片资源，应用九宫格拉伸规则</em>
        Image($r('app.media.bubble'))
          .resizable({
            slice: {
              top: '80px',
              left: '30px',
              bottom: '30px',
              right: '80px'
            }
          })
          .width('100%')
          .height('100%');
        Column() {
          Text('实现四角+箭头不拉伸,其他内部文字可以撑开固定区域,比如下面这一段文字，可以把这个气泡撑开，圆角箭头无变形，来达到四角和箭头不拉伸')
            .fontColor(Color.White)
            .padding({
              left: 10,
              right: 15,
            });
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      }
      .alignContent(Alignment.TopStart)
      .width(240)
      .height(120);
    }
    .margin(20);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/SZX4njH2TiaZ9CiCzV62IQ/zh-cn_image_0000002628554754.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=50526980D219AF9E2C9735EDE58FE868B5658D35C4F2910DA750EA683C5C26E5)

- **方案二**、针对结构复杂的气泡图，可以通过ResizableOptions类型的lattice参数，将图像划分为一个矩形网格来实现拉伸控制。拉伸示例图如下（灰色为可拉伸区域）：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Scptf98AREKloD-AGoVurw/zh-cn_image_0000002628394860.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=2F71A0FA5ED2984D99D6DF5C708641AFBD18F970A22D68F5212F88D72ADB71AA)


1. 首先将原图划分为矩形网格，使无需发生形变的区域处于矩形网格的偶数行偶数列，并获取相应像素值。如上图所示，气泡图的水平方向包含左、中、右三个固定区域（图中黑色标注部分），因此水平上一共划分为五个区域。垂直方向上，则只有中间部分为可拉伸区域（图中灰色标注部分），因此垂直方向上共划分为三个区域。

2. 创建DrawingLattice对象，并应用在Stack中作为背景图片的Image上。

  
> [!NOTE]
> lattice参数对同样可以设置图像拉伸的 backgroundImageResizable 接口不生效。


  
```text
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
 <em> // X轴分割线：定义图片在水平方向的4条切割线（单位：像素）,将图片分为5个区域</em>
  xDivs: Array<number> = [79, 162, 198, 279];
 <em> // Y轴分割线：定义垂直方向的2条切割线（单位：像素）,将图片分为2个区域</em>
  yDivs: Array<number> = [78, 81];
 <em> // 创建九宫格拉伸规则对象,水平分割线数组，垂直分割线数组，水平分区数(5区域)，垂直分区数(3区域)</em>
  lattice: DrawingLattice =
    drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.xDivs.length, this.yDivs.length);

  build() {
    Column({ space: 20 }) {
  <em>    // 第一个Stack：显示原始图片</em>
      Stack() {
     <em>   // 加载原始图片资源（不进行任何拉伸处理）</em>
        Image($r('app.media.9patch'))
          .objectFit(ImageFit.None);
        Column() {
          Text('初始图片')
            .fontColor(Color.White);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('calc(100% - 20px)');
      }
      .height(65);

  <em>    // 第二个Stack：显示应用九宫格拉伸的图片</em>
      Stack() {
     <em>   // 加载相同图片资源，应用九宫格拉伸规则</em>
        Image($r('app.media.9patch'))
     <em>   // 应用自定义拉伸规则</em>
          .resizable({ lattice: this.lattice })
          .width('100%')
          .height('100%');
        Column() {
          Text('实现四角+底部中间箭头不拉伸呵呵')
            .fontColor(Color.White)
            .padding({
              left: 15,
              right: 15,
            });
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('calc(100% - 20px)');
      }
      .alignContent(Alignment.TopStart)
      .width(240)
      .height(65);
    }
    .margin(20);
  }
}
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/gNp8BujKRI6KMbS6WOMShA/zh-cn_image_0000002658914079.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=D3D8334FB3A2B43749C8F931473C909EF34ED6E97374B720C449E3EE35EE39CB)
