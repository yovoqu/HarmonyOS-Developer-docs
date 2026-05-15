# FIDO2_CapabilityArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array


## 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)


## 汇总


### 成员变量


| 名称 | 描述 |
| --- | --- |
| uint32_t [number](#number) | 能力的数量。 |
| [FIDO2_Capability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability) * [capability](#capability) | 能力的数组。 |


## 结构体成员变量说明


### capability


```cpp
FIDO2_Capability* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。


### number


```cpp
uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。
