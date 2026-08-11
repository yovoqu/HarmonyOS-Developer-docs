# custom_attributes.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-node-attributes-custom-attributes-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

为NativeNode API提供自定义节点事件定义。
 
**引用文件：** <arkui/node_attributes/custom_attributes.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [native_node_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/native_node_sample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_NodeCustomEventType | ArkUI_NodeCustomEventType | 定义自定义组件事件类型。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_NodeCustomEventType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_NodeCustomEventType
```
 
**描述：**
 
定义自定义组件事件类型。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_NODE_CUSTOM_EVENT_ON_MEASURE = 1 << 0 | 自定义测量类型。 起始版本： 12 |
| ARKUI_NODE_CUSTOM_EVENT_ON_LAYOUT = 1 << 1 | 自定义布局类型。 起始版本： 12 |
| ARKUI_NODE_CUSTOM_EVENT_ON_DRAW = 1 << 2 | 自定义内容层绘制类型。 起始版本： 12 |
| ARKUI_NODE_CUSTOM_EVENT_ON_FOREGROUND_DRAW = 1 << 3 | 自定义前景绘制类型。 起始版本： 12 |
| ARKUI_NODE_CUSTOM_EVENT_ON_OVERLAY_DRAW = 1 << 4 | 自定义浮层绘制类型。 起始版本： 12 |
| ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_FRONT = 1 << 5 | 自定义内容层前景绘制类型。 起始版本： 20 |
| ARKUI_NODE_CUSTOM_EVENT_ON_DRAW_BEHIND = 1 << 6 | 自定义内容层背景绘制类型。 起始版本： 20 |
