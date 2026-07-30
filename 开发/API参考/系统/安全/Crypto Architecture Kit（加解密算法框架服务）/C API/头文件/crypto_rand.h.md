# crypto_rand.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义随机数生成器接口。
 
**引用文件：** <CryptoArchitectureKit/crypto_rand.h>
 
**库：** libohcrypto.so
 
**系统能力：** SystemCapability.Security.CryptoFramework
 
**起始版本：** 20
 
**相关模块：** [CryptoRandApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CryptoRand | OH_CryptoRand | 随机数生成器结构体，表示随机数生成器上下文。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_Crypto_ErrCode OH_CryptoRand_Create(OH_CryptoRand **ctx) | 创建随机数生成器上下文。 注意：创建的资源必须通过OH_CryptoRand_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoRand_GenerateRandom(OH_CryptoRand *ctx, int len, Crypto_DataBlob *out) | 生成随机数。 注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放out内存。 |
| const char *OH_CryptoRand_GetAlgoName(OH_CryptoRand *ctx) | 获取随机数生成器的算法名称。 |
| OH_Crypto_ErrCode OH_CryptoRand_SetSeed(OH_CryptoRand *ctx, Crypto_DataBlob *seed) | 设置随机数生成器的种子。 |
| OH_Crypto_ErrCode OH_CryptoRand_EnableHardwareEntropy(OH_CryptoRand *ctx) | 启用硬件熵源。 |
| void OH_CryptoRand_Destroy(OH_CryptoRand *ctx) | 销毁随机数生成器上下文。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_CryptoRand_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoRand_Create(OH_CryptoRand **ctx)
```
 
**描述**
 
创建随机数生成器上下文。
 
注意：创建的资源必须通过[OH_CryptoRand_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h#oh_cryptorand_destroy)销毁。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand **ctx | [out] 指向随机数生成器上下文指针的指针。ctx不能为NULL，*ctx必须为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoRand_GenerateRandom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoRand_GenerateRandom(OH_CryptoRand *ctx, int len, Crypto_DataBlob *out)
```
 
**描述**
 
生成随机数。
 
注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h#oh_crypto_freedatablob)释放out内存。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand *ctx | [in] 随机数生成器上下文。不能为NULL。 |
| int len | [in] 随机数的字节长度。 |
| Crypto_DataBlob *out | [out] 指向用于存储随机数的Crypto_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx或out为NULL，或len小于等于0。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoRand_GetAlgoName()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char *OH_CryptoRand_GetAlgoName(OH_CryptoRand *ctx)
```
 
**描述**
 
获取随机数生成器的算法名称。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand *ctx | [in] 随机数生成器上下文。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| const char * | 返回随机数生成器的算法名称，不需要调用者释放，上下文销毁后不可使用。 |
 
 
  

#### OH_CryptoRand_SetSeed()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoRand_SetSeed(OH_CryptoRand *ctx, Crypto_DataBlob *seed)
```
 
**描述**
 
设置随机数生成器的种子。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand *ctx | [in] 随机数生成器上下文。不能为NULL。 |
| Crypto_DataBlob *seed | [in] 种子数据。本接口会对seed中的数据进行深拷贝，调用者在接口返回后可立即释放seed。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx为NULL， 或seed无效（seed为NULL、seed->data为NULL、seed->len为0、或seed->len超过INT_MAX）。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoRand_EnableHardwareEntropy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Crypto_ErrCode OH_CryptoRand_EnableHardwareEntropy(OH_CryptoRand *ctx)
```
 
**描述**
 
启用硬件熵源。
 
**起始版本：** 21
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand *ctx | [in] 随机数生成器上下文。不能为NULL。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。 CRYPTO_PARAMETER_CHECK_FAILED：ctx为NULL。 CRYPTO_NOT_SUPPORTED：不支持的操作或算法。 CRYPTO_MEMORY_ERROR：内存操作失败。 CRYPTO_OPERTION_ERROR：密码操作失败。 |
 
 
  

#### OH_CryptoRand_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_CryptoRand_Destroy(OH_CryptoRand *ctx)
```
 
**描述**
 
销毁随机数生成器上下文。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_CryptoRand *ctx | [in] 随机数生成器上下文。 |
