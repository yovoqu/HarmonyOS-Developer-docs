# 使用rotate接口对PixelMap多次旋转后图像逐渐变小

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-60

#### 问题现象

使用[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)组件显示[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)图像数据，对PixelMap图像使用[rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#rotate9)接口多次旋转后，图片逐渐变小，直到几乎消失不见。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/ImulG6fERCa1oi0XYPmojw/zh-cn_image_0000002628552512.png?HW-CC-KV=V1&HW-CC-Date=20260730T072620Z&HW-CC-Expire=86400&HW-CC-Sign=34C22BBE773F8966916ABFC43F35833A06699E8DE1D3F934A1732BFD02D157D5)

 
 

#### 背景知识

- [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)组件用于显示图片，支持加载PixelMap类型的数据源。[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)属性用于设置图片的填充效果，当取值为[ImageFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagefit).Contain时将会对图片保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。
- [PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)是图像像素类，用于读取或写入图像数据以及获取图像信息。[rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#rotate9)接口会根据输入的角度对PixelMap进行旋转，当旋转的角度不是90的整数倍时，旋转后PixelMap的尺寸会发生改变。

 
 

#### 问题定位

出现问题的核心代码如下：
 1. 使用Image组件显示PixelMap数据，组件id为'ImageContent'，objectFit属性设置为ImageFit.Contain，确保图片完整显示。
2. 旋转图片时，先获取Image组件的组件截图，对组件截图旋转相应的角度后，将旋转后的PixelMap赋值给状态变量currentPixelMap，显示在Image组件上。
```text
<em>// 显示PixelMap图像</em>
Image(this.currentPixelMap)
  .id('ImageContent')
  .objectFit(ImageFit.Contain)

<em>// 旋转PixelMap图像的函数</em>
rotateImage: (rotate: number) => void = (rotate: number) => {
  let pixelMap = componentSnapshot.getSync('ImageContent'); <em>// 获取Image组件的组件截图</em>
  pixelMap?.rotateSync(rotate);                             <em>// 对Image组件的截图旋转相应的角度</em>
  this.currentPixelMap = pixelMap;                          <em>// 用旋转后的组件截图刷新Image组件显示的PixelMap数据</em>
}
```

 
每次旋转时都是对Image组件截图，并对截图内容进行旋转，然后将旋转后的内容重新显示在Image组件上。存在以下问题：
 1. Image组件本身会对图像进行缩放，当objectFit属性设置为ImageFit.Contain时，会放大或者缩小图像使得图像完全显示在显示边界内，若图像本身的宽高比和Image组件的宽高比不一致时，图像不能正好完全铺满Image组件，这时对Image组件截图得到的PixelMap中图像只占一部分，另一部分是组件的背景。
2. 使用rotate接口对图像进行旋转后，当旋转角度不是90的整数倍时，旋转后图像的尺寸会变大，这时旋转前的图像只占据了旋转后图像的一部分。如果对旋转后的图像继续旋转非90度的整数倍，那么图像的尺寸会再次变大，原始图像占据的部分会越来越小，显示在Image组件上时就会逐渐变小。
 
 

#### 分析结论

在旋转图像时，旋转的不是原始图像，而是对Image组件的截图进行旋转，并且每次旋转都是在上一次旋转得到的图像上进行旋转，而旋转角度为非90度的整数倍时，旋转后的图像尺寸会发生变化，旋转前只占据旋转后图像的一部分，连续多次旋转后，原始图像在图像中占据的部分会越来越小，因此当显示在Image组件上时，看起来图像逐渐变小。
 
参考代码如下：
 
```json
import image from '@ohos.multimedia.image';
import { Context } from '@kit.AbilityKit';

@Entry
@Component
export struct PixelMapRotateSmallerDemo {
  @State rotationPixelMap: image.PixelMap | undefined = undefined; <em>// 旋转PixelMap</em>
  private pixelMap: image.PixelMap | undefined = undefined; <em>// 原始PixelMap</em>
  private rotation: number = 0; <em>// 旋转角度</em>

  async aboutToAppear(): Promise<void> {
    let imageSource: image.ImageSource | undefined;
    try {
     <em> // 读取图片文件，这里以Rawfile目录下的img.png图片为例</em>
      let context = this.getUIContext().getHostContext() as Context;
      let fileData: Uint8Array = context.resourceManager.getRawFileContentSync('img.png');
      <em>// 解码图片文件为PixelMap</em>
      imageSource = image.createImageSource(fileData.buffer.slice(0));
      this.pixelMap = await imageSource.createPixelMap();

      this.rotationPixelMap = await this.getPixelmap();
    } catch (err) {
      console.error(`Failed to load image, Cause: ${JSON.stringify(err)}`);
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
    }
  }

  async getPixelmap() {
    if (this.pixelMap === undefined) {
      return undefined;
    }
    try {
      <em>// 从原始PixelMap读取像素数据</em>
      let bufferSize = this.pixelMap.getPixelBytesNumber();
      let pixelsBuffer = new ArrayBuffer(bufferSize);
      this.pixelMap.readPixelsToBufferSync(pixelsBuffer);
      let info = this.pixelMap.getImageInfoSync();
      <em>// 创建新的PixelMap，确保每次都在原图基础上旋转</em>
      let initOpts: image.InitializationOptions = {
        size: info.size,
        srcPixelFormat: info.pixelFormat,
      };
      let pixelMap = await image.createPixelMap(pixelsBuffer, initOpts);
      return pixelMap;
    } catch (err) {
      console.error(`Failed to copy pixelmap, Cause: ${JSON.stringify(err)}`);
      return undefined;
    }
  }

  async rotatePixelmap() {
    <em>// 设置旋转角度，每次旋转30度</em>
    this.rotation = (this.rotation + 30) % 360;
    let oldPixelMap: image.PixelMap | undefined;
    try {
      let newPixelMap = await this.getPixelmap();
      if (newPixelMap === undefined) {
        return;
      }
      <em>// 旋转PixelMap</em>
      newPixelMap.rotateSync(this.rotation);
      <em>// 保存旧PixelMap</em>
      oldPixelMap = this.rotationPixelMap;
      <em>// 更新PixelMap</em>
      this.rotationPixelMap = newPixelMap;
    } catch (err) {
      console.error(`failed to rotate image, Cause: ${JSON.stringify(err)}`);
    } finally {
      if (oldPixelMap) {
        oldPixelMap.release();
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      Image(this.rotationPixelMap)
        .width('100%')
        .aspectRatio(1)
        .objectFit(ImageFit.None);

      Button() {
        Text('Rotate')
          .padding(8)
          .fontSize(30)
          .fontColor(Color.White);
      }
      .backgroundColor('#0A59F7')
      .onClick(() => {
        this.rotatePixelmap();
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
 
 

#### 修改建议

多次旋转图像时，确保每次旋转都是在原始图像的基础上旋转。
