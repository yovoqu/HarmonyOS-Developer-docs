# XEG_RTShadowParameters

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowparameters
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

光线追踪阴影（Shadow）算法参数。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_rt_visible_mask.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-visible-mask-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| float rayTMax | 阴影光线的tMax值。 |
| float rayTMin | 阴影光线的tMin值。 |
| float sunDirection [3] | 方向光的方向。 |
| float raySourceAngleInDegree = 0.0f | 沿光源方向进行阴影采样的角度范围，值越大，半影区域越大。此参数的值将被限制在[0.0, 90.0]范围内。默认值为0.0。 |
| uint32_t shadowCullMask = 0x5FF | 配置光线查询rayQueryInitializeEXT函数中的rayFlags和cullMask参数，高24bit表示rayFlags，低8bit表示cullMask。 默认值为0x5FF，即 ((gl_RayFlagsOpaqueEXT \| gl_RayFlagsTerminateOnFirstHitEXT) << 8) \| 0xFF。 |
| float shadowCullDistance | 阴影剔除的世界空间距离，场景中像素超过此距离时不计算阴影，必须大于0。 |
| uint32_t rayPerPixel = 1 | 每像素采样数，当前仅支持1spp。默认值为1。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### rayPerPixel

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
uint32_t XEG_RTShadowParameters::rayPerPixel = 1
```
 
**描述**
 
每像素采样数，当前仅支持1spp。默认值为1。
 
  

#### raySourceAngleInDegree

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowParameters::raySourceAngleInDegree = 0.0f
```
 
**描述**
 
沿光源方向进行阴影采样的角度范围，值越大，半影区域越大。此参数的值将被限制在[0.0, 90.0]范围内。默认值为0.0。
 
  

#### rayTMax

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowParameters::rayTMax
```
 
**描述**
 
阴影光线的tMax值。
 
  

#### rayTMin

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowParameters::rayTMin
```
 
**描述**
 
阴影光线的tMin值。
 
  

#### shadowCullDistance

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowParameters::shadowCullDistance
```
 
**描述**
 
阴影剔除的世界空间距离，场景中像素超过此距离时不计算阴影，必须大于0。
 
  

#### shadowCullMask

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
uint32_t XEG_RTShadowParameters::shadowCullMask = 0x5FF
```
 
**描述**
 
配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数，高24bit表示rayFlags，低8bit表示cullMask。 默认值为0x5FF，即 ((gl_RayFlagsOpaqueEXT | gl_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF。
 
  

#### sunDirection

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowParameters::sunDirection[3]
```
 
**描述**
 
方向光的方向。
