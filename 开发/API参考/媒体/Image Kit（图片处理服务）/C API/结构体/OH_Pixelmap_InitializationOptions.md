# OH_Pixelmap_InitializationOptions

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/age-nativemodule-oh-pixelmap-initializationoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Pixelmap_InitializationOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_Pixelmap_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。
 
创建OH_Pixelmap_InitializationOptions对象使用[OH_PixelmapInitializationOptions_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_create)函数。
 
释放OH_Pixelmap_InitializationOptions对象使用[OH_PixelmapInitializationOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapinitializationoptions_release)函数。
 
OH_Pixelmap_InitializationOptions结构体内容和操作方式如下：
  
| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32_t | width | 图片宽 | OH_PixelmapInitializationOptions_GetWidth | 获取图片宽。 |
| uint32_t | width | 图片宽 | OH_PixelmapInitializationOptions_SetWidth | 设置图片宽。 |
| uint32_t | height | 图片高 | OH_PixelmapInitializationOptions_GetHeight | 获取图片高。 |
| uint32_t | height | 图片高 | OH_PixelmapInitializationOptions_SetHeight | 设置图片高。 |
| int32_t | pixelFormat | 像素格式 | OH_PixelmapInitializationOptions_GetPixelFormat | 获取像素格式。 |
| int32_t | pixelFormat | 像素格式 | OH_PixelmapInitializationOptions_SetPixelFormat | 设置像素格式。 |
| int32_t | alphaType | 透明度类型 | OH_PixelmapInitializationOptions_GetAlphaType | 获取透明度类型。 |
| int32_t | alphaType | 透明度类型 | OH_PixelmapInitializationOptions_SetAlphaType | 设置透明度类型。 |
 
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [pixelmap_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)
