# Rcp_DnsOverHttps

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char * url | DOH服务器的URL。 |
| bool skipCertificatesValidation | 判断是否跳过证书验证。true代表跳过，false代表不跳过，默认值为false。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### skipCertificatesValidation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool Rcp_DnsOverHttps::skipCertificatesValidation
```
 
**描述**
 
判断是否跳过证书验证。默认值为false。
 
  

#### url

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* Rcp_DnsOverHttps::url
```
 
**描述**
 
DOH服务器的URL。
