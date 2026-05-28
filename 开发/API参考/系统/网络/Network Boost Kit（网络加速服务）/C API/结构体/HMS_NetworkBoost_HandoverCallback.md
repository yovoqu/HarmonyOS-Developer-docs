# HMS_NetworkBoost_HandoverCallback

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_callback
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

回调函数，返回连接迁移开始和完成的详细信息。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| HMS_NetworkBoost_OnHandoverStart onNetworkHandoverStart | 连接迁移开始的回调。 |
| HMS_NetworkBoost_OnHandoverComplete onNetworkHandoverComplete | 连接迁移结束的回调。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

##### onNetworkHandoverStart

**支持设备：** Phone | PC/2in1 | Tablet

```text
HMS_NetworkBoost_OnHandoverStart HMS_NetworkBoost_HandoverCallback::onNetworkHandoverStart
```
 
**描述**
 
连接迁移开始的回调。
 
  

##### onNetworkHandoverComplete

**支持设备：** Phone | PC/2in1 | Tablet

```text
HMS_NetworkBoost_OnHandoverComplete HMS_NetworkBoost_HandoverCallback::onNetworkHandoverComplete
```
 
**描述**
 
连接迁移结束的回调。
