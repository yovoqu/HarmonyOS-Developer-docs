# Rcp_QuicStreamData

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_stream_data
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

quic连接中用于接收流式数据的存储结构。
 
**起始版本：** 26.0.0
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp_quic.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_quic_h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_QuicIoVec *iov | 指向Rcp_QuicIoVec结构体数组的指针。 |
| uint32_t iovLen | Rcp_QuicIoVec结构体数组的长度。 |
| bool fin | 标记是否为流式传输的最后数据。true表示是流式传输的最后数据。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### iov

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_QuicIoVec* Rcp_QuicStreamData::iov
```
 
**描述**
 
指向[Rcp_QuicIoVec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_io_vec)结构体数组的指针。
 
  

#### iovLen

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint32_t Rcp_QuicStreamData::iovLen
```
 
**描述**
 
[Rcp_QuicIoVec](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___quic_io_vec)结构体数组的长度。
 
  

#### fin

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_QuicStreamData::fin
```
 
**描述**
 
标记是否为流式传输的最后数据。true表示是流式传输的最后数据。
