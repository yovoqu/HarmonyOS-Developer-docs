# Image_String

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-string
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Image_String {...}
typedef struct Image_String Image_MimeType
typedef struct Image_String Image_String
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

字符串结构，用于描述字符串数据地址和数据长度。Image_MimeType是Image_String的别名，用于表示MIME类型。
 
作为输入参数使用时，调用方负责保证data和size有效；作为输出参数使用时，data的分配和释放方式以具体接口说明为准。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [image_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char *data = nullptr | 指向字符串数据首地址的指针。 |
| size_t size = 0 | 字符串数据长度。 |
