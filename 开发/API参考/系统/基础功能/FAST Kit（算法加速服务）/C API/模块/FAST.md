# FAST

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。

**起始版本：** 6.0.2(22)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。


### 文件
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [fast_ads_segment_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-segment-map-8h) | 线段表相关数据结构及函数定义。 |
| [fast_ads_concurrent_hashmap.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-concurrent-hashmap-8h) | 并发哈希表相关数据结构及函数定义。 |
| [fast_common_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-common-def-8h) | FAST Kit错误码等类型的公共定义。 |
| [fast_dsp_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h) | 数字信号处理（DSP）通用数据结构和工具函数定义。 |
| [fast_solver_rect_partition.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h) | 矩形划分求解器相关数据结构及函数定义。 |


### 结构体
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| struct  [FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) | 定义矩形的数据结构。 |
| struct  [FAST_SplitComplex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplex) | 定义单精度浮点复数信号的数据结构（分离格式）。 |
| struct  [FAST_SplitComplexD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplexd) | 定义双精度浮点复数信号的数据结构（分离格式）。 |
| struct  [FAST_BiquadCoefficients](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients) | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct  [FAST_BiquadCoefficientsD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficientsd) | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct  [FAST_BiquadState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate) | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct  [FAST_BiquadStateD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstated) | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct  [FAST_Biquadm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadm) | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct  [FAST_BiquadmD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadmd) | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |


