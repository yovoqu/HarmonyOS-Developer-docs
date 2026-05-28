# OH_Huks_KeyAliasSet

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyaliasset
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Huks_KeyAliasSet {...}
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义密钥别名集的结构体类型。
 
**起始版本：** 20
 
**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
 
**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t aliasesCnt | 密钥别名集个数。 |
| struct OH_Huks_Blob *aliases | 指向密钥别名集数据的指针。 |
