# OH_Huks_PubKeyInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-pubkeyinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Huks_PubKeyInfo {...}
```
  

##### 概述

定义公钥信息的结构体类型。
 
**起始版本：** 9
 
**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
 
**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| enum OH_Huks_KeyAlg keyAlg | 公钥的算法类型。 |
| uint32_t keySize | 公钥的长度。 |
| uint32_t nOrXSize | n或X值的长度。 |
| uint32_t eOrYSize | e或Y值的长度。 |
| uint32_t placeHolder | 占位符大小。 |
