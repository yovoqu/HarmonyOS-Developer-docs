# WebSocket

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct WebSocket {...}
```
  

##### 概述

WebSocket客户端结构体。
 
**起始版本：** 11
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| WebSocket_OnOpenCallback onOpen | 客户端接收连接消息的回调指针。 |
| WebSocket_OnMessageCallback onMessage | 客户端接收消息的回调指针。 |
| WebSocket_OnErrorCallback onError | 客户端接收错误消息的回调指针。 |
| WebSocket_OnCloseCallback onClose | 客户端接收关闭消息的回调指针。 |
| WebSocket_RequestOptions requestOptions | 客户端建立连接请求内容。 |
