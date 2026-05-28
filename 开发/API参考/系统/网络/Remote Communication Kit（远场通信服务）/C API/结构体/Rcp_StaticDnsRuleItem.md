# Rcp_StaticDnsRuleItem

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

描述单个静态DNS规则。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char host [RCP_HOST_MAX_LEN] | 主机名。 |
| uint16_t port | 端口号。范围： [0, 65535]。 |
| Rcp_IpAddress * ipAddresses | 表示Rcp_StaticDnsRuleItem.host对应的IP地址。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### host

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char Rcp_StaticDnsRuleItem::host[RCP_HOST_MAX_LEN]
```
 
**描述**
 
主机名。
 
  

#### ipAddresses

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_IpAddress* Rcp_StaticDnsRuleItem::ipAddresses
```
 
**描述**
 
表示[Rcp_StaticDnsRuleItem.host](#host)对应的IP地址。
 
  

#### port

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint16_t Rcp_StaticDnsRuleItem::port
```
 
**描述**
 
端口号。范围： [0, 65535]。
