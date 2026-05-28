# Rcp_SessionListener

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_listener
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

关闭或取消会话事件的回调函数。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| void(* onClosed )(void) | 此函数在Rcp_Session关闭时调用此函数。 |
| void(* onCanceled )(void) | 此函数在Rcp_Session取消时调用此函数。 |
 
 
  

##### 结构体成员变量说明

  

##### onCanceled

```text
void(* Rcp_SessionListener::onCanceled) (void)
```
 
**描述**
 
此函数在[Rcp_Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_session)取消时调用此函数。
 
  

##### onClosed

```text
void(* Rcp_SessionListener::onClosed) (void)
```
 
**描述**
 
此函数在[Rcp_Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_session)关闭时调用此函数。
