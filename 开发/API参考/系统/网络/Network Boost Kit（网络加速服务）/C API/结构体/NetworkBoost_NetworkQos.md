# NetworkBoost_NetworkQos

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_qos
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

网络质量回调信息。
 
**起始版本：** 5.1.0(18)
 
**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)
 
**所在头文件：** [network_boost_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| NetworkBoost_PathType pathType | 相应的数据路径上的网络质量信息。 |
| uint64_t linkUpBandwidth | 上行带宽信息，单位为bps。 |
| uint64_t linkDownBandwidth | 下行带宽信息，单位为bps。 |
| uint64_t linkUpRate | 上行速率，单位为bps。 |
| uint64_t linkDownRate | 下行速率，单位为bps。 |
| uint32_t rttMs | RTT时延，表示统计时间间隔内，pathType对应数据路径上，所有的TCP上下行数据包的平均往返时延。取值范围为0或任意正数，单位：毫秒（ms）。 如果在统计时间间隔内没有收到某次TCP请求的回复，则该次的RTT时延不会被计入该统计时间间隔内。因此，在完全不可上网的场景下，由于无法收到TCP的回复，回调中的RTT时延值会比较小，与实际状态不一致。针对完全不可上网的场景，建议结合on('netCapabilitiesChange')方法进行综合判断。 |
| uint32_t linkUpBufferDelayMs | 上行发送空口缓冲时延，单位为ms，取值范围是任意正数。 |
| uint32_t linkUpBufferCongestionPercent | 上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet

  

#### linkDownBandwidth

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_NetworkQos::linkDownBandwidth
```
 
**描述**
 
下行带宽信息，单位为bps。
 
  

#### linkDownRate

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_NetworkQos::linkDownRate
```
 
**描述**
 
下行速率，单位为bps。
 
  

#### linkUpBandwidth

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_NetworkQos::linkUpBandwidth
```
 
**描述**
 
上行带宽信息，单位为bps。
 
  

#### linkUpBufferCongestionPercent

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_NetworkQos::linkUpBufferCongestionPercent
```
 
**描述**
 
上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。
 
  

#### linkUpBufferDelayMs

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_NetworkQos::linkUpBufferDelayMs
```
 
**描述**
 
上行发送空口缓冲时延（单位ms），取值范围是任意正数。
 
  

#### linkUpRate

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint64_t NetworkBoost_NetworkQos::linkUpRate
```
 
**描述**
 
上行速率，单位为bps。
 
  

#### pathType

**支持设备：** Phone | PC/2in1 | Tablet

```text
NetworkBoost_PathType NetworkBoost_NetworkQos::pathType
```
 
**描述**
 
相应的数据路径上的网络质量信息。
 
  

#### rttMs

**支持设备：** Phone | PC/2in1 | Tablet

```text
uint32_t NetworkBoost_NetworkQos::rttMs
```
 
**描述**
 
RTT时延（单位ms），取值范围是任意正数。
