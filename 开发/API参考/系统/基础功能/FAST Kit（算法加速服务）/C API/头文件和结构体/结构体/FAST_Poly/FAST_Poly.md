# FAST_Poly

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-poly
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

定义稀疏格式多项式的数据结构。多项式
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/SbRIg1LrQjueHw0aneLAnA/zh-cn_image_0000002686088885.png?HW-CC-KV=V1&HW-CC-Date=20260730T072232Z&HW-CC-Expire=86400&HW-CC-Sign=9A67CDB4AD334E162E3B63BDB20AA90B2F5A2D407891DE7418B4F9F4BD798930)
由系数数组coeff和指数数组pow共同描述，且需按指数升序排列。
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_solver_polynomial.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-polynomial-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| double * coeff | 多项式的系数数组。 |
| uint32_t * pow | 多项式的指数数组。 |
| size_t length | 多项式的项数。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### coeff

**支持设备：** Phone | PC/2in1 | Tablet

```text
double * FAST_Poly::coeff
```
 
**描述**
 
多项式的系数数组，与pow数组一一对应，表示对应指数项的系数值。
 
  

#### length

**支持设备：** Phone | PC/2in1 | Tablet

```text
size_t FAST_Poly::length
```
 
**描述**
 
多项式的项数，即coeff和pow数组的长度。
 
  

#### pow

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t * FAST_Poly::pow
```
 
**描述**
 
多项式的指数数组，与coeff数组一一对应，且需按指数升序排列。
