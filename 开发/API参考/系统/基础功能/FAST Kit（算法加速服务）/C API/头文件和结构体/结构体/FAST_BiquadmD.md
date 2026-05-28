# FAST_BiquadmD

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadmd
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

定义双精度多通道、多节二阶IIR滤波器组的数据结构。
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint8_t* activeFilters | 活跃滤波器掩码数组。 |
| uint8_t isInitialized | 初始化标志。 |
| double* channelGains | 每通道线性增益因子数组。 |
| FAST_BiquadCoefficientsD* coefficients | 滤波器系数数组。 |
| size_t maxFrames | 单次处理最大采样数。 |
| size_t numChannels | 音频或信号通道数。 |
| size_t numSections | 每通道级联的 biquad 节数。 |
| FAST_BiquadStateD* states | 滤波器状态数组。 |
 
 
  

##### 结构体成员变量说明

  

##### activeFilters

```text
uint8_t* FAST_BiquadmD::activeFilters
```
 
**描述**
 
活跃滤波器掩码数组（大小为[numSections](#numsections)），非零表示该节滤波器处于激活状态。
 
  

##### channelGains

```text
double* FAST_BiquadmD::channelGains
```
 
**描述**
 
每通道线性增益因子数组（大小为[numChannels](#numchannels)），用于对每个通道的输出进行增益调整。
 
  

##### coefficients

```text
FAST_BiquadCoefficientsD* FAST_BiquadmD::coefficients
```
 
**描述**
 
滤波器系数数组（大小为[numChannels](#numchannels) * [numSections](#numsections)），存储所有通道的所有滤波器节系数。
 
  

##### isInitialized

```text
uint8_t FAST_BiquadmD::isInitialized
```
 
**描述**
 
初始化标志，值为1表示结构体已正确初始化，值为0表示未初始化。
 
  

##### maxFrames

```text
size_t FAST_BiquadmD::maxFrames
```
 
**描述**
 
单次处理的最大采样数（每通道），处理长度不能超过此值。
 
  

##### numChannels

```text
size_t FAST_BiquadmD::numChannels
```
 
**描述**
 
音频或信号通道数，必须大于0。
 
  

##### numSections

```text
size_t FAST_BiquadmD::numSections
```
 
**描述**
 
每通道级联的biquad节数，必须大于0。
 
  

##### states

```text
FAST_BiquadStateD* FAST_BiquadmD::states
```
 
**描述**
 
滤波器状态数组（大小为[numChannels](#numchannels) * [numSections](#numsections)），存储所有通道的所有滤波器节状态变量。
