# OH_Pixelmap_HdrMetadataValue

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-image-nativemodule-oh-pixelmap-hdrmetadatavalue
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Pixelmap_HdrMetadataValue {...} OH_Pixelmap_HdrMetadataValue
```
  

##### 概述

Pixelmap使用的HDR元数据值，和OH_Pixelmap_HdrMetadataKey关键字相对应。用于[OH_PixelmapNative_SetMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_getmetadata)，有相应[OH_Pixelmap_HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| OH_Pixelmap_HdrMetadataType type | HDR_METADATA_TYPE关键字对应的具体值。 |
| OH_Pixelmap_HdrStaticMetadata staticMetadata | HDR_STATIC_METADATA关键字对应的具体值。 |
| OH_Pixelmap_HdrDynamicMetadata dynamicMetadata | HDR_DYNAMIC_METADATA关键字对应的具体值。 |
| OH_Pixelmap_HdrGainmapMetadata gainmapMetadata | HDR_GAINMAP_METADATA关键字对应的具体值。 |
