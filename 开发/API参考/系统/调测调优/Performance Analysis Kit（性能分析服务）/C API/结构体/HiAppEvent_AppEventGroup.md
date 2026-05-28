# HiAppEvent_AppEventGroup

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HiAppEvent_AppEventGroup {...} HiAppEvent_AppEventGroup
```
  

##### 概述

一组事件信息，包含事件组的名称，按名称分组的单个事件信息数组，事件数组的长度。
 
**起始版本：** 12
 
**相关模块：** [HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent)
 
**所在头文件：** [hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| const char* name | 事件数组中相同的事件名称。 |
| const struct HiAppEvent_AppEventInfo* appEventInfos | 具有相同事件名称的事件数组。 |
| uint32_t infoLen | 具有相同事件名称的事件数组的长度。 |
