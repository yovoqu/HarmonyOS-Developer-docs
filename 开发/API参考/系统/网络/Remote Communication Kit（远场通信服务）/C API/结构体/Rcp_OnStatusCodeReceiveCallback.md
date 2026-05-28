# Rcp_OnStatusCodeReceiveCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_status_code_callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

响应的状态码接收回调函数。可以通过[HMS_Rcp_SetRequestOnStatusCodeReceiveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestonstatuscodereceivecallback)为请求设置相应回调函数。
 
**起始版本：** 6.0.1(21)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_OnStatusCodeReceiveCallbackFunc callback | 请求过程中接收响应状态码的回调函数。 |
| void *usrObject | 用户定义的对象，在回调函数中使用。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### callback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_OnStatusCodeReceiveCallbackFunc Rcp_OnStatusCodeReceiveCallback::callback
```
 
**描述**
 
响应状态码接收回调函数。
 
  

#### usrObject

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* Rcp_OnStatusCodeReceiveCallback::usrObject
```
 
**描述**
 
用户定义的对象，在回调函数中使用。
