# NetConn_TraceRouteInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义跟踪路由信息。
 
**起始版本：** 20
 
**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)
 
**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t jumpNo | 跳数。 |
| char address[NETCONN_MAX_STR_LEN] | 主机名或地址。 |
| uint32_t rtt[NETCONN_MAX_RTT_NUM] | 往返时间（单位：毫秒)，包含最大、最小、平均、标准差。 |
