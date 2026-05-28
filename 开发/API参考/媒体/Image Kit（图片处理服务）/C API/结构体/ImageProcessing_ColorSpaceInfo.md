# ImageProcessing_ColorSpaceInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-imageprocessing-imageprocessing-colorspaceinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```


##### 概述

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH_ImageProcessing_IsColorSpaceConversionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscolorspaceconversionsupported), [OH_ImageProcessing_IsCompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscompositionsupported), [OH_ImageProcessing_IsDecompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：** [ImageProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing)

**所在头文件：** [image_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-types-h)



##### 汇总



##### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32_t metadataType | 定义元数据类型，参考OH_Pixelmap_HdrMetadataKey。 |
| int32_t colorSpace | 定义色彩空间，参考ColorSpaceName。 |
| int32_t pixelFormat | 定义像素格式，参考PIXEL_FORMAT。 |
