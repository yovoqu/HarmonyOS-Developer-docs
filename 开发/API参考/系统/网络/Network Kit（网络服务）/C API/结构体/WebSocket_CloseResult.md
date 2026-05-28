# WebSocket_CloseResult

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeresult
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct WebSocket_CloseResult {...}
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

websocket客户端接收到服务端关闭的参数。
 
**起始版本：** 11
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t code | 错误值。 |
| const char *reason | 错误原因。 |
