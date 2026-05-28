# FG_ImageSync_VK

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k
**支持设备：** Phone | Tablet | TV

#### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)
 
  

#### 汇总

**支持设备：** Phone | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| VkAccessFlagBits accessMask | 内存访问类型的位掩码。 |
| VkImageLayout layout | 图像和图像子资源的内存布局。 |
| VkPipelineStageFlagBits stages | 管线阶段的位掩码。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

#### accessMask

**支持设备：** Phone | Tablet | TV

```text
VkAccessFlagBits FG_ImageSync_VK::accessMask
```
 
**描述**
 
内存访问类型的位掩码。
 
  

#### layout

**支持设备：** Phone | Tablet | TV

```text
VkImageLayout FG_ImageSync_VK::layout
```
 
**描述**
 
图像和图像子资源的内存布局。
 
  

#### stages

**支持设备：** Phone | Tablet | TV

```text
VkPipelineStageFlagBits FG_ImageSync_VK::stages
```
 
**描述**
 
管线阶段的位掩码。
