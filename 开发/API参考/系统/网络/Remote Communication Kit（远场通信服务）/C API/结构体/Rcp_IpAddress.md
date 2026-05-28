# Rcp_IpAddress

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char ipAddress [RCP_IP_MAX_LEN] | IP地址。 |
| struct Rcp_IpAddress * next | 链式存储。指向下一个Rcp_IpAddress。 |
 
 
  

##### 结构体成员变量说明

  

##### ipAddress

```text
char Rcp_IpAddress::ipAddress[RCP_IP_MAX_LEN]
```
 
**描述**
 
ip地址。
 
  

##### next

```text
struct Rcp_IpAddress* Rcp_IpAddress::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)。
