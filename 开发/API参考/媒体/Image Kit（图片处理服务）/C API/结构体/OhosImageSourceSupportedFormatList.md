# OhosImageSourceSupportedFormatList

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OhosImageSourceSupportedFormatList {...}
```
  

##### 概述

定义图像源支持的格式字符串列表。由[OH_ImageSource_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getsupportedformats)获取。
 
**起始版本：** 10
 
**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)
 
**所在头文件：** [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| struct OhosImageSourceSupportedFormat** supportedFormatList = nullptr | 图像源支持的格式字符串列表头地址。 |
| size_t size = 0 | 图像源支持的格式字符串列表大小。 |
