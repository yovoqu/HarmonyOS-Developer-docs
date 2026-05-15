# OhosImageSourceSupportedFormat

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
struct OhosImageSourceSupportedFormat {...}
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist)和[OH_ImageSource_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getsupportedformats)接口使用。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| char* format = nullptr | 图像源支持的格式字符串头地址。 |
| size_t size = 0 | 图像源支持的格式字符串大小。 |
