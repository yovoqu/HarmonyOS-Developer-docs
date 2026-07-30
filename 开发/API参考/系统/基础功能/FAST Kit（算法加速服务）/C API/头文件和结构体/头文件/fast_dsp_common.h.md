# fast_dsp_common.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

数字信号处理（DSP）通用数据结构和工具函数定义，包括向量运算、复数处理以及二阶IIR滤波器管理。支持单精度（float）和双精度（double）算术运算。
 
**引用文件：** <FASTKit/fast_dsp_common.h>
 
**库：** libfast_dsp.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 6.1.1(24)
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 结构体

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
 
 
  

#### 类型定义

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
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| HMS_FAST_HannWindowType { HMS_FAST_HANN_DENORMALIZE_FULL = 0x00, HMS_FAST_HANN_NORMALIZE_FULL = 0x01, HMS_FAST_HANN_DENORMALIZE_HALF = 0x10, HMS_FAST_HANN_NORMALIZE_HALF = 0x11 } | 汉宁窗类型枚举。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| float HMS_FAST_DSP_Maxmgv (const float* input, size_t stride, size_t length) | 计算步长实数向量中的最大幅值（单精度）。 |
| double HMS_FAST_DSP_MaxmgvD (const double* input, size_t stride, size_t length) | 计算步长实数向量中的最大幅值（双精度）。 |
| void HMS_FAST_DSP_Maxvi (const float* input, size_t stride, size_t length, float* value, size_t* index) | 查找步长实数向量中的最大值及其索引（单精度）。 |
| void HMS_FAST_DSP_MaxviD (const double* input, size_t stride, size_t length, double* value, size_t* index) | 查找步长实数向量中的最大值及其索引（双精度）。 |
| float HMS_FAST_DSP_Meamgv (const float* input, size_t stride, size_t length) | 计算步长实数向量绝对值的均值（单精度）。 |
| double HMS_FAST_DSP_MeamgvD (const double* input, size_t stride, size_t length) | 计算步长实数向量绝对值的均值（双精度）。 |
| float HMS_FAST_DSP_Sve (const float* input, size_t stride, size_t length) | 计算步长实数向量的和（单精度）。 |
| double HMS_FAST_DSP_SveD (const double* input, size_t stride, size_t length) | 计算步长实数向量的和（双精度）。 |
| float HMS_FAST_DSP_Svemg (const float* input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double HMS_FAST_DSP_SvemgD (const double* input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float HMS_FAST_DSP_Dotpr (const float* inputA, size_t strideA, const float* inputB, size_t strideB, size_t length) | 计算两个步长实数向量的点积（单精度）。 |
| double HMS_FAST_DSP_DotprD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, size_t length) | 计算两个步长实数向量的点积（双精度）。 |
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
| void HMS_FAST_DSP_Zvabs (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 计算复数向量的幅值（单精度）。 |
| void HMS_FAST_DSP_ZvabsD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 计算复数向量的幅值（双精度）。 |
| void HMS_FAST_DSP_Zvmags (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 计算复数向量的幅值平方（单精度）。 |
| void HMS_FAST_DSP_ZvmagsD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 计算复数向量的幅值平方（双精度）。 |
| void HMS_FAST_DSP_Zvphas (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 计算复数向量的相位角（单精度）。 |
| void HMS_FAST_DSP_ZvphasD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 计算复数向量的相位角（双精度）。 |
| void HMS_FAST_DSP_Vsmul (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length) | 将向量的每个元素乘以标量（单精度）。 |
| void HMS_FAST_DSP_VsmulD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length) | 将向量的每个元素乘以标量（双精度）。 |
| void HMS_FAST_DSP_Vsdiv (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length) | 将向量的每个元素除以标量（单精度）。 |
| void HMS_FAST_DSP_VsdivD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length) | 将向量的每个元素除以标量（双精度）。 |
| void HMS_FAST_DSP_Svdiv (const float scalar, const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 将标量除以向量的每个元素（单精度）。 |
| void HMS_FAST_DSP_SvdivD (const double scalar, const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 将标量除以向量的每个元素（双精度）。 |
| void HMS_FAST_DSP_Vsadd (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length) | 将标量加到向量的每个元素（单精度）。 |
| void HMS_FAST_DSP_VsaddD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length) | 将标量加到向量的每个元素（双精度）。 |
| void HMS_FAST_DSP_Vadd (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length) | 执行向量逐元素加法（单精度）。 |
| void HMS_FAST_DSP_VaddD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length) | 执行向量逐元素加法（双精度）。 |
| void HMS_FAST_DSP_Vsub (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length) | 执行向量逐元素减法（单精度）。 |
| void HMS_FAST_DSP_VsubD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length) | 执行向量逐元素减法（双精度）。 |
| void HMS_FAST_DSP_Vmul (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length) | 执行向量逐元素乘法（单精度）。 |
| void HMS_FAST_DSP_VmulD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length) | 执行向量逐元素乘法（双精度）。 |
| void HMS_FAST_DSP_Vdiv (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length) | 执行向量逐元素除法（单精度）。 |
| void HMS_FAST_DSP_VdivD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length) | 执行向量逐元素除法（双精度）。 |
| void HMS_FAST_DSP_Vdist (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length) | 计算两个向量对应元素的欧几里得范数（单精度）。 |
| void HMS_FAST_DSP_VdistD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length) | 计算两个向量对应元素的欧几里得范数（双精度）。 |
| float HMS_FAST_DSP_Svesq (const float* input, size_t stride, size_t length) | 计算向量元素的平方和（单精度）。 |
| double HMS_FAST_DSP_SvesqD (const double* input, size_t stride, size_t length) | 计算向量元素的平方和（双精度）。 |
| void HMS_FAST_DSP_Minvi (const float* input, size_t stride, size_t length, float* value, size_t* index) | 查找步长实数向量中的最小值及其索引（单精度）。 |
| void HMS_FAST_DSP_MinviD (const double* input, size_t stride, size_t length, double* value, size_t* index) | 查找步长实数向量中的最小值及其索引（双精度）。 |
| void HMS_FAST_DSP_Vsq (const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 计算向量每个元素的平方（单精度）。 |
| void HMS_FAST_DSP_VsqD (const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 计算向量每个元素的平方（双精度）。 |
| void HMS_FAST_DSP_Vabs (const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 计算向量每个元素的绝对值（单精度）。 |
| void HMS_FAST_DSP_VabsD (const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 计算向量每个元素的绝对值（双精度）。 |
| void HMS_FAST_DSP_Vthr (const float* input, size_t strideInput, const float threshold, float* output, size_t strideOutput, size_t length) | 对向量应用阈值（单精度）。 |
| void HMS_FAST_DSP_VthrD (const double* input, size_t strideInput, const double threshold, double* output, size_t strideOutput, size_t length) | 对向量应用阈值（双精度）。 |
| void HMS_FAST_DSP_Vrvrs (float* vector, size_t stride, size_t length) | 原地反转向量中元素的顺序（单精度）。 |
| void HMS_FAST_DSP_VrvrsD (double* vector, size_t stride, size_t length) | 原地反转向量中元素的顺序（双精度）。 |
| void HMS_FAST_DSP_Vspdp (const float* input, size_t strideInput, double* output, size_t strideOutput, size_t length) | 将单精度向量转换为双精度向量。 |
| void HMS_FAST_DSP_Vdpsp (const double* input, size_t strideInput, float* output, size_t strideOutput, size_t length) | 将双精度向量转换为单精度向量。 |
| void HMS_FAST_DSP_Vfill (float* vector, size_t stride, size_t length, const float scalar) | 使用指定标量值填充向量（单精度）。 |
| void HMS_FAST_DSP_VfillD (double* vector, size_t stride, size_t length, const double scalar) | 使用指定标量值填充向量（双精度）。 |
| void HMS_FAST_DSP_Vclr (float* vector, size_t stride, size_t length) | 将向量所有元素清零（单精度）。 |
| void HMS_FAST_DSP_VclrD (double* vector, size_t stride, size_t length) | 将向量所有元素清零（双精度）。 |
| void HMS_FAST_DSP_Conv (const float* input, size_t strideInput, const float* filter, size_t strideFilter, float* output, size_t strideOutput, size_t outputLength, size_t filterLength) | 执行两个向量的卷积运算（单精度）。 |
| void HMS_FAST_DSP_ConvD (const double* input, size_t strideInput, const double* filter, size_t strideFilter, double* output, size_t strideOutput, size_t outputLength, size_t filterLength) | 执行两个向量的卷积运算（双精度）。 |
| void HMS_FAST_DSP_HannWindow (float* output, size_t length, HMS_FAST_HannWindowType type) | 生成汉宁窗序列（单精度）。 |
| void HMS_FAST_DSP_HannWindowD (double* output, size_t length, HMS_FAST_HannWindowType type) | 生成汉宁窗序列（双精度）。 |
| void HMS_FAST_DSP_Mmul (const float* matrixA, size_t strideA, const float* matrixB, size_t strideB, float* matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP) | 执行矩阵乘法：C = A * B（单精度）。 |
| void HMS_FAST_DSP_MmulD (const double* matrixA, size_t strideA, const double* matrixB, size_t strideB, double* matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP) | 执行矩阵乘法：C = A * B（双精度）。 |
| void HMS_FAST_DSP_Vvpow (const float* inputA, const float* inputB, float* outputC, size_t length) | 执行向量逐元素幂运算：C[i] = pow(A[i], B[i])（单精度）。 |
| void HMS_FAST_DSP_VvpowD (const double* inputA, const double* inputB, double* outputC, size_t length) | 执行向量逐元素幂运算：C[i] = pow(A[i], B[i])（双精度）。 |
| void HMS_FAST_DSP_Vsort (float* vector, size_t length, int order) | 对向量进行原地排序（单精度）。 |
| void HMS_FAST_DSP_VsortD (double* vector, size_t length, int order) | 对向量进行原地排序（双精度）。 |
