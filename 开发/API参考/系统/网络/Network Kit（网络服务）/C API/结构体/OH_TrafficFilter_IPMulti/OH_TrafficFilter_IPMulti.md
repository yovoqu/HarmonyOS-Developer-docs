# OH_TrafficFilter_IPMulti

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipmulti
**支持设备：** PC/2in1

```text
typedef struct OH_TrafficFilter_IPMulti {...} OH_TrafficFilter_IPMulti
```
  

#### 概述

**支持设备：** PC/2in1

多IP匹配的IP匹配值。
 
**起始版本：** 26.0.0
 
**相关模块：** [TrafficFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter)
 
**所在头文件：** [net_trafficfilter_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-trafficfilter-type-h)
 
  

#### 汇总

**支持设备：** PC/2in1

  

#### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| uint32_t ipCount | 数组中的IP地址数量。 起始版本： 26.0.0 |
| OH_TrafficFilter_IPAddress ips[OH_TRAFFICFILTER_MAX_MULTI_IP_COUNT] | IP地址数组。 起始版本： 26.0.0 |
