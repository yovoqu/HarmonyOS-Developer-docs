# OH_DecodingOptions

更新时间：2026-08-07 10:00:25

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_DecodingOptions OH_DecodingOptions
```


#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_DecodingOptions是native层封装的解码选项参数结构体，用于设置解码选项参数，在创建Pixelmap时作为入参传入，详细信息见[OH_ImageSourceNative_CreatePixelmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmap)。

OH_DecodingOptions结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

使用[OH_DecodingOptions_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_decodingoptions_create)函数创建OH_DecodingOptions对象。

使用[OH_DecodingOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_decodingoptions_release)函数释放OH_DecodingOptions对象。

使用约束：OH_DecodingOptions用于配置PixelMap解码参数，通常作为[OH_ImageSourceNative_CreatePixelmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmap)、[OH_ImageSourceNative_CreatePixelmapUsingAllocator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmapusingallocator)或[OH_ImageSourceNative_CreatePixelmapList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmaplist)的入参。使用前需通过[OH_DecodingOptions_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_decodingoptions_create)创建对象；使用完成后，应调用[OH_DecodingOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_decodingoptions_release)释放对象。

资源管理：释放OH_ImageSourceNative或解码生成的OH_PixelmapNative对象，不会自动释放OH_DecodingOptions对象。OH_DecodingOptions释放后，不应继续传入解码接口或调用其字段获取和设置接口。

OH_DecodingOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段默认值 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- | --- |
| int32_t | pixelFormat | 像素格式。 | RGBA_8888 | OH_DecodingOptions_GetPixelFormat | OH_DecodingOptions_SetPixelFormat |
| uint32_t | index | 解码图片序号。 | 0 | OH_DecodingOptions_GetIndex | OH_DecodingOptions_SetIndex |
| float | rotate | 旋转角度。 | 单位为角度（deg），默认值为0 | OH_DecodingOptions_GetRotate | OH_DecodingOptions_SetRotate |
| Image_Size | desiredSize | 期望输出大小。 | 默认为原始图片尺寸。 | OH_DecodingOptions_GetDesiredSize | OH_DecodingOptions_SetDesiredSize |
| Image_Region | desiredRegion | 解码区域。 | 默认为完整图片大小的区域。 | OH_DecodingOptions_GetDesiredRegion | OH_DecodingOptions_SetDesiredRegion |
| int32_t | desiredDynamicRange | 期望动态范围。 | SDR | OH_DecodingOptions_GetDesiredDynamicRange | OH_DecodingOptions_SetDesiredDynamicRange |
| int32_t | desiredColorSpace | 期望色彩空间。 | 默认色彩空间。 | OH_DecodingOptions_GetDesiredColorSpace | OH_DecodingOptions_SetDesiredColorSpace |
| Image_Region | cropRegion | 裁剪区域。 | 默认为完整图片大小的区域。 | OH_DecodingOptions_GetCropRegion | OH_DecodingOptions_SetCropRegion |
| int32_t | cropAndScaleStrategy | 裁剪和缩放策略。 | 0 | OH_DecodingOptions_GetCropAndScaleStrategy | OH_DecodingOptions_SetCropAndScaleStrategy |


**起始版本：** 12

**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [image_source_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h)

**相关开发指导：** [使用Image_NativeModule完成图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c)、[图片区域解码与下采样(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-region-and-downsampling-c)、[使用Image_NativeModule完成HDR图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-hdr-decoding-c)
