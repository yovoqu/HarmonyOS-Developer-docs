# Rcp_ClientCertificate

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char * content | 客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。 |
| char * filePath | 客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。 |
| char * key | 客户端证书私钥的文件名。 |
| char * keyPassword | 客户端证书私钥的密码。 |
| Rcp_CertType type | 客户端证书类型。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### content

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* Rcp_ClientCertificate::content
```
 
**描述**
 
客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。
 
  

##### filePath

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* Rcp_ClientCertificate::filePath
```
 
**描述**
 
客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。
 
  

##### key

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* Rcp_ClientCertificate::key
```
 
**描述**
 
客户端证书私钥的文件名。
 
  

##### keyPassword

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
char* Rcp_ClientCertificate::keyPassword
```
 
**描述**
 
客户端证书私钥的密码。
 
  

##### type

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
Rcp_CertType Rcp_ClientCertificate::type
```
 
**描述**
 
客户端证书类型。
