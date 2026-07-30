# OH_PictureNative_MetadataCopyItem

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative-metadatacopyitem
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_PictureNative_MetadataCopyItem {...} OH_PictureNative_MetadataCopyItem
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

此结构体用于在创建PictureNative对象的深拷贝时指定元数据的拷贝规则。描述如何将元数据从一种类型拷贝到另一种类型。
 
**起始版本：** 26.0.0
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [picture_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picture-native-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Image_MetadataType srcType | 源元数据类型，指定要从源图片中拷贝的元数据类型。 起始版本： 26.0.0 |
| Image_MetadataType dstType | 目标元数据类型，指定拷贝的元数据在目标图片中存储的类型。 起始版本： 26.0.0 |
