# image_span.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-span-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义ImageSpan相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/image_span.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [native_type_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_ImageSpanAlignment | ArkUI_ImageSpanAlignment | 定义图片基于文本的对齐方式。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_ImageSpanAlignment

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ImageSpanAlignment
```
 
**描述**
 
定义图片基于文本的对齐方式。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_IMAGE_SPAN_ALIGNMENT_BASELINE = 0 | 图片下边沿与文本BaseLine对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_BOTTOM = 1 | 图片下边沿与文本下边沿对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_CENTER = 2 | 图片中间与文本中间对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_TOP = 3 | 图片上边沿与文本上边沿对齐。 |
| ARKUI_IMAGE_SPAN_ALIGNMENT_FOLLOW_PARAGRAPH = 4 | 图片对齐方式跟随Text组件对齐方式。 起始版本： 20 |
