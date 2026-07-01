# WebSocket发送消息失败，错误码是-1的原因

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-103

## WebSocket发送消息失败，错误码是-1的原因
 


##### 问题现象

通过WebSocket发送消息，返回错误码为-1，请问是什么原因？
 
```text
09-26 14:46:56.819  9308  9456 I C015B0/***/NETSTACK: [websocket_exec.cpp:1003] OnClose 1011 The link is down
09-26 14:46:56.824  9308  9308 I C015B0/***/NETSTACK: [module_template.h:46] js invoke WebSocketSend
09-26 14:46:56.824  9308  9308 I C015B0/***/NETSTACK: [send_context.cpp:38] SendContext data is String
09-26 14:46:56.825  9308  9325 E C015B0/***/NETSTACK: [websocket_exec.cpp:809] user data is nullptr
09-26 14:46:56.825  9308  9308 D A0000F/***/Utils: *** sendMessage the subscribeDevice result is: undefined
09-26 14:46:56.825  9308  9308 E A0FFFF/***/Utils: *** sendMessage subscribeDevice got an error! Err.code is: -1, Err.message is: Websocket Unknown Other Error
```
 
 

##### 解决方案

根据如上日志分析，WebSocket没有连接到服务器导致该问题出现：
 
- 确定服务器是否可连接：
使用ping命令检查服务器是否在线，是否响应ICMP请求，成功时显示响应时间和数据包丢失率。
- 使用telnet或nc测试端口检查服务器的指定端口是否开放，连接后显示空白或服务器响应。
- 通过浏览器或curl发起HTTP请求，成功后返回HTTP状态码（如200、OK）。

 

- 确认服务器可连接后，使用WebSocket进行连接服务器，详情可见[WebSocket使用示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/websocket-connection)。
