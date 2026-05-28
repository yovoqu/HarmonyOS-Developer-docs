# FG_DispatchDescription_GLES

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___g_l_e_s
**支持设备：** Phone | Tablet | TV

##### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述下发帧生成命令[HMS_FG_Dispatch_GLES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_gles)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_gles.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__gles_8h)
 
  

##### 汇总

**支持设备：** Phone | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t inputColor | 真实渲染帧颜色缓冲区索引，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。 取值范围：[0, 2^32 -1]。 |
| uint32_t inputDepthStencil | 真实渲染帧深度模板缓冲区索引，支持格式包括GL_DEPTH24_STENCIL8、GL_DEPTH32F_STENCIL8。 取值范围：[0, 2^32 -1]。 |
| FG_Mat4x4 viewProj | 真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| FG_Mat4x4 invViewProj | 真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| uint32_t outputColor | 预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。 取值范围：[0, 2^32 -1]。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

##### inputColor

**支持设备：** Phone | Tablet | TV

```text
uint32_t FG_DispatchDescription_GLES::inputColor
```
 
**描述**
 
真实渲染帧颜色缓冲区索引，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。
 
  

##### inputDepthStencil

**支持设备：** Phone | Tablet | TV

```text
uint32_t FG_DispatchDescription_GLES::inputDepthStencil
```
 
**描述**
 
真实渲染帧深度模板缓冲区索引，支持格式包括GL_DEPTH24_STENCIL8、GL_DEPTH32F_STENCIL8。
 
  

##### invViewProj

**支持设备：** Phone | Tablet | TV

```text
FG_Mat4x4 FG_DispatchDescription_GLES::invViewProj
```
 
**描述**
 
真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
 
  

##### outputColor

**支持设备：** Phone | Tablet | TV

```text
uint32_t FG_DispatchDescription_GLES::outputColor
```
 
**描述**
 
预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL_RGBA8、GL_R11F_G11F_B10F、GL_RGBA16F。
 
  

##### viewProj

**支持设备：** Phone | Tablet | TV

```text
FG_Mat4x4 FG_DispatchDescription_GLES::viewProj
```
 
**描述**
 
真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
