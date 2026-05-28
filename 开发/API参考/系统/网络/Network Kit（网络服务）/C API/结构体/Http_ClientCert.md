# Http_ClientCert

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-clientcert
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Http_ClientCert {...} Http_ClientCert
```
  

##### 概述

发送到服务端的客户端证书配置，服务端将通过客户端证书校验客户端身份。
 
**起始版本：** 20
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char *certPath | 证书路径。 |
| Http_CertType type | 证书类型，默认是PEM，参考Http_CertType。 |
| char *keyPath | 证书密钥的路径。 |
| char *keyPassword | 证书密钥的密码。 |
