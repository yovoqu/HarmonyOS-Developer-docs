# OH_ArkUI_CustomSpan

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-customspan
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_ArkUI_CustomSpan OH_ArkUI_CustomSpan
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义自定义绘制Span。 
 
 可以通过[OH_ArkUI_CustomSpan_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_customspan_create)接口创建对应的自定义绘制Span对象。 
 
 可以通过[OH_ArkUI_CustomSpan_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_customspan_destroy)接口销毁自定义绘制Span对象。 
 
 对象创建后通过[OH_ArkUI_CustomSpan_RegisterOnMeasureCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_customspan_registeronmeasurecallback)和[OH_ArkUI_CustomSpan_RegisterOnDrawCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_customspan_registerondrawcallback)接口注册绘制回调函数。
 
**起始版本：** 24
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [styled_string.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h)
