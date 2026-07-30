# ImageBitmap

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagebitmap
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建[Worker线程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction)，支持使用postMessage将ImageBitmap实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

> [!NOTE]
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 ImageBitmap对象仅支持加载静态图片，如需播放动图，建议使用 Image 组件。



#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(src: string)

通过图片数据源创建ImageBitmap对象。

> [!NOTE]
> 使用完毕后应调用close()方法释放资源，避免图形资源泄漏。


**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片数据源，支持本地图片。 1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。 type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。 2、支持本地图片类型：bmp、jpg、png、svg和webp类型。 说明： - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |




#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(data: PixelMap)

通过PixelMap创建ImageBitmap对象。

> [!NOTE]
> 使用完毕后应调用close()方法释放资源，避免图形资源泄漏。


**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | PixelMap | 是 | 图片数据源，通过PixelMap对象设置。适用于需要对图片进行解码、处理后再绘制的场景，可提高图片加载性能。 |




#### constructor12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(src: string, unit: LengthMetricsUnit)

通过图片数据源创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

> [!NOTE]
> 使用完毕后应调用close()方法释放资源，避免图形资源泄漏。


**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片数据源，支持本地图片。 1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。 type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。 2、支持本地图片类型：bmp、jpg、png、svg和webp类型。 说明： - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |
| unit | LengthMetricsUnit | 是 | 用于配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。 默认值：LengthMetricsUnit.DEFAULT。 异常值undefined、NaN和Infinity按默认值处理。 |




#### constructor12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(data: PixelMap, unit: LengthMetricsUnit)

通过PixelMap创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

> [!NOTE]
> 使用完毕后应调用close()方法释放资源，避免图形资源泄漏。


**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | PixelMap | 是 | 图片数据源，通过PixelMap对象设置。适用于需要对图片进行解码、处理后再绘制的场景，可提高图片加载性能。 |
| unit | LengthMetricsUnit | 是 | 用于配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。 默认值：LengthMetricsUnit.DEFAULT。 异常值undefined、NaN和Infinity按默认值处理。 |




#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(data: Resource, unit?: LengthMetricsUnit)

通过Resource创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

> [!NOTE]
> 使用完毕后应调用close()方法释放资源，避免图形资源泄漏。


**起始版本：** 26.0.0

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Resource | 是 | 图片数据源，通过Resource资源引用方式设置。适用于引用应用资源目录下的图片资源，如\$r('app.media.example')，可避免硬编码路径。 支持图片类型：bmp、jpg、png、svg和webp类型。 |
| unit | LengthMetricsUnit | 否 | 用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同CanvasRenderingContext2D。 默认值：LengthMetricsUnit.DEFAULT。 异常值undefined、NaN和Infinity按默认值处理。 |




#### close

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): void

释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。

> [!NOTE]
> 必须与 constructor() 方法配对使用，创建ImageBitmap对象后，应在使用完毕时调用close()释放资源。未调用close()可能导致图形资源泄漏，影响应用性能。 建议在Canvas绘制完成后调用，如在 onReady 回调的最后调用close()。


**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | ImageBitmap的宽度。 单位：vp。 |
| height | number | 是 | 否 | ImageBitmap的高度。 单位：vp。 |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（加载图片）

通过ImageBitmap加载本地图片。

> [!NOTE]
> 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需启用相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中 copyCodeResource 相关介绍。


```ArkTS
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap('common/images/example.jpg');

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/OHJ9FPtKRQKCR1H4IhNUWw/zh-cn_image_0000002686088267.png?HW-CC-KV=V1&HW-CC-Date=20260730T071510Z&HW-CC-Expire=86400&HW-CC-Sign=B913BCA521FE8C75EBE87347326239DE7FDFA575A365A0BE3D74E9BE89AE1359)




#### 示例2（创建ImageBitmap）

通过PixelMap创建ImageBitmap对象。

> [!NOTE]
> DevEco Studio的预览器不支持getPixelMap接口，不支持显示PixelMap绘制的内容。


```ArkTS
// xxx.ets
@Entry
@Component
struct Demo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = '#00ff00'
          this.context.fillRect(0, 0, 100, 100)
          let pixel = this.context.getPixelMap(0, 0, 100, 100)
          let image = new ImageBitmap(pixel)
          this.context.drawImage(image, 100, 100)
        })

    }
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-9QQYJ3RTWqzMwxfKNHyeQ/zh-cn_image_0000002685928437.png?HW-CC-KV=V1&HW-CC-Date=20260730T071510Z&HW-CC-Expire=86400&HW-CC-Sign=1F9ECB88F8D2BF11D91DE51DCB1D617A2680C036FE0BA7FCFFAACA55C095479F)




#### 示例3（支持并发线程绘制）

通过创建Worker线程，实现并发线程绘制。

> [!NOTE]
> DevEco Studio的预览器不支持显示在Worker线程中绘制的内容。


```ArkTS
import { worker } from '@kit.ArkTS';

@Entry
@Component
struct imageBitmapExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.myWorker.postMessage({ myImage: this.img });
          this.myWorker.onmessage = (e): void => {
            if (e.data.myImage) {
              let image: ImageBitmap = e.data.myImage
              this.context.transferFromImageBitmap(image)
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。

```text
import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  if (e.data.myImage) {
    let img: ImageBitmap = e.data.myImage
    let offCanvas = new OffscreenCanvas(600, 600)
    let offContext = offCanvas.getContext('2d')
    offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
    let image = offCanvas.transferToImageBitmap()
    workerPort.postMessage({ myImage: image });
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/r6aw7YhtQJSI0wyTket9Xg/zh-cn_image_0000002686088267.png?HW-CC-KV=V1&HW-CC-Date=20260730T071510Z&HW-CC-Expire=86400&HW-CC-Sign=642C8522E8FBE75995727F073B17165953DAFDAF21AC8D3DB56DA350D87983ED)




#### 示例4（加载Resource图片）

通过constructor接口创建Resource类型的ImageBitmap对象，用于Canvas绘制。

从API版本26.0.0开始，新增[constructor](#constructor-2)接口。

```ArkTS
// xxx.ets
@Entry
@Component
struct ImageBitmapResourceExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "app.media.example"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap($r("app.media.example"));

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/nWUJyMEsQx-xbzkgLHiRyQ/zh-cn_image_0000002656008760.png?HW-CC-KV=V1&HW-CC-Date=20260730T071510Z&HW-CC-Expire=86400&HW-CC-Sign=34953F937CCC34B0290A67989F797A1CA9E319262A9668626DB189D1B6D254EF)
