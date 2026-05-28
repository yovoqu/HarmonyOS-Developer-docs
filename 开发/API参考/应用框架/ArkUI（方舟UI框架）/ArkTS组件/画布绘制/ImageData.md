# ImageData

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ImageData对象可以存储canvas渲染的像素数据。
 
> [!NOTE]
> 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 创建ImageData时，宽高不超过16384px，最大面积不超过16000px*16000px，超过最大面积则无法正常绘制。当创建面积超过536870911px时，返回值的width和height均为0px，data为undefined。

  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(width: number, height: number, data?: Uint8ClampedArray)
 
创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 矩形区域宽度，默认单位为vp。 异常值NaN和Infinity按0处理。 |
| height | number | 是 | 矩形区域高度，默认单位为vp。 异常值NaN和Infinity按0处理。 |
| data | Uint8ClampedArray | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 传入异常值undefined时，data为undefined。 默认值：值全为0的一维数组 |
 
 
  

#### constructor12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
 
创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组，支持使用unit配置ImageData对象的单位模式。
 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 矩形区域宽度，默认单位为vp。 异常值NaN和Infinity按0处理。 |
| height | number | 是 | 矩形区域高度，默认单位为vp。 异常值NaN和Infinity按0处理。 |
| data | Uint8ClampedArray | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 传入异常值undefined时，data为undefined。 默认值：值全为0的一维数组 |
| unit | LengthMetricsUnit | 否 | 用来配置ImageData对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。 异常值undefined、NaN和Infinity按默认值处理。 默认值：DEFAULT |
 
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 矩形区域实际像素宽度。 单位为px。 |
| height | number | 是 | 否 | 矩形区域实际像素高度。 单位为px。 |
| data | Uint8ClampedArray | 是 | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |
 
 
> [!NOTE]
> 可使用 px2vp 接口进行单位转换。

 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

使用getImageData接口获得一个ImageData对象。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/1234.png"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/1234.png");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 130, 130)
          let imageData = this.context.getImageData(50, 50, 130, 130)
          this.context.putImageData(imageData, 150, 150)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
 
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/SfytEVK6SaKQV3zahLU-jQ/zh-cn_image_0000002611835925.png?HW-CC-KV=V1&HW-CC-Date=20260528T025539Z&HW-CC-Expire=86400&HW-CC-Sign=344B1C0561510B84268058CD9F877DADF60A20711DB1A92A8A06A06D9189A661)
