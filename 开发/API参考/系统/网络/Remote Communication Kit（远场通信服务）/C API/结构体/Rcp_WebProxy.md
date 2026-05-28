# Rcp_WebProxy

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自定义代理配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char * url | 代理服务器的URL。如果您没有明确设置端口，则端口将为1080。 |
| Rcp_ProxyTunnelMode createTunnel | 用于控制何时创建代理隧道。 |
| Rcp_Exclusions exclusions | 如果Rcp_Request.url匹配Rcp_Exclusions规则，则Rcp_Request将不使用代理。 |
| Rcp_SecurityConfiguration securityConfiguration | 代理中的Rcp_SecurityConfiguration。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### createTunnel

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ProxyTunnelMode Rcp_WebProxy::createTunnel
```
 
**描述**
 
用于控制何时创建代理隧道。
 
  

#### exclusions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Exclusions Rcp_WebProxy::exclusions
```
 
**描述**
 
如果[Rcp_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)将不使用代理。
 
  

#### securityConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_SecurityConfiguration Rcp_WebProxy::securityConfiguration
```
 
**描述**
 
代理中的[Rcp_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)。
 
  

#### url

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* Rcp_WebProxy::url
```
 
**描述**
 
代理服务器的URL。如果您没有明确设置端口，则端口将为1080。
