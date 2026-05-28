# OH_Huks_ExternalCryptoParamSet

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ternalcryptotypeapi-oh-huks-externalcryptoparamset
**支持设备：** PC/2in1 | Tablet

```text
typedef struct OH_Huks_ExternalCryptoParamSet {...} OH_Huks_ExternalCryptoParamSet
```
  

##### 概述

**支持设备：** PC/2in1 | Tablet

定义外部加密参数集合的结构。
 
**起始版本：** 22
 
**相关模块：** [HuksExternalCryptoTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi)
 
**所在头文件：** [native_huks_external_crypto_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-type-h)
 
  

##### 汇总

**支持设备：** PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| uint32_t paramSetSize | 参数集合所占内存大小，单位：Byte。 起始版本： 22 |
| uint32_t paramsCnt | 参数集合中的参数数量。 起始版本： 22 |
| OH_Huks_ExternalCryptoParam params[] | 参数数组，大小由paramSetSize与paramsCnt决定。 起始版本： 22 |
