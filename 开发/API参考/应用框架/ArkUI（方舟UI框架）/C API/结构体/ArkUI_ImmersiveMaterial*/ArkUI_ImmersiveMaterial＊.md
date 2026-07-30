# ArkUI_ImmersiveMaterial*

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-immersivematerialhandle
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_ImmersiveMaterial* ArkUI_ImmersiveMaterialHandle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义指向沉浸式材质对象的指针，沉浸式材质用于实现的沉浸式视觉效果对象。
 
可以通过[OH_ArkUI_NativeModule_ImmersiveMaterial_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-material-h#oh_arkui_nativemodule_immersivematerial_create)创建沉浸式材质对象，创建后必须在使用完毕时调用[OH_ArkUI_NativeModule_ImmersiveMaterial_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-material-h#oh_arkui_nativemodule_immersivematerial_destroy)销毁沉浸式材质对象以释放资源，避免内存泄漏。
 
**起始版本：** 26.0.0
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_material.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-material-h)
