# FIDO2_AuthenticatorMetadataArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array

##### 概述

描述支持的认证器数组。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t number | 认证器数目。 |
| FIDO2_AuthenticatorMetadata * authenticators | 认证器支持的扩展。 |
 
 
  

##### 结构体成员变量说明

  

##### authenticators

```text
FIDO2_AuthenticatorMetadata* FIDO2_AuthenticatorMetadataArray::authenticators
```
 
**描述**
 
认证器支持的扩展。
 
  

##### number

```text
uint32_t FIDO2_AuthenticatorMetadataArray::number
```
 
**描述**
 
认证器数目。
