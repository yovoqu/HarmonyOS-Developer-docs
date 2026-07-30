# OH_TrafficFilter_IPCidr

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipcidr
**支持设备：** PC/2in1

```text
typedef struct OH_TrafficFilter_IPCidr {...} OH_TrafficFilter_IPCidr
```
  

#### 概述

**支持设备：** PC/2in1

CIDR（Classless Inter-Domain Routing，无类别域间路由）匹配的IP匹配值。
 
**起始版本：** 26.0.0
 
**相关模块：** [TrafficFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter)
 
**所在头文件：** [net_trafficfilter_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-trafficfilter-type-h)
 
  

#### 汇总

**支持设备：** PC/2in1

  

#### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| OH_TrafficFilter_IPAddress base | CIDR（无类别域间路由）块的基IP地址。 起始版本： 26.0.0 |
| uint8_t prefixLen | CIDR前缀长度，表示网络掩码中前导1的位数（如24表示子网掩码255.255.255.0）。 起始版本： 26.0.0 |
