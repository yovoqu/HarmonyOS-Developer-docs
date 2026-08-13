# NetworkBoost_HandoverStart

更新时间：2026-08-11 11:13:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_start
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

连接迁移开始信息。该结构体用于配置连接迁移开始时的相关参数，通常系统发起多网迁移（Wi-Fi与蜂窝网络切换，主卡与副卡切换等）开始时使用，其主要作用是设置迁移过程中的超时时间和老链路的发包建议，以保证迁移过程的稳定性和效率。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| uint32_t expires | 连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。 |
| NetworkBoost_DataSpeedAction dataSpeedAction | 老链路的发包建议。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### dataSpeedAction

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_DataSpeedAction NetworkBoost_HandoverStart::dataSpeedAction
```
 
**描述**
 
老链路的发包建议。
 
  

#### expires

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_HandoverStart::expires
```
 
**描述**
 
连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。
