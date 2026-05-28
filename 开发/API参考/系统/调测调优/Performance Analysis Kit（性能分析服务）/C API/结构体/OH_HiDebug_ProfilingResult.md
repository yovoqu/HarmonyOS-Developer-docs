# OH_HiDebug_ProfilingResult

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-oh-hidebug-profilingresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_HiDebug_ProfilingResult {...} OH_HiDebug_ProfilingResult
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

封装单次资源采集的结果。
 
**起始版本：** 24
 
**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
 
**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_HiDebug_ResourceType resourceType | 资源采集类型。 起始版本： 24 |
| const char* filePath | 资源采集结果文件路径。如果采集失败则为空值。 起始版本： 24 |
