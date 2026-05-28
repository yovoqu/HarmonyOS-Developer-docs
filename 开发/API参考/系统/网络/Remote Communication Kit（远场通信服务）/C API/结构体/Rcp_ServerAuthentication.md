# Rcp_ServerAuthentication

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

服务器身份验证。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Rcp_Credential credential | 服务器的凭据。 |
| Rcp_AuthenticationType authenticationType | 服务器的身份验证类型。如果未设置，请与服务器协商。 |
 
 
  

##### 结构体成员变量说明

  

##### authenticationType

```text
Rcp_AuthenticationType Rcp_ServerAuthentication::authenticationType
```
 
**描述**
 
服务器的身份验证类型。如果未设置，请与服务器协商。
 
  

##### credential

```text
Rcp_Credential Rcp_ServerAuthentication::credential
```
 
**描述**
 
服务器的凭据。
