# rich_editor.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义RichEditor相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/rich_editor.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 24
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [native_type_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions | OH_ArkUI_TextEditorSelectionMenuOptions | 定义文本编辑器的文本选择菜单选项。 |
| OH_ArkUI_TextEditorPlaceholderOptions | OH_ArkUI_TextEditorPlaceholderOptions | 定义文本编辑器无输入时的提示文本选项。 |
| OH_ArkUI_TextEditorStyledStringController | OH_ArkUI_TextEditorStyledStringController | 定义文本编辑器的属性字符串控制器。 |
| OH_ArkUI_TextEditorParagraphStyle | OH_ArkUI_TextEditorParagraphStyle | 定义文本编辑器的段落样式。 |
| OH_ArkUI_TextEditorTextStyle | OH_ArkUI_TextEditorTextStyle | 定义文本编辑器的文本样式。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ArkUI_HapticFeedbackMode | OH_ArkUI_HapticFeedbackMode | 震动效果类型枚举。 |
| OH_ArkUI_TextEditorSpanType | OH_ArkUI_TextEditorSpanType | 自定义文本选择菜单span类型枚举。 |
| OH_ArkUI_TextEditorResponseType | OH_ArkUI_TextEditorResponseType | 自定义文本选择菜单响应类型枚举。 |
| OH_ArkUI_TextMenuType | OH_ArkUI_TextMenuType | 文本菜单类型枚举。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* OH_ArkUI_TextEditorPlaceholderOptions_Create() | 创建一个无输入时的提示文本的选项对象。当该对象不再使用时，请调用OH_ArkUI_TextEditorPlaceholderOptions_Destroy销毁。 |
| void OH_ArkUI_TextEditorPlaceholderOptions_Destroy(OH_ArkUI_TextEditorPlaceholderOptions* options) | 销毁无输入时的提示文本的选项对象。 |
| OH_ArkUI_TextEditorStyledStringController* OH_ArkUI_TextEditorStyledStringController_Create() | 为文本编辑器创建一个属性字符串控制器对象。当该对象不再使用时，请调用OH_ArkUI_TextEditorStyledStringController_Destroy销毁。 |
| void OH_ArkUI_TextEditorStyledStringController_Destroy(OH_ArkUI_TextEditorStyledStringController* controller) | 销毁属性字符串控制器。 |
| OH_ArkUI_TextEditorParagraphStyle* OH_ArkUI_TextEditorParagraphStyle_Create() | 为文本编辑器创建一个段落样式对象。当该对象不再使用时，请调用OH_ArkUI_TextEditorParagraphStyle_Destroy销毁。 |
| void OH_ArkUI_TextEditorParagraphStyle_Destroy(OH_ArkUI_TextEditorParagraphStyle* style) | 销毁段落样式对象。 |
| OH_ArkUI_TextEditorTextStyle* OH_ArkUI_TextEditorTextStyle_Create() | 创建一个文本样式对象。当该对象不再使用时，请调用OH_ArkUI_TextEditorTextStyle_Destroy销毁。 |
| void OH_ArkUI_TextEditorTextStyle_Destroy(OH_ArkUI_TextEditorTextStyle* style) | 销毁文本样式对象。 |
| OH_ArkUI_TextEditorSelectionMenuOptions* OH_ArkUI_TextEditorSelectionMenuOptions_Create() | 创建一个文本编辑器文本选择菜单选项对象。当该对象不再使用时，请调用OH_ArkUI_TextEditorSelectionMenuOptions_Destroy销毁。 |
| void OH_ArkUI_TextEditorSelectionMenuOptions_Destroy(OH_ArkUI_TextEditorSelectionMenuOptions* options) | 销毁文本编辑器文本选择菜单选项对象。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_HapticFeedbackMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_HapticFeedbackMode
```
 
**描述**
 
震动效果类型枚举。
 
**起始版本：** 24
  
| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_HAPTIC_FEEDBACK_MODE_DISABLED = 0 | 无震动效果。 |
| OH_ARKUI_HAPTIC_FEEDBACK_MODE_ENABLED = 1 | 有震动效果。 |
| OH_ARKUI_HAPTIC_FEEDBACK_MODE_AUTO = 2 | 跟随系统的震动效果。 |
 
 
  

#### OH_ArkUI_TextEditorSpanType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_TextEditorSpanType
```
 
**描述**
 
自定义文本选择菜单span类型枚举。
 
**起始版本：** 24
  
| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_TEXT_EDITOR_SPAN_TYPE_TEXT = 0 | 文本span。 |
| OH_ARKUI_TEXT_EDITOR_SPAN_TYPE_IMAGE = 1 | 图片span。 |
| OH_ARKUI_TEXT_EDITOR_SPAN_TYPE_MIXED = 2 | 混合span。 |
| OH_ARKUI_TEXT_EDITOR_SPAN_TYPE_BUILDER = 3 | 自定义布局span。 |
| OH_ARKUI_TEXT_EDITOR_SPAN_TYPE_DEFAULT = 4 | 默认span。 |
 
 
  

#### OH_ArkUI_TextEditorResponseType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_TextEditorResponseType
```
 
**描述**
 
自定义文本选择菜单响应类型枚举。
 
**起始版本：** 24
  
| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_TEXT_EDITOR_RESPONSE_TYPE_RIGHT_CLICK = 0 | 通过鼠标右键触发菜单弹出。 |
| OH_ARKUI_TEXT_EDITOR_RESPONSE_TYPE_LONG_PRESS = 1 | 通过长按触发菜单弹出。 |
| OH_ARKUI_TEXT_EDITOR_RESPONSE_TYPE_SELECT = 2 | 通过鼠标选中触发菜单弹出。 |
| OH_ARKUI_TEXT_EDITOR_RESPONSE_TYPE_DEFAULT = 3 | 默认响应类型。 |
 
 
  

#### OH_ArkUI_TextMenuType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_ArkUI_TextMenuType
```
 
**描述**
 
文本菜单类型枚举。
 
**起始版本：** 24
  
| 枚举项 | 描述 |
| --- | --- |
| OH_ARKUI_TEXT_EDITOR_SELECTION_MENU = 0 | 文本选择菜单。 |
| OH_ARKUI_TEXT_EDITOR_PREVIEW_MENU = 1 | 预览菜单。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_TextEditorPlaceholderOptions_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_TextEditorPlaceholderOptions* OH_ArkUI_TextEditorPlaceholderOptions_Create()
```
 
**描述**
 
创建一个无输入时的提示文本的选项对象。当该对象不再使用时，请调用[OH_ArkUI_TextEditorPlaceholderOptions_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h#oh_arkui_texteditorplaceholderoptions_destroy)销毁。
 
**起始版本：** 24
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorPlaceholderOptions_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_TextEditorPlaceholderOptions_Destroy(OH_ArkUI_TextEditorPlaceholderOptions* options)
```
 
**描述**
 
销毁无输入时的提示文本的选项对象。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorPlaceholderOptions* options | 指向OH_ArkUI_TextEditorPlaceholderOptions对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorStyledStringController_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_TextEditorStyledStringController* OH_ArkUI_TextEditorStyledStringController_Create()
```
 
**描述**
 
为文本编辑器创建一个属性字符串控制器对象。当该对象不再使用时，请调用[OH_ArkUI_TextEditorStyledStringController_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h#oh_arkui_texteditorstyledstringcontroller_destroy)销毁。
 
**起始版本：** 24
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorStyledStringController_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_TextEditorStyledStringController_Destroy(OH_ArkUI_TextEditorStyledStringController* controller)
```
 
**描述**
 
销毁属性字符串控制器。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorStyledStringController* controller | 指向OH_ArkUI_TextEditorStyledStringController对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorParagraphStyle_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_TextEditorParagraphStyle* OH_ArkUI_TextEditorParagraphStyle_Create()
```
 
**描述**
 
为文本编辑器创建一个段落样式对象。当该对象不再使用时，请调用[OH_ArkUI_TextEditorParagraphStyle_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h#oh_arkui_texteditorparagraphstyle_destroy)销毁。
 
**起始版本：** 24
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorParagraphStyle_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_TextEditorParagraphStyle_Destroy(OH_ArkUI_TextEditorParagraphStyle* style)
```
 
**描述**
 
销毁段落样式对象。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorParagraphStyle* style | 指向OH_ArkUI_TextEditorParagraphStyle对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorTextStyle_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_TextEditorTextStyle* OH_ArkUI_TextEditorTextStyle_Create()
```
 
**描述**
 
创建一个文本样式对象。当该对象不再使用时，请调用[OH_ArkUI_TextEditorTextStyle_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h#oh_arkui_texteditortextstyle_destroy)销毁。
 
**起始版本：** 24
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* | 指向OH_ArkUI_TextEditorTextStyle对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorTextStyle_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_TextEditorTextStyle_Destroy(OH_ArkUI_TextEditorTextStyle* style)
```
 
**描述**
 
销毁文本样式对象。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorTextStyle* style | 指向OH_ArkUI_TextEditorTextStyle对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorSelectionMenuOptions_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_ArkUI_TextEditorSelectionMenuOptions* OH_ArkUI_TextEditorSelectionMenuOptions_Create()
```
 
**描述**
 
创建一个文本编辑器文本选择菜单选项对象。当该对象不再使用时，请调用[OH_ArkUI_TextEditorSelectionMenuOptions_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rich-editor-h#oh_arkui_texteditorselectionmenuoptions_destroy)销毁。
 
**起始版本：** 24
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
 
 
  

#### OH_ArkUI_TextEditorSelectionMenuOptions_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_TextEditorSelectionMenuOptions_Destroy(OH_ArkUI_TextEditorSelectionMenuOptions* options)
```
 
**描述**
 
销毁文本编辑器文本选择菜单选项对象。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_TextEditorSelectionMenuOptions* options | 指向OH_ArkUI_TextEditorSelectionMenuOptions对象的指针。 |
