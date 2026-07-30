# OH_Pixelmap_HdrDynamicMetadata

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrdynamicmetadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_Pixelmap_HdrDynamicMetadata {...} OH_Pixelmap_HdrDynamicMetadata
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示HDR_DYNAMIC_METADATA关键字对应的动态元数据值，用于存储HDR图像的动态元数据。HDR动态元数据可用于在显示过程中动态调整HDR图像的显示参数，以适配不同显示设备的能力，获得更准确的HDR显示效果。在调用[OH_PixelmapNative_SetMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_setmetadata)和[OH_PixelmapNative_GetMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_getmetadata)时作为[OH_Pixelmap_HdrMetadataValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue)的成员使用。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t *data | 动态元数据值的指针，指向存储动态元数据的二进制数据缓冲区，缓冲区长度由length成员指定。 |
| uint32_t length | 动态元数据值的长度，单位：字节（Byte），取值需与data指向的数据缓冲区实际长度一致。 |
