# Rcp_TracingConfiguration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

请求追踪配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| bool verbose | 请求运行时是否记录详细日志。true表示开启捕获，false表示不开启。默认值为false。如果设置了infoToCollect中的选项，则自动启用。 |
| Rcp_InfoToCollect infoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| bool collectTimeInfo | 是否收集请求计时信息。true代表收集，false代表不收集。默认值为false。 |
| Rcp_EventsHandler httpEventsHandler | 监听不同HTTP事件的回调函数。 |
 
 
  

##### 结构体成员变量说明

  

##### collectTimeInfo

```text
bool Rcp_TracingConfiguration::collectTimeInfo
```
 
**描述**
 
是否收集请求计时信息。true代表收集，false代表不收集。默认值为false。
 
  

##### httpEventsHandler

```text
Rcp_EventsHandler Rcp_TracingConfiguration::httpEventsHandler
```
 
**描述**
 
监听不同HTTP事件的回调函数。
 
  

##### infoToCollect

```text
Rcp_InfoToCollect Rcp_TracingConfiguration::infoToCollect
```
 
**描述**
 
指定要收集的请求处理事件。可以通过响应对象检查收集的事件。
 
  

##### verbose

```text
bool Rcp_TracingConfiguration::verbose
```
 
**描述**
 
请求运行时是否记录详细日志。true表示开启捕获，false表示不开启。默认值为false。如果设置了infoToCollect中的选项，则自动启用。
