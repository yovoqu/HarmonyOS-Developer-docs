# crypto_signature.h

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义签名验签接口。
 
**引用文件：** <CryptoArchitectureKit/crypto_signature.h>
 
**库：** libohcrypto.so
 
**系统能力：** SystemCapability.Security.CryptoFramework
 
**起始版本：** 12
 
**相关模块：** [CryptoSignatureApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CryptoVerify | OH_CryptoVerify | 验签结构体，表示验签上下文。 |
| OH_CryptoSign | OH_CryptoSign | 签名结构体，表示签名上下文。 |
| OH_CryptoEccSignatureSpec | OH_CryptoEccSignatureSpec | ECC签名规格结构体，表示ECC签名规格。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| CryptoSignature_ParamType | CryptoSignature_ParamType | 定义签名参数类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify) | 根据给定的算法名称创建验签上下文。 注意：创建的资源必须通过OH_CryptoVerify_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey) | 使用给定的公钥初始化验签上下文。 |
| OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in) | 追加待验签的消息数据。 |
| bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData) | 验签消息数据。 |
| OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData, Crypto_DataBlob *rawSignData) | 恢复签名数据，仅支持RSA算法。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放rawSignData内存。 |
| const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx) | 获取验签上下文的算法名称。 |
| OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value) | 设置验签上下文的指定参数。 |
| OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value) | 获取验签上下文的指定参数。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放value内存。 |
| void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx) | 销毁验签上下文。 |
| OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign) | 根据给定的算法名称创建签名上下文。 注意：创建的资源必须通过OH_CryptoSign_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey) | 初始化签名上下文。 |
| OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in) | 更新待签名的数据。 |
| OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out) | 结束签名操作。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放out内存。 |
| const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx) | 获取签名上下文的算法名称。 |
| OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, const Crypto_DataBlob *value) | 设置签名上下文的指定参数。 |
| OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value) | 获取签名上下文的指定参数。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放value内存。 |
| void OH_CryptoSign_Destroy(OH_CryptoSign *ctx) | 销毁签名上下文。 |
| OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature, OH_CryptoEccSignatureSpec **spec) | 创建ECC签名规格，同时支持SM2签名。 注意：创建的资源必须通过OH_CryptoEccSignatureSpec_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s) | 获取ECC签名规格中的r和s值。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放r和s内存。 |
| OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s) | 设置ECC签名规格中的r和s值。 |
| OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out) | 将ECC签名规格编码为DER格式的签名数据。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放out内存。 |
| void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec) | 销毁ECC签名规格。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### CryptoSignature_ParamType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum CryptoSignature_ParamType
```
 
**描述**
 
定义签名参数类型。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| CRYPTO_PSS_MD_NAME_STR = 100 | 表示消息摘要函数的算法名称。 |
| CRYPTO_PSS_MGF_NAME_STR = 101 | 表示掩码生成函数的算法名称。 |
| CRYPTO_PSS_MGF1_NAME_STR = 102 | 表示MGF1掩码生成函数的消息摘要参数。 |
| CRYPTO_PSS_SALT_LEN_INT = 103 | 表示盐值的字节长度。 |
| CRYPTO_PSS_TRAILER_FIELD_INT = 104 | 表示尾部字段的值。 |
| CRYPTO_SM2_USER_ID_DATABLOB = 105 | 表示SM2算法的用户ID值。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_CryptoVerify_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify)
```
 
**描述**
 
根据给定的算法名称创建验签上下文。
 
