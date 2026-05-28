# FIDO2_PublicKeyAttestationCredential

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_attestation_credential

#### 概述

定义获取注册结果结构体。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Uint8Buff rawId | 原始凭据标识符。 |
| FIDO2_AuthenticatorAttestationResponse response | 认证器证明响应。 |
| FIDO2_AuthenticatorAttachment authenticatorAttachment | 认证器信息（平台、漫游）。默认值为FIDO2_PLATFORM。可选。 |
| const char * id | 凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。 |
| const char * type | 此属性返回接口对象中指定凭据类型的插槽，它指定此对象所代表的凭据类型。 |
| AuthenticationExtensionsClientOutputs clientExtensionResults | 客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。 |
 
 
  

#### 结构体成员变量说明

  

#### authenticatorAttachment

```text
FIDO2_AuthenticatorAttachment FIDO2_PublicKeyAttestationCredential::authenticatorAttachment
```
 
**描述**
 
认证器信息（平台、漫游）。可选。
 
  

#### clientExtensionResults

```text
AuthenticationExtensionsClientOutputs FIDO2_PublicKeyAttestationCredential::clientExtensionResults
```
 
**描述**
 
客户端扩展结果。当前版本不支持扩展，因此占位符始终为NULL，必须将clientExtensionResults键对应的值解析为{}。
 
  

#### id

```text
const char* FIDO2_PublicKeyAttestationCredential::id
```
 
**描述**
 
凭据的标识符。对于每种类型的凭据，标识符的要求都是不同的。
 
  

#### rawId

```text
Uint8Buff FIDO2_PublicKeyAttestationCredential::rawId
```
 
**描述**
 
原始凭据标识符。
 
  

#### response

```text
FIDO2_AuthenticatorAttestationResponse FIDO2_PublicKeyAttestationCredential::response
```
 
**描述**
 
认证器证明响应。
 
  

#### type

```text
const char* FIDO2_PublicKeyAttestationCredential::type
```
 
**描述**
 
此属性返回接口对象中指定凭据类型的插槽，它指定此对象所代表的凭据类型。
