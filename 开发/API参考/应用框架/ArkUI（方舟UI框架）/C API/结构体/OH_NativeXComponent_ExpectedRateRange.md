# OH_NativeXComponent_ExpectedRateRange

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent-expectedraterange
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_NativeXComponent_ExpectedRateRange
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义期望帧率范围。该结构体用于设置XComponent的帧率范围，支持在高性能渲染场景下进行精确的帧率控制，帮助平衡画面流畅度与功耗。
 
**起始版本：** 11
 
**相关模块：** [OH_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)
 
**所在头文件：** [native_interface_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t min | 期望帧率范围最小值。单位为帧/秒。取值范围：[0, +∞)。需满足 min <= max。 |
| int32_t max | 期望帧率范围最大值。单位为帧/秒。取值范围：[0, +∞)。需满足 max >= min。 |
| int32_t expected | 期望帧率。单位为帧/秒。取值范围：[0, +∞)，且应在[min, max]范围内。 |
