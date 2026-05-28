# FAST_SplitComplexD

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplexd
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| double* real | 实部数组指针。 |
| double* imag | 虚部数组指针。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

##### imag

**支持设备：** Phone | PC/2in1 | Tablet

```text
double* FAST_SplitComplexD::imag
```
 
**描述**
 
指向虚部数组的指针。数组长度应与实部数组相同，存储复数信号的虚部数据。
 
  

##### real

**支持设备：** Phone | PC/2in1 | Tablet

```text
double* FAST_SplitComplexD::real
```
 
**描述**
 
指向实部数组的指针。数组长度应与虚部数组相同，存储复数信号的实部数据。
