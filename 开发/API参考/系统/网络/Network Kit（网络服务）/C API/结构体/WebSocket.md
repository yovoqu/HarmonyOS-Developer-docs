# WebSocket

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
struct WebSocket {...}
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

WebSocket客户端结构体。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [WebSocket_OnOpenCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onopencallback) onOpen | 客户端接收连接消息的回调指针。 |
| [WebSocket_OnMessageCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onmessagecallback) onMessage | 客户端接收消息的回调指针。 |
| [WebSocket_OnErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onerrorcallback) onError | 客户端接收错误消息的回调指针。 |
| [WebSocket_OnCloseCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onclosecallback) onClose | 客户端接收关闭消息的回调指针。 |
| [WebSocket_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-requestoptions) requestOptions | 客户端建立连接请求内容。 |
