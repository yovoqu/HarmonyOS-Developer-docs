# Rcp_ProxyConfiguration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

代理配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_ProxyType proxyType | 区分请求使用的代理类型。 |
| Rcp_WebProxy customProxy | 自定义代理配置，参见Rcp_WebProxy。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### customProxy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_WebProxy Rcp_ProxyConfiguration::customProxy
```
 
**描述**
 
自定义代理配置，参见[Rcp_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy)。
 
  

##### proxyType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ProxyType Rcp_ProxyConfiguration::proxyType
```
 
**描述**
 
区分请求使用的代理类型。
