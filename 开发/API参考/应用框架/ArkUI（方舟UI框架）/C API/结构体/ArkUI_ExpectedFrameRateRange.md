# ArkUI_ExpectedFrameRateRange

更新时间：2026-07-28 11:23:46（官网已下线）

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-expectedframeraterange
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_ExpectedFrameRateRange
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

设置动画的期望帧率。该结构体通过min、max和expected三个字段定义帧率范围，系统尽可能满足期望帧率。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_animate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t min | 期望的最小帧率，单位为帧/秒（fps）。取值原则：min需小于等于max，且min需小于等于expected。取值需满足min <= expected <= max。 |
| uint32_t max | 期望的最大帧率，单位为帧/秒（fps）。取值原则：max需大于等于min，且max需大于等于expected。取值需满足min <= expected <= max。 |
| uint32_t expected | 期望的最优帧率，单位为帧/秒（fps）。取值原则：expected需在[min, max]范围内取值。 |
