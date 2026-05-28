# fast_dsp_common.h

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

数字信号处理（DSP）通用数据结构和工具函数定义，包括向量运算、复数处理以及二阶IIR滤波器管理。支持单精度（float）和双精度（double）算术运算。
 
**引用文件：** <FASTKit/fast_dsp_common.h>
 
**库：** libfast_dsp.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 结构体

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct FAST_SplitComplex | 定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct FAST_SplitComplexD | 定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct FAST_BiquadCoefficients | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct FAST_BiquadCoefficientsD | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct FAST_BiquadState | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct FAST_BiquadStateD | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct FAST_Biquadm | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct FAST_BiquadmD | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |
 
 
  

##### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef struct FAST_SplitComplex FAST_SplitComplex | 单精度浮点复数信号结构体。 |
| typedef struct FAST_SplitComplexD FAST_SplitComplexD | 双精度浮点复数信号结构体。 |
| typedef struct FAST_BiquadCoefficients FAST_BiquadCoefficients | 单精度二阶IIR滤波器系数。 |
| typedef struct FAST_BiquadCoefficientsD FAST_BiquadCoefficientsD | 双精度二阶IIR滤波器系数。 |
| typedef struct FAST_BiquadState FAST_BiquadState | 单精度二阶IIR滤波器状态。 |
| typedef struct FAST_BiquadStateD FAST_BiquadStateD | 双精度二阶IIR滤波器状态。 |
| typedef struct FAST_Biquadm FAST_Biquadm | 单精度多通道多节IIR滤波器组。 |
| typedef struct FAST_BiquadmD FAST_BiquadmD | 双精度多通道多节IIR滤波器组。 |
 
 
  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| float HMS_FAST_DSP_Maxmgv (const float* input, size_t stride, size_t length) | 计算步长实值向量中的最大幅值（单精度）。 |
| double HMS_FAST_DSP_MaxmgvD (const double* input, size_t stride, size_t length) | 计算步长实值向量中的最大幅值（双精度）。 |
| void HMS_FAST_DSP_Maxvi (const float* input, size_t stride, size_t length, float* value, size_t* index) | 查找步长实值向量中的最大值及其索引（单精度）。 |
| void HMS_FAST_DSP_MaxviD (const double* input, size_t stride, size_t length, double* value, size_t* index) | 查找步长实值向量中的最大值及其索引（双精度）。 |
| float HMS_FAST_DSP_Meamgv (const float* input, size_t stride, size_t length) | 计算步长实值向量绝对值的均值（单精度）。 |
| double HMS_FAST_DSP_MeamgvD (const double* input, size_t stride, size_t length) | 计算步长实值向量绝对值的均值（双精度）。 |
| float HMS_FAST_DSP_Sve (const float* input, size_t stride, size_t length) | 计算步长实值向量的和（单精度）。 |
| double HMS_FAST_DSP_SveD (const double* input, size_t stride, size_t length) | 计算步长实值向量的和（双精度）。 |
| float HMS_FAST_DSP_Svemg (const float* input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double HMS_FAST_DSP_SvemgD (const double* input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float HMS_FAST_DSP_Dotpr (const float* inputA, size_t strideA, const float* inputB, size_t strideB, size_t length) | 计算两个步长实值向量的点积（单精度）。 |
| double HMS_FAST_DSP_DotprD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, size_t length) | 计算两个步长实值向量的点积（双精度）。 |
| void HMS_FAST_DSP_Vsbsm (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float scalar, float* outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（单精度）。 |
| void HMS_FAST_DSP_VsbsmD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double scalar, double* outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（双精度）。 |
| void HMS_FAST_DSP_Ctoz (const float* input, size_t strideInput, FAST_SplitComplex* output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void HMS_FAST_DSP_CtozD (const double* input, size_t strideInput, FAST_SplitComplexD* output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void HMS_FAST_DSP_Ztoc (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void HMS_FAST_DSP_ZtocD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFilters (FAST_Biquadm* filter, const uint8_t* activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFiltersD (FAST_BiquadmD* filter, const uint8_t* activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingle (FAST_Biquadm* filter, const float* coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDouble (FAST_Biquadm* filter, const double* coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingleD (FAST_BiquadmD* filter, const float* coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDoubleD (FAST_BiquadmD* filter, const double* coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_Create (size_t numChannels, size_t numSections, size_t maxFrames, FAST_Biquadm** filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_CreateD (size_t numChannels, size_t numSections, size_t maxFrames, FAST_BiquadmD** filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void HMS_FAST_Biquadm_Destroy (FAST_Biquadm* filter) | 销毁二阶滤波器实例（单精度）。 |
| void HMS_FAST_Biquadm_DestroyD (FAST_BiquadmD* filter) | 销毁二阶滤波器实例（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm (FAST_Biquadm* filter, const float** input, const size_t strideInput, float** output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| FAST_ErrorCode HMS_FAST_BiquadmD (FAST_BiquadmD* filter, const double** input, const size_t strideInput, double** output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
