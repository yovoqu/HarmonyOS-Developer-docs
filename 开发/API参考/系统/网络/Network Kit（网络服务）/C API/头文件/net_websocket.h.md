# net_websocket.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

定义WebSocket客户端模块的接口。
 
**引用文件：** <network/netstack/net_websocket.h>
 
**库：** libnet_websocket.so
 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 11
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
  

##### 汇总

  

##### 函数
 
| 名称 | 描述 |
| --- | --- |
| struct WebSocket *OH_WebSocketClient_Constructor(WebSocket_OnOpenCallback onOpen, WebSocket_OnMessageCallback onMessage,WebSocket_OnErrorCallback onError, WebSocket_OnCloseCallback onclose) | WebSocket客户端的构造函数。 |
| int OH_WebSocketClient_AddHeader(struct WebSocket *client, struct WebSocket_Header header) | 将header头信息添加到client客户端request中。 |
| int OH_WebSocketClient_Connect(struct WebSocket *client, const char *url, struct WebSocket_RequestOptions options) | 客户端连接服务端。 |
| int OH_WebSocketClient_Send(struct WebSocket *client, char *data, size_t length) | 客户端向服务端发送数据。 |
| int OH_WebSocketClient_Close(struct WebSocket *client, struct WebSocket_CloseOption options) | 客户端主动关闭WebSocket连接。 |
| int OH_WebSocketClient_Destroy(struct WebSocket *client) | 释放WebSocket连接上下文和资源。 |
 
 
  

##### 函数说明

  

##### OH_WebSocketClient_Constructor()

```text
struct WebSocket *OH_WebSocketClient_Constructor(WebSocket_OnOpenCallback onOpen, WebSocket_OnMessageCallback onMessage,WebSocket_OnErrorCallback onError, WebSocket_OnCloseCallback onclose)
```
 
**描述**
 
WebSocket客户端的构造函数。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| WebSocket_OnOpenCallback onOpen | 客户端定义的建立连接消息的回调函数。 |
| WebSocket_OnMessageCallback onMessage | 客户端定义的接收消息的回调函数。 |
| WebSocket_OnErrorCallback onError | 客户端定义的错误消息的回调函数。 |
| WebSocket_OnCloseCallback onclose | 客户端定义的关闭消息的回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| struct WebSocket * | 成功返回客户端指针，失败返回为NULL。 |
 
 
  

##### OH_WebSocketClient_AddHeader()

```text
int OH_WebSocketClient_AddHeader(struct WebSocket *client, struct WebSocket_Header header)
```
 
**描述**
 
将header头信息添加到client客户端request中。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端指针。 |
| struct WebSocket_Header header | Header头信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |
 
 
  

##### OH_WebSocketClient_Connect()

```text
int OH_WebSocketClient_Connect(struct WebSocket *client, const char *url, struct WebSocket_RequestOptions options)
```
 
**描述**
 
客户端连接服务端。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**需要权限：** ohos.permission.INTERNET
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端指针。 |
| const char *url | 客户端要连接到服务端的地址。 |
| struct WebSocket_RequestOptions options | 发起连接的可选参数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |
 
 
  

##### OH_WebSocketClient_Send()

```text
int OH_WebSocketClient_Send(struct WebSocket *client, char *data, size_t length)
```
 
**描述**
 
客户端向服务端发送数据。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**需要权限：** ohos.permission.INTERNET
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |
| char *data | 客户端发送的数据。 |
| size_t length | 客户端发送的数据长度。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |
 
 
  

##### OH_WebSocketClient_Close()

```text
int OH_WebSocketClient_Close(struct WebSocket *client, struct WebSocket_CloseOption options)
```
 
**描述**
 
客户端主动关闭WebSocket连接。
 
**系统能力：** SystemCapability.Communication.NetStack
 
**需要权限：** ohos.permission.INTERNET
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |
| struct WebSocket_CloseOption options | 发起关闭连接的可选参数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |
 
 
  

##### OH_WebSocketClient_Destroy()

```text
int OH_WebSocketClient_Destroy(struct WebSocket *client)
```
 
**描述**
 
释放WebSocket连接上下文和资源。使用方式如下：
 1. 调用[WebSocket_OnCloseCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onclosecallback)订阅WebSocket连接关闭事件，并在该回调函数中调用[OH_WebSocketClient_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h#oh_websocketclient_destroy)方法。
2. 调用[OH_WebSocketClient_Close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h#oh_websocketclient_close)关闭WebSocket连接。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Psa4bVa5Qte8xW8Q5OAOJw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260528T013542Z&HW-CC-Expire=86400&HW-CC-Sign=0FAADBCB07D1716073BAD2F3F2748FC54293A6799775536EB427895E023C321A)
 
 
确保触发[WebSocket_OnCloseCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h#websocket_onclosecallback)回调后再调用该接口，否则系统内存资源被释放后可能出现socket泄露以及连接未关闭的情况。
  

 
**系统能力：** SystemCapability.Communication.NetStack
 
**需要权限：** ohos.permission.INTERNET
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| struct WebSocket *client | 客户端。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回值为0表示执行成功，返回值不为0表示失败。返回值详细信息可以查看OH_Websocket_ErrCode。 |
