# XEG_DDGICreateInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

此结构体描述创建具有DDGI特性的[XEG_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| XEG_StructureType sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针。 |
| XEG_RTGIQualityMode qualityMode | 输出图像的质量模式，必须为XEG_RTGIQualityMode中的枚举值。 |
| uint32_t numberVolume | 需要同时渲染的最大体积数量，范围为[1, 9]。 |
| VkExtent2D scaledView | 渲染宽高缩小倍率，建议范围为[1, 4]，必须不小于1。 |
| VkExtent2D viewSize | 输出GI图像的渲染宽高。 |
| bool enableCloud | 是否开启端云模式，true为开启，false为关闭。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### enableCloud

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
bool XEG_DDGICreateInfo::enableCloud
```
 
**描述**
 
是否开启端云模式，true为开启，false为关闭。
 
  

#### numberVolume

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
uint32_t XEG_DDGICreateInfo::numberVolume
```
 
**描述**
 
需要同时渲染的最大体积数量，范围为[1, 9]。
 
  

#### pNext

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
const void* XEG_DDGICreateInfo::pNext
```
 
**描述**
 
指向扩展结构的指针。
 
  

#### qualityMode

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
XEG_RTGIQualityMode XEG_DDGICreateInfo::qualityMode
```
 
**描述**
 
输出图像的质量模式，必须为[XEG_RTGIQualityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgiqualitymode)中的枚举值。
 
  

#### scaledView

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkExtent2D XEG_DDGICreateInfo::scaledView
```
 
**描述**
 
渲染宽高缩小倍率，建议范围为[1, 4]，必须不小于1。
 
  

#### sType

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
XEG_StructureType XEG_DDGICreateInfo::sType
```
 
**描述**
 
识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_DDGI_CREATE_INFO。
 
  

#### viewSize

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkExtent2D XEG_DDGICreateInfo::viewSize
```
 
**描述**
 
输出GI图像的渲染宽高。
