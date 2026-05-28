# Rcp_SessionConfiguration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

会话配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_SessionType type | 会话类型。 |
| Rcp_InterceptorArray interceptors | 用户自定义的异步拦截器数组。 |
| Rcp_SyncInterceptorArray syncInterceptors | 用户定义的同步拦截器数组。 |
| const char * baseUrl | 基本URL。 |
| Rcp_Headers * headers | 请求标头。 |
| Rcp_RequestCookies * cookies | 请求的Cookie。 |
| Rcp_SessionListener sessionListener | 回调函数，供session监听close()或cancel()事件。 |
| Rcp_Configuration * requestConfiguration | 默认请求配置。这些选项可以通过Request.configuration覆盖。 |
| Rcp_ConnectionConfiguration connectionConfiguration | 连接配置。 |
 
 
  

##### 结构体成员变量说明

  

##### baseUrl

```text
const char* Rcp_SessionConfiguration::baseUrl
```
 
**描述**
 
基本URL。
 
举例， 如果请求的url为 '?name=value', 基本url是 “https://example.com”，那么最后当请求被送往服务端时的最终url为 “https://example.com?name=value”。
 
  

##### connectionConfiguration

```text
Rcp_ConnectionConfiguration Rcp_SessionConfiguration::connectionConfiguration
```
 
**描述**
 
连接配置。
 
它用于指定此会话中允许的最大同时连接总数以及允许连接到单个主机的最大同时连接数。
 
  

##### cookies

```text
Rcp_RequestCookies* Rcp_SessionConfiguration::cookies
```
 
**描述**
 
请求的Cookie。
 
如果调用了[HMS_Rcp_Fetch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_fetch)或者[HMS_Rcp_FetchSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_fetchsync)，在参数中的[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)中没有[Rcp_RequestCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_requestcookies)，则[Rcp_SessionConfiguration.cookies](#cookies)将是[Rcp_Request.cookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#cookies)，如果两者都存在，则将它们合并。
 
  

##### headers

```text
Rcp_Headers* Rcp_SessionConfiguration::headers
```
 
**描述**
 
请求标头。
 
如果调用了[HMS_Rcp_Fetch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_fetch)或[HMS_Rcp_FetchSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_fetchsync)，并且[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)中没有[Rcp_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_headers)，[Rcp_SessionConfiguration.headers](#headers)将是[Rcp_Request.headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#headers)，如果两者都存在，则将它们合并。
 
  

##### interceptors

```text
Rcp_InterceptorArray Rcp_SessionConfiguration::interceptors
```
 
**描述**
 
用户自定义的异步拦截器数组。
 
异步拦截器将被制成拦截器链。
 
输入: [A, B, C, D]， 处理逻辑将为 A->B->C->D->defaultHandler。
 
  

##### requestConfiguration

```text
Rcp_Configuration* Rcp_SessionConfiguration::requestConfiguration
```
 
**描述**
 
默认请求配置。这些选项可以通过[Request.configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#configuration)覆盖。
 
  

##### sessionListener

```text
Rcp_SessionListener Rcp_SessionConfiguration::sessionListener
```
 
**描述**
 
回调函数，供session监听close()或cancel()事件。
 
  

##### syncInterceptors

```text
Rcp_SyncInterceptorArray Rcp_SessionConfiguration::syncInterceptors
```
 
**描述**
 
用户定义的同步拦截器数组。
 
同步拦截器会被做成拦截器链。
 
输入: [A, B, C, D], 处理逻辑将为 A->B->C->D->defaultHandler。
 
  

##### type

```text
Rcp_SessionType Rcp_SessionConfiguration::type
```
 
**描述**
 
会话类型。
