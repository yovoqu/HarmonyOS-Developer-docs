# OH_ArkUI_LineSpacingStyle

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-linespacingstyle
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_ArkUI_LineSpacingStyle OH_ArkUI_LineSpacingStyle
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义行间距样式。 
 
 可以通过[OH_ArkUI_LineSpacingStyle_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_linespacingstyle_create)接口创建对应的行间距样式对象，[OH_ArkUI_LineSpacingStyle_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_linespacingstyle_destroy)接口销毁行间距样式对象。 
 
 对象创建后可以通过[OH_ArkUI_LineSpacingStyle_SetLineSpacing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_linespacingstyle_setlinespacing)接口设置具体的行间距值，通过[OH_ArkUI_LineSpacingStyle_SetOnlyBetweenLines](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h#oh_arkui_linespacingstyle_setonlybetweenlines)接口设置行间距是否只在行间生效。
 
**起始版本：** 26.0.0
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [styled_string.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h)
