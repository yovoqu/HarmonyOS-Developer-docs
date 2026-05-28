# Rcp_StaticDnsRule

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

静态DNS规则。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_StaticDnsRuleItem staticDnsRule | 单个静态DNS规则。 |
| struct Rcp_StaticDnsRule * next | 链式存储。指向下一个Rcp_StaticDnsRule的指针。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_StaticDnsRule* Rcp_StaticDnsRule::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule)的指针。
 
  

#### staticDnsRule

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_StaticDnsRuleItem Rcp_StaticDnsRule::staticDnsRule
```
 
**描述**
 
单个静态DNS规则。
