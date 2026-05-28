# Rcp_DnsConfiguration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

DNS解析配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_DnsRule * dnsRules | DNS规则配置。 |
| Rcp_DnsOverHttps dnsOverHttps | DOH配置。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### dnsOverHttps

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_DnsOverHttps Rcp_DnsConfiguration::dnsOverHttps
```
 
**描述**
 
DOH配置。
 
  

##### dnsRules

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_DnsRule* Rcp_DnsConfiguration::dnsRules
```
 
**描述**
 
DNS规则配置。
 
[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers): 表示优先使用指定的dns服务器解析主机名。
 
[Rcp_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule): 表示如果主机名匹配，则优先使用指定的地址。
 
[Rcp_DynamicDnsRuleFunction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_dynamicdnsrulefunction): 表示优先使用函数中返回的地址。
