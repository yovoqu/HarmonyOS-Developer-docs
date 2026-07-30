# FAST

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。
 
**起始版本：** 6.0.2(22)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。
 
  

#### 文件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| fast_ads_segment_map.h | 线段表相关数据结构及函数定义。 |
| fast_ads_concurrent_hashmap.h | 并发哈希表相关数据结构及函数定义。 |
| fast_common_def.h | FAST Kit错误码等类型的公共定义。 |
| fast_dsp_common.h | 数字信号处理（DSP）通用数据结构和工具函数定义。 |
| fast_dsp_transform.h | 数字信号处理（DSP）变换函数定义，包括FFT、IFFT等。 |
| fast_solver_rect_partition.h | 矩形划分求解器相关数据结构及函数定义。 |
| fast_solver_polynomial.h | 多项式零点求解器相关数据结构及函数定义。 |
| fast_collections_hashmap.h | 适用于单线程场景的哈希表相关数据结构及函数定义。 |
| fast_utils_algorithm.h | 通用算法实现，目前提供排序相关的数据结构和函数定义。 |
| scheduling_optimization.h | 系统性能优化相关数据结构及函数定义。 |
 
 
  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| struct FAST_Rect | 定义矩形的数据结构。 |
| struct FAST_Poly | 定义稀疏格式多项式的数据结构。 |
| struct FAST_SplitComplex | 定义单精度浮点复数信号的数据结构（分离格式）。 |
| struct FAST_SplitComplexD | 定义双精度浮点复数信号的数据结构（分离格式）。 |
| struct FAST_BiquadCoefficients | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct FAST_BiquadCoefficientsD | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct FAST_BiquadState | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct FAST_BiquadStateD | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct FAST_Biquadm | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct FAST_BiquadmD | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct HMS_FAST_SortData | 定义待排序的连续数据块的数据结构。 |
 
 
  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType | 线段表支持的查询操作类型。 |
| typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType | 线段表支持的更新操作类型。 |
| typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void * FAST_SegmentMapHandle | 线段表的句柄。 |
| typedef enum FAST_ErrorCode FAST_ErrorCode | FAST Kit的错误码。 |
| typedef enum HMS_FAST_HannWindowType HMS_FAST_HannWindowType | 汉宁窗类型枚举。 |
| typedef struct FAST_Rect FAST_Rect | 定义矩形的数据结构。 |
| typedef struct FAST_Poly FAST_Poly | 定义稀疏格式多项式的数据结构。 |
| typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig | 矩形划分求解器的不透明配置。 |
| typedef struct FAST_SplitComplex FAST_SplitComplex | 单精度浮点复数信号结构体。 |
| typedef struct FAST_SplitComplexD FAST_SplitComplexD | 双精度浮点复数信号结构体。 |
| typedef struct FAST_BiquadCoefficients FAST_BiquadCoefficients | 单精度二阶IIR滤波器系数。 |
| typedef struct FAST_BiquadCoefficientsD FAST_BiquadCoefficientsD | 双精度二阶IIR滤波器系数。 |
| typedef struct FAST_BiquadState FAST_BiquadState | 单精度二阶IIR滤波器状态。 |
| typedef struct FAST_BiquadStateD FAST_BiquadStateD | 双精度二阶IIR滤波器状态。 |
| typedef struct FAST_Biquadm FAST_Biquadm | 单精度多通道多节IIR滤波器组。 |
| typedef struct FAST_BiquadmD FAST_BiquadmD | 双精度多通道多节IIR滤波器组。 |
| typedef struct FAST_FFTConfig FAST_FFTConfig | 快速傅里叶变换的不透明配置。 |
| typedef void* FAST_HashmapHandle | 哈希表的句柄。 |
| typedef void* FAST_HashmapKeyPtr | 哈希表键指针。 |
| typedef void* FAST_HashmapValuePtr | 哈希表的值指针。 |
| typedef uint64_t(* HMS_FAST_Hashmap_HashFunc) (const FAST_HashmapKeyPtr key) | 自定义的哈希值计算函数。 |
| typedef int32_t(* HMS_FAST_Hashmap_KeyEqualFunc) (const FAST_HashmapKeyPtr leftKey, const FAST_HashmapKeyPtr rightKey) | 自定义的键比较函数。 |
| typedef int32_t(* HMS_FAST_Hashmap_HookFunc) (const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr value, void* context) | 自定义的通用回调函数形式。 |
| typedef void* FAST_ConcurrentHashmapHandle | 并发哈希表的句柄。 |
| typedef void* FAST_ConcurrentHashmapKeyPtr | 并发哈希表键指针。 |
| typedef void* FAST_ConcurrentHashmapValuePtr | 并发哈希表的值指针。 |
| typedef uint64_t (*HMS_FAST_ConcurrentHashmap_HashFunc) (const FAST_ConcurrentHashmapKeyPtr key) | 开发者自定义的哈希值计算函数。 |
| typedef int32_t (*HMS_FAST_ConcurrentHashmap_KeyEqualFunc) (const FAST_ConcurrentHashmapKeyPtr leftKey, const FAST_ConcurrentHashmapKeyPtr rightKey) | 开发者自定义的键比较函数。 |
| typedef int32_t (*HMS_FAST_ConcurrentHashmap_HookFunc) (const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr value, void* context) | 开发者自定义的通用回调函数形式。 |
| typedef struct HMS_FAST_SortData HMS_FAST_SortData | 定义待排序的连续数据块的数据结构。 |
| typedef void* HMS_FAST_SortElementPtr | 表示通用容器中单个元素的opaque pointer类型。 |
| typedef const void* HMS_FAST_SortElementConstPtr | 表示通用容器中单个元素的const opaque pointer类型。 |
| typedef int32_t(* HMS_FAST_Sort_CompFunc) (HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second) | 用户自定义比较函数的回调函数指针类型。 |
| typedef struct HMS_FAST_PerfHintConfigBuilder HMS_FAST_PerfHintConfigBuilder | 系统性能优化配置参数构建器。 |
| typedef struct HMS_FAST_PerfHintConfig HMS_FAST_PerfHintConfig | 系统性能优化配置参数。 |
 
 
  

