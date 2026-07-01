# 如何将app.media.app_icon，转换为PixelMap

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-9

使用getMediaContent获取媒体文件内容。使用createPixelMap创建PixelMap。
 
参考代码如下：
 
```text
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: PixelMap | null = null;

  convert() {
    try {
      <em>// Byte array of media files</em>
      this.getUIContext().getHostContext()!.resourceManager.getMediaContent($r('app.media.startIcon').id,
        (error: BusinessError, value: Uint8Array) => {
          if (error) {
            console.error(`getMediaContent failed: ${error.code}, ${error.message}`);
            return;
          }
          let pixelMapInitOptions: image.InitializationOptions = {
            editable: true,
            pixelFormat: 3,
            size: { height: 4, width: 6 }
          };
          <em>// Create an imageSource instance</em>
          let imageSource = image.createImageSource(value.buffer);
          <em>// Decoding to generate PixelMap</em>
          imageSource.createPixelMap(pixelMapInitOptions).then((pixelMap) => {
            this.pixelMap = pixelMap;
            <em>// Pixel operations or rendering can be performed here.</em>
          }).catch((decodeError: BusinessError) => {
            console.error(`Decode failed: ${decodeError.code}, ${decodeError.message}`);
          });
        });
    } catch (error) {
      console.error(`Global error: ${error.code}, ${error.message}`);
    }
  }


  build() {
    Column() {
      Button('Click to convert')
        .onClick(() => {
          this.convert();
        })
        .margin({ bottom: 16 })
      Image(this.pixelMap)
    }
    .padding(16)
  }
}
```
 
**参考链接**
 
[getMediaContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getmediacontent9)
 
[image.createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)
