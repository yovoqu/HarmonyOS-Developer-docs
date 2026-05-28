# FIDO2_PublicKeyCredentialRequestOptions

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_request_options

#### 概述

定义通行密钥认证请求参数。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Uint8Buff challenge | 获取挑战值。 |
| uint32_t timeout | 认证操作最长时间，单位为mm。默认为300000（5分钟）。可选。 |
| char * rpId | 依赖方标识（如域名等）。默认空。可选。 |
| FIDO2_PublicKeyCredentialDescriptorArray allowCredentials | 认证凭据的附加参数列表。默认空列表。可选。 |
| FIDO2_UserVerificationRequirement userVerification | 用户认证需求枚举。默认值为FIDO2_PREFERRED。可选。 |
| FIDO2_PublicKeyCredentialHintArray hints | 认证方式指示。默认值为[]。可选。 |
| char * extensions | 扩展名必须是表示Map<string, Object> object的JSON字符串。默认空。可选。 |
 
 
  

#### 结构体成员变量说明

  

#### allowCredentials

```text
FIDO2_PublicKeyCredentialDescriptorArray FIDO2_PublicKeyCredentialRequestOptions::allowCredentials
```
 
**描述**
 
认证凭据的附加参数列表。可选。
 
  

#### challenge

```text
Uint8Buff FIDO2_PublicKeyCredentialRequestOptions::challenge
```
 
**描述**
 
获取挑战值。
 
  

#### extensions

```text
char* FIDO2_PublicKeyCredentialRequestOptions::extensions
```
 
**描述**
 
扩展名必须是表示Map<string, Object> object的JSON字符串。可选。
 
  

#### hints

```text
FIDO2_PublicKeyCredentialHintArray FIDO2_PublicKeyCredentialRequestOptions::hints
```
 
**描述**
 
认证方式指示。默认值为[]。可选。
 
  

#### rpId

```text
char* FIDO2_PublicKeyCredentialRequestOptions::rpId
```
 
**描述**
 
依赖方标识。可选。
 
  

#### timeout

```text
uint32_t FIDO2_PublicKeyCredentialRequestOptions::timeout
```
 
**描述**
 
认证操作最长时间，单位为mm。可选。
 
  

#### userVerification

```text
FIDO2_UserVerificationRequirement FIDO2_PublicKeyCredentialRequestOptions::userVerification
```
 
**描述**
 
用户认证需求枚举。默认值为FIDO2_PREFERRED。可选。