注意：创建的资源必须通过[OH_CryptoVerify_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_destroy)销毁。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char *algoName | [in] 验签算法名称，不能为NULL。取值如下： - RSA PKCS1模式：格式为"RSA\|PKCS1\|摘要"，示例："RSA\|PKCS1\|SHA256"、"RSA\|PKCS1\|SHA512"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - RSA PSS模式：格式为"RSA\|PSS\|摘要\|MGF1摘要"，示例："RSA\|PSS\|SHA256\|MGF1_SHA256"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。MGF1摘要支持"MGF1_MD5"、"MGF1_SHA1"、"MGF1_SHA224"、"MGF1_SHA256"、"MGF1_SHA384"、"MGF1_SHA512"。 - RSA验签恢复：格式为"RSA\|PKCS1\|摘要\|Recover"，示例："RSA\|PKCS1\|SHA256\|Recover"、"RSA\|PKCS1\|SHA512\|Recover"。摘要支持"NoHash"、"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - ECDSA算法：格式为"ECC\|摘要"，示例："ECC\|SHA256"、"ECC\|SHA384"。摘要支持"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - DSA算法：格式为"DSA\|摘要"，示例："DSA\|SHA256"、"DSA\|SHA384"。摘要支持"NoHash"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - SM2算法：取值为"SM2\|SM3"。 - Ed25519算法：取值为"Ed25519"。 |
| OH_CryptoVerify **verify | [out] 指向验签上下文指针的指针。verify不能为NULL，*verify必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：verify为NULL，algoName为NULL。 CRYPTO_NOT_SUPPORTED：不支持该算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
**参考：**
 
[OH_CryptoVerify_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_init) 使用给定的公钥初始化验签上下文。
 
  

#### OH_CryptoVerify_Init()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey)
```
 
**描述**
 
使用给定的公钥初始化验签上下文。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| OH_CryptoPubKey *pubKey | [in] 公钥。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：ctx或pubKey为NULL，或密钥类型与签名算法不匹配。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：验签初始化失败。 |
 
 
**参考：**
 
[OH_CryptoVerify_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_update) 追加待验签的消息数据。
 
[OH_CryptoVerify_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_final) 验签消息数据。
 
[OH_CryptoVerify_Recover](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_recover) 恢复签名数据。
 
  

#### OH_CryptoVerify_Update()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in)
```
 
**描述**
 
追加待验签的消息数据。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| Crypto_DataBlob *in | [in] 待验签的数据。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：ctx或in为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_INVALID_CALL：无效的函数调用。适用版本：26.0.0+ CRYPTO_OPERTION_ERROR：验签更新失败。 |
 
 
**参考：**
 
[OH_CryptoVerify_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoverify_final) 验签消息数据。
 
  

#### OH_CryptoVerify_Final()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData)
```
 
**描述**
 
验签消息数据。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| Crypto_DataBlob *in | [in] 待验签的数据。如果数据已通过OH_CryptoVerify_Update接口更新了所有数据，此参数可以为NULL。 |
| Crypto_DataBlob *signData | [in] 签名数据。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| bool | 返回bool类型的验签结果。返回true表示验签通过，返回false表示验签失败。可能的原因：公钥不正确、签名数据损坏、摘要算法不匹配、 填充模式不匹配，或数据与原始签名数据不匹配。 |
 
 
  

#### OH_CryptoVerify_Recover()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData, Crypto_DataBlob *rawSignData)
```
 
**描述**
 
恢复签名数据，仅支持RSA算法。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放rawSignData内存。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| Crypto_DataBlob *signData | [in] 签名数据。不能为NULL。 |
| Crypto_DataBlob *rawSignData | [out] 指向用于存储原始签名数据的Crypto_DataBlob结构体的指针。不能为NULL。 调用前需将rawSignData初始化为{0}，不要预分配rawSignData->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：ctx、signData或rawSignData为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_INVALID_CALL：无效的函数调用。 适用版本：26.0.0+ CRYPTO_OPERTION_ERROR：恢复失败。可能的原因：签名数据长度与RSA密钥模数大小不匹配。 |
 
 
  

#### OH_CryptoVerify_GetAlgoName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx)
```
 
**描述**
 
获取验签上下文的算法名称。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char * | 返回验签算法名称，不需要调用者释放，在上下文销毁后不可使用。 |
 
 
  

#### OH_CryptoVerify_SetParam()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```
 
**描述**
 
设置验签上下文的指定参数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| CryptoSignature_ParamType type | [in] 签名参数类型。 |
| Crypto_DataBlob *value | [in] 输入数据。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：ctx或value为NULL，value->data为NULL， value->len与type期望的大小不匹配，或type不是有效的CryptoSignature_ParamType。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：设置参数失败。 |
 
 
  

