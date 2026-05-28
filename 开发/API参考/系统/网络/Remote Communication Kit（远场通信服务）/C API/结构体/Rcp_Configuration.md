# Rcp_Configuration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

请求配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_TransferConfiguration transferConfiguration | 传输配置。 |
| Rcp_TracingConfiguration tracingConfiguration | 请求追踪配置。 |
| Rcp_ProxyConfiguration proxyConfiguration | 代理配置。 |
| Rcp_DnsConfiguration dnsConfiguration | DNS配置。 |
| Rcp_SecurityConfiguration securityConfiguration | 安全配置。 |
| void * configurationPrivate | 可扩展字段。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### configurationPrivate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* Rcp_Configuration::configurationPrivate
```
 
**描述**
 
可扩展字段。
 
  

#### dnsConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_DnsConfiguration Rcp_Configuration::dnsConfiguration
```
 
**描述**
 
DNS配置。
 
  

#### proxyConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ProxyConfiguration Rcp_Configuration::proxyConfiguration
```
 
**描述**
 
代理配置。
 
  

#### securityConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_SecurityConfiguration Rcp_Configuration::securityConfiguration
```
 
**描述**
 
安全配置。
 
  

#### tracingConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_TracingConfiguration Rcp_Configuration::tracingConfiguration
```
 
**描述**
 
请求追踪配置。
 
  

#### transferConfiguration

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_TransferConfiguration Rcp_Configuration::transferConfiguration
```
 
**描述**
 
传输配置。
