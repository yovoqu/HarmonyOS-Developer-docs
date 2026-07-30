# ArkUI_TouchTestInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_TouchTestInfo ArkUI_TouchTestInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义触摸测试信息，用于设置命中测试策略和结果作用的子组件，并获取各子组件的触摸测试结果。
 
当用户通过[registerNodeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent)注册了[NODE_ON_CHILD_TOUCH_TEST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)事件时，开发者才能在事件回调中获取此触摸测试信息结构体。
 
该结构体支持设置触摸测试策略（取值原则参见[ArkUI_TouchTestStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h#arkui_touchteststrategy)）和命中测试过程中需要作用的子组件ID，并可获取包含各子组件详细测试结果的触摸测试信息项数组。
 
**起始版本：** 22
 
**相关模块：** [ArkUI_EventModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule)
 
**所在头文件：** [ui_input_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h)