#### OH_CryptoVerify_GetParam()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```
 
**描述**
 
获取验签上下文的指定参数。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放value内存。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。不能为NULL。 |
| CryptoSignature_ParamType type | [in] 签名参数类型。 |
| Crypto_DataBlob *value | [out] 指向用于存储输出数据的Crypto_DataBlob结构体的指针。不能为NULL。 调用前需将value初始化为{0}，不要预分配value->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_INVALID_PARAMS：ctx或value为NULL，或type不是有效的CryptoSignature_ParamType。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：输出数据的内存分配失败。 CRYPTO_OPERTION_ERROR：获取参数失败。 |
 
 
  

#### OH_CryptoVerify_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx)
```
 
**描述**
 
销毁验签上下文。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoVerify *ctx | [in] 验签上下文。 |
 
 
  

#### OH_CryptoSign_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign)
```
 
**描述**
 
根据给定的算法名称创建签名上下文。
 
注意：创建的资源必须通过[OH_CryptoSign_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptosign_destroy)销毁。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char *algoName | [in] 签名算法名称，不能为NULL。取值如下： - RSA PKCS1模式：格式为"RSA\|PKCS1\|摘要"，示例："RSA\|PKCS1\|SHA256"、"RSA\|PKCS1\|SHA512"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - RSA PSS模式：格式为"RSA\|PSS\|摘要\|MGF1摘要"，示例："RSA\|PSS\|SHA256\|MGF1_SHA256"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。MGF1摘要支持"MGF1_MD5"、"MGF1_SHA1"、"MGF1_SHA224"、"MGF1_SHA256"、"MGF1_SHA384"、"MGF1_SHA512"。 - RSA仅签名：格式为"RSA\|PKCS1\|摘要\|OnlySign"，示例："RSA\|PKCS1\|SHA256\|OnlySign"、"RSA\|PKCS1\|SHA512\|OnlySign"。摘要支持"NoHash"、"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - ECDSA算法：格式为"ECC\|摘要"，示例："ECC\|SHA256"、"ECC\|SHA384"。摘要支持"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - DSA算法：格式为"DSA\|摘要"，示例："DSA\|SHA256"、"DSA\|SHA384"。摘要支持"NoHash"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。 - SM2算法：取值为"SM2\|SM3"。 - Ed25519算法：取值为"Ed25519"。 |
| OH_CryptoSign **sign | [out] 指向签名上下文指针的指针。sign不能为NULL，*sign必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：sign或algoName为NULL。 CRYPTO_NOT_SUPPORTED：不支持该算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
**参考：**
 
[OH_CryptoSign_Init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptosign_init) 初始化签名上下文。
 
  

#### OH_CryptoSign_Init()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey)
```
 
**描述**
 
初始化签名上下文。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
| OH_CryptoPrivKey *privKey | [in] 私钥。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或privKey为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：签名初始化失败。 |
 
 
**参考：**
 
[OH_CryptoSign_Update](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptosign_update) 更新待签名的数据。
 
[OH_CryptoSign_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptosign_final) 结束签名操作。
 
  

#### OH_CryptoSign_Update()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in)
```
 
**描述**
 
更新待签名的数据。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
| const Crypto_DataBlob *in | [in] 待签名的数据。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或in为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_INVALID_CALL：无效的函数调用。适用版本：26.0.0+ CRYPTO_OPERTION_ERROR：签名更新失败。 |
 
 
**参考：**
 
[OH_CryptoSign_Final](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptosign_final) 结束签名操作。
 
  

#### OH_CryptoSign_Final()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```
 
**描述**
 
结束签名操作。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
| const Crypto_DataBlob *in | [in] 待签名的数据。如果数据已通过OH_CryptoSign_Update接口更新了所有数据，此参数可以为NULL。 |
| Crypto_DataBlob *out | [out] 指向用于存储签名结果的Crypto_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或out为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：签名失败。 |
 
 
  

