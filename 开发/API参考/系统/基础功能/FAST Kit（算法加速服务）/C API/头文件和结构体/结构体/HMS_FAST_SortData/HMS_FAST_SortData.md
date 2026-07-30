# HMS_FAST_SortData

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--hms-fast-sortdata
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

描述待排序的连续内存数据块。
 
**系统能力：** SystemCapability.FAST.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)
 
**所在头文件：** [fast_utils_algorithm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-utils-algorithm-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| size_t sizeOf | 连续内存容器中单个元素的大小。 |
| size_t length | 连续内存容器中的元素个数。 |
| HMS_FAST_SortElementPtr data | 指向待排序的连续内存起始地址的指针。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### sizeOf

**支持设备：** Phone | PC/2in1 | Tablet

```text
size_t HMS_FAST_SortData::sizeOf
```
 
**描述**
 
data所指向的连续内存容器中单个元素的大小。
 
  

#### length

**支持设备：** Phone | PC/2in1 | Tablet

```text
size_t HMS_FAST_SortData::length
```
 
**描述**
 
data所指向的连续内存容器中的元素个数。
 
  

#### data

**支持设备：** Phone | PC/2in1 | Tablet

```text
HMS_FAST_SortElementPtr HMS_FAST_SortData::data
```
 
**描述**
 
指向待排序的连续内存起始地址的指针。
