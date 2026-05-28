# JSVM_HeapStatistics

更新时间：2026-03-17 02:21:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-heapstatistics
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_HeapStatistics
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

用于保存有关JavaScript堆内存使用情况的统计信息。
 
**起始版本：** 12
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| size_t totalHeapSize | 总堆大小，单位KB。 |
| size_t totalHeapSizeExecutable | 可执行堆的总大小，单位KB。 |
| size_t totalPhysicalSize | 总的物理内存大小，单位KB。 |
| size_t totalAvailableSize | 总的可用内存大小，单位KB。 |
| size_t usedHeapSize | 已使用的堆大小，单位KB。 |
| size_t heapSizeLimit | 堆大小限制，单位KB。 |
| size_t mallocedMemory | 已分配内存的大小，单位KB。 |
| size_t externalMemory | 外部内存大小，单位KB。 |
| size_t peakMallocedMemory | 最大可分配内存的大小，单位KB。 |
| size_t numberOfNativeContexts | 表示当前活跃的native上下文的数量，该数值一直增加可能指示存在内存泄漏。 |
| size_t numberOfDetachedContexts | 表示已经脱离的上下文数量。 |
| size_t totalGlobalHandlesSize | 全局Handle的总大小，单位KB。 |
| size_t usedGlobalHandlesSize | 已经使用的全局Handle的大小，单位KB。 |
