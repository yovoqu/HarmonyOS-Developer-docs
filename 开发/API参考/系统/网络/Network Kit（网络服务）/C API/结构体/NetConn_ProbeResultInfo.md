# NetConn_ProbeResultInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct NetConn_ProbeResultInfo {...} NetConn_ProbeResultInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义探测结果信息。
 
**起始版本：** 20
 
**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)
 
**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t lossRate | 丢包率，百分制，值100表示100%丢包；50表示50%丢包。 |
| uint32_t rtt[NETCONN_MAX_RTT_NUM] | 时延结果，包含最小、最大、平均、标准差。 |
