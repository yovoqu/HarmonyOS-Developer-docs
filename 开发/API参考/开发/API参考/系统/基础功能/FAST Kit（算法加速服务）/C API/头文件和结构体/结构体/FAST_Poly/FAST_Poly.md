# FAST_Poly

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-poly
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

定义稀疏格式多项式的数据结构。多项式
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/onzRR1s1RO26Q7FNLxUl8w/zh-cn_image_0000002698143501.png?HW-CC-KV=V1&HW-CC-Date=20260811T005502Z&HW-CC-Expire=86400&HW-CC-Sign=E91C579CA4E297DA8E2808FE17A6F3C9BCEE21C69233EB3E19190207D6733D02)
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
