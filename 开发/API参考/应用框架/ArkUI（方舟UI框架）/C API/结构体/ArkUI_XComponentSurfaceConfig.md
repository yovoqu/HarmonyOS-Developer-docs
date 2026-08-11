# ArkUI_XComponentSurfaceConfig

更新时间：2026-07-28 11:23:46（官网已下线）

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-arkui-xcomponentsurfaceconfig
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct ArkUI_XComponentSurfaceConfig ArkUI_XComponentSurfaceConfig
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义该Surface配置，用于设置XComponent组件持有的Surface在渲染时是否被视为不透明。适用于对XComponent渲染性能有要求的场景，将Surface设置为不透明可以减少渲染合成开销，提升渲染性能。需要注意的是，仅当Surface实际渲染的内容全部为不透明时才应设置为不透明，否则可能导致透明区域渲染异常。
 
**起始版本：** 22
 
**相关模块：** [OH_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)
 
**所在头文件：** [native_interface_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)
