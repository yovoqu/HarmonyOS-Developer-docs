# TransientTask_DelaySuspendInfo

更新时间：2026-04-10 09:55:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-delaysuspendinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct TransientTask_DelaySuspendInfo {...} TransientTask_DelaySuspendInfo
```
  

##### 概述

定义短时任务返回信息结构体。用于返回当前短时任务的任务ID和剩余时间。
 
**起始版本：** 13
 
**相关模块：** [TransientTask](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask)
 
**所在头文件：** [transient_task_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| int32_t requestId | 短时任务请求ID。 |
| int32_t actualDelayTime | 剩余时间（单位：毫秒）。 |
