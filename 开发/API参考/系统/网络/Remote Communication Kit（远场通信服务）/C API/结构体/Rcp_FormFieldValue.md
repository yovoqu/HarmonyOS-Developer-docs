# Rcp_FormFieldValue

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

简单表单数据字段值，参见[Rcp_Form](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_form)和[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_FormValueType type | 表示union中使用的数据类型。 |
| union { uint8_t varBool; int32_t varInt32; int64_t varInt64; double varDouble; Rcp_Buffer varStr; } data | bool类型。值为0表示false，值大于0表示true。 int32类型。 int64类型。 double类型。 string类型。 |
| struct Rcp_FormFieldValue * next | 指向下一个Rcp_FormFieldValue。链式存储。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_FormFieldValue* Rcp_FormFieldValue::next
```
 
**描述**
 
指向下一个[Rcp_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)。链式存储。
 
  

#### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_FormValueType Rcp_FormFieldValue::type
```
 
**描述**
 
表示union中使用的数据类型。
 
  

#### varBool

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
uint8_t Rcp_FormFieldValue::varBool
```
 
**描述**
 
bool类型。值为0表示false，值大于0表示true。
 
  

#### varDouble

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
double Rcp_FormFieldValue::varDouble
```
 
**描述**
 
double类型。
 
  

#### varInt32

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t Rcp_FormFieldValue::varInt32
```
 
**描述**
 
int32类型。
 
  

#### varInt64

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int64_t Rcp_FormFieldValue::varInt64
```
 
**描述**
 
int64类型。
 
  

#### varStr

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Buffer Rcp_FormFieldValue::varStr
```
 
**描述**
 
string类型。
