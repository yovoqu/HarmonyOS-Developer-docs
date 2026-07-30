# ArkUI_CustomProperty

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_CustomProperty ArkUI_CustomProperty
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义表示组件自定义属性的 ArkUI_CustomProperty 结构体。通过相关接口，可以为 ArkUI 组件添加、移除和获取自定义属性，以及获取自定义属性的字符串值。
 
**起始版本：** 14
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
 
**相关接口：**
  
| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_NodeUtils_AddCustomProperty | 添加组件的自定义属性。 |
| OH_ArkUI_NodeUtils_RemoveCustomProperty | 移除组件已设置的自定义属性。 |
| OH_ArkUI_NodeUtils_GetCustomProperty | 获取组件的自定义属性，并通过handle返回ArkUI_CustomProperty实例。 |
| OH_ArkUI_CustomProperty_Destroy | 销毁 ArkUI_CustomProperty 实例。 |
| OH_ArkUI_CustomProperty_GetStringValue | 获取自定义属性的字符串值。 |
