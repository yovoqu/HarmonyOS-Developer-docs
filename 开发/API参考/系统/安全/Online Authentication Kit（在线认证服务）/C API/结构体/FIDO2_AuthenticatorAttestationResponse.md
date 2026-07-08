# FIDO2_AuthenticatorAttestationResponse

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_attestation_response

#### 概述

认证器声明响应。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| Uint8Buff attestationObject | 声明对象。 |
| Uint8Buff clientDataJson | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| Uint8Buff publicKey | 注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。 |
| Uint8Buff authenticatorData | 认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。 |
| FIDO2_Algorithm publicKeyAlgorithm | 密码算法。 |
| FIDO2_AuthenticatorTransportArray transports | 定义身份认证器访问类型数组。 |
 
 
  

#### 结构体成员变量说明

  

#### attestationObject

```text
Uint8Buff FIDO2_AuthenticatorAttestationResponse::attestationObject
```
 
**描述**
 
声明对象。
 
  

#### authenticatorData

```text
Uint8Buff FIDO2_AuthenticatorAttestationResponse::authenticatorData
```
 
**描述**
 
认证器数据，包含依赖方ID哈希、用户存在/已验证标志位、签名计数器、凭证数据等信息，用于验证认证响应的合法性。
 
  

#### clientDataJson

```json
Uint8Buff FIDO2_AuthenticatorAttestationResponse::clientDataJson
```
 
**描述**
 
获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。
 
  

#### publicKey

```text
Uint8Buff FIDO2_AuthenticatorAttestationResponse::publicKey
```
 
**描述**
 
注册时生成的公钥数据，包含公钥算法类型和密钥参数，用于服务器保存并后续验证认证签名。
 
  

#### publicKeyAlgorithm

```text
FIDO2_Algorithm FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```
 
**描述**
 
密码算法。
 
  

#### transports

```text
FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorAttestationResponse::transports
```
 
**描述**
 
定义身份认证器访问类型数组。
