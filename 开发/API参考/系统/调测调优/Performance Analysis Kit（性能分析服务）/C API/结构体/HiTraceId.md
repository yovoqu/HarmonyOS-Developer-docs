# HiTraceId

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct HiTraceId {...} HiTraceId
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

HiTraceId定义。

**起始版本：** 12

**相关模块：** [HiTrace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace)

**所在头文件：** [trace.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trace-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

如果字节序为小端模式，结构体顺序如下表所示：


| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64_t valid | 1 | HiTraceId是否有效。 |
| uint64_t ver | 3 | HiTraceId的版本号。 |
| uint64_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64_t flags | 12 | HiTraceId的跟踪标志位。 |
| uint64_t spanId | 26 | HiTraceId的分支标识。 |
| uint64_t parentSpanId | 26 | HiTraceId的父分支标识。 |


如果字节序为大端模式，结构体顺序如下表所示：


| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64_t ver | 3 | HiTraceId的版本号。 |
| uint64_t valid | 1 | HiTraceId是否有效。 |
| uint64_t parentSpanId | 26 | HiTraceId的父分支标识。 |
| uint64_t spanId | 26 | HiTraceId的分支标识。 |
| uint64_t flags | 12 | HiTraceId的跟踪标志位。 |