### 类型定义
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| typedef enum [FAST_SegmentMapQueryType](#fast_segmentmapquerytype-1) [FAST_SegmentMapQueryType](#fast_segmentmapquerytype) | 线段表支持的查询操作类型。 |
| typedef enum [FAST_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) [FAST_SegmentMapUpdateType](#fast_segmentmapupdatetype) | 线段表支持的更新操作类型。 |
| typedef struct [FAST_SegmentMapConfig](#fast_segmentmapconfig) [FAST_SegmentMapConfig](#fast_segmentmapconfig) | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void * [FAST_SegmentMapHandle](#fast_segmentmaphandle) | 线段表的句柄。 |
| typedef enum [FAST_ErrorCode](#fast_errorcode-1) [FAST_ErrorCode](#fast_errorcode) | FAST Kit的错误码。 |
| typedef struct [FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) [FAST_Rect](#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST_RectPartitionConfig](#fast_rectpartitionconfig) [FAST_RectPartitionConfig](#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |
| typedef struct [FAST_SplitComplex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplex) [FAST_SplitComplex](#fast_splitcomplex) | 单精度浮点复数信号结构体。 |
| typedef struct [FAST_SplitComplexD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-splitcomplexd) [FAST_SplitComplexD](#fast_splitcomplexd) | 双精度浮点复数信号结构体。 |
| typedef struct [FAST_BiquadCoefficients](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients) [FAST_BiquadCoefficients](#fast_biquadcoefficients) | 单精度二阶IIR滤波器系数。 |
| typedef struct [FAST_BiquadCoefficientsD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficientsd) [FAST_BiquadCoefficientsD](#fast_biquadcoefficientsd) | 双精度二阶IIR滤波器系数。 |
| typedef struct [FAST_BiquadState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate) [FAST_BiquadState](#fast_biquadstate) | 单精度二阶IIR滤波器状态。 |
| typedef struct [FAST_BiquadStateD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstated) [FAST_BiquadStateD](#fast_biquadstated) | 双精度二阶IIR滤波器状态。 |
| typedef struct [FAST_Biquadm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadm) [FAST_Biquadm](#fast_biquadm) | 单精度多通道多节IIR滤波器组。 |
| typedef struct [FAST_BiquadmD](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadmd) [FAST_BiquadmD](#fast_biquadmd) | 双精度多通道多节IIR滤波器组。 |


### 枚举
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [FAST_SegmentMapQueryType](#fast_segmentmapquerytype-1) { FAST_SEGMENTMAP_QUERY_TYPE_SUM = 0, FAST_SEGMENTMAP_QUERY_TYPE_MIN = 1, FAST_SEGMENTMAP_QUERY_TYPE_MAX = 2 } | 线段表支持的查询操作类型。 |
| [FAST_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) { FAST_SEGMENTMAP_UPDATE_TYPE_SET = 0, FAST_SEGMENTMAP_UPDATE_TYPE_ADD = 1, FAST_SEGMENTMAP_UPDATE_TYPE_SUB = 2 } | 线段表支持的更新操作类型。 |
| [FAST_ErrorCode](#fast_errorcode-1) { FAST_ERROR_CODE_SUCCESS = 1023100000, FAST_ERROR_CODE_FAIL = 1023100001, FAST_ERROR_CODE_ILLEGAL_INPUT = 1023100002, FAST_ERROR_CODE_INVALID_PTR = 1023100003, FAST_ERROR_CODE_OOM = 1023199001 } | FAST Kit的错误码。 |


### 函数
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_CreateConfig](#hms_fast_segmentmap_createconfig) ([FAST_SegmentMapConfig](#fast_segmentmapconfig) **config) | 创建线段表不透明配置实例。 |
| FAST_EXPORT void [HMS_FAST_SegmentMap_DestroyConfig](#hms_fast_segmentmap_destroyconfig) ([FAST_SegmentMapConfig](#fast_segmentmapconfig) *config) | 销毁线段表的不透明配置实例并释放内存。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_SetQueryType](#hms_fast_segmentmap_setquerytype) ([FAST_SegmentMapConfig](#fast_segmentmapconfig) *config, [FAST_SegmentMapQueryType](#fast_segmentmapquerytype-1) type) | 设置线段表不透明配置中的查询类型。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_SetUpdateType](#hms_fast_segmentmap_setupdatetype) ([FAST_SegmentMapConfig](#fast_segmentmapconfig) *config, [FAST_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) type) | 设置线段表不透明配置中的更新类型。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_Create](#hms_fast_segmentmap_create) ([FAST_SegmentMapHandle](#fast_segmentmaphandle) *handle, size_t size, const int32_t *array, [FAST_SegmentMapConfig](#fast_segmentmapconfig) *config) | 创建线段表。 |
| FAST_EXPORT void [HMS_FAST_SegmentMap_Destroy](#hms_fast_segmentmap_destroy) ([FAST_SegmentMapHandle](#fast_segmentmaphandle) handle) | 销毁线段表实例。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_Update](#hms_fast_segmentmap_update) ([FAST_SegmentMapHandle](#fast_segmentmaphandle) handle, size_t left, size_t right, int32_t value) | 更新线段表的区间。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_SegmentMap_Query](#hms_fast_segmentmap_query) ([FAST_SegmentMapHandle](#fast_segmentmaphandle) handle, size_t left, size_t right, int32_t *result) | 查询线段表的区间。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_RectPartition_CreateConfig](#hms_fast_rectpartition_createconfig) ([FAST_RectPartitionConfig](#fast_rectpartitionconfig) **config) | 创建矩形划分求解器的不透明配置。 |
| FAST_EXPORT void [HMS_FAST_RectPartition_DestroyConfig](#hms_fast_rectpartition_destroyconfig) ([FAST_RectPartitionConfig](#fast_rectpartitionconfig) *config) | 销毁矩形划分求解器的不透明配置。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_RectPartition_SetAlgo](#hms_fast_rectpartition_setalgo) ([FAST_RectPartitionConfig](#fast_rectpartitionconfig) *config, const char *name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_RectPartition_Solve](#hms_fast_rectpartition_solve) ([FAST_RectPartitionConfig](#fast_rectpartitionconfig) *config, size_t size, const [FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) *origin, [FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) *result, size_t *resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。 说明： 1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST_ERROR_CODE_ILLEGAL_INPUT。 2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |
| float [HMS_FAST_DSP_Maxmgv](#hms_fast_dsp_maxmgv) (const float *input, size_t stride, size_t length) | 计算步长实值向量中的最大幅值（单精度）。 |
| double [HMS_FAST_DSP_MaxmgvD](#hms_fast_dsp_maxmgvd) (const double *input, size_t stride, size_t length) | 计算步长实值向量中的最大幅值（双精度）。 |
| void [HMS_FAST_DSP_Maxvi](#hms_fast_dsp_maxvi) (const float *input, size_t stride, size_t length, float *value, size_t *index) | 查找步长实值向量中的最大值及其索引（单精度）。 |
| void [HMS_FAST_DSP_MaxviD](#hms_fast_dsp_maxvid) (const double *input, size_t stride, size_t length, double *value, size_t *index) | 查找步长实值向量中的最大值及其索引（双精度）。 |
| float [HMS_FAST_DSP_Sve](#hms_fast_dsp_sve) (const float *input, size_t stride, size_t length) | 计算步长实值向量的和（单精度）。 |
| double [HMS_FAST_DSP_SveD](#hms_fast_dsp_sved) (const double *input, size_t stride, size_t length) | 计算步长实值向量的和（双精度）。 |
| float [HMS_FAST_DSP_Svemg](#hms_fast_dsp_svemg) (const float *input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS_FAST_DSP_SvemgD](#hms_fast_dsp_svemgd) (const double *input, size_t stride, size_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS_FAST_DSP_Meamgv](#hms_fast_dsp_meamgv) (const float *input, size_t stride, size_t length) | 计算步长实值向量绝对值的均值（单精度）。 |
| double [HMS_FAST_DSP_MeamgvD](#hms_fast_dsp_meamgvd) (const double *input, size_t stride, size_t length) | 计算步长实值向量绝对值的均值（双精度）。 |
| float [HMS_FAST_DSP_Dotpr](#hms_fast_dsp_dotpr) (const float *inputA, size_t strideA, const float *inputB, size_t strideB, size_t length) | 计算两个步长实值向量的点积（单精度）。 |
| double [HMS_FAST_DSP_DotprD](#hms_fast_dsp_dotprd) (const double *inputA, size_t strideA, const double *inputB, size_t strideB, size_t length) | 计算两个步长实值向量的点积（双精度）。 |
| void [HMS_FAST_DSP_Vsbsm](#hms_fast_dsp_vsbsm) (const float *inputA, size_t strideA, const float *inputB, size_t strideB, float scalar, float *outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（单精度）。 |
| void [HMS_FAST_DSP_VsbsmD](#hms_fast_dsp_vsbsmd) (const double *inputA, size_t strideA, const double *inputB, size_t strideB, double scalar, double *outputC, size_t strideC, size_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * scalar（双精度）。 |
| void [HMS_FAST_DSP_Ctoz](#hms_fast_dsp_ctoz) (const float *input, size_t strideInput, [FAST_SplitComplex](#fast_splitcomplex) *output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS_FAST_DSP_CtozD](#hms_fast_dsp_ctozd) (const double *input, size_t strideInput, [FAST_SplitComplexD](#fast_splitcomplexd) *output, size_t strideOutput, size_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS_FAST_DSP_Ztoc](#hms_fast_dsp_ztoc) (const [FAST_SplitComplex](#fast_splitcomplex) *input, size_t strideInput, float *output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS_FAST_DSP_ZtocD](#hms_fast_dsp_ztocd) (const [FAST_SplitComplexD](#fast_splitcomplexd) *input, size_t strideInput, double *output, size_t strideOutput, size_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetActiveFilters](#hms_fast_biquadm_setactivefilters) ([FAST_Biquadm](#fast_biquadm) *filter, const uint8_t *activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetActiveFiltersD](#hms_fast_biquadm_setactivefiltersd) ([FAST_BiquadmD](#fast_biquadmd) *filter, const uint8_t *activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetCoeffSingle](#hms_fast_biquadm_setcoeffsingle) ([FAST_Biquadm](#fast_biquadm) *filter, const float *coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetCoeffDouble](#hms_fast_biquadm_setcoeffdouble) ([FAST_Biquadm](#fast_biquadm) *filter, const double *coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetCoeffSingleD](#hms_fast_biquadm_setcoeffsingled) ([FAST_BiquadmD](#fast_biquadmd) *filter, const float *coeff, size_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_SetCoeffDoubleD](#hms_fast_biquadm_setcoeffdoubled) ([FAST_BiquadmD](#fast_biquadmd) *filter, const double *coeff, size_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_Create](#hms_fast_biquadm_create) (size_t numChannels, size_t numSections, size_t maxFrames, [FAST_Biquadm](#fast_biquadm) **filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm_CreateD](#hms_fast_biquadm_created) (size_t numChannels, size_t numSections, size_t maxFrames, [FAST_BiquadmD](#fast_biquadmd) **filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS_FAST_Biquadm_Destroy](#hms_fast_biquadm_destroy) ([FAST_Biquadm](#fast_biquadm) *filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS_FAST_Biquadm_DestroyD](#hms_fast_biquadm_destroyd) ([FAST_BiquadmD](#fast_biquadmd) *filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_Biquadm](#hms_fast_biquadm) ([FAST_Biquadm](#fast_biquadm) *filter, const float **input, const size_t strideInput, float **output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_BiquadmD](#hms_fast_biquadmd) ([FAST_BiquadmD](#fast_biquadmd) *filter, const double **input, const size_t strideInput, double **output, const size_t strideOutput, size_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_ConcurrentHashmap_Create](#hms_fast_concurrenthashmap_create) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, [HMS_FAST_ConcurrentHashmap_HashFunc](#hms_fast_concurrenthashmap_hashfunc) hasher, [HMS_FAST_ConcurrentHashmap_KeyEqualFunc](#hms_fast_concurrenthashmap_keyequalfunc) equaler, float maxLoadFac, size_t numShards) | 使用给定配置创建并发哈希表。 |
| FAST_EXPORT void [HMS_FAST_ConcurrentHashmap_Destroy](#hms_fast_concurrenthashmap_destroy) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle) | 销毁指定并发哈希表。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_ConcurrentHashmap_Insert](#hms_fast_concurrenthashmap_insert) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, const [FAST_ConcurrentHashmapKeyPtr](#fast_concurrenthashmapkeyptr) key, const [FAST_ConcurrentHashmapValuePtr](#fast_concurrenthashmapvalueptr) value, [FAST_ConcurrentHashmapValuePtr](#fast_concurrenthashmapvalueptr)* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_ConcurrentHashmap_Find](#hms_fast_concurrenthashmap_find) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, const [FAST_ConcurrentHashmapKeyPtr](#fast_concurrenthashmapkeyptr) key, [FAST_ConcurrentHashmapValuePtr](#fast_concurrenthashmapvalueptr)* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_ConcurrentHashmap_Erase](#hms_fast_concurrenthashmap_erase) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, const [FAST_ConcurrentHashmapKeyPtr](#fast_concurrenthashmapkeyptr) key, [FAST_ConcurrentHashmapKeyPtr](#fast_concurrenthashmapkeyptr)* originKey, [FAST_ConcurrentHashmapValuePtr](#fast_concurrenthashmapvalueptr)* originValue) | 在给定哈希表中删除输入的键，并将键和值分别保存在originKey和originValue中。 |
| FAST_EXPORT [FAST_ErrorCode](#fast_errorcode-1) [HMS_FAST_ConcurrentHashmap_TryInsert](#hms_fast_concurrenthashmap_tryinsert) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, const [FAST_ConcurrentHashmapKeyPtr](#fast_concurrenthashmapkeyptr) key, const [FAST_ConcurrentHashmapValuePtr](#fast_concurrenthashmapvalueptr) value) | 将给定的键值对插入并发哈希表中，如果键已经存在，则不执行任何操作。 |
| FAST_EXPORT size_t [HMS_FAST_ConcurrentHashmap_Size](#hms_fast_concurrenthashmap_size) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle) | 返回给定哈希表当前的元素个数。 |
| FAST_EXPORT void [HMS_FAST_ConcurrentHashmap_Clear](#hms_fast_concurrenthashmap_clear) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle) | 清空给定哈希表中维护的所有元素。 |
| FAST_EXPORT size_t [HMS_FAST_ConcurrentHashmap_EraseIf](#hms_fast_concurrenthashmap_eraseif) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, [HMS_FAST_ConcurrentHashmap_HookFunc](#hms_fast_concurrenthashmap_hookfunc) condFunc, void* condCtx, [HMS_FAST_ConcurrentHashmap_HookFunc](#hms_fast_concurrenthashmap_hookfunc) freeFunc, void* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。 |
| FAST_EXPORT void [HMS_FAST_ConcurrentHashmap_Traverse](#hms_fast_concurrenthashmap_traverse) ([FAST_ConcurrentHashmap](#fast_concurrenthashmaphandle)* handle, [HMS_FAST_ConcurrentHashmap_HookFunc](#hms_fast_concurrenthashmap_hookfunc) condFunc, void* condCtx, [HMS_FAST_ConcurrentHashmap_HookFunc](#hms_fast_concurrenthashmap_hookfunc) workFunc, void* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。 |


## 类型定义说明
**支持设备：** Phone / PC/2in1 / Tablet


### FAST_ErrorCode
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef enum FAST_ErrorCode FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)


### FAST_Rect
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_Rect FAST_Rect
```

**描述**

定义矩形的数据结构。

**起始版本：** 6.0.2(22)


### FAST_RectPartitionConfig
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig
```

**描述**

矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。

**起始版本：** 6.0.2(22)


### FAST_SegmentMapConfig
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig
```

**描述**

线段表的不透明配置（Opaque Configuration）。

**起始版本：** 6.0.2(22)


### FAST_SegmentMapHandle
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef void* FAST_SegmentMapHandle
```

**描述**

线段表的句柄。

**起始版本：** 6.0.2(22)


### FAST_SegmentMapQueryType
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType
```

**描述**

线段表数据结构支持的区间查询操作类型。

**起始版本：** 6.0.2(22)


### FAST_SegmentMapUpdateType
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType
```

**描述**

线段表数据结构支持的区间更新操作类型。

**起始版本：** 6.0.2(22)


### FAST_ConcurrentHashmapHandle
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef void* FAST_ConcurrentHashmapHandle
```

**描述**

并发哈希表的句柄。

**起始版本：** 6.1.1(24)


### FAST_ConcurrentHashmapKeyPtr
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef void* FAST_ConcurrentHashmapKeyPtr
```

**描述**

并发哈希表的键指针。

**起始版本：** 6.1.1(24)


### FAST_ConcurrentHashmapValuePtr
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef void* FAST_ConcurrentHashmapValuePtr
```

**描述**

并发哈希表的值指针。

**起始版本：** 6.1.1(24)


### HMS_FAST_ConcurrentHashmap_HashFunc
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef uint64_t (*HMS_FAST_ConcurrentHashmap_HashFunc)(const FAST_ConcurrentHashmapKeyPtr key)
```

**描述**

并发哈希表的哈希值计算回调函数类型。

**起始版本：** 6.1.1(24)


### HMS_FAST_ConcurrentHashmap_KeyEqualFunc
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef int32_t (*HMS_FAST_ConcurrentHashmap_KeyEqualFunc)(
const FAST_ConcurrentHashmapKeyPtr leftKey,
const FAST_ConcurrentHashmapKeyPtr rightKey
)
```

**描述**

并发哈希表的键比较回调函数类型。

**起始版本：** 6.1.1(24)


### HMS_FAST_ConcurrentHashmap_HookFunc
**支持设备：** Phone / PC/2in1 / Tablet


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


### FAST_SplitComplex
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_SplitComplex FAST_SplitComplex
```

**描述**

定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

**起始版本：** 6.1.1(24)


### FAST_SplitComplexD
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_SplitComplexD FAST_SplitComplexD
```

**描述**

定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

**起始版本：** 6.1.1(24)


### FAST_BiquadCoefficients
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_BiquadCoefficients FAST_BiquadCoefficients
```

**描述**

定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。

**起始版本：** 6.1.1(24)


### FAST_BiquadCoefficientsD
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_BiquadCoefficientsD FAST_BiquadCoefficientsD
```

**描述**

定义双精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。

**起始版本：** 6.1.1(24)


### FAST_BiquadState
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_BiquadState FAST_BiquadState
```

**描述**

定义单精度二阶IIR滤波器节的状态变量。

**起始版本：** 6.1.1(24)


### FAST_BiquadStateD
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_BiquadStateD FAST_BiquadStateD
```

**描述**

定义双精度二阶IIR滤波器节的状态变量。

**起始版本：** 6.1.1(24)


### FAST_Biquadm
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_Biquadm FAST_Biquadm
```

**描述**

定义单精度多通道、多节二阶IIR滤波器组的数据结构。

**起始版本：** 6.1.1(24)


### FAST_BiquadmD
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct FAST_BiquadmD FAST_BiquadmD
```

**描述**

定义双精度多通道、多节二阶IIR滤波器组的数据结构。

**起始版本：** 6.1.1(24)


## 枚举类型说明
**支持设备：** Phone / PC/2in1 / Tablet


### FAST_ErrorCode
**支持设备：** Phone / PC/2in1 / Tablet


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


### FAST_SegmentMapQueryType
**支持设备：** Phone / PC/2in1 / Tablet


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


### FAST_SegmentMapUpdateType
**支持设备：** Phone / PC/2in1 / Tablet


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


## 函数说明
**支持设备：** Phone / PC/2in1 / Tablet


### HMS_FAST_RectPartition_CreateConfig()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig ** config)
```

**描述**

创建矩形划分求解器的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| config | 指向矩形划分求解器不透明配置[FAST_RectPartitionConfig](#fast_rectpartitionconfig)的指针。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。


### HMS_FAST_RectPartition_DestroyConfig()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig * config)
```

**描述**

销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| config | 待销毁的矩形划分求解器的不透明配置[FAST_RectPartitionConfig](#fast_rectpartitionconfig)。 |


### HMS_FAST_RectPartition_SetAlgo()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig * config, const char * name )
```

**描述**

设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为O(N logN)。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| config | 待设置的矩形划分求解器的不透明配置[FAST_RectPartitionConfig](#fast_rectpartitionconfig)。 |
| name | 矩形求解器使用的算法名称。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当config或name为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当算法不支持时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。


### HMS_FAST_RectPartition_Solve()
**支持设备：** Phone / PC/2in1 / Tablet


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
| size | 待划分的矩形[FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)数量。 |
| origin | 待划分的矩形[FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)源数组。 |
| result | 由矩形划分求解器得到的[FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)结果，在调用函数之前需要初始化该结果数组，大小需要和源数组相等，否则可能导致溢出。 |
| resultSize | 划分之后的[FAST_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)数量。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当入参指针为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当输入非法时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)，如矩形存在相交。

当算法求解失败时，返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)。

**注解：**


1. 当选择“SweepLineAlgo”时，不应该返回[FAST_ERROR_CODE_FAIL](#fast_errorcode-1)，此处仅作为预防性设置。


### HMS_FAST_SegmentMap_Create()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle * handle, size_t size, const int32_t * array, FAST_SegmentMapConfig * config )
```

**描述**

创建线段表。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| handle | 指向线段表句柄[FAST_SegmentMapHandle](#fast_segmentmaphandle)的指针。 |
| size | 底层数组的大小（元素数量）。 |
| array | 可选；用于初始化线段表的底层数组。如果为NULL，则线段表中的元素均初始化为0，否则数组大小必须与参数size保持一致。 |
| config | 线段表的不透明配置[FAST_SegmentMapConfig](#fast_segmentmapconfig)，若该参数为NULL或未配置，默认查询类型为[FAST_SEGMENTMAP_QUERY_TYPE_SUM](#fast_segmentmapquerytype-1)、更新类型为[FAST_SEGMENTMAP_UPDATE_TYPE_SET](#fast_segmentmapupdatetype-1)。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当config或handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。


### HMS_FAST_SegmentMap_CreateConfig()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig ** config)
```

**描述**

创建线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| config | 指向线段表不透明配置[FAST_SegmentMapConfig](#fast_segmentmapconfig)的指针。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。


### HMS_FAST_SegmentMap_Destroy()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle)
```

**描述**

销毁线段表实例。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| handle | 待销毁线段表句柄[FAST_SegmentMapHandle](#fast_segmentmaphandle)。 |


### HMS_FAST_SegmentMap_DestroyConfig()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig * config)
```

**描述**

销毁线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**


| 名称 | 描述 |
| --- | --- |
| config | 待销毁线段表不透明配置[FAST_SegmentMapConfig](#fast_segmentmapconfig)。 |


### HMS_FAST_SegmentMap_Query()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_SegmentMap_SetQueryType()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_SegmentMap_SetUpdateType()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_SegmentMap_Update()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_Create()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_CreateD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_Destroy()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_DestroyD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_SetCoeffSingle()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_SetCoeffDouble()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_SetCoeffSingleD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_SetCoeffDoubleD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_Biquadm_SetActiveFilters()
**支持设备：** Phone / PC/2in1 / Tablet


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
| activeMask | 布尔数组（大小为 filter-&gt;numSections）；非零表示激活。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。


### HMS_FAST_Biquadm_SetActiveFiltersD()
**支持设备：** Phone / PC/2in1 / Tablet


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
| activeMask | 布尔数组（大小为 filter-&gt;numSections）；非零表示激活。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当filter未初始化时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。


### HMS_FAST_Biquadm()
**支持设备：** Phone / PC/2in1 / Tablet


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
| input | 输入通道指针数组（大小为 filter-&gt;numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter-&gt;numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter-&gt;maxFrames）。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当filter、coeff或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当filter未初始化或length超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。


### HMS_FAST_BiquadmD()
**支持设备：** Phone / PC/2in1 / Tablet


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
| input | 输入通道指针数组（大小为 filter-&gt;numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter-&gt;numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter-&gt;maxFrames）。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当filter、coeff或output为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当filter未初始化或length超出范围时，返回[FAST_ERROR_CODE_ILLEGAL_INPUT](#fast_errorcode-1)。


### HMS_FAST_DSP_Maxmgv()
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HMS_FAST_DSP_Maxmgv (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量中的最大幅值（单精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |


**返回：**

向量中的最大绝对值。如果length为0，则返回0.0f。


### HMS_FAST_DSP_MaxmgvD()
**支持设备：** Phone / PC/2in1 / Tablet


```text
double HMS_FAST_DSP_MaxmgvD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量中的最大幅值（双精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |


**返回：**

向量中的最大绝对值。如果length为0，则返回0.0。


### HMS_FAST_DSP_Maxvi()
**支持设备：** Phone / PC/2in1 / Tablet


```text
void HMS_FAST_DSP_Maxvi (const float * input, size_t stride, size_t length, float * value, size_t * index)
```

**描述**

查找步长实值向量中的最大值及其索引（单精度）。

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


### HMS_FAST_DSP_MaxviD()
**支持设备：** Phone / PC/2in1 / Tablet


```text
void HMS_FAST_DSP_MaxviD (const double * input, size_t stride, size_t length, double * value, size_t * index)
```

**描述**

查找步长实值向量中的最大值及其索引（双精度）。

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


### HMS_FAST_DSP_Sve()
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HMS_FAST_DSP_Sve (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量的和（单精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |


**返回：**

input[i]的和。如果length为0，则返回0.0f。


### HMS_FAST_DSP_SveD()
**支持设备：** Phone / PC/2in1 / Tablet


```text
double HMS_FAST_DSP_SveD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量的和（双精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |


**返回：**

input[i]的和。如果length为0，则返回0.0。


### HMS_FAST_DSP_Svemg()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_SvemgD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_Meamgv()
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HMS_FAST_DSP_Meamgv (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量绝对值的均值（单精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |


**返回：**

|input[i]|的均值。如果length为0，则返回0.0f。


### HMS_FAST_DSP_MeamgvD()
**支持设备：** Phone / PC/2in1 / Tablet


```text
double HMS_FAST_DSP_MeamgvD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实值向量绝对值的均值（双精度）。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |


**返回：**

|input[i]|的均值。如果length为0，则返回0.0。


### HMS_FAST_DSP_Dotpr()
**支持设备：** Phone / PC/2in1 / Tablet


```text
float HMS_FAST_DSP_Dotpr (const float * inputA, size_t strideA, const float * inputB, size_t strideB, size_t length)
```

**描述**

计算两个步长实值向量的点积（单精度）。

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


### HMS_FAST_DSP_DotprD()
**支持设备：** Phone / PC/2in1 / Tablet


```text
double HMS_FAST_DSP_DotprD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, size_t length)
```

**描述**

计算两个步长实值向量的点积（双精度）。

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


### HMS_FAST_DSP_Vsbsm()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_VsbsmD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_Ctoz()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_CtozD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_Ztoc()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_DSP_ZtocD()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_Create()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create(
FAST_ConcurrentHashmapHandle* handle,
HMS_FAST_ConcurrentHashmap_HashFunc hasher,
HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler,
double maxLoadFac,
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


### HMS_FAST_ConcurrentHashmap_Destroy()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_Insert()
**支持设备：** Phone / PC/2in1 / Tablet


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


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当handle为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当哈希表中存在相同的键时，使用value覆盖已有的值并返回[FAST_ERROR_CODE_KEY_EXISTS](#fast_errorcode-1)。

当内存耗尽时，返回[FAST_ERROR_CODE_OOM](#fast_errorcode-1)。


### HMS_FAST_ConcurrentHashmap_Find()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_Erase()
**支持设备：** Phone / PC/2in1 / Tablet


```text
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase(
FAST_ConcurrentHashmapHandle handle,
const FAST_ConcurrentHashmapKeyPtr key,
FAST_ConcurrentHashmapKeyPtr* originKey,
FAST_ConcurrentHashmapValuePtr* originValue
)
```

**描述**

在并发哈希表中删除给定的键及其对应的值，并将其值保存在originalKey和originalValue中以便于开发者进行内存管理; 实际使用时也可根据需求将originalKey或originalValue设为nullptr，此时则不会将键或值的地址返回。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待删除的键指针。 |
| originKey | 用于返回哈希表中保存的键的指针，可为nullptr。 |
| originValue | 用于返回哈希表中保存的值得指针，可为nullptr。 |


**返回：**

当成功时，返回[FAST_ERROR_CODE_SUCCESS](#fast_errorcode-1)。

当handle或key为NULL时，返回[FAST_ERROR_CODE_INVALID_PTR](#fast_errorcode-1)。

当哈希表中不存在匹配的键时，返回[FAST_ERROR_CODE_KEY_NOT_EXISTS](#fast_errorcode-1)。


### HMS_FAST_ConcurrentHashmap_TryInsert()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_Size()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_Clear()
**支持设备：** Phone / PC/2in1 / Tablet


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


### HMS_FAST_ConcurrentHashmap_EraseIf()
**支持设备：** Phone / PC/2in1 / Tablet


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

遍历哈希表并删除所有符合给定条件的键值对，同时使用开发者定义的freeFunc释放键值对的内存；实际使用时freeFunc可为nullptr，此时要求开发者另行完成内存管理动作。注意：请避免在condFunc和freeFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的删除条件回调函数。 |
| condCtx | 条件回调函数的上下文。 |
| freeFunc | 开发者定义的内存释放回调函数，可为nullptr。 |
| freeCtx | 内存释放回调函数的上下文。 |


**返回：**

完成删除操作的元素个数。


### HMS_FAST_ConcurrentHashmap_Traverse()
**支持设备：** Phone / PC/2in1 / Tablet


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

遍历哈希表并对所有符合开发者condFunc的键值对执行workFunc中的修改；如果condFunc为nullptr，则对于表中存在的所有键值对都将执行开发者定义的workFunc。注意：请避免在condFunc和workFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。

**起始版本：** 6.1.1(24)

**参数：**


| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的条件回调函数，可为nullptr。 |
| condCtx | 回调函数的上下文。 |
| workFunc | 开发者定义的修改回调函数。 |
| workCtx | 修改函数的上下文。 |
