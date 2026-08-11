# net_ethernet.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ethernet-h
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

为以太网网卡模块提供C接口。
 
**引用文件：** <network/net_ethernet/net_ethernet.h>
 
**库：** libnet_ethernet.so
 
**系统能力：** SystemCapability.Communication.NetManager.Ethernet
 
**起始版本：** 26.0.0
 
**相关模块：** [NetEthernet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t OH_Ethernet_GetMacAddress(Ethernet_MacAddrInfoList *macAddrList) | 获取以太网网卡MAC地址列表。 |
| int32_t OH_Ethernet_GetNetAddress(Ethernet_NetAddrList *netAddrList) | 获取以太网网卡IP地址列表。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### OH_Ethernet_GetMacAddress()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
int32_t OH_Ethernet_GetMacAddress(Ethernet_MacAddrInfoList *macAddrList)
```
 
**描述**
 
获取以太网网卡MAC地址列表。
 
**系统能力：** SystemCapability.Communication.NetManager.Ethernet
 
**需要权限：** ohos.permission.GET_ETHERNET_LOCAL_MAC
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Ethernet_MacAddrInfoList *macAddrList | 以太网网卡MAC地址列表。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。 201 - 缺少权限。 2200001 - 参数错误。 2200002 - 无法连接到服务。 2201005 - 设备信息不存在。 |
 
 
  

#### OH_Ethernet_GetNetAddress()

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
int32_t OH_Ethernet_GetNetAddress(Ethernet_NetAddrList *netAddrList)
```
 
**描述**
 
获取以太网网卡IP地址列表。
 
**系统能力：** SystemCapability.Communication.NetManager.Ethernet
 
**需要权限：** ohos.permission.GET_NETWORK_INFO
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Ethernet_NetAddrList *netAddrList | 以太网网卡IP地址列表。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。 201 - 缺少权限。 2200001 - 参数错误。 2200002 - 无法连接到服务。 2201005 - 设备信息不存在。 |
