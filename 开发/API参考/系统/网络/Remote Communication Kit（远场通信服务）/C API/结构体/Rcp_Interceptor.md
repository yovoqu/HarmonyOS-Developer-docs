# Rcp_Interceptor

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

异步拦截器。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t(* intercept )(Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback) | 指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### intercept

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t(* Rcp_Interceptor::intercept) (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback)
```
 
**描述**
 
指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。
 
**起始版本：** 5.0.0(12)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| request | 指向Rcp_Request的指针。 |
| next | 指向下一个异步处理器的指针Rcp_RequestHandler。 |
| responseCallback | 指向Rcp_ResponseCallbackObject的指针。 |
 
 
**返回：**
 
uint32_t 返回表示拦截器的返回值。
