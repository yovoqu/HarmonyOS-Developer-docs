# Rcp_OnVoidCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_void_callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

在[Rcp_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的数据结束或已取消事件的回调配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_OnVoidCallbackFunc callback | DataEnd或Canceled事件回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |
 
 
  

##### 结构体成员变量说明

  

##### callback

```text
Rcp_OnVoidCallbackFunc Rcp_OnVoidCallback::callback
```
 
**描述**
 
DataEnd或Canceled事件回调函数。
 
  

##### usrObject

```text
void* Rcp_OnVoidCallback::usrObject
```
 
**描述**
 
用户定义的对象，在回调函数中使用。
