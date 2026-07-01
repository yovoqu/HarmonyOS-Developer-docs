# OH_PictureMetadata

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturemetadata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_PictureMetadata OH_PictureMetadata
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_PictureMetadata用于承载Picture元数据。
 
有多种方式创建和获取OH_PictureMetadata：
  
| 函数 | 描述 |
| --- | --- |
| OH_PictureMetadata_Create() | 创建OH_PictureMetadata指针。 |
| OH_PictureMetadata_Clone() | 拷贝元数据。 |
| OH_PictureNative_GetMetadata() | 获取主图的元数据。 |
| OH_AuxiliaryPictureNative_GetMetadata() | 获取辅助图的元数据。 |
 
 
使用[OH_PictureMetadata_Release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#oh_picturemetadata_release)函数释放OH_PictureMetadata对象。
 
资源管理：通过[OH_PictureMetadata_Create()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#oh_picturemetadata_create)、[OH_PictureMetadata_Clone()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#oh_picturemetadata_clone)、[OH_PictureNative_GetMetadata()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_picturenative_getmetadata)或[OH_AuxiliaryPictureNative_GetMetadata()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_getmetadata)获取到的OH_PictureMetadata对象由调用方管理，使用完成后应调用[OH_PictureMetadata_Release()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#oh_picturemetadata_release)释放。通过[OH_PictureNative_SetMetadata()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_picturenative_setmetadata)或[OH_AuxiliaryPictureNative_SetMetadata()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h#oh_auxiliarypicturenative_setmetadata)设置元数据时，接口不会释放传入的OH_PictureMetadata对象。
 
OH_PictureMetadata结构体内容和操作方式如下：
  
| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| Image_String | property | 元数据属性。 | OH_PictureMetadata_GetProperty()、OH_PictureMetadata_GetPropertyWithNull() | OH_PictureMetadata_SetProperty() |
| OH_PictureMetadata | metadata | 元数据对象副本。 | OH_PictureMetadata_Clone() | - |
 
 
**起始版本：** 13
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [image_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)
