# Types

更新时间：2026-03-09 07:25:19

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### HdrMetadataValue12+

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata
 
PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)关键字相对应。
 
**系统能力：** SystemCapability.Multimedia.Image.Core
  
| 类型 | 说明 |
| --- | --- |
| HdrMetadataType | HdrMetadataKey中HDR_METADATA_TYPE关键字对应的元数据值类型。 |
| HdrStaticMetadata | HdrMetadataKey中HDR_STATIC_METADATA关键字对应的元数据值类型。 |
| ArrayBuffer | HdrMetadataKey中HDR_DYNAMIC_METADATA关键字对应的元数据值类型。 |
| HdrGainmapMetadata | HdrMetadataKey中HDR_GAINMAP_METADATA关键字对应的元数据值类型。 |
