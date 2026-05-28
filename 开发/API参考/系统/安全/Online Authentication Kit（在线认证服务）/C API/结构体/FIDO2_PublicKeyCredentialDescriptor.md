# FIDO2_PublicKeyCredentialDescriptor

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor

#### 概述

用于注册或认证凭据的参数。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| FIDO2_PublicKeyCredentialType type | 凭证类型。 |
| Uint8Buff id | 凭据标识符。 |
| FIDO2_AuthenticatorTransportArray transports | 定义身份认证器访问类型数组。 |
 
 
  

#### 结构体成员变量说明

  

#### id

```text
Uint8Buff FIDO2_PublicKeyCredentialDescriptor::id
```
 
**描述**
 
凭据标识符。
 
  

#### transports

```text
FIDO2_AuthenticatorTransportArray FIDO2_PublicKeyCredentialDescriptor::transports
```
 
**描述**
 
定义身份认证器访问类型数组。
 
  

#### type

```text
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialDescriptor::type
```
 
**描述**
 
凭证类型。
