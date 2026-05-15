# NetConn_NetCapabilities

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netcapabilities
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct NetConn_NetCapabilities {...} NetConn_NetCapabilities
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

网络能力集。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint32_t linkUpBandwidthKbps | 上行带宽。 |
| uint32_t linkDownBandwidthKbps | 下行带宽。 |
| [NetConn_NetCap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#netconn_netcap) netCaps[[NETCONN_MAX_CAP_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络能力列表。 |
| int32_t netCapsSize | 网络能力列表的实际size。 |
| [NetConn_NetBearerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#netconn_netbearertype) bearerTypes[[NETCONN_MAX_BEARER_TYPE_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 承载类型列表 |
| int32_t bearerTypesSize | 承载类型列表的实际size |
