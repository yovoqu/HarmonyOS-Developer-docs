# OH_TrafficFilter_IPAddress

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipaddress
**支持设备：** PC/2in1

```text
typedef struct OH_TrafficFilter_IPAddress {...} OH_TrafficFilter_IPAddress
```
  

#### 概述

**支持设备：** PC/2in1

二进制形式的IP地址，支持IPv4和IPv6。
 
**起始版本：** 26.0.0
 
**相关模块：** [TrafficFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter)
 
**所在头文件：** [net_trafficfilter_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-trafficfilter-type-h)
 
  

#### 汇总

**支持设备：** PC/2in1

  

#### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| OH_TrafficFilter_IPFamily family | 地址族。若指定为OH_TRAFFICFILTER_IP_FAMILY_UNSPEC，默认使用IPv4。 起始版本： 26.0.0 |
| uint8_t addr[OH_TRAFFICFILTER_IP_ADDRLEN] | IP地址字节。字节必须以网络字节序存储。对于IPv4，addr[0]到addr[3]存储IPv4地址，addr[4]到addr[15]必须设置为0。对于IPv6，addr[0]到addr[15]存储IPv6地址。如果字节与family要求的地址布局不匹配，使用该结构的接口将返回OH_TRAFFICFILTER_ERROR_INVALID_PARAM。 起始版本： 26.0.0 |
