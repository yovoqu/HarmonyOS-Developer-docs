# OhosImageSourceInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OhosImageSourceInfo {...}
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义图像源信息，由[OH_ImageSource_GetImageInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getimageinfo)获取。
 
**起始版本：** 10
 
**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)
 
**所在头文件：** [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t pixelFormat | 图像源像素格式，由OH_ImageSource_CreateFromUri、OH_ImageSource_CreateFromFd和OH_ImageSource_CreateFromData设置。 |
| int32_t colorSpace | 图像源色彩空间。 |
| int32_t alphaType | 图像源透明度类型。 |
| int32_t density | 图像源密度，由OH_ImageSource_CreateFromUri、OH_ImageSource_CreateFromFd和OH_ImageSource_CreateFromData设置。 |
| struct OhosImageSize size | 图像源像素宽高的大小。 |
