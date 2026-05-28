# Rcp_DnsServers

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

DNS服务器。[Rcp_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_IpAndPort ipAndPort | IP和端口。 |
| struct Rcp_DnsServers * next | 链式存储。指向下一个Rcp_DnsServers的指针。 |
 
 
  

##### 结构体成员变量说明

  

##### ipAndPort

```text
Rcp_IpAndPort Rcp_DnsServers::ipAndPort
```
 
**描述**
 
IP和端口。
 
  

##### next

```text
struct Rcp_DnsServers* Rcp_DnsServers::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)的指针。
