# Rcp_OnBinaryReceiveCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

响应的二进制数据接收回调函数。可以通过[HMS_Rcp_SetRequestOnBinaryDataRecvCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestonbinarydatarecvcallback)为请求设置相应回调函数。
 
**起始版本：** 5.0.1(13)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_OnBinaryReceiveCallbackFunc callback | 请求过程中接收二进制数据的回调函数。 |
| void *usrObject | 用户定义的对象，在回调函数中使用。 |
 
 
  

##### 结构体成员变量说明

  

##### callback

```text
Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```
 
**描述**
 
二进制数据接收回调函数。
 
  

##### usrObject

```text
void* Rcp_OnBinaryReceiveCallback::usrObject
```
 
**描述**
 
用户定义的对象，在回调函数中使用。
