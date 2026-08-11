# Ethernet_NetAddr

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-netaddr
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct Ethernet_NetAddr {...} Ethernet_NetAddr
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

网络地址。
 
**起始版本：** 26.0.0
 
**相关模块：** [NetEthernet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet)
 
**所在头文件：** [net_ethernet_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t family | 网络地址族。IPv4 = 1，IPv6 = 2。 |
| uint8_t prefixlen | 前缀长度。 |
| uint16_t port | 端口号。 |
| char address[ETHERNET_MAX_STR_LEN] | IP地址。 |
