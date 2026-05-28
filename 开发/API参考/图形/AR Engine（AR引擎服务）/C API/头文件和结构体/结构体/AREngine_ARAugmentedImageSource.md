# AREngine_ARAugmentedImageSource

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-araugmentedimagesource
**支持设备：** Phone | Tablet | TV

#### 概述

**支持设备：** Phone | Tablet | TV

图像数据。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)
 
**所在头文件：** [ar_engine_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)
 
  

#### 汇总

**支持设备：** Phone | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| const char *imageName | 图像名，不允许为空，255个字符以内，超过255个字符的部分将被自动截断。 |
| const uint8_t *imageData | 灰度图像元素数组地址。 |
| int32_t pixelWidth | 图像像素宽度。 |
| int32_t pixelHeight | 图像像素高度。 |
| int32_t stride | 图像步幅。 |
| float realWidthInMeters | 图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

#### imageName

**支持设备：** Phone | Tablet | TV

```text
const char* AREngine_ARAugmentedImageSource::imageName
```
 
**描述**
 
图像名，不允许为空，255个字符以内，超过255个字符的部分将被自动截断。
 
  

#### imageData

**支持设备：** Phone | Tablet | TV

```text
const uint8_t* AREngine_ARAugmentedImageSource::imageData
```
 
**描述**
 
灰度图像元素数组地址。
 
  

#### pixelWidth

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARAugmentedImageSource::pixelWidth
```
 
**描述**
 
图像像素宽度。
 
  

#### pixelHeight

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARAugmentedImageSource::pixelHeight
```
 
**描述**
 
图像像素高度。
 
  

#### stride

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARAugmentedImageSource::stride
```
 
**描述**
 
图像步幅。
 
  

#### realWidthInMeters

**支持设备：** Phone | Tablet | TV

```text
float AREngine_ARAugmentedImageSource::realWidthInMeters
```
 
**描述**
 
图像中对象的实际物理宽度。无限制，默认值为291mm。
