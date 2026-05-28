# Rcp_OnProgressCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

收发时回调配置，在[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_OnProgressCallbackFunc callback | 收发过程中的回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### callback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_OnProgressCallbackFunc Rcp_OnProgressCallback::callback
```
 
**描述**
 
收发过程中的回调函数。
 
  

##### usrObject

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* Rcp_OnProgressCallback::usrObject
```
 
**描述**
 
用户定义的对象，在回调函数中使用。
