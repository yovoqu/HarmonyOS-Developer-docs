# Interface (QuickImageDataHandler)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-quickimagedatahandler
**支持设备：** Phone / PC/2in1 / Tablet / TV

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / TV


```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```


## onDataPrepared13+
**支持设备：** Phone / PC/2in1 / Tablet / TV

onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void

当请求的图片资源准备就绪时，系统会回调媒体资源就绪通知方法。如果资源准备出错，回调的data将为undefined。

map支持返回的信息：


| map键名 | 值说明 |
| --- | --- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |


**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 已就绪的图片资源数据。泛型，支持[Picture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture)数据类型。 |
| imageSource | image.ImageSource | 是 | 已就绪的图片资源数据。 |
| map13+ | Map&lt;string, string&gt; | 是 | 用于获取图片资源的额外信息，如图片质量。仅支持'quality'。 |


**示例：**


```ts
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(
    data: image.Picture,
    imageSource: image.ImageSource,
    map: Map<string, string>,
  ) {
    console.info('on image data prepared');
  }
}
```
