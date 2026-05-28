# OH_Huks_KeyMaterialDsa

更新时间：2026-03-27 08:08:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdsa
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Huks_KeyMaterialDsa {...}
```
  

##### 概述

定义DSA密钥的结构体类型。
 
**起始版本：** 9
 
**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
 
**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 密钥的算法类型。 |
| uint32_t keySize | 密钥的长度。 |
| uint32_t xSize | x值的长度。 |
| uint32_t ySize | y值的长度。 |
| uint32_t pSize | p值的长度。 |
| uint32_t qSize | q值的长度。 |
| uint32_t gSize | g值的长度。 |
