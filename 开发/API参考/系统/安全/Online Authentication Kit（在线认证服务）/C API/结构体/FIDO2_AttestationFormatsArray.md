# FIDO2_AttestationFormatsArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___attestation_formats_array

##### 概述

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t attestationFormatsNum | PubKeyCredParam个数。 |
| char ** attestationFormats | 认证凭据的附加参数列表。 |
 
 
  

##### 结构体成员变量说明

  

##### attestationFormats

```text
char** FIDO2_AttestationFormatsArray::attestationFormats
```
 
**描述**
 
认证凭据的附加参数列表。
 
  

##### attestationFormatsNum

```text
uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```
 
**描述**
 
认证凭据的附加参数列表长度。
