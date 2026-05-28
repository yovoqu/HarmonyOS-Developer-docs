# OH_Huks_KeyMaterialRsa

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialrsa
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Huks_KeyMaterialRsa {...}
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义Rsa密钥的结构体类型。
 
**起始版本：** 9
 
**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
 
**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 密钥的算法类型。 |
| uint32_t keySize | 密钥的长度。 |
| uint32_t nSize | n值的长度。 |
| uint32_t eSize | e值的长度。 |
| uint32_t dSize | d值的长度。 |
