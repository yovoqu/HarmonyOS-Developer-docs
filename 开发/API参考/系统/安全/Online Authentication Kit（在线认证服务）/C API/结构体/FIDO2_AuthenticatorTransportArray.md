# FIDO2_AuthenticatorTransportArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array


## 概述

认证器传输方式数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)


## 汇总


### 成员变量


| 名称 | 描述 |
| --- | --- |
| uint32_t [transportNum](#transportnum) | 传输方式数量。 |
| [FIDO2_AuthenticatorTransport](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_authenticatortransport-1) * [transports](#transports) | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |


## 结构体成员变量说明


### transportNum


```cpp
uint32_t FIDO2_AuthenticatorTransportArray::transportNum
```

**描述**

传输方式数量。


### transports


```cpp
FIDO2_AuthenticatorTransport* FIDO2_AuthenticatorTransportArray::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。
