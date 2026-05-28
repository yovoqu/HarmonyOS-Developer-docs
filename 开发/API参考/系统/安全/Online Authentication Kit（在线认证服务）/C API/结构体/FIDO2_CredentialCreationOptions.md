# FIDO2_CredentialCreationOptions

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_options

#### 概述

凭据请求的选项。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

#### 汇总

  

#### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| FIDO2_CredentialMediationRequirement mediation | 该操作是否需要用户参与。 |
| FIDO2_PublicKeyCredentialCreationOptions publicKey | publicKey凭证请求的选项。 |
 
 
  

#### 结构体成员变量说明

  

#### mediation

```text
FIDO2_CredentialMediationRequirement FIDO2_CredentialCreationOptions::mediation
```
 
**描述**
 
操作是否需要用户参与。
 
  

#### publicKey

```text
FIDO2_PublicKeyCredentialCreationOptions FIDO2_CredentialCreationOptions::publicKey
```
 
**描述**
 
publicKey凭证请求的选项。
