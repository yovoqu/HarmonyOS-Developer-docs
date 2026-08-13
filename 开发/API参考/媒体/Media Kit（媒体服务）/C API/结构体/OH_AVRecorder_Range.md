# OH_AVRecorder_Range

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-range
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVRecorder_Range {...} OH_AVRecorder_Range;
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示AVRecorder相关参数（如比特率、帧率等）的取值范围，用于限定录制参数的可配置范围，开发者应在min和max所界定的范围内设置参数值以确保配置有效。
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
**所在头文件：** [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t min | AVRecorder相关参数取值范围的最小值。单位与所描述的参数一致。 |
| int32_t max | AVRecorder相关参数取值范围的最大值。单位与所描述的参数一致。 |
