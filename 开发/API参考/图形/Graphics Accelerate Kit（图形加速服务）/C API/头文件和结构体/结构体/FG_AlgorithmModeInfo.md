# FG_AlgorithmModeInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___algorithm_mode_info
**支持设备：** Phone | Tablet | TV

#### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述超帧算法模式信息。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__base_8h)
 
  

#### 汇总

**支持设备：** Phone | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| FG_PredictionMode predictionMode | 超帧预测算法模式，支持内插模式和外插模式。 |
| FG_MeMode meMode | 超帧运动估计算法模式，支持基础模式和增强模式。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

#### meMode

**支持设备：** Phone | Tablet | TV

```text
FG_MeMode FG_AlgorithmModeInfo::meMode
```
 
**描述**
 
超帧运动估计算法模式，支持基础模式和增强模式。
 
  

#### predictionMode

**支持设备：** Phone | Tablet | TV

```text
FG_PredictionMode FG_AlgorithmModeInfo::predictionMode
```
 
**描述**
 
超帧预测算法模式，支持内插模式和外插模式。
