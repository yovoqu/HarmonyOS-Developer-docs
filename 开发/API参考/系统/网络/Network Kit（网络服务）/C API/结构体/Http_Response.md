# Http_Response

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Http_Response {...} Http_Response
```
  

##### 概述

定义HTTP响应的结构体。
 
**起始版本：** 20
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Http_Buffer body | HTTP请求响应的数据，参考Http_Buffer。 |
| Http_ResponseCode responseCode | HTTP请求响应码，参考Http_ResponseCode。 |
| Http_Headers *headers | HTTP响应的头，指向Http_Headers的指针，参考Http_Headers。 |
| char *cookies | HTTP响应Cookies。 |
| Http_PerformanceTiming *performanceTiming | HTTP响应时间信息，指向Http_PerformanceTiming的指针，参考Http_PerformanceTiming。 |
 
 
  

##### 成员函数
 
| 名称 | 描述 |
| --- | --- |
| void (*destroyResponse)(struct Http_Response **response) | 销毁HTTP响应的回调函数 |
 
 
  

##### 成员函数说明

  

##### destroyResponse()

```text
void (*destroyResponse)(struct Http_Response **response)
```
 
**描述**
 
销毁HTTP响应的回调函数
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct Http_Response **response | 要销毁的HTTP响应，指向Http_Response的指针，参考Http_Response。 |
