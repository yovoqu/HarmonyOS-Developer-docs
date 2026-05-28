# NetConn_NetHandleList

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

网络列表。
 
**起始版本：** 11
 
**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)
 
**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| NetConn_NetHandle netHandles[NETCONN_MAX_NET_SIZE] | netHandle列表。 |
| int32_t netHandleListSize | netHandleList的实际大小。 |
