# Rcp_Exclusions

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

代理配置中用于过滤不使用代理的urls。
 
如果[Rcp_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)不会使用代理。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_ExclusionsValueType type | 表示union中使用的数据类型。 |
| union { Rcp_Urls * urls; Rcp_ExclusionFunction exclusionFunction; } data | Urls。链式存储url。 回调函数。通过回调函数过滤url。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### exclusionFunction

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ExclusionFunction Rcp_Exclusions::exclusionFunction
```
 
**描述**
 
通过回调过滤。
 
  

##### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ExclusionsValueType Rcp_Exclusions::type
```
 
**描述**
 
表示union中使用的数据类型。
 
  

##### urls

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Urls* Rcp_Exclusions::urls
```
 
**描述**
 
Urls。
