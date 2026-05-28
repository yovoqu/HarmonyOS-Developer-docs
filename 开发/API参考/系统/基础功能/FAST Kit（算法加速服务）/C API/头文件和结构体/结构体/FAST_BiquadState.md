# FAST_BiquadState

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

定义单精度二阶IIR滤波器节的状态变量。
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| float d1 | 第一个延迟单元（y[n-1]）。 |
| float d2 | 第二个延迟单元（y[n-2]）。 |
 
 
  

##### 结构体成员变量说明

  

##### d1

```text
float FAST_BiquadState::d1
```
 
**描述**
 
第一个延迟单元，存储上一时刻的输出值y[n-1]。
 
  

##### d2

```text
float FAST_BiquadState::d2
```
 
**描述**
 
第二个延迟单元，存储上上时刻的输出值y[n-2]。
