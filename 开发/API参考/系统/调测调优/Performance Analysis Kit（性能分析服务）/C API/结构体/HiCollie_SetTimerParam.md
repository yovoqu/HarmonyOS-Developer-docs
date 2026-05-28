# HiCollie_SetTimerParam

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-settimerparam
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HiCollie_SetTimerParam {...} HiCollie_SetTimerParam
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义OH_HiCollie_SetTimer函数的输入参数。
 
**起始版本：** 18
 
**相关模块：** [HiCollie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie)
 
**所在头文件：** [hicollie.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char *name | timer任务名称。 |
| unsigned int timeout | 任务超时时间阈值，单位：s。 |
| OH_HiCollie_Callback func | 超时发生时执行的回调函数。 |
| void *arg | 回调函数的参数。 |
| HiCollie_Flag flag | 超时发生时执行的动作，参考HiCollie_Flag。 |
