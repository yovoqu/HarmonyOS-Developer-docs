# ArkUI_CustomDialogOptions

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_CustomDialogOptions ArkUI_CustomDialogOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义自定义弹窗的选项对象。该对象不暴露任何成员字段，开发者通过 [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule) 中以 OH_ArkUI_CustomDialog_Set 为前缀的接口（如设置背景、圆角、阴影、模糊、位置、模态等）配置弹窗属性，再调用 OH_ArkUI_CustomDialog_OpenDialog 打开弹窗。
 
**起始版本：** 19
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)
