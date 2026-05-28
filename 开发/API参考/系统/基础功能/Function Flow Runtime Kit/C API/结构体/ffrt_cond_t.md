# ffrt_cond_t

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-cond-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ffrt_cond_t
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

FFRT条件变量结构。
 
**起始版本：** 10
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
**所在头文件：** [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t storage[(ffrt_cond_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)] | FFRT条件变量占用空间 |
