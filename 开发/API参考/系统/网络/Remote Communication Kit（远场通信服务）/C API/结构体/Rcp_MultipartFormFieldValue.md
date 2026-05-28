# Rcp_MultipartFormFieldValue

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

多部分表单域值，在[Rcp_MultipartForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_multipartform)中使用。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_MultipartValueType type | 表示union中使用的数据类型。 |
| union { Rcp_FormFieldValue formValue; Rcp_FormFieldFileValue formFileValue; } data | formValue：简单表单数据字段值。 formFileValue：简单表单数据字段文件值。 |
| struct Rcp_MultipartFormFieldValue * next | 指向下一个Rcp_MultipartFormFieldValue。链式存储。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### formFileValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_FormFieldFileValue Rcp_MultipartFormFieldValue::formFileValue
```
 
**描述**
 
简单表单数据字段文件值。
 
  

##### formValue

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_FormFieldValue Rcp_MultipartFormFieldValue::formValue
```
 
**描述**
 
简单表单数据字段值。
 
  

##### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_MultipartFormFieldValue* Rcp_MultipartFormFieldValue::next
```
 
**描述**
 
指向下一个[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。链式存储。
 
  

##### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_MultipartValueType Rcp_MultipartFormFieldValue::type
```
 
**描述**
 
表示union中使用的数据类型。
