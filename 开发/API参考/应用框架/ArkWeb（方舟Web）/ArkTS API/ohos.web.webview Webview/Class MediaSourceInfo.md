# Class (MediaSourceInfo)

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

MediaSourceInfo 是表示媒体源信息的数据类。在 Web 媒体播放场景中，MediaSourceInfo 类封装了媒体源的基本信息，帮助应用了解媒体源的类型、地址和格式，应用根据这些信息创建自定义播放器并开始播放。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本Class首批接口从API version 12开始支持。 示例效果请以真机运行为准。

  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Web.Webview.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type12+ | SourceType | 否 | 否 | 媒体源的类型。 |
| source12+ | string | 否 | 否 | 媒体源地址。 |
| format12+ | string | 否 | 否 | 媒体源格式，可能为空，需要开发者自行判断格式。 |
 
 
**示例：**
 
```ArkTS
// xxx.ets
import { webview } from '@kit.ArkWeb';

const mediaInfo: webview.MediaSourceInfo = {
  type: webview.SourceType.URL,
  source: 'https://example.com/video.mp4',
  format: 'mp4'
};
```
