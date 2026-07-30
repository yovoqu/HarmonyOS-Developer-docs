# ffrt_fiber_t

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ffrt_fiber_t
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

纤程结构体，用于存储纤程执行上下文。
 
**起始版本：** 20
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
**所在头文件：** [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uintptr_t storage[ffrt_fiber_storage_size] | 纤程执行上下文的内部存储。请勿直接访问，通过ffrt_fiber_init初始化，通过ffrt_fiber_switch切换。 |
