# Interface (MediaAssetProgressHandler)

更新时间：2026-03-19 08:47:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-photoaccesshelper-mediaassetprogresshandler
**支持设备：** Phone / PC/2in1 / Tablet / TV

媒体资产进度处理器，应用于onProgress方法中获取媒体资产进度。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / TV


```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```


## onProgress15+
**支持设备：** Phone / PC/2in1 / Tablet / TV

onProgress(progress: number): void

当所请求的视频资源返回进度时系统会回调此方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | 返回的进度百分比，范围为[0, 100]。 |
