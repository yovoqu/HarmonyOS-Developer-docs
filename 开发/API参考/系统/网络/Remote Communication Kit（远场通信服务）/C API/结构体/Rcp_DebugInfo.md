# Rcp_DebugInfo

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

描述存储在[Rcp_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_DebugEvent type | 调试事件类型。 |
| Rcp_Buffer data | 调试信息。 |
| struct Rcp_DebugInfo * next | 链式存储。指向下一个Rcp_DebugInfo。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### data

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Buffer Rcp_DebugInfo::data
```
 
**描述**
 
调试信息。
 
  

##### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_DebugInfo* Rcp_DebugInfo::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info)。
 
  

##### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_DebugEvent Rcp_DebugInfo::type
```
 
**描述**
 
调试事件类型。
