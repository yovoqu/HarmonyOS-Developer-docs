# OH_PackingOptions

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_PackingOptions OH_PackingOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。
 
使用[OH_PackingOptions_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_packingoptions_create)函数创建OH_PackingOptions对象。
 
使用[OH_PackingOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_packingoptions_release)函数释放OH_PackingOptions对象。
 
使用约束：OH_PackingOptions用于配置ImageSource、PixelMap或Picture编码参数。
 
- ImageSource编码需传入[OH_ImagePackerNative_PackToDataFromImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtodatafromimagesource)或[OH_ImagePackerNative_PackToFileFromImageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtofilefromimagesource)使用。
- PixelMap编码需传入[OH_ImagePackerNative_PackToDataFromPixelmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtodatafrompixelmap)或[OH_ImagePackerNative_PackToFileFromPixelmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtofilefrompixelmap)使用。
- Picture编码需传入[OH_ImagePackerNative_PackToDataFromPicture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtodatafrompicture)或[OH_ImagePackerNative_PackToFileFromPicture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_packtofilefrompicture)使用。
- PixelMap序列编码请使用[OH_PackingOptionsForSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptionsforsequence)。

 
资源管理：释放OH_ImagePackerNative对象不会自动释放OH_PackingOptions对象。OH_PackingOptions使用完成后，应调用[OH_PackingOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_packingoptions_release)释放，释放后不应继续传入图像编码接口或调用其字段获取和设置接口。
 
OH_PackingOptions结构体内容和操作方式如下：
  
| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| Image_MimeType | mimeType | 目标编码格式的MIME类型。ImageSource或PixelMap编码支持image/jpeg、image/webp、image/png、image/heic或image/heif、image/sdr_astc_4x4、image/sdr_sut_superfast_4x4、image/hdr_astc_4x4；Picture编码支持image/jpeg、image/heic或image/heif。实际支持范围以OH_ImagePackerNative_GetSupportedFormats返回结果为准。 | OH_PackingOptions_GetMimeType、OH_PackingOptions_GetMimeTypeWithNull | OH_PackingOptions_SetMimeType |
| uint32_t | quality | 编码质量，实际编码效果取决于目标编码格式。 | OH_PackingOptions_GetQuality | OH_PackingOptions_SetQuality |
| bool | needsPackProperties | 是否需要编码图像属性，例如Exif。 | OH_PackingOptions_GetNeedsPackProperties | OH_PackingOptions_SetNeedsPackProperties |
| int32_t | desiredDynamicRange | 编码时期望的图片动态范围，取值见IMAGE_PACKER_DYNAMIC_RANGE。 | OH_PackingOptions_GetDesiredDynamicRange | OH_PackingOptions_SetDesiredDynamicRange |
 
 
> [!NOTE]
> 通过 OH_PackingOptions_SetMimeType 设置MIME类型时，接口会拷贝传入的format->data，不会持有调用方传入的数据指针。 通过 OH_PackingOptions_GetMimeType 或 OH_PackingOptions_GetMimeTypeWithNull 获取MIME类型时，接口成功返回的format.data由接口分配，使用完成后调用方应使用free()释放。

 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [image_packer_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h)
