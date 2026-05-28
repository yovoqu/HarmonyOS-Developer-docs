# Rcp_ContentOrPathOrCallback

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

[Rcp_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Rcp_ContentOrPathOrCallbackType type | 表示union中使用的数据类型。 |
| union { Rcp_Buffer content; char path [RCP_MAX_PATH_LEN]; Rcp_GetDataCallback callback; } data | content: 文本数据。 path: 文件路径。 callback: 获取数据的回调函数。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### callback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```
 
**描述**
 
获取数据的回调。
 
  

#### content

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```
 
**描述**
 
文本数据。
 
  

#### path

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char Rcp_ContentOrPathOrCallback::path[RCP_MAX_PATH_LEN]
```
 
**描述**
 
文件路径。
 
  

#### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```
 
**描述**
 
union中使用的数据类型。
