# XEG_TemporalUpscaleCreateInfo

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscalecreateinfo
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

此结构体描述创建[XEG_TemporalUpscale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG_TemporalUpscale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_temporalupscale)对象。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_temporal_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-temporal-upscale-8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| VkExtent2D inputSize | 输入图像的尺寸。支持的最大尺寸为2048 * 1024。 |
| VkExtent2D outputSize | 输出图像的尺寸。 |
| VkRect2D outputRegion | 超分输出图像区域。 |
| VkFormat outputFormat | 输出图像的格式。 |
| int jitterNum | 相机抖动的周期数，取值范围为[4, 16]，如果该值不在范围内，则创建操作将失败，并返回错误代码VK_ERROR_VALIDATION_FAILED_EXT，推荐8。 |
| bool isDepthReversed | 是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### inputSize

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkExtent2D XEG_TemporalUpscaleCreateInfo::inputSize
```
 
**描述**
 
输入图像的尺寸。支持的最大尺寸为2048 * 1024。
 
  

##### isDepthReversed

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
bool XEG_TemporalUpscaleCreateInfo::isDepthReversed
```
 
**描述**
 
是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。
 
  

##### jitterNum

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
int XEG_TemporalUpscaleCreateInfo::jitterNum
```
 
**描述**
 
相机抖动的周期数，取值范围为[4, 16]，如果该值不在范围内，则创建操作将失败，并返回错误代码VK_ERROR_VALIDATION_FAILED_EXT，推荐8。
 
  

##### outputFormat

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkFormat XEG_TemporalUpscaleCreateInfo::outputFormat
```
 
**描述**
 
输出图像的格式。
 
  

##### outputRegion

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkRect2D XEG_TemporalUpscaleCreateInfo::outputRegion
```
 
**描述**
 
超分输出图像区域。
 
  

##### outputSize

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkExtent2D XEG_TemporalUpscaleCreateInfo::outputSize
```
 
**描述**
 
输出图像的尺寸。
