# FIDO2_AuthenticatorResponse

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_response

#### 概述

定义获取认证器断言响应的结构体。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2（通行密钥服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
**所在头文件：** [fido2_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication_capi_header_fido2)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Uint8Buff authenticatorData | 身份认证器数据。 |
| Uint8Buff signature | FIDO2认证的签名信息。 |
| Uint8Buff userHandle | 用户句柄（用户ID）。默认值为空。长度限制0到4096。可选。 |
| Uint8Buff clientDataJson | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
 
 
  

#### 结构体成员变量说明

  

#### authenticatorData

```text
Uint8Buff FIDO2_AuthenticatorResponse::authenticatorData
```
 
**描述**
 
身份认证器数据。
 
  

#### clientDataJson

```json
Uint8Buff FIDO2_AuthenticatorResponse::clientDataJson
```
 
**描述**
 
获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。
 
  

#### signature

```text
Uint8Buff FIDO2_AuthenticatorResponse::signature
```
 
**描述**
 
FIDO2认证的签名信息。
 
  

#### userHandle

```text
Uint8Buff FIDO2_AuthenticatorResponse::userHandle
```
 
**描述**
 
用户句柄。可选。
