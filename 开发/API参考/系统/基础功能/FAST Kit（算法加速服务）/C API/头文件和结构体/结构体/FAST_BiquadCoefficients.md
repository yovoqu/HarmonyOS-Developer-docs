# FAST_BiquadCoefficients

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。
 
传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/yb2Y6NOuRRC6Bzo9EBl9Sw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T025200Z&HW-CC-Expire=86400&HW-CC-Sign=CFF8E22B3E3398CC7E01B9E9E63A14F24ED78F36B2024D00E2FCDAB8544C3155)
 
 
分母中的1实际上为系数a0归一化后的结果。
  

 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| float a1 | z⁻¹ 分母系数。 |
| float a2 | z⁻² 分母系数。 |
| float b0 | z⁰ 分子系数。 |
| float b1 | z⁻¹ 分子系数。 |
| float b2 | z⁻² 分子系数。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### a1

**支持设备：** Phone | PC/2in1 | Tablet

```text
float FAST_BiquadCoefficients::a1
```
 
**描述**
 
z⁻¹ 分母系数。
 
  

#### a2

**支持设备：** Phone | PC/2in1 | Tablet

```text
float FAST_BiquadCoefficients::a2
```
 
**描述**
 
z⁻² 分母系数。
 
  

#### b0

**支持设备：** Phone | PC/2in1 | Tablet

```text
float FAST_BiquadCoefficients::b0
```
 
**描述**
 
z⁰ 分子系数。
 
  

#### b1

**支持设备：** Phone | PC/2in1 | Tablet

```text
float FAST_BiquadCoefficients::b1
```
 
**描述**
 
z⁻¹ 分子系数。
 
  

#### b2

**支持设备：** Phone | PC/2in1 | Tablet

```text
float FAST_BiquadCoefficients::b2
```
 
**描述**
 
z⁻² 分子系数。
