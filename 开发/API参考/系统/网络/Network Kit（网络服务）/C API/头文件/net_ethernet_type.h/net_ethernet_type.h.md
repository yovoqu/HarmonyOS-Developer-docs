# net_ethernet_type.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-type-h
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

为以太网网卡模块C接口定义数据结构。
 
**引用文件：** <network/net_ethernet/net_ethernet_type.h>
 
**库：** libnet_ethernet.so
 
**系统能力：** SystemCapability.Communication.NetManager.Ethernet
 
**起始版本：** 26.0.0
 
**相关模块：** [NetEthernet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Ethernet_MacAddressInfo | Ethernet_MacAddressInfo | 以太网网卡MAC地址信息。 |
| Ethernet_MacAddrInfoList | Ethernet_MacAddrInfoList | 以太网网卡MAC地址信息列表。 |
| Ethernet_NetAddr | Ethernet_NetAddr | 网络地址。 |
| Ethernet_NetAddrInfo | Ethernet_NetAddrInfo | 以太网网卡网络地址信息，包含以太网网卡名称及网络地址信息。 |
| Ethernet_NetAddrList | Ethernet_NetAddrList | 以太网网卡网络地址列表。 |
 
 
  

#### 宏定义

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| ETHERNET_MAX_NET_SIZE 32 | 以太网网卡最大连接数量。 起始版本： 26.0.0 |
| ETHERNET_MAX_STR_LEN 256 | 以太网网卡MAC地址、IP地址最大长度。 起始版本： 26.0.0 |
