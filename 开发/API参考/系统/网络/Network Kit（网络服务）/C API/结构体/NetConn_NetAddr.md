# NetConn_NetAddr

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```
  

##### 概述

网络地址。
 
**起始版本：** 11
 
**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)
 
**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint8_t family | 网络地址族。 |
| uint8_t prefixlen | 前缀长度。 |
| uint8_t port | 端口号。 |
| char address[NETCONN_MAX_STR_LEN] | 地址。 |
