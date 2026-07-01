# fast_dsp_transform.h

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-transform-8h
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

提供高性能数字信号处理（DSP）变换函数，包括FFT（快速傅里叶变换）、IFFT（逆快速傅里叶变换）等。
 
**引用文件：** <FASTKit/fast_dsp_transform.h>
 
**库：** libfast_dsp.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef struct FAST_FFTConfig FAST_FFTConfig | 快速傅里叶变换的不透明配置。 |
 
 
  

#### 常量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| const uint32_t FAST_MAX_FFT_LOG2N = 16 | FFT支持的最大点数对应的以2为底的对数值。值为16，即最大点数为65536。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_FFT_CreateConfig (FAST_FFTConfig** config, const uint32_t log2n) | 创建单精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=FAST_MAX_FFT_LOG2N，即1到16）。 |
| FAST_ErrorCode HMS_FAST_FFT_CreateConfigD (FAST_FFTConfig** config, const uint32_t log2n) | 创建双精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=FAST_MAX_FFT_LOG2N，即1到16）。 |
| void HMS_FAST_FFT_DestroyConfig (FAST_FFTConfig* config) | 销毁FFT配置对象并释放资源。 |
| FAST_ErrorCode HMS_FAST_FFT_ForwardTransform (FAST_FFTConfig* config, const uint32_t length, const float input[], float outputRe[], float outputIm[]) | 计算单精度实数时域信号的DFT。 |
| FAST_ErrorCode HMS_FAST_FFT_ForwardTransformD (FAST_FFTConfig* config, const uint32_t length, const double input[], double outputRe[], double outputIm[]) | 计算双精度实数时域信号的DFT。 |
| FAST_ErrorCode HMS_FAST_FFT_InverseTransform (FAST_FFTConfig* config, const uint32_t length, const float inputRe[], const float inputIm[], float output[]) | 计算单精度复数频域序列的逆DFT。 |
| FAST_ErrorCode HMS_FAST_FFT_InverseTransformD (FAST_FFTConfig* config, const uint32_t length, const double inputRe[], const double inputIm[], double output[]) | 计算双精度复数频域序列的逆DFT。 |