#### OH_CryptoSign_GetAlgoName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx)
```
 
**描述**
 
获取签名上下文的算法名称。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char * | 返回签名算法名称，不需要调用者释放，在上下文销毁后不可使用。 |
 
 
  

#### OH_CryptoSign_SetParam()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, const Crypto_DataBlob *value)
```
 
**描述**
 
设置签名上下文的指定参数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
| CryptoSignature_ParamType type | [in] 签名参数类型。 |
| const Crypto_DataBlob *value | [in] 输入数据。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或value为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoSign_GetParam()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```
 
**描述**
 
获取签名上下文的指定参数。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放value内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。不能为NULL。 |
| CryptoSignature_ParamType type | [in] 签名参数类型。 |
| Crypto_DataBlob *value | [out] 指向用于存储输出数据的Crypto_DataBlob结构体的指针。不能为NULL。 调用前需将value初始化为{0}，不要预分配value->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或value为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 #CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoSign_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoSign_Destroy(OH_CryptoSign *ctx)
```
 
**描述**
 
销毁签名上下文。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoSign *ctx | [in] 签名上下文。 |
 
 
  

#### OH_CryptoEccSignatureSpec_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature, OH_CryptoEccSignatureSpec **spec)
```
 
**描述**
 
创建ECC签名规格，同时支持SM2签名。
 
注意：创建的资源必须通过[OH_CryptoEccSignatureSpec_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoeccsignaturespec_destroy)销毁。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| Crypto_DataBlob *eccSignature | [in] DER格式的ECC签名数据，如果为NULL则创建空的签名规格。 |
| OH_CryptoEccSignatureSpec **spec | [out] 指向ECC签名规格指针的指针。spec不能为NULL，*spec必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：spec为NULL或spec不为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：解析eccSignature失败，或eccSignature包含无效的DER编码ECDSA-Sig-Value。 |
 
 
**参考：**
 
[OH_CryptoEccSignatureSpec_GetRAndS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoeccsignaturespec_getrands) 获取ECC签名规格中的r和s值。
 
[OH_CryptoEccSignatureSpec_SetRAndS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoeccsignaturespec_setrands) 设置ECC签名规格中的r和s值。
 
  

#### OH_CryptoEccSignatureSpec_GetRAndS()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```
 
**描述**
 
获取ECC签名规格中的r和s值。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放r和s内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoEccSignatureSpec *spec | [in] ECC签名规格。不能为NULL。 |
| Crypto_DataBlob *r | [out] 指向用于存储r值的Crypto_DataBlob结构体的指针。不能为NULL。调用前需将r初始化为{0}，不要预分配r->data内存。 |
| Crypto_DataBlob *s | [out] 指向用于存储s值的Crypto_DataBlob结构体的指针。不能为NULL。调用前需将s初始化为{0}，不要预分配s->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：spec、r或s为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoEccSignatureSpec_SetRAndS()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```
 
**描述**
 
设置ECC签名规格中的r和s值。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoEccSignatureSpec *spec | [in] ECC签名规格。不能为NULL。 |
| Crypto_DataBlob *r | [in] r值。本接口会对r和s中的数据进行深拷贝，调用者在接口返回后可立即释放r和s。不能为NULL。 |
| Crypto_DataBlob *s | [in] s值。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：spec、r或s为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
**参考：**
 
[OH_CryptoEccSignatureSpec_Encode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h#oh_cryptoeccsignaturespec_encode) 将ECC签名规格编码为DER格式的签名数据。
 
  

#### OH_CryptoEccSignatureSpec_Encode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out)
```
 
**描述**
 
将ECC签名规格编码为DER格式的签名数据。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoEccSignatureSpec *spec | [in] ECC签名规格。不能为NULL。 |
| Crypto_DataBlob *out | [out] 指向用于存储编码签名数据的Crypto_DataBlob结构体的指针。不能为NULL。 调用前需将out初始化为{0}，不要预分配out->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：spec或out为NULL，或尚未通过OH_CryptoEccSignatureSpec_SetRAndS设置r和s值。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：编码失败。 |
 
 
  

#### OH_CryptoEccSignatureSpec_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec)
```
 
**描述**
 
销毁ECC签名规格。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoEccSignatureSpec *spec | [in] ECC签名规格。 |
