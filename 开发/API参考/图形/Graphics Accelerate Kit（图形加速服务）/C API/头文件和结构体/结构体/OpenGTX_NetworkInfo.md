# OpenGTX_NetworkInfo

更新时间：2026-05-19 09:13:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_info
**支持设备：** Phone | Tablet | TV

##### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [opengtx_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)
 
  

##### 汇总

**支持设备：** Phone | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| OpenGTX_NetworkLatency networkLatency | 游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。 |
| char* networkServerIP | 游戏服务器的IP地址，字节长度范围[1,256]。示例："10.10.10.10"。该参数支持IPv4和IPv6地址格式，长度范围为1-256字节；不支持空字符串或null值；建议在设置前进行格式校验。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

##### networkLatency

**支持设备：** Phone | Tablet | TV

```text
OpenGTX_NetworkLatency OpenGTX_NetworkInfo::networkLatency
```
 
**描述**
 
游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。
 
  

##### networkServerIP

**支持设备：** Phone | Tablet | TV

```text
char* OpenGTX_NetworkInfo::networkServerIP
```
 
**描述**
 
游戏服务器的IP地址，字节长度范围[1,256]。
