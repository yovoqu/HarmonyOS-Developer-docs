# OH_ArkUI_SpanStyle

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-spanstyle
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_ArkUI_SpanStyle OH_ArkUI_SpanStyle
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义属性字符串样式对象。 
 
 可以通过[OH_ArkUI_SpanStyle_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_spanstyle_create)接口创建对应的属性字符串样式对象。 
 
 可以通过[OH_ArkUI_SpanStyle_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_spanstyle_destroy)接口销毁属性字符串样式对象。 
 
 对象创建后通过[OH_ArkUI_SpanStyle_SetStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_spanstyle_setstart)和[OH_ArkUI_SpanStyle_SetLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_spanstyle_setlength)指定样式作用的范围。 
 
 对象创建后通过OH_ArkUI_SpanStyle_SetXXXStyle系列接口设置生效的具体样式，例如通过[OH_ArkUI_SpanStyle_SetTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_spanstyle_settextstyle)设置字体样式效果。
 
**起始版本：** 24
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [styled_string.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h)
