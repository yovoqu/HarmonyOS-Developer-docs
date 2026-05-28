# Rcp_InfoToCollect

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| bool textual | 是否收集文本信息事件。true表示收集文本信息事件，false表示不收集文本信息事件。默认值为false。 |
| bool incomingHeader | 是否收集传入的header信息事件。true表示收集传入的header信息事件，false表示不收集传入的header信息事件。默认值为false。 |
| bool outgoingHeader | 是否收集传出的header信息事件。true表示收集传出的header信息事件，false表示不收集传出的header信息事件。默认值为false。 |
| bool incomingData | 是否收集传入的数据信息事件。true表示收集传入的数据信息事件，false表示不收集传入的数据信息事件。默认值为false。 |
| bool outgoingData | 是否收集传出的数据信息事件。true表示收集传出的数据信息事件，false表示不收集传出的数据信息事件。默认值为false。 |
| bool incomingSslData | 是否收集传入的SSL/TLS数据信息事件。true表示收集传入的SSL/TLS数据信息事件，false表示不收集传入的SSL/TLS数据信息事件。默认值为false。 |
| bool outgoingSslData | 是否收集传出的SSL/TLS数据信息事件。true表示收集传出的SSL/TLS数据信息事件，false表示不收集传出的SSL/TLS数据信息事件。默认值为false。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### incomingData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::incomingData
```
 
**描述**
 
是否收集传入的数据信息事件。true表示收集传入的数据信息事件，false表示不收集传入的数据信息事件。默认值为false。
 
  

#### incomingHeader

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::incomingHeader
```
 
**描述**
 
是否收集传入HTTP标头事件。true表示收集传入的header信息事件，false表示不收集传入的header信息事件。默认值为false。
 
  

#### incomingSslData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::incomingSslData
```
 
**描述**
 
是否收集传入的SSL/TLS数据信息事件。true表示收集传入的SSL/TLS数据信息事件，false表示不收集传入的SSL/TLS数据信息事件。默认值为false。
 
  

#### outgoingData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::outgoingData
```
 
**描述**
 
是否收集传出的数据信息事件。true表示收集传出的数据信息事件，false表示不收集传出的数据信息事件。默认值为false。
 
  

#### outgoingHeader

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::outgoingHeader
```
 
**描述**
 
是否收集传出的header信息事件。true表示收集传出的header信息事件，false表示不收集传出的header信息事件。默认值为false。
 
  

#### outgoingSslData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::outgoingSslData
```
 
**描述**
 
是否收集传出的SSL/TLS数据信息事件。true表示收集传出的SSL/TLS数据信息事件，false表示不收集传出的SSL/TLS数据信息事件。默认值为false。
 
  

#### textual

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_InfoToCollect::textual
```
 
**描述**
 
是否收集文本信息事件。true表示收集文本信息事件，false表示不收集文本信息事件。默认值为false。
