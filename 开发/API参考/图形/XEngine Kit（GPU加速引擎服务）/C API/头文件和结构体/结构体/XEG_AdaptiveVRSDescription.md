# XEG_AdaptiveVRSDescription

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrsdescription
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_adaptive_vrs.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-adaptive-vrs-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| float * reprojectionMatrix | 参数可选，参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵*上一帧的观察矩阵）*（（当前帧的投影矩阵*当前帧的观察矩阵）的逆矩阵），矩阵必须是4*4列主序的矩阵。 |
| VkImageView inputColorImage | 上一帧渲染管线最终渲染结果颜色附件的VkImageView。 |
| VkImageView inputDepthImage | 当前帧渲染管线深度附件的VkImageView。 |
| VkImageView outputShadingRateImage | 准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。 |
 
 
> [!NOTE]
> 对创建VkImageView的VkImage对象有以下约束： imageType = VK_IMAGE_TYPE_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

 
  

##### 结构体成员变量说明

  

##### inputColorImage

```text
VkImageView XEG_AdaptiveVRSDescription::inputColorImage
```
 
**描述**
 
上一帧渲染管线最终渲染结果颜色附件的VkImageView。
 
  

##### inputDepthImage

```text
VkImageView XEG_AdaptiveVRSDescription::inputDepthImage
```
 
**描述**
 
当前帧渲染管线深度附件的VkImageView。
 
  

##### outputShadingRateImage

```text
VkImageView XEG_AdaptiveVRSDescription::outputShadingRateImage
```
 
**描述**
 
准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。
 
  

##### reprojectionMatrix

```text
float* XEG_AdaptiveVRSDescription::reprojectionMatrix
```
 
**描述**
 
参数可选，默认值为nullptr, 参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵*上一帧的观察矩阵）*（（当前帧的投影矩阵*当前帧的观察矩阵）的逆矩阵），矩阵必须是4*4列主序的矩阵。
