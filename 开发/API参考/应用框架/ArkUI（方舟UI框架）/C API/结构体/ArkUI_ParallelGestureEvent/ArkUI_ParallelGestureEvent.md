# ArkUI_ParallelGestureEvent

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-parallelgestureevent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_ParallelGestureEvent ArkUI_ParallelGestureEvent
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义并行手势事件。该结构体作为[setGestureParallelTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-3#setgestureparallelto)回调函数的参数传递，包含当前手势识别器、响应链中的冲突手势识别器和用户自定义数据，供回调选择需要与当前手势并行识别的对象。
 
**起始版本：** 26.0.0
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_gesture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h)
