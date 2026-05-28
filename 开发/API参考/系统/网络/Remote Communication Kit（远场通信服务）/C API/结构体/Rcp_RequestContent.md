# Rcp_RequestContent

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

请求的内容。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_ContentType type | 表示union中使用的数据类型。 |
| union { Rcp_Buffer contentStr; Rcp_Form * form; Rcp_MultipartForm * multipartForm; Rcp_GetDataCallback getDataCallback; } data | contentStr：文本。 form：表单。 multipartForm：多部分表单。 getDataCallback：使用回调函数获取数据。 |
 
 
  

##### 结构体成员变量说明

  

##### contentStr

```text
Rcp_Buffer Rcp_RequestContent::contentStr
```
 
**描述**
 
字符串内容。
 
  

##### form

```text
Rcp_Form* Rcp_RequestContent::form
```
 
**描述**
 
表单内容。
 
  

##### getDataCallback

```text
Rcp_GetDataCallback Rcp_RequestContent::getDataCallback
```
 
**描述**
 
回调函数。
 
  

##### multipartForm

```text
Rcp_MultipartForm* Rcp_RequestContent::multipartForm
```
 
**描述**
 
多部分表单内容。
 
  

##### type

```text
Rcp_ContentType Rcp_RequestContent::type
```
 
**描述**
 
表示union中使用的数据类型。
