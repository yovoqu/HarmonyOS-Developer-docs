# fast_utils_algorithm.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-utils-algorithm-8h
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

通用算法工具头文件，目前提供排序相关的数据结构和函数定义。
 
**引用文件：** <FASTKit/fast_utils_algorithm.h>
 
**库：** libfast_utils.so
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| struct HMS_FAST_SortData | 描述待排序的连续内存数据块。 |
 
 
  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef struct HMS_FAST_SortData HMS_FAST_SortData | 描述待排序的连续内存数据块。 |
| typedef void* HMS_FAST_SortElementPtr | 表示通用容器中单个元素的opaque pointer类型。 |
| typedef const void* HMS_FAST_SortElementConstPtr | 表示通用容器中单个元素的const opaque pointer类型。 |
| typedef int32_t(*HMS_FAST_Sort_CompFunc) (HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second) | 开发者自定义比较函数的回调函数指针类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| FAST_ErrorCode HMS_FAST_Algo_Sort (HMS_FAST_SortData *data, HMS_FAST_Sort_CompFunc comp) | 使用开发者提供的比较函数对任意类型数组进行完整排序。 |
| FAST_ErrorCode HMS_FAST_Algo_PartialSortAt (HMS_FAST_SortData *data, size_t offset, size_t count, HMS_FAST_Sort_CompFunc comp) | 对数组进行原地部分排序，使指定区间对应排序后的相应段。 |
| FAST_ErrorCode HMS_FAST_Algo_NaturalSort (HMS_FAST_SortData *data, int32_t ascend) | 使用自然语言规则对UTF-8字符串数组进行排序。 |
| FAST_ErrorCode HMS_FAST_Algo_NaturalPartialSortAt (HMS_FAST_SortData *data, size_t offset, size_t count, int32_t ascend) | 使用自然语言规则对UTF-8字符串数组进行部分排序，使指定区间对应排序后的相应段。 |
