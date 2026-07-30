# slider.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-slider-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

为NativeNode API提供Slider节点类型定义。
 
**引用文件：** <arkui/node_attributes/slider.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_SliderBlockStyle | ArkUI_SliderBlockStyle | 定义滑块形状。 |
| ArkUI_SliderDirection | ArkUI_SliderDirection | 定义滑动条滑动方向。 |
| ArkUI_SliderStyle | ArkUI_SliderStyle | 定义滑块与滑轨显示样式。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_SliderBlockStyle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SliderBlockStyle
```
 
**描述：**
 
定义滑块形状。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_BLOCK_STYLE_DEFAULT = 0 | 使用默认滑块（圆形）。 |
| ARKUI_SLIDER_BLOCK_STYLE_IMAGE = 1 | 使用图片资源作为滑块。 |
| ARKUI_SLIDER_BLOCK_STYLE_SHAPE = 2 | 使用自定义形状作为滑块。 |
 
 
  

#### ArkUI_SliderDirection

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SliderDirection
```
 
**描述：**
 
定义滑动条滑动方向。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_DIRECTION_VERTICAL = 0 | 方向为纵向。 |
| ARKUI_SLIDER_DIRECTION_HORIZONTAL = 1 | 方向为横向。 |
 
 
  

#### ArkUI_SliderStyle

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_SliderStyle
```
 
**描述：**
 
定义滑块与滑轨显示样式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_SLIDER_STYLE_OUT_SET = 0 | 滑块在滑轨上。 |
| ARKUI_SLIDER_STYLE_IN_SET = 1 | 滑块在滑轨内。 |
| ARKUI_SLIDER_STYLE_NONE = 2 | 无滑块。 |
