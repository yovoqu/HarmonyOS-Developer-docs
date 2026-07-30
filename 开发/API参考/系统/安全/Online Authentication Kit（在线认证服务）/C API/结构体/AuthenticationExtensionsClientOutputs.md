# AuthenticationExtensionsClientOutputs

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs

#### 概述

身份认证扩展输出。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2（通行密钥服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
**所在头文件：** [fido2_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char * placeholder | 占位符，表示返回的JSON消息中包含key值"clientExtensionResults"。始终返回NULL。 |
 
 
  

#### 结构体成员变量说明

  

#### placeholder

```text
char* AuthenticationExtensionsClientOutputs::placeholder
```
 
**描述**
 
占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。该值始终返回NULL。