#### 常量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const uint32_t FAST_MAX_FFT_LOG2N = 16 | FFT支持的最大点数对应的以2为底的对数值。值为16，即最大点数为65536。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| FAST_SegmentMapQueryType { FAST_SEGMENTMAP_QUERY_TYPE_SUM = 0, FAST_SEGMENTMAP_QUERY_TYPE_MIN = 1, FAST_SEGMENTMAP_QUERY_TYPE_MAX = 2 } | 线段表支持的查询操作类型。 |
| FAST_SegmentMapUpdateType { FAST_SEGMENTMAP_UPDATE_TYPE_SET = 0, FAST_SEGMENTMAP_UPDATE_TYPE_ADD = 1, FAST_SEGMENTMAP_UPDATE_TYPE_SUB = 2 } | 线段表支持的更新操作类型。 |
| FAST_ErrorCode { FAST_ERROR_CODE_SUCCESS = 1023100000, FAST_ERROR_CODE_FAIL = 1023100001, FAST_ERROR_CODE_ILLEGAL_INPUT = 1023100002, FAST_ERROR_CODE_INVALID_PTR = 1023100003, FAST_ERROR_CODE_KEY_EXISTS = 1023110000, FAST_ERROR_CODE_KEY_NOT_EXISTS = 1023110001, FAST_ERROR_CODE_OOM = 1023199001 } | FAST Kit的错误码。 |
| HMS_FAST_HannWindowType { HMS_FAST_HANN_DENORMALIZE_FULL = 0x00, HMS_FAST_HANN_NORMALIZE_FULL = 0x01, HMS_FAST_HANN_DENORMALIZE_HALF = 0x10, HMS_FAST_HANN_NORMALIZE_HALF = 0x11 } | 汉宁窗类型枚举。 |
| HMS_FAST_SchedulingOptimization_SceneType { HMS_FAST_APP_LAUNCH = 1, HMS_FAST_PAGE_TRANSITION = 2, HMS_FAST_PAGE_LOAD = 3, HMS_FAST_NETWORK_FILE_PROCESSING = 4, HMS_FAST_LOCAL_FILE_PROCESSING = 5, HMS_FAST_PAGE_DRAWING = 6, HMS_FAST_ANIMATION = 7, HMS_FAST_MEDIA_PLAYBACK = 8, HMS_FAST_MEDIA_ENCODING_AND_DECODING = 9 } | 需要系统性能优化的场景类型。 |
| HMS_FAST_SchedulingOptimization_SceneState { HMS_FAST_END = 0, HMS_FAST_BEGIN = 1 } | 需要系统性能优化的场景状态。 |
| HMS_FAST_SchedulingOptimization_DurationType { HMS_FAST_SHORT = 1, HMS_FAST_MEDIUM = 2, HMS_FAST_LONG = 3 } | 需要系统性能优化的持续时间选项。 |
| HMS_FAST_SchedulingOptimization_ErrorCode { HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS = 0, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_HIGH_SYSTEM_LOAD = 1027700001, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_POWER_SAVING_MODE = 1027700002, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_LOW_POWER_MODE = 1027700003, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NON_FRONTEND = 1027700004, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INTERVAL = 1027700005, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_EXECUTE_ERROR = 1027700006, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM = 1027700007, HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NO_MEMORY = 1027700008 } | 系统性能优化的错误码。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig **config) | 创建线段表不透明配置实例。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig *config) | 销毁线段表的不透明配置实例并释放内存。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig *config, FAST_SegmentMapQueryType type) | 设置线段表不透明配置中的查询类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig *config, FAST_SegmentMapUpdateType type) | 设置线段表不透明配置中的更新类型。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle *handle, size_t size, const int32_t *array, FAST_SegmentMapConfig *config) | 创建线段表。 |
| FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle) | 销毁线段表实例。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value) | 更新线段表的区间。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t *result) | 查询线段表的区间。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig **config) | 创建矩形划分求解器的不透明配置。 |
| FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig *config) | 销毁矩形划分求解器的不透明配置。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig *config, const char *name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig *config, size_t size, const FAST_Rect *origin, FAST_Rect *result, size_t *resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。 说明： 1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST_ERROR_CODE_ILLEGAL_INPUT。 2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRoots (const FAST_Poly *poly, const size_t maxRootCount, double *root, size_t *rootCount) | 计算多项式的给定实数根的实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeSingle (const FAST_Poly *poly, double *root) | 计算多项式的主导(绝对值最大)实根。 |
| FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRootIntervals (const FAST_Poly *poly, const size_t maxRootCount, double *leftBoundary, double *rightBoundary, size_t *rootCount) | 计算多项式给定个数实根的隔离区间，输出每个实根的左右边界。 |
| float HMS_FAST_DSP_Maxmgv (const float *input, size_t stride, size_t length) | 计算步长实数向量中的最大幅值（单精度）。 |
| double HMS_FAST_DSP_MaxmgvD (const double *input, size_t stride, size_t length) | 计算步长实数向量中的最大幅值（双精度）。 |
| void HMS_FAST_DSP_Maxvi (const float *input, size_t stride, size_t length, float *value, size_t *index) | 查找步长实数向量中的最大值及其索引（单精度）。 |
| void HMS_FAST_DSP_MaxviD (const double *input, size_t stride, size_t length, double *value, size_t *index) | 查找步长实数向量中的最大值及其索引（双精度）。 |
| float HMS_FAST_DSP_Sve (const float *input, size_t stride, size_t length) | 计算步长实数向量的和（单精度）。 |
| double HMS_FAST_DSP_SveD (const double *input, size_t stride, size_t length) | 计算步长实数向量的和（双精度）。 |
| float HMS_FAST_DSP_Svemg (const float *input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double HMS_FAST_DSP_SvemgD (const double *input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float HMS_FAST_DSP_Meamgv (const float *input, size_t stride, size_t length) | 计算步长实数向量绝对值的均值（单精度）。 |
| double HMS_FAST_DSP_MeamgvD (const double *input, size_t stride, size_t length) | 计算步长实数向量绝对值的均值（双精度）。 |
| float HMS_FAST_DSP_Dotpr (const float *inputA, size_t strideA, const float *inputB, size_t strideB, size_t length) | 计算两个步长实数向量的点积（单精度）。 |
| double HMS_FAST_DSP_DotprD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, size_t length) | 计算两个步长实数向量的点积（双精度）。 |
| void HMS_FAST_DSP_Vsbsm (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float scalar, float *outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（单精度）。 |
| void HMS_FAST_DSP_VsbsmD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double scalar, double *outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（双精度）。 |
| void HMS_FAST_DSP_Ctoz (const float *input, size_t strideInput, FAST_SplitComplex *output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void HMS_FAST_DSP_CtozD (const double *input, size_t strideInput, FAST_SplitComplexD *output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void HMS_FAST_DSP_Ztoc (const FAST_SplitComplex *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void HMS_FAST_DSP_ZtocD (const FAST_SplitComplexD *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| void HMS_FAST_DSP_Zvabs (const FAST_SplitComplex *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 计算复数向量的幅值（单精度）。 |
| void HMS_FAST_DSP_ZvabsD (const FAST_SplitComplexD *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 计算复数向量的幅值（双精度）。 |
| void HMS_FAST_DSP_Zvmags (const FAST_SplitComplex *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 计算复数向量的幅值平方（单精度）。 |
| void HMS_FAST_DSP_ZvmagsD (const FAST_SplitComplexD *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 计算复数向量的幅值平方（双精度）。 |
| void HMS_FAST_DSP_Zvphas (const FAST_SplitComplex *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 计算复数向量的相位角（单精度）。 |
| void HMS_FAST_DSP_ZvphasD (const FAST_SplitComplexD *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 计算复数向量的相位角（双精度）。 |
| void HMS_FAST_DSP_Vsmul (const float *input, size_t strideInput, const float scalar, float *output, size_t strideOutput, size_t length) | 将向量的每个元素乘以标量（单精度）。 |
| void HMS_FAST_DSP_VsmulD (const double *input, size_t strideInput, const double scalar, double *output, size_t strideOutput, size_t length) | 将向量的每个元素乘以标量（双精度）。 |
| void HMS_FAST_DSP_Vsdiv (const float *input, size_t strideInput, const float scalar, float *output, size_t strideOutput, size_t length) | 将向量的每个元素除以标量（单精度）。 |
| void HMS_FAST_DSP_VsdivD (const double *input, size_t strideInput, const double scalar, double *output, size_t strideOutput, size_t length) | 将向量的每个元素除以标量（双精度）。 |
| void HMS_FAST_DSP_Svdiv (const float scalar, const float *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 将标量除以向量的每个元素（单精度）。 |
| void HMS_FAST_DSP_SvdivD (const double scalar, const double *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 将标量除以向量的每个元素（双精度）。 |
| void HMS_FAST_DSP_Vsadd (const float *input, size_t strideInput, const float scalar, float *output, size_t strideOutput, size_t length) | 将标量加到向量的每个元素（单精度）。 |
| void HMS_FAST_DSP_VsaddD (const double *input, size_t strideInput, const double scalar, double *output, size_t strideOutput, size_t length) | 将标量加到向量的每个元素（双精度）。 |
| void HMS_FAST_DSP_Vadd (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float *outputC, size_t strideC, size_t length) | 执行向量逐元素加法（单精度）。 |
| void HMS_FAST_DSP_VaddD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double *outputC, size_t strideC, size_t length) | 执行向量逐元素加法（双精度）。 |
| void HMS_FAST_DSP_Vsub (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float *outputC, size_t strideC, size_t length) | 执行向量逐元素减法（单精度）。 |
| void HMS_FAST_DSP_VsubD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double *outputC, size_t strideC, size_t length) | 执行向量逐元素减法（双精度）。 |
| void HMS_FAST_DSP_Vmul (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float *outputC, size_t strideC, size_t length) | 执行向量逐元素乘法（单精度）。 |
| void HMS_FAST_DSP_VmulD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double *outputC, size_t strideC, size_t length) | 执行向量逐元素乘法（双精度）。 |
| void HMS_FAST_DSP_Vdiv (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float *outputC, size_t strideC, size_t length) | 执行向量逐元素除法（单精度）。 |
| void HMS_FAST_DSP_VdivD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double *outputC, size_t strideC, size_t length) | 执行向量逐元素除法（双精度）。 |
| void HMS_FAST_DSP_Vdist (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float *outputC, size_t strideC, size_t length) | 计算两个向量对应元素的欧几里得范数（单精度）。 |
| void HMS_FAST_DSP_VdistD (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double *outputC, size_t strideC, size_t length) | 计算两个向量对应元素的欧几里得范数（双精度）。 |
| float HMS_FAST_DSP_Svesq (const float *input, size_t stride, size_t length) | 计算向量元素的平方和（单精度）。 |
| double HMS_FAST_DSP_SvesqD (const double *input, size_t stride, size_t length) | 计算向量元素的平方和（双精度）。 |
| void HMS_FAST_DSP_Minvi (const float *input, size_t stride, size_t length, float *value, size_t *index) | 查找步长实数向量中的最小值及其索引（单精度）。 |
| void HMS_FAST_DSP_MinviD (const double *input, size_t stride, size_t length, double *value, size_t *index) | 查找步长实数向量中的最小值及其索引（双精度）。 |
| void HMS_FAST_DSP_Vsq (const float *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 计算向量每个元素的平方（单精度）。 |
| void HMS_FAST_DSP_VsqD (const double *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 计算向量每个元素的平方（双精度）。 |
| void HMS_FAST_DSP_Vabs (const float *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 计算向量每个元素的绝对值（单精度）。 |
| void HMS_FAST_DSP_VabsD (const double *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 计算向量每个元素的绝对值（双精度）。 |
| void HMS_FAST_DSP_Vthr (const float *input, size_t strideInput, const float threshold, float *output, size_t strideOutput, size_t length) | 对向量应用阈值（单精度）。 |
| void HMS_FAST_DSP_VthrD (const double *input, size_t strideInput, const double threshold, double *output, size_t strideOutput, size_t length) | 对向量应用阈值（双精度）。 |
| void HMS_FAST_DSP_Vrvrs (float *vector, size_t stride, size_t length) | 原地反转向量中元素的顺序（单精度）。 |
| void HMS_FAST_DSP_VrvrsD (double *vector, size_t stride, size_t length) | 原地反转向量中元素的顺序（双精度）。 |
| void HMS_FAST_DSP_Vspdp (const float *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 将单精度向量转换为双精度向量。 |
| void HMS_FAST_DSP_Vdpsp (const double *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 将双精度向量转换为单精度向量。 |
| void HMS_FAST_DSP_Vfill (float *vector, size_t stride, size_t length, const float scalar) | 使用指定标量值填充向量（单精度）。 |
| void HMS_FAST_DSP_VfillD (double *vector, size_t stride, size_t length, const double scalar) | 使用指定标量值填充向量（双精度）。 |
| void HMS_FAST_DSP_Vclr (float *vector, size_t stride, size_t length) | 将向量所有元素清零（单精度）。 |
| void HMS_FAST_DSP_VclrD (double *vector, size_t stride, size_t length) | 将向量所有元素清零（双精度）。 |
| void HMS_FAST_DSP_Conv (const float *input, size_t strideInput, const float *filter, size_t strideFilter, float *output, size_t strideOutput, size_t outputLength, size_t filterLength) | 执行两个向量的卷积运算（单精度）。 |
| void HMS_FAST_DSP_ConvD (const double *input, size_t strideInput, const double *filter, size_t strideFilter, double *output, size_t strideOutput, size_t outputLength, size_t filterLength) | 执行两个向量的卷积运算（双精度）。 |
| void HMS_FAST_DSP_HannWindow (float *output, size_t length, HMS_FAST_HannWindowType type) | 生成汉宁窗序列（单精度）。 |
| void HMS_FAST_DSP_HannWindowD (double *output, size_t length, HMS_FAST_HannWindowType type) | 生成汉宁窗序列（双精度）。 |
| void HMS_FAST_DSP_Mmul (const float *matrixA, size_t strideA, const float *matrixB, size_t strideB, float *matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP) | 执行矩阵乘法：C = A * B（单精度）。 |
| void HMS_FAST_DSP_MmulD (const double *matrixA, size_t strideA, const double *matrixB, size_t strideB, double *matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP) | 执行矩阵乘法：C = A * B（双精度）。 |
| void HMS_FAST_DSP_Vvpow (const float *inputA, const float *inputB, float *outputC, size_t length) | 执行向量逐元素幂运算（单精度）。 |
| void HMS_FAST_DSP_VvpowD (const double *inputA, const double *inputB, double *outputC, size_t length) | 执行向量逐元素幂运算（双精度）。 |
| void HMS_FAST_DSP_Vsort (float *vector, size_t length, int order) | 对向量进行原地排序（单精度）。 |
| void HMS_FAST_DSP_VsortD (double *vector, size_t length, int order) | 对向量进行原地排序（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFilters (FAST_Biquadm *filter, const uint8_t *activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFiltersD (FAST_BiquadmD *filter, const uint8_t *activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingle (FAST_Biquadm *filter, const float *coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDouble (FAST_Biquadm *filter, const double *coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingleD (FAST_BiquadmD *filter, const float *coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDoubleD (FAST_BiquadmD *filter, const double *coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_Create (size_t numChannels, size_t numSections, size_t maxFrames, FAST_Biquadm **filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm_CreateD (size_t numChannels, size_t numSections, size_t maxFrames, FAST_BiquadmD **filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void HMS_FAST_Biquadm_Destroy (FAST_Biquadm *filter) | 销毁二阶滤波器实例（单精度）。 |
| void HMS_FAST_Biquadm_DestroyD (FAST_BiquadmD *filter) | 销毁二阶滤波器实例（双精度）。 |
| FAST_ErrorCode HMS_FAST_Biquadm (FAST_Biquadm *filter, const float **input, const size_t strideInput, float **output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| FAST_ErrorCode HMS_FAST_BiquadmD (FAST_BiquadmD *filter, const double **input, const size_t strideInput, double **output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
| FAST_ErrorCode HMS_FAST_FFT_CreateConfig (FAST_FFTConfig** config, const uint32_t log2n) | 创建单精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=FAST_MAX_FFT_LOG2N，即1到16）。 |
| FAST_ErrorCode HMS_FAST_FFT_CreateConfigD (FAST_FFTConfig** config, const uint32_t log2n) | 创建双精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=FAST_MAX_FFT_LOG2N，即1到16）。 |
| void HMS_FAST_FFT_DestroyConfig (FAST_FFTConfig* config) | 销毁FFT配置对象并释放资源。 |
| FAST_ErrorCode HMS_FAST_FFT_ForwardTransform (FAST_FFTConfig* config, const uint32_t length, const float input[], float outputRe[], float outputIm[]) | 计算单精度实数信号的FFT。 |
| FAST_ErrorCode HMS_FAST_FFT_ForwardTransformD (FAST_FFTConfig* config, const uint32_t length, const double input[], double outputRe[], double outputIm[]) | 计算双精度实数信号的FFT。 |
| FAST_ErrorCode HMS_FAST_FFT_InverseTransform (FAST_FFTConfig* config, const uint32_t length, const float inputRe[], const float inputIm[], float output[]) | 计算单精度复数频域信号的逆FFT。 |
| FAST_ErrorCode HMS_FAST_FFT_InverseTransformD (FAST_FFTConfig* config, const uint32_t length, const double inputRe[], const double inputIm[], double output[]) | 计算双精度复数频域信号的逆FFT。 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create (FAST_ConcurrentHashmapHandle* handle, HMS_FAST_ConcurrentHashmap_HashFunc hasher, HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler, float maxLoadFac, size_t numShards) | 使用给定配置创建并发哈希表。 |
| void HMS_FAST_ConcurrentHashmap_Destroy (FAST_ConcurrentHashmapHandle handle) | 销毁指定并发哈希表。 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Insert (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value, FAST_ConcurrentHashmapValuePtr* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Find (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中。 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapKeyPtr* originKey, FAST_ConcurrentHashmapValuePtr* originValue) | 在给定哈希表中删除输入的键，并将键和值分别保存在originKey和originValue中。 |
| FAST_ErrorCode HMS_FAST_ConcurrentHashmap_TryInsert (FAST_ConcurrentHashmapHandle handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value) | 将给定的键值对插入并发哈希表中，如果键已经存在，则不执行任何操作。 |
| size_t HMS_FAST_ConcurrentHashmap_Size (FAST_ConcurrentHashmapHandle handle) | 返回给定哈希表当前的元素个数。 |
| void HMS_FAST_ConcurrentHashmap_Clear (FAST_ConcurrentHashmapHandle handle) | 清空给定哈希表中维护的所有元素。 |
| size_t HMS_FAST_ConcurrentHashmap_EraseIf (FAST_ConcurrentHashmapHandle handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc freeFunc, void* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。 |
| void HMS_FAST_ConcurrentHashmap_Traverse (FAST_ConcurrentHashmapHandle handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc workFunc, void* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Create (FAST_HashmapHandle* handle, HMS_FAST_Hashmap_HashFunc hasher, HMS_FAST_Hashmap_KeyEqualFunc equaler) | 创建哈希表实例。 |
| void HMS_FAST_Hashmap_Destroy (FAST_HashmapHandle handle) | 销毁哈希表实例。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Insert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value, FAST_HashmapValuePtr* originValue) | 将给定的键值对插入哈希表中，如果键已经存在，则使用value覆写原有的值，并将原有值的地址保存在originValue中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Find (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr* value) | 检索与给定键关联的值，并将对应的值保存在value中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_Erase (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapKeyPtr* originKey, FAST_HashmapValuePtr* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| FAST_ErrorCode HMS_FAST_Hashmap_TryInsert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value) | 将给定的键值对插入哈希表中，如果键已经存在、则不做操作。 |
| size_t HMS_FAST_Hashmap_Size (FAST_HashmapHandle handle) | 返回哈希表中的元素个数。 |
| void HMS_FAST_Hashmap_Clear (FAST_HashmapHandle handle) | 从哈希表中删除所有元素。 |
| size_t HMS_FAST_Hashmap_EraseIf (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc freeFunc, void* freeCtx) | 删除哈希表中符合输入条件的所有元素，并使用自定义的方式释放其内存。 |
| void HMS_FAST_Hashmap_Traverse (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc workFunc, void* workCtx) | 遍历哈希表，将所有符合输入条件的键值对按自定义的方式修改。 |
| FAST_ErrorCode HMS_FAST_Algo_Sort (HMS_FAST_SortData *data, HMS_FAST_Sort_CompFunc comp) | 使用用户提供的比较函数对任意类型数组进行完整排序。 |
| FAST_ErrorCode HMS_FAST_Algo_PartialSortAt (HMS_FAST_SortData *data, size_t offset, size_t count, HMS_FAST_Sort_CompFunc comp) | 对数组进行原地部分排序，使指定区间对应排序后的相应段。 |
| FAST_ErrorCode HMS_FAST_Algo_NaturalSort (HMS_FAST_SortData *data, int32_t ascend) | 使用自然语言规则对UTF-8字符串数组进行排序。 |
| FAST_ErrorCode HMS_FAST_Algo_NaturalPartialSortAt (HMS_FAST_SortData *data, size_t offset, size_t count, int32_t ascend) | 使用自然语言规则对UTF-8字符串数组进行部分排序，使指定区间对应排序后的相应段。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Create (HMS_FAST_PerfHintConfigBuilder** builder) | 创建构建器实例。 |
| void HMS_FAST_PerfHintConfigBuilder_Destroy (HMS_FAST_PerfHintConfigBuilder* builder) | 销毁构建器。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneType sceneType) | 设置需要系统性能优化的场景类型。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneState (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneState sceneState) | 设置需要系统性能优化的场景状态。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetDurationType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_DurationType durationType) | 设置需要系统性能优化的持续时间选项。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetTids (HMS_FAST_PerfHintConfigBuilder* builder, int* tids, uint32_t tidsSize) | 设置需要优化的线程ID。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Build (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_PerfHintConfig** config) | 创建系统性能优化配置参数。 |
| void HMS_FAST_PerfHintConfig_Destroy (HMS_FAST_PerfHintConfig* config) | 销毁系统性能优化配置参数。 |
| HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_SchedulingOptimization_PerfHint (const HMS_FAST_PerfHintConfig* config) | 系统性能优化接口。 |
 
 
  

#### 类型定义说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### FAST_ErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum FAST_ErrorCode FAST_ErrorCode
```
 
**描述**
 
FAST Kit的错误码。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_Rect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_Rect FAST_Rect
```
 
**描述**
 
定义矩形的数据结构。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_RectPartitionConfig

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig
```
 
**描述**
 
矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_Poly

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_Poly FAST_Poly
```
 
**描述**
 
定义稀疏格式多项式的数据结构。多项式
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5v9IYZeEShiz10EVf3Lxjg/zh-cn_image_0000002686088885.png?HW-CC-KV=V1&HW-CC-Date=20260730T071635Z&HW-CC-Expire=86400&HW-CC-Sign=F9AB1FF8A0067407E3A920BB8B7A197ABECF1604AE563CB6CB4476CC5E555B35)
由系数数组coeff和指数数组pow共同描述，且需按指数升序排列。
 
**起始版本：** 26.0.0
 
  

#### FAST_SegmentMapConfig

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig
```
 
**描述**
 
线段表的不透明配置（Opaque Configuration）。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_SegmentMapHandle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_SegmentMapHandle
```
 
**描述**
 
线段表的句柄。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_SegmentMapQueryType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType
```
 
**描述**
 
线段表数据结构支持的区间查询操作类型。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_SegmentMapUpdateType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType
```
 
**描述**
 
线段表数据结构支持的区间更新操作类型。
 
**起始版本：** 6.0.2(22)
 
  

#### FAST_ConcurrentHashmapHandle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_ConcurrentHashmapHandle
```
 
**描述**
 
并发哈希表的句柄。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_ConcurrentHashmapKeyPtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_ConcurrentHashmapKeyPtr
```
 
**描述**
 
并发哈希表的键指针。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_ConcurrentHashmapValuePtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_ConcurrentHashmapValuePtr
```
 
**描述**
 
并发哈希表的值指针。
 
**起始版本：** 6.1.1(24)
 
  

#### HMS_FAST_ConcurrentHashmap_HashFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef uint64_t (*HMS_FAST_ConcurrentHashmap_HashFunc)(const FAST_ConcurrentHashmapKeyPtr key)
```
 
**描述**
 
并发哈希表的哈希值计算回调函数类型。
 
**起始版本：** 6.1.1(24)
 
  

#### HMS_FAST_ConcurrentHashmap_KeyEqualFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int32_t (*HMS_FAST_ConcurrentHashmap_KeyEqualFunc)(
    const FAST_ConcurrentHashmapKeyPtr leftKey,
    const FAST_ConcurrentHashmapKeyPtr rightKey
)
```
 
**描述**
 
并发哈希表的键比较回调函数类型。
 
**起始版本：** 6.1.1(24)
 
  

#### HMS_FAST_ConcurrentHashmap_HookFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int32_t (*HMS_FAST_ConcurrentHashmap_HookFunc)(
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapValuePtr value,
    void* context
)
```
 
**描述**
 
并发哈希表的通用回调函数形式。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_SplitComplex

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_SplitComplex FAST_SplitComplex
```
 
**描述**
 
定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_SplitComplexD

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_SplitComplexD FAST_SplitComplexD
```
 
**描述**
 
定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_BiquadCoefficients

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_BiquadCoefficients FAST_BiquadCoefficients
```
 
**描述**
 
定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_BiquadCoefficientsD

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_BiquadCoefficientsD FAST_BiquadCoefficientsD
```
 
**描述**
 
定义双精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_BiquadState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_BiquadState FAST_BiquadState
```
 
**描述**
 
定义单精度二阶IIR滤波器节的状态变量。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_BiquadStateD

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_BiquadStateD FAST_BiquadStateD
```
 
**描述**
 
定义双精度二阶IIR滤波器节的状态变量。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_Biquadm

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_Biquadm FAST_Biquadm
```
 
**描述**
 
定义单精度多通道、多节二阶IIR滤波器组的数据结构。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_BiquadmD

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_BiquadmD FAST_BiquadmD
```
 
**描述**
 
定义双精度多通道、多节二阶IIR滤波器组的数据结构。
 
**起始版本：** 6.1.1(24)
 
  

#### FAST_FFTConfig

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct FAST_FFTConfig FAST_FFTConfig
```
 
**描述**
 
快速傅里叶变换的不透明配置（Opaque Configuration）。该对象是非线程安全的，在多线程环境中，严禁多个线程同时操作同一个FAST_FFTConfig配置对象。
 
**起始版本：** 26.0.0
 
  

#### FAST_HashmapHandle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_HashmapHandle
```
 
哈希表的句柄。
 
**起始版本：** 26.0.0
 
  

#### FAST_HashmapKeyPtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_HashmapKeyPtr
```
 
**描述**
 
哈希表的键指针。
 
**起始版本：** 26.0.0
 
  

#### FAST_HashmapValuePtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* FAST_HashmapValuePtr
```
 
**描述**
 
哈希表的值指针。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_Hashmap_HashFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef uint64_t(* HMS_FAST_Hashmap_HashFunc) (const FAST_HashmapKeyPtr key)
```
 
**描述**
 
哈希表的哈希计算回调函数类型。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| key | 要计算哈希的FAST_HashmapKeyPtr。 |
 
 
**返回：**
 
从键派生的64位哈希值。
 
  

#### HMS_FAST_Hashmap_HookFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int32_t(* HMS_FAST_Hashmap_HookFunc) (const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr value, void* context)
```
 
**描述**
 
哈希表的通用回调函数形式。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| key | 正在访问的当前元素的键。 |
| value | 与键关联的值。 |
| context | 通过遍历API传递的用户定义上下文。 |
 
 
**返回：**
 
非零表示条件满足（例如，用于过滤）；否则为零。
 
**注解：**
 
此函数通常用于支持条件处理的API，如选择性删除或转换。返回值的精确解释取决于调用函数：
 
- 在谓词上下文中（例如erase-if），非零返回值通常表示“匹配”。
- 在操作上下文中，返回值可能被忽略。

 
  

#### HMS_FAST_Hashmap_KeyEqualFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int32_t(* HMS_FAST_Hashmap_KeyEqualFunc) (const FAST_HashmapKeyPtr leftKey, const FAST_HashmapKeyPtr rightKey)
```
 
**描述**
 
自定义键相等比较函数回调。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| leftKey | 指向哈希表中键的指针，作为相等比较的左操作数传递。 |
| rightKey | 指向哈希表中另一个键的指针，作为相等比较的右操作数传递。 |
 
 
**返回：**
 
如果键被视为相等则非零；否则为零。
 
  

#### HMS_FAST_SortElementPtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void* HMS_FAST_SortElementPtr
```
 
**描述**
 
表示通用容器中单个元素的opaque pointer类型。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_SortElementConstPtr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef const void* HMS_FAST_SortElementConstPtr
```
 
**描述**
 
表示通用容器中单个元素的const opaque pointer类型。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_Sort_CompFunc

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef int32_t(* HMS_FAST_Sort_CompFunc) (HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second)
```
 
**描述**
 
用户自定义比较函数的回调函数类型。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| first | 指向第一个元素的指针。 |
| second | 指向第二个元素的指针。 |
 
 
**返回值：**
 
比较结果。必须返回：
 
- 负数表示first小于second
- 零表示first等于second
- 正数表示first大于second

 
  

#### HMS_FAST_SortData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HMS_FAST_SortData HMS_FAST_SortData
```
 
**描述**
 
描述待排序的连续内存数据块。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_HannWindowType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef enum HMS_FAST_HannWindowType HMS_FAST_HannWindowType
```
 
**描述**
 
汉宁窗类型枚举。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_PerfHintConfigBuilder

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HMS_FAST_PerfHintConfigBuilder HMS_FAST_PerfHintConfigBuilder
```
 
**描述**
 
系统性能优化配置参数构建器。
 
**起始版本：** 26.0.0
 
  

#### HMS_FAST_PerfHintConfig

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HMS_FAST_PerfHintConfig HMS_FAST_PerfHintConfig
```
 
**描述**
 
系统性能优化配置参数。
 
**起始版本：** 26.0.0
 
  

#### 常量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### FAST_MAX_FFT_LOG2N

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const uint32_t FAST_MAX_FFT_LOG2N = 16;
```
 
**描述**
 
FFT支持的最大点数N对应的以2为底的对数值。即FAST_MAX_FFT_LOG2N=
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/xS6a52XXR8uIlYGaVIO2vQ/zh-cn_image_0000002685929053.png?HW-CC-KV=V1&HW-CC-Date=20260730T071635Z&HW-CC-Expire=86400&HW-CC-Sign=BBEADCB5CC6E0462EF4EA31CD3D41856DEFAD9704C413D4E6000E0D2132F6805)
，其中N为FFT支持的最大点数，例如该值为16时，最大点数为65536。
 
**起始版本**：26.0.0
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### FAST_ErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum FAST_ErrorCode
```
 
**描述**
 
FAST Kit的错误码。
 
**起始版本：** 6.0.2(22)
  
| 枚举值 | 描述 |
| --- | --- |
| FAST_ERROR_CODE_SUCCESS = 1023100000 | 成功。 |
| FAST_ERROR_CODE_FAIL = 1023100001 | 失败。 |
| FAST_ERROR_CODE_ILLEGAL_INPUT = 1023100002 | 非法输入。 |
| FAST_ERROR_CODE_INVALID_PTR = 1023100003 | 无效指针（例如 NULL）。 |
| FAST_ERROR_CODE_KEY_EXISTS = 1023110000 | 键已存在。 起始版本：6.1.1(24) |
| FAST_ERROR_CODE_KEY_NOT_EXISTS = 1023110001 | 键不存在。 起始版本：6.1.1(24) |
| FAST_ERROR_CODE_OOM = 1023199001 | 内存溢出。 |
 
 
  

#### FAST_SegmentMapQueryType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum FAST_SegmentMapQueryType
```
 
**描述**
 
线段表支持的查询操作类型。
 
该枚举定义了线段表数据结构能够处理的各种区间查询操作。
 
**起始版本：** 6.0.2(22)
  
| 枚举值 | 描述 |
| --- | --- |
| FAST_SEGMENTMAP_QUERY_TYPE_SUM | 区间求和查询。 |
| FAST_SEGMENTMAP_QUERY_TYPE_MIN | 区间最小值查询。 |
| FAST_SEGMENTMAP_QUERY_TYPE_MAX | 区间最大值查询。 |
 
 
  

#### FAST_SegmentMapUpdateType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum FAST_SegmentMapUpdateType
```
 
**描述**
 
线段表支持的更新操作类型。
 
该枚举定义了线段表数据结构能够处理的各种区间更新操作。
 
**起始版本：** 6.0.2(22)
  
| 枚举值 | 描述 |
| --- | --- |
| FAST_SEGMENTMAP_UPDATE_TYPE_SET | 赋值更新，区间内的每一个元素赋同一个值。 |
| FAST_SEGMENTMAP_UPDATE_TYPE_ADD | 加法更新，区间内的每一个元素加同一个值。 |
| FAST_SEGMENTMAP_UPDATE_TYPE_SUB | 减法更新，区间内的每一个元素减同一个值。 |
 
 
  

#### HMS_FAST_HannWindowType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum HMS_FAST_HannWindowType
```
 
**描述**
 
汉宁窗类型枚举。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| HMS_FAST_HANN_DENORMALIZE_FULL = 0x00 | 非归一化全窗。 |
| HMS_FAST_HANN_NORMALIZE_FULL = 0x01 | 归一化全窗。 |
| HMS_FAST_HANN_DENORMALIZE_HALF = 0x10 | 非归一化半窗，给定长度为N时，仅包含前(N+1)/2个点。 |
| HMS_FAST_HANN_NORMALIZE_HALF = 0x11 | 归一化半窗，给定长度为N时，仅包含前(N+1)/2个点。 |
 
 
  

#### HMS_FAST_SchedulingOptimization_SceneType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum HMS_FAST_SchedulingOptimization_SceneType
```
 
**描述**
 
需要系统性能优化的场景类型。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| HMS_FAST_APP_LAUNCH = 1 | 应用启动场景。 |
| HMS_FAST_PAGE_TRANSITION = 2 | 页面切换场景。 |
| HMS_FAST_PAGE_LOAD = 3 | 页面加载场景。 |
| HMS_FAST_NETWORK_FILE_PROCESSING = 4 | 网络文件处理场景。 |
| HMS_FAST_LOCAL_FILE_PROCESSING = 5 | 本地文件处理场景。 |
| HMS_FAST_PAGE_DRAWING = 6 | 页面绘制场景。 |
| HMS_FAST_ANIMATION = 7 | 动效场景。 |
| HMS_FAST_MEDIA_PLAYBACK = 8 | 媒体播放场景。 |
| HMS_FAST_MEDIA_ENCODING_AND_DECODING = 9 | 媒体编解码场景。 |
 
 
  

#### HMS_FAST_SchedulingOptimization_SceneState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum HMS_FAST_SchedulingOptimization_SceneState
```
 
**描述**
 
需要系统性能优化的场景状态。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| HMS_FAST_END | 结束系统性能优化。 |
| HMS_FAST_BEGIN | 开始系统性能优化。 |
 
 
  

#### HMS_FAST_SchedulingOptimization_DurationType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum HMS_FAST_SchedulingOptimization_DurationType
```
 
**描述**
 
需要系统性能优化的持续时间选项。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| HMS_FAST_SHORT | 短持续时间。单次最大持续时间：1，间隔大于3。单位：秒。 |
| HMS_FAST_MEDIUM | 中等持续时间。单次最大持续时间：10，间隔大于30。单位：秒。 |
| HMS_FAST_LONG | 长持续时间。单次最大持续时间：60，间隔大于180。单位：秒。 |
 
 
  

#### HMS_FAST_SchedulingOptimization_ErrorCode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum HMS_FAST_SchedulingOptimization_ErrorCode
```
 
**描述**
 
系统性能优化的错误码。
 
**起始版本：** 26.0.0
  
| 枚举值 | 描述 |
| --- | --- |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS | 成功。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_HIGH_SYSTEM_LOAD | 系统高负载。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_POWER_SAVING_MODE | 省电模式。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_LOW_POWER_MODE | 低电量模式。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NON_FRONTEND | 非前台调用场景。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INTERVAL | 间隔不满足要求。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_EXECUTE_ERROR | 执行系统性能优化失败。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM | 参数无效。 |
| HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NO_MEMORY | 内存不足。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### HMS_FAST_RectPartition_CreateConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig ** config)
```
 
**描述**
 
创建矩形划分求解器的不透明配置。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向矩形划分求解器不透明配置FAST_RectPartitionConfig的指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_RectPartition_DestroyConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig * config)
```
 
**描述**
 
销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待销毁的矩形划分求解器的不透明配置FAST_RectPartitionConfig。 |
 
 
  

#### HMS_FAST_RectPartition_SetAlgo()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig * config, const char * name )
```
 
**描述**
 
设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为O(N logN)。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待设置的矩形划分求解器的不透明配置FAST_RectPartitionConfig。 |
| name | 矩形求解器使用的算法名称。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config或name为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当算法不支持时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_RectPartition_Solve()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig * config, size_t size, const FAST_Rect * origin, FAST_Rect * result, size_t * resultSize )
```
 
**描述**
 
在指定不透明配置下求解矩形划分问题。在调用函数之前需要先初始化参数中的结果数组result。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 矩形划分求解器的不透明配置。如果参数config中未设置算法，默认的算法是扫描线算法“SweepLineAlgo”。 |
| size | 待划分的矩形FAST_Rect数量。 |
| origin | 待划分的矩形FAST_Rect源数组。 |
| result | 由矩形划分求解器得到的FAST_Rect结果，在调用函数之前需要初始化该结果数组，大小需要和源数组相等，否则可能导致溢出。 |
| resultSize | 划分之后的FAST_Rect数量。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当入参指针为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)，如矩形存在相交。
 
当算法求解失败时，返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)。
 
**注解：**
 
当config选择"SweepLineAlgo"算法时，结果不会返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)，此处仅作为预防性设置。
 
  

#### HMS_FAST_PolyRoot_ComputeRoots()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRoots (const FAST_Poly * poly, const size_t maxRootCount, double * root, size_t * rootCount )
```
 
**描述**
 
计算多项式的给定数量的实数根。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| poly | 待求根的多项式FAST_Poly。 |
| maxRootCount | 需要返回的实根数量。 |
| root | 输出实根数组。 |
| rootCount | 实际返回的实根数量。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当poly或root或rootCount为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时（如指数未按升序排列），返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_PolyRoot_ComputeSingle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeSingle (const FAST_Poly * poly, double * root )
```
 
**描述**
 
计算多项式的绝对值最大的实根。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| poly | 待求根的多项式FAST_Poly。 |
| root | 计算出的实根。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当poly或root为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时（如指数未按升序排列），返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_PolyRoot_ComputeRootIntervals()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRootIntervals (const FAST_Poly * poly, const size_t maxRootCount, double * leftBoundary, double * rightBoundary, size_t * rootCount )
```
 
**描述**
 
计算多项式给定数量的实根的隔离区间，输出每个实根的左右边界。每个区间包含且仅包含一个实根。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| poly | 待求根区间的多项式FAST_Poly。 |
| maxRootCount | 需要输出的实根的区间数量 |
| leftBoundary | 各个实根区间左边界的数组。 |
| rightBoundary | 各个实根区间右边界的数组。 |
| rootCount | 实际找到并返回的实根数量。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当poly或leftBoundary或rightBoundary或rootCount为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时（如指数未按升序排列），返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_SegmentMap_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle * handle, size_t size, const int32_t * array, FAST_SegmentMapConfig * config )
```
 
**描述**
 
创建线段表。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 指向线段表句柄FAST_SegmentMapHandle的指针。 |
| size | 底层数组的大小（元素数量）。 |
| array | 可选；用于初始化线段表的底层数组。如果为NULL，则线段表中的元素均初始化为0，否则数组大小必须与参数size保持一致。 |
| config | 线段表的不透明配置FAST_SegmentMapConfig，若该参数为NULL或未配置，默认查询类型为FAST_SEGMENTMAP_QUERY_TYPE_SUM、更新类型为FAST_SEGMENTMAP_UPDATE_TYPE_SET。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config或handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_SegmentMap_CreateConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig ** config)
```
 
**描述**
 
创建线段表的不透明配置。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向线段表不透明配置FAST_SegmentMapConfig的指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_SegmentMap_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle)
```
 
**描述**
 
销毁线段表实例。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 待销毁线段表句柄FAST_SegmentMapHandle。 |
 
 
  

#### HMS_FAST_SegmentMap_DestroyConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig * config)
```
 
**描述**
 
销毁线段表的不透明配置。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待销毁线段表不透明配置FAST_SegmentMapConfig。 |
 
 
  

#### HMS_FAST_SegmentMap_Query()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t * result )
```
 
**描述**
 
查询线段表的区间。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间左闭右开。 |
| right | 区间右端点 （不包含），区间左闭右开。 |
| result | 根据区间查询的结果。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)，如左端点大于等于右端点。
 
  

#### HMS_FAST_SegmentMap_SetQueryType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig * config, FAST_SegmentMapQueryType type )
```
 
**描述**
 
设置线段表不透明配置中的查询类型。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 查询类型。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
  

#### HMS_FAST_SegmentMap_SetUpdateType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig * config, FAST_SegmentMapUpdateType type )
```
 
**描述**
 
设置线段表不透明配置中的更新类型。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 更新类型。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
  

#### HMS_FAST_SegmentMap_Update()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value )
```
 
**描述**
 
更新线段表的区间。
 
**起始版本：** 6.0.2(22)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间为左闭右开。 |
| right | 区间右端点 （不包含），区间为左闭右开。 |
| value | 待更新的值。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)，如左端点大于等于右端点。
 
  

#### HMS_FAST_Biquadm_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_Create (size_t numChannels, size_t numSections, size_t maxFrames, FAST_Biquadm ** filter)
```
 
**描述**
 
创建并初始化多通道多节二阶IIR滤波器组（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| numChannels | 信号通道数，必须大于0。 |
| numSections | 每通道级联的 biquad 节数，必须大于0。 |
| maxFrames | 单次处理的最大采样数（每通道），必须大于0。 |
| filter | 指向将接收新创建滤波器地址的变量指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当numChannels、numSections或maxFrames为0时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当内存耗尽分配失败时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_CreateD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_CreateD (size_t numChannels, size_t numSections, size_t maxFrames, FAST_BiquadmD ** filter)
```
 
**描述**
 
创建并初始化多通道多节二阶IIR滤波器组（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| numChannels | 信号通道数，必须大于0。 |
| numSections | 每通道级联的 biquad 节数，必须大于0。 |
| maxFrames | 单次处理的最大采样数（每通道），必须大于0。 |
| filter | 指向将接收新创建滤波器地址的变量指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当numChannels、numSections或maxFrames为0时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当内存耗尽分配失败时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_Biquadm_Destroy (FAST_Biquadm * filter)
```
 
**描述**
 
销毁二阶滤波器实例（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 待销毁的二阶滤波器实例。 |
 
 
  

#### HMS_FAST_Biquadm_DestroyD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_Biquadm_DestroyD (FAST_BiquadmD * filter)
```
 
**描述**
 
销毁二阶滤波器实例（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 待销毁的二阶滤波器实例。 |
 
 
  

#### HMS_FAST_Biquadm_SetCoeffSingle()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingle (FAST_Biquadm * filter, const float * coeff, size_t stride)
```
 
**描述**
 
从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或coeff为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_SetCoeffDouble()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDouble (FAST_Biquadm * filter, const double * coeff, size_t stride)
```
 
**描述**
 
从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或coeff为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_SetCoeffSingleD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingleD (FAST_BiquadmD * filter, const float * coeff, size_t stride)
```
 
**描述**
 
从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或coeff为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_SetCoeffDoubleD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDoubleD (FAST_BiquadmD * filter, const double * coeff, size_t stride)
```
 
**描述**
 
从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或coeff为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_SetActiveFilters()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFilters (FAST_Biquadm * filter, const uint8_t * activeMask)
```
 
**描述**
 
设置二阶滤波器节的激活掩码（单精度）。掩码顺序为：[ch0_sec0, ch0_sec1, ch0_sec2, ..., ch1_sec0, ch1_sec1, ch1_sec2, ...]。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| activeMask | 布尔数组（大小为 filter->numSections）；非零表示激活。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm_SetActiveFiltersD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFiltersD (FAST_BiquadmD * filter, const uint8_t * activeMask)
```
 
**描述**
 
设置二阶滤波器节的激活掩码（双精度）。掩码顺序为：[ch0_sec0, ch0_sec1, ch0_sec2, ..., ch1_sec0, ch1_sec1, ch1_sec2, ...]。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| activeMask | 布尔数组（大小为 filter->numSections）；非零表示激活。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_Biquadm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Biquadm (FAST_Biquadm * filter, const float ** input, const size_t strideInput, float ** output, const size_t strideOutput, size_t length)
```
 
**描述**
 
通过二阶滤波器组处理多通道音频（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 已初始化的滤波器组。 |
| input | 输入通道指针数组（大小为 filter->numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter->numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter->maxFrames）。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter、coeff或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化或length超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_BiquadmD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_BiquadmD (FAST_BiquadmD * filter, const double ** input, const size_t strideInput, double ** output, const size_t strideOutput, size_t length)
```
 
**描述**
 
通过二阶滤波器组处理多通道音频（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| filter | 已初始化的滤波器组。 |
| input | 输入通道指针数组（大小为 filter->numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter->numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter->maxFrames）。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当filter、coeff或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当filter未初始化或length超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_DSP_Maxmgv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Maxmgv (const float * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量中的最大幅值（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |
 
 
**返回：**
 
向量中的最大绝对值。如果length为0，则返回0.0f。
 
  

#### HMS_FAST_DSP_MaxmgvD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_MaxmgvD (const double * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量中的最大幅值（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |
 
 
**返回：**
 
向量中的最大绝对值。如果length为0，则返回0.0。
 
  

#### HMS_FAST_DSP_Maxvi()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Maxvi (const float * input, size_t stride, size_t length, float * value, size_t * index)
```
 
**描述**
 
查找步长实数向量中的最大值及其索引（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
| value | 用于存储最大值的指针。如果length为0，则返回-FLT_MAX。 |
| index | 具有最大值的样本的索引（从0开始）。如果length为0，则返回0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_MaxviD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_MaxviD (const double * input, size_t stride, size_t length, double * value, size_t * index)
```
 
**描述**
 
查找步长实数向量中的最大值及其索引（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
| value | 用于存储最大值的指针。如果length为0，则返回-DBL_MAX。 |
| index | 具有最大值的样本的索引（从0开始）。如果length为0，则返回0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Sve()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Sve (const float * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量的和（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
input[i]的和。如果length为0，则返回0.0f。
 
  

#### HMS_FAST_DSP_SveD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_SveD (const double * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量的和（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
input[i]的和。如果length为0，则返回0.0。
 
  

#### HMS_FAST_DSP_Svemg()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Svemg (const float * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长向量的绝对值之和（L1范数）（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
输入向量内所有元素的绝对值的和。如果length为0，则返回0.0f。
 
  

#### HMS_FAST_DSP_SvemgD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_SvemgD (const double * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长向量的绝对值之和（L1范数）（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
输入向量内所有元素的绝对值的和。如果length为0，则返回0.0。
 
  

#### HMS_FAST_DSP_Meamgv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Meamgv (const float * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量绝对值的均值（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
|input[i]|的均值。如果length为0，则返回0.0f。
 
  

#### HMS_FAST_DSP_MeamgvD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_MeamgvD (const double * input, size_t stride, size_t length)
```
 
**描述**
 
计算步长实数向量绝对值的均值（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
|input[i]|的均值。如果length为0，则返回0.0。
 
  

#### HMS_FAST_DSP_Dotpr()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Dotpr (const float * inputA, size_t strideA, const float * inputB, size_t strideB, size_t length)
```
 
**描述**
 
计算两个步长实数向量的点积（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
点积：sum(inputA[i] * inputB[i])。如果length为0，则返回0.0f。
 
  

#### HMS_FAST_DSP_DotprD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_DotprD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, size_t length)
```
 
**描述**
 
计算两个步长实数向量的点积（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| length | 样本数。 |
 
 
**返回：**
 
点积：sum(inputA[i] * inputB[i])。如果length为0，则返回0.0。
 
  

#### HMS_FAST_DSP_Vsbsm()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsbsm (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float scalar, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| scalar | 用于计算的标量。 |
| outputC | 输出向量（调用者分配）。 |
| strideC | 输出向量的步长。值为1表示连续存储。 |
| length | 样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsbsmD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsbsmD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double scalar, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| scalar | 用于计算的标量。 |
| outputC | 输出向量（调用者分配）。 |
| strideC | 输出向量的步长。值为1表示连续存储。 |
| length | 样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Ctoz()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Ctoz (const float * input, size_t strideInput, FAST_SplitComplex * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将交错复数数组（real, imag, real, imag, ...）转换为分离格式（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 交错复数输入（长度为复数数量的2倍）。 |
| strideInput | 复数样本之间的步长。值为1表示连续存储。 |
| output | 分离复数输出结构体。 |
| strideOutput | 输出数组中实部/虚部样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_CtozD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_CtozD (const double * input, size_t strideInput, FAST_SplitComplexD * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将交错复数数组（real, imag, real, imag, ...）转换为分离格式（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 交错复数输入（长度为复数数量的2倍）。 |
| strideInput | 复数样本之间的步长。值为1表示连续存储。 |
| output | 分离复数输出结构体。 |
| strideOutput | 输出数组中实部/虚部样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Ztoc()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Ztoc (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将分离复数数组转换为交错格式（单精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离复数输入结构体。 |
| strideInput | 实部/虚部数组中样本之间的步长。值为1表示连续存储。 |
| output | 交错输出数组（长度为复数数量的2倍）。 |
| strideOutput | 输出中复数样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_ZtocD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_ZtocD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将分离复数数组转换为交错格式（双精度）。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离复数输入结构体。 |
| strideInput | 实部/虚部数组中样本之间的步长。值为1表示连续存储。 |
| output | 交错输出数组（长度为复数数量的2倍）。 |
| strideOutput | 输出中复数样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Zvabs()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Zvabs (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的幅值（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_ZvabsD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_ZvabsD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的幅值（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Zvmags()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Zvmags (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的幅值平方（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值平方）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_ZvmagsD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_ZvmagsD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的幅值平方（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值平方）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Zvphas()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Zvphas (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的相位角（弧度制）（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（相位角）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_ZvphasD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_ZvphasD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算复数向量的相位角（弧度制）（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（相位角）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsmul()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsmul (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将向量的每个元素乘以标量，output[i] = input[i] * scalar（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 乘法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsmulD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsmulD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将向量的每个元素乘以标量，output[i] = input[i] * scalar（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 乘法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsdiv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsdiv (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将向量的每个元素除以标量，output[i] = input[i] / scalar（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 除数标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsdivD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsdivD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将向量的每个元素除以标量，output[i] = input[i] / scalar（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 除数标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Svdiv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Svdiv (const float scalar, const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将标量除以向量的每个元素，output[i] = scalar / input[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| scalar | 被除数标量。 |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_SvdivD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_SvdivD (const double scalar, const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将标量除以向量的每个元素，output[i] = scalar / input[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| scalar | 被除数标量。 |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsadd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsadd (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将标量加到向量的每个元素，output[i] = input[i] + scalar（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 加法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsaddD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsaddD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将标量加到向量的每个元素，output[i] = input[i] + scalar（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 加法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vadd()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vadd (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素加法，C[i] = A[i] + B[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VaddD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VaddD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素加法，C[i] = A[i] + B[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsub()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsub (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素减法，C[i] = A[i] - B[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsubD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsubD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素减法，C[i] = A[i] - B[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vmul()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vmul (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素乘法，C[i] = A[i] * B[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VmulD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VmulD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素乘法，C[i] = A[i] * B[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vdiv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vdiv (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素除法，C[i] = A[i] / B[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针（被除数）。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针（除数）。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VdivD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VdivD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
执行向量逐元素除法，C[i] = A[i] / B[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针（被除数）。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针（除数）。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vdist()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vdist (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```
 
**描述**
 
计算两个向量对应元素的欧几里得范数（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VdistD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VdistD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```
 
**描述**
 
计算两个向量对应元素的欧几里得范数（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Svesq()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float HMS_FAST_DSP_Svesq (const float * input, size_t stride, size_t length)
```
 
**描述**
 
计算向量元素的平方和（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 输入向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
向量元素的平方和。
 
  

#### HMS_FAST_DSP_SvesqD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double HMS_FAST_DSP_SvesqD (const double * input, size_t stride, size_t length)
```
 
**描述**
 
计算向量元素的平方和（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 输入向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
向量元素的平方和。
 
  

#### HMS_FAST_DSP_Minvi()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Minvi (const float * input, size_t stride, size_t length, float * value, size_t * index)
```
 
**描述**
 
查找步长实数向量中的最小值及其索引（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 待处理的样本数。 |
| value | 输出参数，存储找到的最小值。如果length为0，设置为FLT_MAX。 |
| index | 输出参数，存储最小值的索引（0基）。如果length为0，设置为0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_MinviD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_MinviD (const double * input, size_t stride, size_t length, double * value, size_t * index)
```
 
**描述**
 
查找步长实数向量中的最小值及其索引（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 待处理的样本数。 |
| value | 输出参数，存储找到的最小值。如果length为0，设置为DBL_MAX。 |
| index | 输出参数，存储最小值的索引（0基）。如果length为0，设置为0。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsq()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsq (const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算向量每个元素的平方（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsqD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsqD (const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算向量每个元素的平方（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vabs()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vabs (const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算向量每个元素的绝对值（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VabsD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VabsD (const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
计算向量每个元素的绝对值（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vthr()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vthr (const float * input, size_t strideInput, const float threshold, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
对向量应用阈值，若input[i] < threshold则output[i] = threshold，否则output[i] = input[i]（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| threshold | 阈值标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VthrD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VthrD (const double * input, size_t strideInput, const double threshold, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
对向量应用阈值，若input[i] < threshold则output[i] = threshold，否则output[i] = input[i]（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| threshold | 阈值标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vrvrs()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vrvrs (float * vector, size_t stride, size_t length)
```
 
**描述**
 
原地反转向量中元素的顺序（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待反转的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VrvrsD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VrvrsD (double * vector, size_t stride, size_t length)
```
 
**描述**
 
原地反转向量中元素的顺序（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待反转的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vspdp()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vspdp (const float * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将单精度向量转换为双精度向量。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 单精度输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 双精度输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vdpsp()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vdpsp (const double * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```
 
**描述**
 
将双精度向量转换为单精度向量。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 双精度输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 单精度输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vfill()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vfill (float * vector, size_t stride, size_t length, const float scalar)
```
 
**描述**
 
使用指定标量值填充向量（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待填充的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待填充的元素数量。 |
| scalar | 标量值。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VfillD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VfillD (double * vector, size_t stride, size_t length, const double scalar)
```
 
**描述**
 
使用指定标量值填充向量（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待填充的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待填充的元素数量。 |
| scalar | 标量值。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vclr()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vclr (float * vector, size_t stride, size_t length)
```
 
**描述**
 
将向量所有元素清零（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 输出向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待清零的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VclrD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VclrD (double * vector, size_t stride, size_t length)
```
 
**描述**
 
将向量所有元素清零（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 输出向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待清零的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Conv()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Conv (const float * input, size_t strideInput, const float * filter, size_t strideFilter, float * output, size_t strideOutput, size_t outputLength, size_t filterLength)
```
 
**描述**
 
执行两个向量的卷积运算（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入信号向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| filter | 滤波器系数向量指针。 |
| strideFilter | 滤波器向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| outputLength | 输出向量中的元素数量。 |
| filterLength | 滤波器向量中的元素数量。 |
 
 
**返回：**
 
无。
 
**注解：**
 
input缓冲区长度必须大于outputLength + filterLength - 1，否则将产生未定义行为。
 
  

#### HMS_FAST_DSP_ConvD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_ConvD (const double * input, size_t strideInput, const double * filter, size_t strideFilter, double * output, size_t strideOutput, size_t outputLength, size_t filterLength)
```
 
**描述**
 
执行两个向量的卷积运算（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| input | 输入信号向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| filter | 滤波器系数向量指针。 |
| strideFilter | 滤波器向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| outputLength | 输出向量中的元素数量。 |
| filterLength | 滤波器向量中的元素数量。 |
 
 
**返回：**
 
无。
 
**注解：**
 
input缓冲区长度必须大于outputLength + filterLength - 1，否则将产生未定义行为。
 
  

#### HMS_FAST_DSP_HannWindow()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_HannWindow (float * output, size_t length, HMS_FAST_HannWindowType type)
```
 
**描述**
 
生成汉宁窗序列（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| output | 输出向量指针，用于存放窗系数。 |
| length | 生成的窗点数。 |
| type | 窗类型，参见HMS_FAST_HannWindowType。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_HannWindowD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_HannWindowD (double * output, size_t length, HMS_FAST_HannWindowType type)
```
 
**描述**
 
生成汉宁窗序列（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| output | 输出向量指针，用于存放窗系数。 |
| length | 生成的窗点数。 |
| type | 窗类型，参见HMS_FAST_HannWindowType。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Mmul()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Mmul (const float * matrixA, size_t strideA, const float * matrixB, size_t strideB, float * matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)
```
 
**描述**
 
执行矩阵乘法，C = A * B，其中A为MxP矩阵、B为PxN矩阵、C为MxN矩阵（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| matrixA | 矩阵A指针。 |
| strideA | 矩阵A的元素步长。 |
| matrixB | 矩阵B指针。 |
| strideB | 矩阵B的元素步长。 |
| matrixC | 矩阵C指针（结果）。 |
| strideC | 矩阵C的元素步长。 |
| rowsM | 矩阵A和C的行数。 |
| colsN | 矩阵B和C的列数。 |
| colsP | 矩阵A的列数和矩阵B的行数。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_MmulD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_MmulD (const double * matrixA, size_t strideA, const double * matrixB, size_t strideB, double * matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)
```
 
**描述**
 
执行矩阵乘法，C = A * B，其中A为MxP矩阵、B为PxN矩阵、C为MxN矩阵（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| matrixA | 矩阵A指针。 |
| strideA | 矩阵A的元素步长。 |
| matrixB | 矩阵B指针。 |
| strideB | 矩阵B的元素步长。 |
| matrixC | 矩阵C指针（结果）。 |
| strideC | 矩阵C的元素步长。 |
| rowsM | 矩阵A和C的行数。 |
| colsN | 矩阵B和C的列数。 |
| colsP | 矩阵A的列数和矩阵B的行数。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vvpow()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vvpow (const float * inputA, const float * inputB, float * outputC, size_t length)
```
 
**描述**
 
执行向量逐元素幂运算，C[i]等于A[i]的B[i]次方（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 底数向量A指针。 |
| inputB | 指数向量B指针。 |
| outputC | 输出向量C指针。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VvpowD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VvpowD (const double * inputA, const double * inputB, double * outputC, size_t length)
```
 
**描述**
 
执行向量逐元素幂运算，C[i]等于A[i]的B[i]次方（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| inputA | 底数向量A指针。 |
| inputB | 指数向量B指针。 |
| outputC | 输出向量C指针。 |
| length | 待处理的元素数量。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_Vsort()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_Vsort (float * vector, size_t length, int order)
```
 
**描述**
 
对向量进行原地排序（单精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待排序的向量指针（输入/输出）。 |
| length | 待排序的元素数量。 |
| order | 排序顺序（1表示升序，-1表示降序，其他值不执行操作）。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_DSP_VsortD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_DSP_VsortD (double * vector, size_t length, int order)
```
 
**描述**
 
对向量进行原地排序（双精度）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| vector | 待排序的向量指针（输入/输出）。 |
| length | 待排序的元素数量。 |
| order | 排序顺序（1表示升序，-1表示降序，其他值不执行操作）。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_FFT_CreateConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_CreateConfig (FAST_FFTConfig** config, const uint32_t log2n)
```
 
**描述**
 
创建单精度FFT的不透明配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST_MAX_FFT_LOG2N](#fast_max_fft_log2n)（即1到16）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向快速傅里叶变换的不透明配置FAST_FFTConfig的指针。 |
| log2n | FFT点数对应的以2为底的对数值（即变换长度N=1<<log2n）。必须满足0<log2n<=FAST_MAX_FFT_LOG2N（即1到16）。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当log2n超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_FFT_CreateConfigD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_CreateConfigD (FAST_FFTConfig** config, const uint32_t log2n)
```
 
**描述**
 
创建双精度FFT的不透明配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST_MAX_FFT_LOG2N](#fast_max_fft_log2n)，即1到16）。与[HMS_FAST_FFT_CreateConfig](#hms_fast_fft_createconfig)功能相同，但用于双精度（double）计算，提供更高的数值精度。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向快速傅里叶变换的不透明配置FAST_FFTConfig的指针。 |
| log2n | FFT点数对应的以2为底的对数值（即变换长度N=1<<log2n）。必须满足0<log2n<=FAST_MAX_FFT_LOG2N（即1到16）。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当log2n超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_FFT_DestroyConfig()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_FFT_DestroyConfig (FAST_FFTConfig* config)
```
 
**描述**
 
销毁FFT的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 待销毁的FFT的不透明配置FAST_FFTConfig。 |
 
 
**返回：**
 
无。
 
  

#### HMS_FAST_FFT_ForwardTransform()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_ForwardTransform (FAST_FFTConfig* config, const uint32_t length, const float input[], float outputRe[], float outputIm[])
```
 
**描述**
 
计算单精度实数时域信号的离散傅里叶变换（DFT）。该变换将实数时域信号转换为复数频域信号，最终输出复数频谱。
 
对于长度为N的实数输入，输出包含N/2+1个复数频率分量（由于实信号的频谱共轭对称性，只需存储前半部分）。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由HMS_FAST_FFT_CreateConfig创建。 |
| length | 输入信号长度。必须等于创建配置时指定的2^log2n。 |
| input | 实数时域输入数组，大小为length。 |
| outputRe | 复数频域输出的实部数组，大小为length/2+1。 |
| outputIm | 复数频域输出的虚部数组，大小为length/2+1。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当input、outputRe或outputIm为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当length不等于2^log2n时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_FFT_ForwardTransformD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_ForwardTransformD (FAST_FFTConfig* config, const uint32_t length, const double input[], double outputRe[], double outputIm[])
```
 
**描述**
 
计算双精度实数时域信号的离散傅里叶变换（DFT）。与[HMS_FAST_FFT_ForwardTransform](#hms_fast_fft_forwardtransform) 功能相同，但使用双精度（double）计算。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由HMS_FAST_FFT_CreateConfigD创建。 |
| length | 输入信号长度。必须等于2^log2n。 |
| input | 实数时域输入数组，大小为length。 |
| outputRe | 复数频域输出的实部数组，大小为length/2+1。 |
| outputIm | 复数频域输出的虚部数组，大小为length/2+1。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当input、outputRe或outputIm为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当length不等于2^log2n时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_FFT_InverseTransform()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_InverseTransform (FAST_FFTConfig* config, const uint32_t length, const float inputRe[], const float inputIm[], float output[])
```
 
**描述**
 
计算单精度复数频域序列的逆离散傅里叶变换（IDFT）。将频域信号转换回时域表示。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由HMS_FAST_FFT_CreateConfig 创建。 |
| length | 输出信号长度。必须等于2^log2n。 |
| inputRe | 复数频域输入的实部数组，大小为length/2+1。 |
| inputIm | 复数频域输入的虚部数组，大小为length/2+1。 |
| output | 实数时域输出数组，大小为length。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当inputRe、inputIm或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当length不等于2^log2n时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_FFT_InverseTransformD()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_FFT_InverseTransformD (FAST_FFTConfig* config, const uint32_t length, const double inputRe[], const double inputIm[], double output[])
```
 
**描述**
 
计算双精度复数频域序列的逆离散傅里叶变换（IDFT）。与[HMS_FAST_FFT_InverseTransform](#hms_fast_fft_inversetransform)功能相同，但使用双精度（double）计算。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由HMS_FAST_FFT_CreateConfigD创建。 |
| length | 输出信号长度。必须等于2^log2n。 |
| inputRe | 复数频域输入的实部数组，大小为length/2+1。 |
| inputIm | 复数频域输入的虚部数组，大小为length/2+1。 |
| output | 实数时域输出数组，大小为length。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当inputRe、inputIm或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
length不等于2^log2n时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create(
    FAST_ConcurrentHashmapHandle* handle,
    HMS_FAST_ConcurrentHashmap_HashFunc hasher,
    HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler,
    float maxLoadFac,
    size_t numShards
)
```
 
**描述**
 
根据输入配置创建并发哈希表。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| hasher | 开发者定义的哈希值计算回调函数。 |
| equaler | 开发者定义的键比较回调函数。 |
| maxLoadFac | 初始设定的最大负载因子。 |
| numShards | 初始设定的分段数。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle或相关回调函数为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽构造失败时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_ConcurrentHashmap_Destroy(FAST_ConcurrentHashmapHandle handle)
```
 
**描述**
 
销毁给定并发哈希表。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 待销毁的并发哈希表句柄。 |
 
 
  

#### HMS_FAST_ConcurrentHashmap_Insert()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Insert(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    const FAST_ConcurrentHashmapValuePtr value,
    FAST_ConcurrentHashmapValuePtr* originValue
)
```
 
**描述**
 
将给定键值对插入并发哈希表，如果给定的键在哈希表中已经存在，则覆写原有的值。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待插入的键指针。 |
| value | 待插入的值指针。 |
| originValue | 将被覆盖的值的指针，仅在返回FAST_ERROR_CODE_KEY_EXISTS时有效，如果不需要请传入NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中存在相同的键时，使用value覆盖已有的值并返回[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_Find()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Find(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapValuePtr* value
)
```
 
**描述**
 
查找并发哈希表中给定键对应的值，将结果保存在value指针中。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待查找的键指针。 |
| value | 用于保存查询结果的指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle、key或value为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中不存在匹配的键时，返回[FAST_ERROR_CODE_KEY_NOT_EXISTS](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_Erase()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapKeyPtr* originKey,
    FAST_ConcurrentHashmapValuePtr* originValue
)
```
 
**描述**
 
在并发哈希表中删除给定的键及其对应的值，并将其值保存在originalKey和originalValue中以便于开发者进行内存管理；实际使用时也可根据需求将originalKey或originalValue设为NULL，此时则不会将键或值的地址返回。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待删除的键指针。 |
| originKey | 用于返回哈希表中保存的键的指针，可为NULL。 |
| originValue | 用于返回哈希表中保存的值得指针，可为NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle或key为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中不存在匹配的键时，返回[FAST_ERROR_CODE_KEY_NOT_EXISTS](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_TryInsert()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_TryInsert(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    const FAST_ConcurrentHashmapValuePtr value
)
```
 
**描述**
 
将给定键值对插入并发哈希表，如果给定的键在哈希表中已经存在，则放弃插入保持原状。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待插入的键指针。 |
| value | 待插入的值指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle、key或value为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中存在相同的键时，不执行任何操作并返回[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)。
 
  

#### HMS_FAST_ConcurrentHashmap_Size()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
size_t HMS_FAST_ConcurrentHashmap_Size(FAST_ConcurrentHashmapHandle handle)
```
 
**描述**
 
返回给定并发哈希表中的元素个数。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
 
 
**返回：**
 
给定并发哈希表的元素个数，需注意在重度并发操作下该返回值可能与实际值存在细微偏差。
 
  

#### HMS_FAST_ConcurrentHashmap_Clear()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_ConcurrentHashmap_Clear(FAST_ConcurrentHashmapHandle handle)
```
 
**描述**
 
清空给定并发哈希表中的所有元素。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
 
 
  

#### HMS_FAST_ConcurrentHashmap_EraseIf()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
size_t HMS_FAST_ConcurrentHashmap_EraseIf(
    FAST_ConcurrentHashmapHandle handle,
    HMS_FAST_ConcurrentHashmap_HookFunc condFunc,
    void* condCtx,
    HMS_FAST_ConcurrentHashmap_HookFunc freeFunc,
    void* freeCtx
)
```
 
**描述**
 
遍历哈希表并删除所有符合给定条件的键值对，同时使用开发者定义的freeFunc释放键值对的内存；实际使用时freeFunc可为NULL，此时要求开发者另行完成内存管理动作。注意：请避免在condFunc和freeFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的删除条件回调函数。 |
| condCtx | 条件回调函数的上下文。 |
| freeFunc | 开发者定义的内存释放回调函数，可为NULL。 |
| freeCtx | 内存释放回调函数的上下文。 |
 
 
**返回：**
 
完成删除操作的元素个数。
 
  

#### HMS_FAST_ConcurrentHashmap_Traverse()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_ConcurrentHashmap_Traverse(
    FAST_ConcurrentHashmapHandle handle,
    HMS_FAST_ConcurrentHashmap_HookFunc condFunc,
    void* condCtx,
    HMS_FAST_ConcurrentHashmap_HookFunc workFunc,
    void* workCtx
)
```
 
**描述**
 
遍历哈希表并对所有符合开发者condFunc的键值对执行workFunc中的修改；如果condFunc为NULL，则对于表中存在的所有键值对都将执行开发者定义的workFunc。注意：请避免在condFunc和workFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。
 
**起始版本：** 6.1.1(24)
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的条件回调函数，可为NULL。 |
| condCtx | 回调函数的上下文。 |
| workFunc | 开发者定义的修改回调函数。 |
| workCtx | 修改函数的上下文。 |
 
 
  

#### HMS_FAST_Hashmap_Clear()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_Hashmap_Clear (FAST_HashmapHandle handle)
```
 
**描述**
 
从哈希表中删除所有元素。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
 
 
**返回：**
 
无
 
  

#### HMS_FAST_Hashmap_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Hashmap_Create (FAST_HashmapHandle* handle, HMS_FAST_Hashmap_HashFunc hasher, HMS_FAST_Hashmap_KeyEqualFunc equaler)
```
 
**描述**
 
根据输入配置创建哈希表。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 存储创建的哈希表句柄指针。 |
| hasher | 自定义哈希计算回调函数。 |
| equaler | 自定义的键比较回调函数。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle或相关回调函数为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽构造失败时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_Hashmap_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_Hashmap_Destroy (FAST_HashmapHandle handle)
```
 
**描述**
 
销毁给定哈希表。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 要销毁的哈希表句柄。 |
 
 
**返回：**
 
无
 
**注解：**
 
此函数不释放与键或值相关的内存。调用者保留所有键和值资源的所有权，必须显式释放它们以避免内存泄漏。
 
  

#### HMS_FAST_Hashmap_Erase()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Hashmap_Erase (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapKeyPtr* originKey, FAST_HashmapValuePtr* originValue)
```
 
**描述**
 
从哈希表中按键删除条目。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要删除的条目的键。 |
| originKey | 将被删除的键的指针，仅在成功时有效，如果不需要请传入NULL。 |
| originValue | 将被删除的值的指针，仅在成功时有效，如果不需要请传入NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle或key为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中不存在匹配的键时，返回[FAST_ERROR_CODE_KEY_NOT_EXISTS](#fast_errorcode-1)。
 
**注解：**
 
内存不会自动释放，用户必须使用**originKey**和**originValue**手动释放。
 
  

#### HMS_FAST_Hashmap_EraseIf()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
size_t HMS_FAST_Hashmap_EraseIf (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc freeFunc, void* freeCtx)
```
 
**描述**
 
删除满足给定条件的所有元素。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| condFunc | 自定义的删除条件回调函数。 |
| condCtx | 条件回调函数的上下文。 |
| freeFunc | 开发者定义的内存释放回调函数，可为NULL。 |
| freeCtx | 内存释放回调函数的上下文。 |
 
 
**返回：**
 
成功删除的元素数量。
 
  

#### HMS_FAST_Hashmap_Find()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Hashmap_Find (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr* value)
```
 
**描述**
 
检索与给定键关联的值。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要查找的键。 |
| value | 存储检索值的指针。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle、key或value为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中不存在匹配的键时，返回[FAST_ERROR_CODE_KEY_NOT_EXISTS](#fast_errorcode-1)。
 
  

#### HMS_FAST_Hashmap_Insert()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Hashmap_Insert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value, FAST_HashmapValuePtr* originValue)
```
 
**描述**
 
在哈希表中插入或更新键值对。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要插入或更新的键。 |
| value | 与键关联的值。 |
| originValue | 将被覆盖的值的指针，仅在返回FAST_ERROR_CODE_KEY_EXISTS时有效，如果不需要请传入NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中存在相同的键时，使用value覆盖已有的值并返回[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
**注解：**
 
- 如果键已存在，返回值将为[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)，其值将被覆盖。
- 调用者保留键和值内存的所有权。哈希表仅存储指针；不复制或管理内存。

 
  

#### HMS_FAST_Hashmap_Size()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
size_t HMS_FAST_Hashmap_Size (FAST_HashmapHandle handle)
```
 
**描述**
 
返回哈希表中当前存储的键值对数量。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
 
 
**返回：**
 
哈希表中的元素数量。
 
  

#### HMS_FAST_Hashmap_Traverse()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_Hashmap_Traverse (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc workFunc, void* workCtx)
```
 
**描述**
 
遍历哈希表，可选择过滤元素并应用工作函数。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| condFunc | 可选的条件函数；如果提供，仅当 condFunc 返回非零时才对条目调用 workFunc。传入 NULL 以对所有条目应用 workFunc。 |
| condCtx | 用户定义的上下文，允许用户供应 condFunc 在执行期间可能需要的自定义数据。 |
| workFunc | 对选定条目应用的函数。 |
| workCtx | 用户定义的上下文，允许用户供应 workFunc 在执行期间可能需要的自定义数据。 |
 
 
**返回：**
 
无
 
**注解：**
 
condFunc和workFunc都在内部锁下调用；避免在这些回调中阻塞或重新进入哈希表API。
 
  

#### HMS_FAST_Hashmap_TryInsert()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Hashmap_TryInsert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value)
```
 
**描述**
 
仅当键不存在时插入键值对。
 
**起始版本：** 26.0.0
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要插入的键。 |
| value | 与键关联的值。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当handle、key或value为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当哈希表中存在相同的键时，不执行任何操作并返回[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
**注解：**
 
调用者管理键和值内存的生命周期。
 
  

#### HMS_FAST_Algo_Sort()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Algo_Sort (HMS_FAST_SortData * data, HMS_FAST_Sort_CompFunc comp)
```
 
**描述**
 
使用用户提供的比较函数对任意类型数组进行完整排序。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。data->data不能为NULL，data->sizeOf必须大于0，data->length必须大于0。 |
| comp | 用户自定义的比较函数。不能为NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当data->sizeOf或data->length为0时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当data、data->data或comp为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_Algo_PartialSortAt()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Algo_PartialSortAt (HMS_FAST_SortData * data, size_t offset, size_t count, HMS_FAST_Sort_CompFunc comp)
```
 
**描述**
 
对数组进行原地部分排序，使指定区间[offset, offset + count)包含排序后对应位置的元素。
 
**功能说明：**
 
- 子数组[offset, offset+count)包含排序后的第offset个到第(offset+count-1)个元素，按升序排列。
- offset之前的所有元素小于子数组中的最小元素。
- offset+count之后的所有元素大于子数组中的最大元素。
- 子数组之外的元素不保证排序。

 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。与HMS_FAST_Algo_Sort要求相同。 |
| offset | 子数组的起始索引。 |
| count | 子数组的元素数量。 |
| comp | 用户自定义的比较函数。不能为NULL。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当data->sizeOf或data->length为0，或(offset+count)越界时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当data、data->data或comp为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。
 
  

#### HMS_FAST_Algo_NaturalSort()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Algo_NaturalSort (HMS_FAST_SortData * data, int32_t ascend)
```
 
**描述**
 
使用自然语言规则对UTF-8编码的C字符串数组进行排序。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。data->data不能为NULL，data->sizeOf必须大于0，data->length必须大于0。注意：data->sizeOf必须等于sizeof(char*)。 |
| ascend | 排序方向，非零为升序，零为降序。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当data->length为0，或data->sizeOf不等于sizeof(char*)时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当data或data->data为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当引用的三方库报错导致执行失败时，返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)。
 
**注解：**
 
- 此函数专门用于排序人类可读文本，要求data->data指向char*数组。
- 如果data->data不包含有效的null终止C字符串（如整数、结构体指针等），行为未定义，可能导致崩溃或内存损坏。
- 自然语言排序会将字符串中的数字序列视为数值进行比较，例如：file1, file2, file10, file20。

 
  

#### HMS_FAST_Algo_NaturalPartialSortAt()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FAST_ErrorCode HMS_FAST_Algo_NaturalPartialSortAt (HMS_FAST_SortData * data, size_t offset, size_t count, int32_t ascend)
```
 
**描述**
 
使用自然语言规则对UTF-8编码的C字符串数组进行部分排序，使指定区间[offset, offset + count)包含排序后对应位置的元素。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。与HMS_FAST_Algo_NaturalSort要求相同。 |
| offset | 子数组的起始索引。 |
| count | 子数组的元素数量。 |
| ascend | 排序方向，非零为升序，零为降序。 |
 
 
**返回：**
 
当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。
 
当data->length为0，或(offset+count)越界，或data->sizeOf不等于sizeof(char*)时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。
 
当data或data->data为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。
 
当引用的三方库报错导致执行失败时，返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Create (HMS_FAST_PerfHintConfigBuilder** builder)
```
 
**描述**
 
创建构建器实例。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 指向创建的构建器实例的引用。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
当内存不足，无法分配新实例时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NO_MEMORY](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_PerfHintConfigBuilder_Destroy (HMS_FAST_PerfHintConfigBuilder* builder)
```
 
**描述**
 
销毁构建器。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
 
 
  

#### HMS_FAST_PerfHintConfigBuilder_SetSceneType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneType sceneType)
```
 
**描述**
 
设置需要系统性能优化的场景类型。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| sceneType | 需要系统性能优化的场景类型。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_SetSceneState()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneState (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneState sceneState)
```
 
**描述**
 
设置需要系统性能优化的场景状态。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| sceneState | 需要系统性能优化的场景状态。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_SetDurationType()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetDurationType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_DurationType durationType)
```
 
**描述**
 
设置需要系统性能优化的持续时间选项。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| durationType | 需要系统性能优化的持续时间选项。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_SetTids()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetTids (HMS_FAST_PerfHintConfigBuilder* builder, int* tids, uint32_t tidsSize)
```
 
**描述**
 
设置需要优化的线程ID。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| tids | 需要优化的线程ID数组。 |
| tidsSize | 线程ID数组大小，最大长度为16。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfigBuilder_Build()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Build (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_PerfHintConfig** config)
```
 
**描述**
 
创建系统性能优化配置参数。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| config | 指向接收系统性能优化配置参数对象的指针。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当内存不足，无法分配新实例时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NO_MEMORY](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
 
  

#### HMS_FAST_PerfHintConfig_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void HMS_FAST_PerfHintConfig_Destroy (HMS_FAST_PerfHintConfig* config)
```
 
**描述**
 
销毁系统性能优化配置参数。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 配置参数实例指针。 |
 
 
  

#### HMS_FAST_SchedulingOptimization_PerfHint()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_SchedulingOptimization_PerfHint (const HMS_FAST_PerfHintConfig* config)
```
 
**描述**
 
系统性能优化接口。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向系统性能优化配置参数的指针。 |
 
 
**返回：**
 
当成功时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS](#hms_fast_schedulingoptimization_errorcode)。
 
当系统高负载时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_HIGH_SYSTEM_LOAD](#hms_fast_schedulingoptimization_errorcode)。
 
当省电模式时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_POWER_SAVING_MODE](#hms_fast_schedulingoptimization_errorcode)。
 
当低电量模式时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_LOW_POWER_MODE](#hms_fast_schedulingoptimization_errorcode)。
 
当非前台调用场景时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_NON_FRONTEND](#hms_fast_schedulingoptimization_errorcode)。
 
当间隔不满足要求时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INTERVAL](#hms_fast_schedulingoptimization_errorcode)。
 
当执行系统性能优化失败时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_EXECUTE_ERROR](#hms_fast_schedulingoptimization_errorcode)。
 
当参数无效时，返回[HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_INVALID_PARAM](#hms_fast_schedulingoptimization_errorcode)。
