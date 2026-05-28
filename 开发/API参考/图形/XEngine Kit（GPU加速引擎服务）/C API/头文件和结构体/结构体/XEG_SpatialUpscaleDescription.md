# XEG_SpatialUpscaleDescription

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscaledescription
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_spatial_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-spatial-upscale-8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| VkImageView inputImage | 超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |
| VkImageView outputImage | 超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |
 
 
> [!NOTE]
> 对创建VkImageView的VkImage对象有以下约束： imageType = VK_IMAGE_TYPE_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

##### inputImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_SpatialUpscaleDescription::inputImage
```
 
**描述**
 
超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。
 
  

##### outputImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_SpatialUpscaleDescription::outputImage
```
 
**描述**
 
超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。
