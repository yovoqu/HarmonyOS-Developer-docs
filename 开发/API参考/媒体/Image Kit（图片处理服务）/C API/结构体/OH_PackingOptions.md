# OH_PackingOptions

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_PackingOptions OH_PackingOptions
```
  

##### 概述

OH_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。
 
创建PackingOptions结构体的对象使用[OH_PackingOptions_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_packingoptions_create)函数。
 
释放OH_PackingOptions对象使用[OH_PackingOptions_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_packingoptions_release)函数。
 
OH_PackingOptions结构体内容和操作方式如下：
  
| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| Image_MimeType | mimeType | MIME类型 | OH_PackingOptions_GetMimeType | 获取MIME类型。 |
| Image_MimeType | mimeType | MIME类型 | OH_PackingOptions_SetMimeType | 设置MIME类型。 |
| uint32_t | quality | 编码质量 | OH_PackingOptions_GetQuality | 获取编码质量。 |
| uint32_t | quality | 编码质量 | OH_PackingOptions_SetQuality | 设置编码质量。 |
| int32_t | desiredDynamicRange | 图片动态范围 | OH_PackingOptions_GetDesiredDynamicRange | 获取编码时期望的图片动态范围。 |
| int32_t | desiredDynamicRange | 图片动态范围 | OH_PackingOptions_SetDesiredDynamicRange | 设置编码时期望的图片动态范围。 |
 
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [image_packer_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h)
