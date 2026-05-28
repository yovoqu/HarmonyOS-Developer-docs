# Rcp_TransferConfiguration

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

传输配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| bool autoRedirect | 是否自动遵循HTTP重定向响应。true表示开启自动重定向，false表示不开启自动重定向。默认为true。 |
| Rcp_Timeout timeout | 超时配置。如果未设置此选项，将应用默认超时。 |
| bool assumesHTTP3Capable | 是否假定目标服务器支持HTTP/3。true代表假定目标服务器支持HTTP/3，false代表不假定。默认值为false。 |
| Rcp_PathPreference pathPreference | 请求路径首选项。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### assumesHTTP3Capable

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_TransferConfiguration::assumesHTTP3Capable
```
 
**描述**
 
是否假定目标服务器支持HTTP/3。true代表假定目标服务器支持HTTP/3，false代表不假定。默认值为false。
 
  

#### autoRedirect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_TransferConfiguration::autoRedirect
```
 
**描述**
 
是否自动遵循HTTP重定向响应。true表示开启自动重定向，false表示不开启自动重定向。默认为true。
 
  

#### pathPreference

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_PathPreference Rcp_TransferConfiguration::pathPreference
```
 
**描述**
 
请求路径首选项。
 
  

#### timeout

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_Timeout Rcp_TransferConfiguration::timeout
```
 
**描述**
 
超时配置。如果未设置此选项，将应用默认超时。如果已配置，则使用配置的超时时间。
