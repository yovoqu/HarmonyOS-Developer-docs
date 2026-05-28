# OH_Huks_ParamSet

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct OH_Huks_ParamSet {...}
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义参数集的结构体类型。
 
**起始版本：** 9
 
**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)
 
**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t paramSetSize | 参数集的内存大小。 |
| uint32_t paramsCnt | 参数的个数。 |
| struct OH_Huks_Param params[] | 参数数组。 |
