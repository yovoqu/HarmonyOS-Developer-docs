# ArkUI_GestureEventTargetInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureeventtargetinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_GestureEventTargetInfo ArkUI_GestureEventTargetInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义手势事件目标信息类型，用于在手势处理过程中查询手势事件目标对象的滚动开始、滚动结束等状态，主要适用于滚动类容器组件。开发者可通过[OH_ArkUI_GetGestureEventTargetInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h#oh_arkui_getgestureeventtargetinfo)从手势识别器中获取该对象，并通过目标信息查询接口读取目标状态。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_gesture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h)
