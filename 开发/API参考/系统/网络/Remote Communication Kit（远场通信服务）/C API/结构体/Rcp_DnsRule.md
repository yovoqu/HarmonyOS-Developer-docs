# Rcp_DnsRule

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

DNS规则配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_DnsRuleType type | 表示union中使用的数据类型。 |
| union { Rcp_DnsServers * dnsServers; Rcp_StaticDnsRule * staticDnsRule; Rcp_DynamicDnsRuleFunction dynamicDnsRule; } data | dnsServers：DNS服务器。 staticDnsRule：静态DNS规则。 dynamicDnsRule：动态DNS规则。 |
 
 
  

##### 结构体成员变量说明

  

##### dnsServers

```text
Rcp_DnsServers* Rcp_DnsRule::dnsServers
```
 
**描述**
 
DNS服务器。
 
  

##### dynamicDnsRule

```text
Rcp_DynamicDnsRuleFunction Rcp_DnsRule::dynamicDnsRule
```
 
**描述**
 
动态DNS规则。
 
  

##### staticDnsRule

```text
Rcp_StaticDnsRule* Rcp_DnsRule::staticDnsRule
```
 
**描述**
 
静态DNS规则。
 
  

##### type

```text
Rcp_DnsRuleType Rcp_DnsRule::type
```
 
**描述**
 
表示union中使用的数据类型。
