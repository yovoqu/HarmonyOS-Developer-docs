# NetConn_TraceRouteOption

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteoption
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct NetConn_TraceRouteOption {...} NetConn_TraceRouteOption
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义网络跟踪路由选项。

**起始版本：** 20

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint8_t maxJumpNumber | 探测结果最大跳数，需要和TraceRouteInfo设置一致，最大可设置30跳，默认为30跳。 |
| NetConn_PacketsType packetsType | 探测包协议类型，默认为NETCONN_PACKETS_ICMP。 |
