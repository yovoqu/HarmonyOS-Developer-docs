# OpenGTX_ConfigDescription

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description
**支持设备：** Phone | Tablet | TV

#### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述OpenGTX属性配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [opengtx_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)
 
  

#### 汇总

**支持设备：** Phone | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OpenGTX_LTPO_Mode mode | LTPO方案模式，支持场景模式、触控模式、自适应模式。 |
| int32_t targetFPS | 游戏应用目标帧率，取值范围[30,144]。 |
| char* packageName | 游戏包名，字节长度范围[1,256]。 |
| char* appVersion | 游戏应用版本号，字节长度范围[1,256]。 |
| OpenGTX_EngineType engineType | 游戏引擎类型。 |
| char* engineVersion | 游戏引擎版本号，字节长度范围[0,256]。 |
| OpenGTX_GameType gameType | 游戏类型。 |
| OpenGTX_PictureQualityMaxLevel pictureQualityMaxLevel | 图像质量。 |
| OpenGTX_ResolutionValue resolutionMaxValue | 游戏应用支持的最高分辨率，取值范围360p-8k。 |
| int32_t gameMainThreadId | 游戏应用的逻辑线程ID，取值范围[0,∞)。 |
| int32_t gameRenderThreadId | 游戏应用的渲染线程ID，取值范围[0,∞)。 |
| int32_t gameKeyThreadIds [5] | 游戏应用的关键线程ID列表，取值范围[0,∞)。 |
| bool vulkanSupport | 是否支持Vulkan。 取值范围：[true, false]。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

#### appVersion

**支持设备：** Phone | Tablet | TV

```text
char* OpenGTX_ConfigDescription::appVersion
```
 
**描述**
 
游戏应用版本号，字节长度范围[1,256]。
 
  

#### engineType

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_EngineType OpenGTX_ConfigDescription::engineType
```
 
**描述**
 
游戏引擎类型。
 
  

#### engineVersion

**支持设备：** Phone | Tablet | TV

```text
char* OpenGTX_ConfigDescription::engineVersion
```
 
**描述**
 
游戏引擎版本号，字节长度范围[0,256]。
 
  

#### gameKeyThreadIds[5]

**支持设备：** Phone | Tablet | TV

```text
int32_t OpenGTX_ConfigDescription::gameKeyThreadIds[5]
```
 
**描述**
 
游戏应用的关键线程ID列表，取值范围[0,∞)。
 
  

#### gameMainThreadId

**支持设备：** Phone | Tablet | TV

```text
int32_t OpenGTX_ConfigDescription::gameMainThreadId
```
 
**描述**
 
游戏应用的逻辑线程ID，取值范围[0,∞)。
 
  

#### gameRenderThreadId

**支持设备：** Phone | Tablet | TV

```text
int32_t OpenGTX_ConfigDescription::gameRenderThreadId
```
 
**描述**
 
游戏应用的渲染线程ID，取值范围[0,∞)。
 
  

#### gameType

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_GameType OpenGTX_ConfigDescription::gameType
```
 
**描述**
 
游戏类型。
 
  

#### mode

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_LTPO_Mode OpenGTX_ConfigDescription::mode
```
 
**描述**
 
LTPO方案模式，支持场景模式、触控模式、自适应模式。
 
  

#### packageName

**支持设备：** Phone | Tablet | TV

```text
char* OpenGTX_ConfigDescription::packageName
```
 
**描述**
 
游戏包名，字节长度范围[1,256]。
 
  

#### pictureQualityMaxLevel

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_PictureQualityMaxLevel OpenGTX_ConfigDescription::pictureQualityMaxLevel
```
 
**描述**
 
图像质量。
 
  

#### resolutionMaxValue

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_ResolutionValue OpenGTX_ConfigDescription::resolutionMaxValue
```
 
**描述**
 
游戏应用支持的最高分辨率，取值范围360p-8k。
 
  

#### targetFPS

**支持设备：** Phone | Tablet | TV

```text
int32_t OpenGTX_ConfigDescription::targetFPS
```
 
**描述**
 
游戏应用目标帧率，取值范围[30,144]。
 
  

#### vulkanSupport

**支持设备：** Phone | Tablet | TV

```text
bool OpenGTX_ConfigDescription::vulkanSupport
```
 
**描述**
 
是否支持Vulkan。
