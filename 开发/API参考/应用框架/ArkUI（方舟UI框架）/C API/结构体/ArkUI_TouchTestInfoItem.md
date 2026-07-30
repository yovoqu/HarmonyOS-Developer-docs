# ArkUI_TouchTestInfoItem

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitem
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_TouchTestInfoItem ArkUI_TouchTestInfoItem
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义触摸测试信息项。触摸测试是根据触摸事件坐标判定目标组件的命中测试过程。当用户通过[registerNodeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent)注册了[NODE_ON_CHILD_TOUCH_TEST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)事件时，才能在事件回调中获取触摸测试信息项。该信息项包含触摸测试中子组件的信息，适用于获取和识别子组件信息的场景；开发者可通过[OH_ArkUI_TouchTestInfoItem_GetXXX系列接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h#oh_arkui_touchtestinfoitem_getx)获取信息并处理触摸测试结果。
 
**起始版本：** 22
 
**相关模块：** [ArkUI_EventModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule)
 
**所在头文件：** [ui_input_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h)
