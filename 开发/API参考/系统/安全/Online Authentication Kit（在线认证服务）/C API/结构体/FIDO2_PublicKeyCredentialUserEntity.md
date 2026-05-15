# FIDO2_PublicKeyCredentialUserEntity

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_user_entity


## 概述

创建新凭据时用户的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)


## 汇总


### 成员变量


| 名称 | 描述 |
| --- | --- |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [id](#id) | 凭据的标识符。 |
| char * [displayName](#displayname) | 前台显示的用户名。 |
| char * [name](#name) | 用户名。 |


## 结构体成员变量说明


### displayName


```cpp
char* FIDO2_PublicKeyCredentialUserEntity::displayName
```

**描述**

前台显示的用户名。


### id


```cpp
Uint8Buff FIDO2_PublicKeyCredentialUserEntity::id
```

**描述**

凭据的标识符。


### name


```cpp
char* FIDO2_PublicKeyCredentialUserEntity::name
```

**描述**

用户名。
