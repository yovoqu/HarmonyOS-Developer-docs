# HiDebug_ThreadCpuUsage

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct HiDebug_ThreadCpuUsage {...} HiDebug_ThreadCpuUsage
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

应用程序所有线程的CPU使用率结构体定义。

**起始版本：** 12

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint32_t threadId | 线程ID。 |
| double cpuUsage | 线程CPU使用率百分比。 |
| struct [HiDebug_ThreadCpuUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage) *next | 下一个线程的使用率信息。 |
