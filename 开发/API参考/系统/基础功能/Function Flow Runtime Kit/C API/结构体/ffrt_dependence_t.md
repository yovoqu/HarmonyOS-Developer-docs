# ffrt_dependence_t

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-dependence-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ffrt_dependence_t
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

依赖数据项结构，用于描述任务间的单个依赖关系。
 
**起始版本：** 10
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
**所在头文件：** [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ffrt_dependence_type_t type | 依赖类型。 |
| const void* ptr | 依赖指针。数据依赖时指向数据，任务依赖时指向任务句柄。 |
