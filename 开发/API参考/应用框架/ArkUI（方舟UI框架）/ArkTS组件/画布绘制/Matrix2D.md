# Matrix2D

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于画布绘制[CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)、[OffscreenCanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d)、[CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern)和[Path2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d)的矩阵对象，可以对矩阵进行缩放、旋转和平移等变换。
 
Matrix2D的使用场景包括：
 1. [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)和[OffscreenCanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d)中调用[getTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#gettransform)接口获取画布的图形变换矩阵Matrix2D对象，调用[setTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#settransform-1)接口对后续绘制内容进行Matrix2D对象对应的图形变换。
2. [CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern)中调用[setTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern#settransform)接口对[CanvasPattern](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern)对象进行Matrix2D对象对应的图形变换。
3. [Path2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d)中调用[addPath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d#addpath)接口对[Path2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d)对象进行Matrix2D对象对应的图形变换。
 
> [!NOTE]
> 从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### 构造函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### constructor10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor()
 
构造二维变换矩阵对象，默认值是属性全为0的矩阵。
 
**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(unit: LengthMetricsUnit)
 
构造二维变换矩阵对象，默认值是属性全为0的矩阵，支持配置Matrix2D对象的单位模式。
 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | 是 | 用来配置Matrix2D对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。 异常值NaN和Infinity按默认值处理。 默认值：DEFAULT |
 
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scaleX | number | 否 | 是 | 水平缩放系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| scaleY | number | 否 | 是 | 垂直缩放系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateX | number | 否 | 是 | 水平倾斜系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateY | number | 否 | 是 | 垂直倾斜系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| translateX | number | 否 | 是 | 水平平移距离，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 默认单位：vp |
| translateY | number | 否 | 是 | 垂直平移距离，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 默认单位：vp |
 
 
> [!NOTE]
> 可使用 px2vp 接口进行单位转换。

 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Parameter {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](assets/Matrix2D/file-20260514164110145-2.png)

 
  

#### 方法

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### identity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

identity(): Matrix2D
 
创建单位矩阵。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 单位矩阵。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Identity {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix = this.matrix.identity()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 100, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](assets/Matrix2D/file-20260514164110145-3.png)

 
  

#### invert

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

invert(): Matrix2D
 
获取当前矩阵的逆矩阵。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 逆矩阵结果。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Invert {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.invert()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](assets/Matrix2D/file-20260514164110145-4.png)

 
  

#### multiply(deprecated)

multiply(other?: Matrix2D): Matrix2D
 
当前矩阵与目标矩阵相乘。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。
 
该接口从API version 10开始废弃，且无实际绘制效果，故不提供示例。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Matrix2D | 否 | 目标矩阵。 异常值undefined和null按无效值处理。 默认值：null |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 相乘结果矩阵。 |
 
 
  

#### rotate(deprecated)

rotate(rx?: number, ry?: number): Matrix2D
 
对当前矩阵进行旋转运算。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。
 
该接口从API version 10开始废弃，推荐使用[rotate](#rotate10)。
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(50, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(50, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](assets/Matrix2D/file-20260514164110145-5.png)

 
  

#### rotate10+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

rotate(degree: number, rx?: number, ry?: number): Matrix2D
 
以旋转点为中心，对当前矩阵进行右乘旋转运算。
 
**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转弧度，取值范围无限制。顺时针方向为正弧度，可以通过角度 * Math.PI / 180将角度转换为弧度值传入该接口。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：弧度 |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。 默认单位：vp 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：0 |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。 默认单位：vp 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：0 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(60, 80, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(-60 * Math.PI / 180, 5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(60, 80, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](assets/Matrix2D/file-20260514164110145-6.png)

 
  

#### translate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

translate(tx?: number, ty?: number): Matrix2D
 
对当前矩阵进行左乘平移运算。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tx | number | 否 | 水平方向平移距离，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp 默认值：0 |
| ty | number | 否 | 垂直方向平移距离，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp 默认值：0 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 平移后结果矩阵对象。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(40, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = 0
          this.matrix.rotateY = 0
          this.matrix.translateX = 0
          this.matrix.translateY = 0
          this.matrix.translate(100, 100)
          this.context.setTransform(this.matrix)
          this.context.fillRect(40, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/wMDu6_iUR4uh-BEQ7D1srw/zh-cn_image_0000002611835937.png?HW-CC-KV=V1&HW-CC-Date=20260528T025539Z&HW-CC-Expire=86400&HW-CC-Sign=BD690643C4B1E7D9F70DB147DDD8AEF75EC96069585CEF966C8AF6469CECD665)

 
  

#### scale

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

scale(sx?: number, sy?: number): Matrix2D
 
对当前矩阵进行右乘缩放运算。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| sx | number | 否 | 水平缩放比例系数，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：1.0 |
| sy | number | 否 | 垂直缩放比例系数，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：1.0 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Matrix2D | 缩放结果矩阵对象。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(120, 70, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.scale(0.5, 0.5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(120, 70, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/YHivEQITQcyE3J1qi5_d1A/zh-cn_image_0000002581276192.png?HW-CC-KV=V1&HW-CC-Date=20260528T025539Z&HW-CC-Expire=86400&HW-CC-Sign=7AB2359167946D15823C9A2AA827E34725E985505B03175BAC5DC21B7A869C98)
