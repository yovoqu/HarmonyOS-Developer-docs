# Rcp_FormFieldFileValue

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表单字段文件值。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char contentType [RCP_MAX_CONTENT_TYPE_LEN] | 多部分表单数据内容类型。 |
| char remoteFileName [RCP_MAX_FILENAME_LEN] | 多部分表单数据远程文件名。 |
| Rcp_ContentOrPathOrCallback contentOrPathOrCb | 多部分表单数据内容。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### contentOrPathOrCb

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ContentOrPathOrCallback Rcp_FormFieldFileValue::contentOrPathOrCb
```
 
**描述**
 
多部分表单数据内容。
 
  

#### contentType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char Rcp_FormFieldFileValue::contentType[RCP_MAX_CONTENT_TYPE_LEN]
```
 
**描述**
 
多部分表单数据内容类型。
 
  

#### remoteFileName

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char Rcp_FormFieldFileValue::remoteFileName[RCP_MAX_FILENAME_LEN]
```
 
**描述**
 
多部分表单数据远程文件名。
