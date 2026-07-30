# crypto_kdf.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义密钥派生接口。
 
**引用文件：** <CryptoArchitectureKit/crypto_kdf.h>
 
**库：** libohcrypto.so
 
**系统能力：** SystemCapability.Security.CryptoFramework
 
**起始版本：** 20
 
**相关模块：** [CryptoKdfApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CryptoKdf | OH_CryptoKdf | KDF结构体，表示KDF上下文。 |
| OH_CryptoKdfParams | OH_CryptoKdfParams | KDF参数结构体，表示KDF参数。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| CryptoKdf_ParamType | CryptoKdf_ParamType | 定义KDF参数类型。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params) | 创建KDF参数。 注意：创建的资源必须通过OH_CryptoKdfParams_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value) | 设置KDF参数。 |
| void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params) | 销毁KDF参数。 |
| OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx) | 根据给定的算法名称创建KDF上下文。 注意：创建的资源必须通过OH_CryptoKdf_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key) | 派生密钥。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放key内存。 |
| void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx) | 销毁KDF上下文。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### CryptoKdf_ParamType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum CryptoKdf_ParamType
```
 
**描述**
 
定义KDF参数类型。
 
**起始版本：** 20
  
| 枚举项 | 描述 |
| --- | --- |
| CRYPTO_KDF_KEY_DATABLOB = 0 | 表示KDF的密钥或密码。 |
| CRYPTO_KDF_SALT_DATABLOB = 1 | 表示KDF的盐值。 |
| CRYPTO_KDF_INFO_DATABLOB = 2 | 表示KDF的Info信息。 |
| CRYPTO_KDF_ITER_COUNT_INT = 3 | 表示PBKDF2的迭代次数。 |
| CRYPTO_KDF_SCRYPT_N_UINT64 = 4 | 表示SCRYPT KDF的n参数。 |
| CRYPTO_KDF_SCRYPT_R_UINT64 = 5 | 表示SCRYPT KDF的r参数。 |
| CRYPTO_KDF_SCRYPT_P_UINT64 = 6 | 表示SCRYPT KDF的p参数。 |
| CRYPTO_KDF_SCRYPT_MAX_MEM_UINT64 = 7 | 表示SCRYPT KDF的最大内存参数。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_CryptoKdfParams_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)
```
 
**描述**
 
创建KDF参数。
 
注意：创建的资源必须通过[OH_CryptoKdfParams_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_destroy)销毁。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char *algoName | [in] KDF参数算法名称，不能为NULL。取值如下： - 从API version 20开始支持"HKDF"、"PBKDF2"、"SCRYPT"。 - 从API version 22开始支持"X963KDF"。 |
| OH_CryptoKdfParams **params | [out] 指向KDF参数指针的指针。params不能为NULL，*params必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：algoName或params为NULL， 或者algoName不是支持的KDF类型。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
**参考：**
 
[OH_CryptoKdfParams_SetParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdfparams_setparam) 设置KDF参数。
 
  

#### OH_CryptoKdfParams_SetParam()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value)
```
 
**描述**
 
设置KDF参数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdfParams *params | [in] KDF参数。不能为NULL。 |
| CryptoKdf_ParamType type | [in] KDF参数类型。 |
| Crypto_DataBlob *value | [in] KDF参数值。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：params或value为NULL， value->data为NULL，或者type对于KDF算法无效。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：参数拷贝内存分配失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoKdfParams_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)
```
 
**描述**
 
销毁KDF参数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdfParams *params | [in] KDF参数。 |
 
 
  

#### OH_CryptoKdf_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)
```
 
**描述**
 
根据给定的算法名称创建KDF上下文。
 
注意：创建的资源必须通过[OH_CryptoKdf_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_destroy)销毁。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const char *algoName | [in] KDF算法名称。不能为NULL。格式为"KDF类型\|摘要算法"，取值如下： - 从API version 20开始支持"PBKDF2\|SHA1"、"PBKDF2\|SHA224"、"PBKDF2\|SHA256"、"PBKDF2\|SHA384"、"PBKDF2\|SHA512"、"PBKDF2\|SM3"。从API version 26.0.0开始支持"PBKDF2\|SHA3-256"、"PBKDF2\|SHA3-384"、"PBKDF2\|SHA3-512"。 - 从API version 20开始支持"HKDF\|SHA1"、"HKDF\|SHA224"、"HKDF\|SHA256"、"HKDF\|SHA384"、"HKDF\|SHA512"、"HKDF\|SM3"。HKDF支持可选的第三个参数指定模式："EXTRACT_AND_EXPAND"（默认）、"EXTRACT_ONLY"、"EXPAND_ONLY"，示例："HKDF\|SHA256\|EXTRACT_ONLY"。从API version 26.0.0开始支持"HKDF\|SHA3-256"、"HKDF\|SHA3-384"、"HKDF\|SHA3-512"。 - 从API version 20开始支持"SCRYPT"。 - 从API version 22开始支持"X963KDF\|SHA1"、"X963KDF\|SHA224"、"X963KDF\|SHA256"、"X963KDF\|SHA384"、"X963KDF\|SHA512"。从API version 26.0.0开始支持"X963KDF\|SHA3-256"、"X963KDF\|SHA3-384"、"X963KDF\|SHA3-512"。 |
| OH_CryptoKdf **ctx | [out] 指向KDF上下文指针的指针。ctx不能为NULL，*ctx必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：algoName或ctx为NULL。 CRYPTO_NOT_SUPPORTED：不支持的算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
**参考：**
 
[OH_CryptoKdf_Derive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h#oh_cryptokdf_derive) 派生密钥。
 
  

#### OH_CryptoKdf_Derive()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key)
```
 
**描述**
 
派生密钥。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放key内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdf *ctx | [in] KDF上下文。不能为NULL。 |
| const OH_CryptoKdfParams *params | [in] KDF参数。不能为NULL。 |
| int keyLen | [in] 派生密钥的字节长度。 |
| Crypto_DataBlob *key | [out] 指向用于存储派生密钥的Crypto_DataBlob结构体的指针。不能为NULL。 调用前需将key初始化为{0}，不要预分配key->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx、params或key为NULL， 或者keyLen小于等于0，或者缺少必需的参数（如HKDF的密钥、Scrypt的密码或盐值）。 CRYPTO_NOT_SUPPORTED：不支持的算法。 CRYPTO_MEMORY_ERROR：内存分配失败。 CRYPTO_OPERTION_ERROR：密钥派生失败。 |
 
 
  

#### OH_CryptoKdf_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)
```
 
**描述**
 
销毁KDF上下文。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdf *ctx | [in] KDF上下文。 |
