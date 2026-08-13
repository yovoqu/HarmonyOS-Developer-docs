# NetworkBoost_DataSpeedAction

更新时间：2026-08-11 11:13:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

发包速率建议。该结构体用于网络加速模块中，当系统需要为特定应用提供定制化的上下行带宽建议时使用。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| NetworkBoost_DataSpeedSimpleAction dataSpeedSimpleAction | 应用发包策略的简单建议。该字段表示应用在当前网络环境下推荐使用的发包策略，用于指导应用优化数据传输行为。 |
| uint64_t linkUpBandwidth | 上行带宽，单位为bps。该字段表示设备当前网络连接的上行带宽能力，可用于评估上传速度和资源分配。 |
| uint64_t linkDownBandwidth | 下行带宽，单位为bps。该字段表示设备当前网络连接的下行带宽能力，可用于评估下载速度和资源分配。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### dataSpeedSimpleAction

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedAction::dataSpeedSimpleAction
```
 
**描述**
 
应用发包策略的简单建议。
 
  

#### linkDownBandwidth

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_DataSpeedAction::linkDownBandwidth
```
 
**描述**
 
下行带宽。
 
  

#### linkUpBandwidth

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_DataSpeedAction::linkUpBandwidth
```
 
**描述**
 
上行带宽。
