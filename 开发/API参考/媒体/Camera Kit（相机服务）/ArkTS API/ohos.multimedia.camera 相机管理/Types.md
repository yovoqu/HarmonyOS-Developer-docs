# Types

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### ImageType

type ImageType = image.Image | image.Picture
 
图片容器类型，用于获取全质量图和未压缩图(YUV)。
 
**元服务API：** 从API version 23开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Multimedia.Camera.Core
  
| 类型 | 说明 |
| --- | --- |
| image.Image | 图片容器类型，用于获取全质量图。 |
| image.Picture | 图片容器类型，用于获取未压缩图(YUV)。 |
