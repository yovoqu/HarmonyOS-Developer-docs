# OH_Huks_Param

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
struct OH_Huks_Param {...}
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义参数集中的参数结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native_huks_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint32_t tag | 标签值。 |
| union {  bool boolParam;   int32_t int32Param;   uint32_t uint32Param;   uint64_t uint64Param;   [struct OH_Huks_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) blob;   } | boolParam：bool型参数。 int32Param：int32_t型参数。 uint32Param：uint32_t型参数。 uint64Param：uint64_t型参数。 blob：OH_Huks_Blob型参数。 |
