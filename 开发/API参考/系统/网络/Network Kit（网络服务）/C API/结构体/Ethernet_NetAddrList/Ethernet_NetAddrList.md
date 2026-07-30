# Ethernet_NetAddrList

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet-ethernet-netaddrlist
**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
typedef struct Ethernet_NetAddrList {...} Ethernet_NetAddrList
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

以太网网卡网络地址列表。
 
**起始版本：** 26.0.0
 
**相关模块：** [NetEthernet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet)
 
**所在头文件：** [net_ethernet_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| Ethernet_NetAddrInfo netAddrList[ETHERNET_MAX_NET_SIZE] | 以太网网络地址列表。 |
| int32_t netAddrListSize | netAddrList的实际大小。 |
