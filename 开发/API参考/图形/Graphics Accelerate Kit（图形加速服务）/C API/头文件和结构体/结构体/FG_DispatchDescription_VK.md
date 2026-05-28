# FG_DispatchDescription_VK

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___v_k
**支持设备：** Phone | Tablet | TV

##### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述下发帧生成命令[HMS_FG_Dispatch_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)需要的参数信息，每一帧都需要进行更新。该接口仅适配Vulkan图形API平台。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)
 
  

##### 汇总

**支持设备：** Phone | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| FG_ImageInfo_VK inputColorInfo | 真实渲染帧颜色缓冲区图像实例，该图像实例由HMS_FG_CreateImage_VK创建，由HMS_FG_DestroyImage_VK销毁。 |
| FG_ImageInfo_VK inputDepthStencilInfo | 真实渲染帧深度模板缓冲区图像实例，该图像实例由HMS_FG_CreateImage_VK创建，由HMS_FG_DestroyImage_VK销毁。 |
| FG_ImageInfo_VK outputColorInfo | 预测帧缓冲区图像实例 ，该图像实例由HMS_FG_CreateImage_VK创建，由HMS_FG_DestroyImage_VK销毁。 |
| FG_Mat4x4 viewProj | 真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| FG_Mat4x4 invViewProj | 真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| VkCommandBuffer vkCommandBuffer | 用于录入超帧绘制指令的命令缓冲区。 |
| uint8_t frameIdx | 当前帧序号，序号计数从0开始。该值必须小于FG_ContextDescription_VK中的framesInFlight，否则会返回错误码FG_INVALID_PARAMETER。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

##### frameIdx

**支持设备：** Phone | Tablet | TV

```text
uint8_t FG_DispatchDescription_VK::frameIdx
```
 
**描述**
 
当前帧序号，序号计数从0开始。该值必须小于[FG_ContextDescription_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___context_description___v_k)中的framesInFlight，否则会返回错误码FG_INVALID_PARAMETER。
 
  

##### inputColorInfo

**支持设备：** Phone | Tablet | TV

```text
FG_ImageInfo_VK FG_DispatchDescription_VK::inputColorInfo
```
 
**描述**
 
真实渲染帧颜色缓冲图像实例，该图像实例由[HMS_FG_CreateImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)创建，由[HMS_FG_DestroyImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)销毁。
 
  

##### inputDepthStencilInfo

**支持设备：** Phone | Tablet | TV

```text
FG_ImageInfo_VK FG_DispatchDescription_VK::inputDepthStencilInfo
```
 
**描述**
 
真实渲染帧深度模板缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)创建，由[HMS_FG_DestroyImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)销毁。
 
  

##### invViewProj

**支持设备：** Phone | Tablet | TV

```text
FG_Mat4x4 FG_DispatchDescription_VK::invViewProj
```
 
**描述**
 
真实渲染帧视图投影逆矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
 
  

##### outputColorInfo

**支持设备：** Phone | Tablet | TV

```text
FG_ImageInfo_VK FG_DispatchDescription_VK::outputColorInfo
```
 
**描述**
 
预测帧缓冲区图像实例，该图像实例由[HMS_FG_CreateImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)创建，由[HMS_FG_DestroyImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)销毁。
 
  

##### viewProj

**支持设备：** Phone | Tablet | TV

```text
FG_Mat4x4 FG_DispatchDescription_VK::viewProj
```
 
**描述**
 
真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
 
  

##### vkCommandBuffer

**支持设备：** Phone | Tablet | TV

```text
VkCommandBuffer FG_DispatchDescription_VK::vkCommandBuffer
```
 
**描述**
 
用于录入超帧绘制指令的命令缓冲区。
