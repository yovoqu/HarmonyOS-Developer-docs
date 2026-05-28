# Rcp_HeaderEntry

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

请求或响应的标头的所有键值对。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char * key | 键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。 |
| Rcp_HeaderValue * value | 值。 |
| struct Rcp_HeaderEntry * next | 链式存储。指向下一个键值对Rcp_HeaderEntry。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### key

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* Rcp_HeaderEntry::key
```
 
**描述**
 
键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。
 
  

##### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_HeaderEntry* Rcp_HeaderEntry::next
```
 
**描述**
 
链式存储。指向下一个键值对[Rcp_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)。
 
  

##### value

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_HeaderValue* Rcp_HeaderEntry::value
```
 
**描述**
 
标头键值对的值。
