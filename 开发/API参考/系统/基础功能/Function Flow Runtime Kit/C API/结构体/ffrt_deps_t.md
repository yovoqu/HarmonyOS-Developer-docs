# ffrt_deps_t

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-deps-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ffrt_deps_t
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

依赖结构体，用于保存任务的依赖列表。
 
**起始版本：** 10
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
**所在头文件：** [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t len | 依赖数量。 |
| const ffrt_dependence_t* items | 依赖数据数组。 |
