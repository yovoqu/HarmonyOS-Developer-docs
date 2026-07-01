# Rcp_OnGetDataCallback

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_get_data_callback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

## Rcp_OnGetDataCallback
 
 

##### 概述

获取数据的回调。可以通过[HMS_Rcp_SetRequestGetDataCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestgetdatacallback)为请求设置相应回调函数。
 
**起始版本：** 26.0.0
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### [h2]成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_GetDataCallbackFunc callback | 请求过程中获取数据的回调函数。 |
| void *userObject | 用户定义的对象，在回调函数中使用。 |
 
 
  

##### 结构体成员变量说明

  

##### [h2]callback

```text
Rcp_GetDataCallbackFunc Rcp_OnGetDataCallback::callback
```
 
**描述**
 
获取数据的回调函数。
 
  

##### [h2]userObject

```text
void* Rcp_OnGetDataCallback::userObject
```
 
**描述**
 
用户定义的对象，在回调函数中使用。
