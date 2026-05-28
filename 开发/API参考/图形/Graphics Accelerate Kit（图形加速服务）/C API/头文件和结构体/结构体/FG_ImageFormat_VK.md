# FG_ImageFormat_VK

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_format___v_k
**支持设备：** Phone | Tablet | TV

##### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)
 
  

##### 汇总

**支持设备：** Phone | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| VkFormat inputColorFormat | 真实渲染帧颜色缓冲区图像格式。 |
| VkFormat inputDepthStencilFormat | 深度模板缓冲区图像格式。 |
| VkFormat outputColorFormat | 预测帧缓冲区图像格式。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

##### inputColorFormat

**支持设备：** Phone | Tablet | TV

```text
VkFormat FG_ImageFormat_VK::inputColorFormat
```
 
**描述**
 
真实渲染帧颜色缓冲区图像格式。
 
  

##### inputDepthStencilFormat

**支持设备：** Phone | Tablet | TV

```text
VkFormat FG_ImageFormat_VK::inputDepthStencilFormat
```
 
**描述**
 
深度模板缓冲区图像格式。
 
  

##### outputColorFormat

**支持设备：** Phone | Tablet | TV

```text
VkFormat FG_ImageFormat_VK::outputColorFormat
```
 
**描述**
 
预测帧缓冲区图像格式。
