# OH_AuxiliaryPictureNative

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-auxiliarypicturenative
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AuxiliaryPictureNative OH_AuxiliaryPictureNative
```


#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AuxiliaryPicture结构体类型，用于执行AuxiliaryPicture相关操作。

使用[OH_AuxiliaryPictureNative_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_create)函数创建OH_AuxiliaryPictureNative对象。

使用[OH_PictureNative_GetAuxiliaryPicture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_picturenative_getauxiliarypicture)函数从OH_PictureNative对象中按辅助图类型获取OH_AuxiliaryPictureNative对象。

使用[OH_AuxiliaryPictureNative_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_release)函数释放OH_AuxiliaryPictureNative对象。

使用约束：使用OH_AuxiliaryPictureNative对象前，需先创建或获取对象；使用完成后，应调用[OH_AuxiliaryPictureNative_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_release)释放对象。通过[OH_AuxiliaryPictureNative_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_create)创建对象时，data、size和auxiliaryPicture均不能为空指针，dataLength必须大于0，type必须为当前支持的[Image_AuxiliaryPictureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#image_auxiliarypicturetype)。

资源管理：释放OH_PictureNative对象不会自动释放已经获取出的OH_AuxiliaryPictureNative对象；释放OH_AuxiliaryPictureNative对象也不会从OH_PictureNative对象中移除对应辅助图。通过[OH_AuxiliaryPictureNative_GetInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_getinfo)获取到的OH_AuxiliaryPictureInfo对象由调用方管理，使用完成后应调用[OH_AuxiliaryPictureInfo_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypictureinfo_release)释放。通过[OH_AuxiliaryPictureNative_GetMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_getmetadata)获取到的OH_PictureMetadata对象由调用方管理，使用完成后应调用[OH_PictureMetadata_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#oh_picturemetadata_release)释放。接口返回失败时，输出参数的内容不能在后续流程中继续使用。

OH_AuxiliaryPictureNative结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint8_t | pixels | 辅助图像素数据。 | OH_AuxiliaryPictureNative_ReadPixels | 读取辅助图的像素数据。 |
| uint8_t | pixels | 辅助图像素数据。 | OH_AuxiliaryPictureNative_WritePixels | 写入辅助图的像素数据。 |
| Image_AuxiliaryPictureType | type | 辅助图类型。 | OH_AuxiliaryPictureNative_GetType | 获取辅助图类型。 |
| OH_AuxiliaryPictureInfo | info | 辅助图信息。 | OH_AuxiliaryPictureNative_GetInfo | 获取辅助图信息。 |
| OH_AuxiliaryPictureInfo | info | 辅助图信息。 | OH_AuxiliaryPictureNative_SetInfo | 设置辅助图信息。 |
| OH_PictureMetadata | metadata | 辅助图元数据。 | OH_AuxiliaryPictureNative_GetMetadata | 获取辅助图的元数据。 |
| OH_PictureMetadata | metadata | 辅助图元数据。 | OH_AuxiliaryPictureNative_SetMetadata | 设置辅助图的元数据。 |


**起始版本：** 13

**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [picture_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h)

**相关开发指导：** [使用Image_NativeModule完成多图对象解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-picture-c)
