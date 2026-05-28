# WebSocket_Header

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct WebSocket_Header {...}
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

websocket客户端增加header的链表节点。
 
**起始版本：** 11
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char *fieldName | header的字段名。 |
| const char *fieldValue | header的字段内容。 |
| struct WebSocket_Header *next | header链表的next指针。 |
