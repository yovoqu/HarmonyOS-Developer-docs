# OH_Pixelmap_ImageInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-imageinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Pixelmap_ImageInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_Pixelmap_ImageInfo是Native层封装的图像像素信息结构体，保存图像像素的宽高、行跨距、像素格式、透明度类型、是否为HDR等信息，适用于在Native层查询Pixelmap属性的场景。
 
创建OH_Pixelmap_ImageInfo对象使用[OH_PixelmapImageInfo_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapimageinfo_create)函数，使用完成后需调用[OH_PixelmapImageInfo_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapimageinfo_release)函数释放资源，两者需配对使用，否则会导致内存泄漏。
 
OH_Pixelmap_ImageInfo结构体内容和操作方式如下：
  
| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32_t | width | 图片宽，单位：像素（px）。 | OH_PixelmapImageInfo_GetWidth | 获取图片宽。 |
| uint32_t | height | 图片高，单位：像素（px）。 | OH_PixelmapImageInfo_GetHeight | 获取图片高。 |
| uint32_t | rowStride | 行跨距，单位：字节（Byte）。表示每行像素数据在内存中占用的字节数。受内存对齐影响，该值可能大于图片宽度对应的实际像素数据字节数。 | OH_PixelmapImageInfo_GetRowStride | 获取行跨距。 |
| int32_t | pixelFormat | 像素格式，取值参考PIXEL_FORMAT。 | OH_PixelmapImageInfo_GetPixelFormat | 获取像素格式。 |
| int32_t | alphaType | 透明度类型，取值参考PIXELMAP_ALPHA_TYPE。 | OH_PixelmapImageInfo_GetAlphaType | 获取透明度类型。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息。true表示是HDR，false表示非HDR。 | OH_PixelmapImageInfo_GetDynamicRange | 获取Pixelmap是否为高动态范围的信息。返回true表示是HDR，返回false表示非HDR。 |
 
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
