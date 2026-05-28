# NetworkBoost_NetworkQosArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos_array
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

网络质量变化的详细信息。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| uint32_t pathNum | 网络质量信息中的路径数量，取值范围 [1, 4]。 |
| NetworkBoost_NetworkQos networkQos [NETBOOST_MAX_PATH_NUM] | 多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

##### networkQos

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_NetworkQos NetworkBoost_NetworkQosArray::networkQos[NETBOOST_MAX_PATH_NUM]
```
 
**描述**
 
多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。
 
  

##### pathNum

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_NetworkQosArray::pathNum
```
 
**描述**
 
网络质量信息中的路径数量，取值范围 [1, 4]。
