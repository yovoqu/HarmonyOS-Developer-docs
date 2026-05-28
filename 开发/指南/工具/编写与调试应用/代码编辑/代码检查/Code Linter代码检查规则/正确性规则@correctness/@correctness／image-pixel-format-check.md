# @correctness/image-pixel-format-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-pixel-format-check

在使用Image组件[createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)接口时，建议不要选择RGB_565档位，避免出现色阶问题。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@correctness/image-pixel-format-check": "warn"
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例

```text
import image from '@ohos.multimedia.image';
const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: height, width: width }
    })
  }
  
}
```
 
 

#### 反例

```text
import image from '@ohos.multimedia.image';
const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    // warning
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: height, width: width }
    })
  }
}
```
 
 

#### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@correctness/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
