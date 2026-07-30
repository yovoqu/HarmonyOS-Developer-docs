# custom_span.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-custom-span-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义CustomSpan相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/custom_span.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [native_type_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_CustomSpanMeasureInfo | ArkUI_CustomSpanMeasureInfo | 自定义Span组件的测量信息。该结构体用于在自定义Span组件的测量回调中提供组件的测量数据，帮助开发者实现自定义文本组件的精确尺寸测量与布局排版。 |
| ArkUI_CustomSpanMetrics | ArkUI_CustomSpanMetrics | 自定义Span组件的度量指标，用于描述自定义Span的宽高、位置等布局信息。开发者可通过该结构体设置自定义Span的宽高数据，实现更精准的文本布局控制和排版优化。适用于需要精细控制文本显示效果的场景，如富文本编辑器中的图文混排、聊天应用中的表情内嵌、文档应用中的自定义标记等。 |
| ArkUI_CustomSpanDrawInfo | ArkUI_CustomSpanDrawInfo | 自定义段落组件的绘制信息，用于在该组件的绘制回调中向开发者传递绘制信息，开发者可在自定义绘制流程中获取并使用该信息，实现定制化的段落组件绘制效果。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* OH_ArkUI_CustomSpanMeasureInfo_Create(void) | 创建自定义段落组件测量信息。 |
| void OH_ArkUI_CustomSpanMeasureInfo_Dispose(ArkUI_CustomSpanMeasureInfo* info) | 销毁自定义段落组件测量信息。 |
| float OH_ArkUI_CustomSpanMeasureInfo_GetFontSize(ArkUI_CustomSpanMeasureInfo* info) | 获取自定义段落组件的父节点Text的字体大小。 |
| ArkUI_CustomSpanMetrics* OH_ArkUI_CustomSpanMetrics_Create(void) | 创建自定义段落组件度量信息。 |
| void OH_ArkUI_CustomSpanMetrics_Dispose(ArkUI_CustomSpanMetrics* metrics) | 销毁自定义段落组件度量信息。 |
| int32_t OH_ArkUI_CustomSpanMetrics_SetWidth(ArkUI_CustomSpanMetrics* metrics, float width) | 设置自定义段落组件的宽度。 |
| int32_t OH_ArkUI_CustomSpanMetrics_SetHeight(ArkUI_CustomSpanMetrics* metrics, float height) | 设置自定义段落组件的高度。 |
| ArkUI_CustomSpanDrawInfo* OH_ArkUI_CustomSpanDrawInfo_Create(void) | 创建自定义段落组件绘制信息。 |
| void OH_ArkUI_CustomSpanDrawInfo_Dispose(ArkUI_CustomSpanDrawInfo* info) | 销毁自定义段落组件绘制信息。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetXOffset(ArkUI_CustomSpanDrawInfo* info) | 获取自定义段落组件相对于挂载组件的x轴偏移值。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetLineTop(ArkUI_CustomSpanDrawInfo* info) | 获取自定义段落组件相对于挂载组件的上边距。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetLineBottom(ArkUI_CustomSpanDrawInfo* info) | 获取自定义段落组件相对于挂载组件的下边距。 |
| float OH_ArkUI_CustomSpanDrawInfo_GetBaseline(ArkUI_CustomSpanDrawInfo* info) | 获取自定义段落组件相对于挂载组件的基线偏移量。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_CustomSpanMeasureInfo_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_CustomSpanMeasureInfo* OH_ArkUI_CustomSpanMeasureInfo_Create(void)
```
 
**描述**
 
创建自定义段落组件测量信息。
 
**起始版本：** 12
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* | CustomSpanMeasureInfo实例。 如果返回空指针，可能是因为内存不足。 |
 
 
  

#### OH_ArkUI_CustomSpanMeasureInfo_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CustomSpanMeasureInfo_Dispose(ArkUI_CustomSpanMeasureInfo* info)
```
 
**描述**
 
销毁自定义段落组件测量信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* info | 自定义段落组件测量信息指针。 |
 
 
  

#### OH_ArkUI_CustomSpanMeasureInfo_GetFontSize()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_CustomSpanMeasureInfo_GetFontSize(ArkUI_CustomSpanMeasureInfo* info)
```
 
**描述**
 
获取自定义段落组件的父节点Text的字体大小。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMeasureInfo* info | 自定义段落组件测量信息指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 父节点Text的字体大小，单位为fp。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanMetrics_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_CustomSpanMetrics* OH_ArkUI_CustomSpanMetrics_Create(void)
```
 
**描述**
 
创建自定义段落组件度量信息。
 
**起始版本：** 12
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanMetrics* | CustomSpanMetrics实例。 如果返回空指针，可能是因为内存不足。 |
 
 
  

#### OH_ArkUI_CustomSpanMetrics_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CustomSpanMetrics_Dispose(ArkUI_CustomSpanMetrics* metrics)
```
 
**描述**
 
销毁自定义段落组件度量信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |
 
 
  

#### OH_ArkUI_CustomSpanMetrics_SetWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_CustomSpanMetrics_SetWidth(ArkUI_CustomSpanMetrics* metrics, float width)
```
 
**描述**
 
设置自定义段落组件的宽度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |
| float width | 宽度大小，单位为vp。默认值为0.0f，负值与默认值效果一致。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanMetrics_SetHeight()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t OH_ArkUI_CustomSpanMetrics_SetHeight(ArkUI_CustomSpanMetrics* metrics, float height)
```
 
**描述**
 
设置自定义段落组件的高度。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanMetrics* metrics | CustomSpanMetrics实例。 |
| float height | 高度大小，单位为vp。默认值为0.0f，负值与默认值效果一致。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 异常原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_CustomSpanDrawInfo* OH_ArkUI_CustomSpanDrawInfo_Create(void)
```
 
**描述**
 
创建自定义段落组件绘制信息。
 
**起始版本：** 12
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* | CustomSpanDrawInfo实例。 如果返回空指针，可能是因为内存不足。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_CustomSpanDrawInfo_Dispose(ArkUI_CustomSpanDrawInfo* info)
```
 
**描述**
 
销毁自定义段落组件绘制信息。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_GetXOffset()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_CustomSpanDrawInfo_GetXOffset(ArkUI_CustomSpanDrawInfo* info)
```
 
**描述**
 
获取自定义段落组件相对于挂载组件的x轴偏移值。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | x轴偏移值，单位为px。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_GetLineTop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_CustomSpanDrawInfo_GetLineTop(ArkUI_CustomSpanDrawInfo* info)
```
 
**描述**
 
获取自定义段落组件相对于挂载组件的上边距。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 上边距值，单位为px。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_GetLineBottom()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_CustomSpanDrawInfo_GetLineBottom(ArkUI_CustomSpanDrawInfo* info)
```
 
**描述**
 
获取自定义段落组件相对于挂载组件的下边距。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 下边距值，单位为px。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |
 
 
  

#### OH_ArkUI_CustomSpanDrawInfo_GetBaseline()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_CustomSpanDrawInfo_GetBaseline(ArkUI_CustomSpanDrawInfo* info)
```
 
**描述**
 
获取自定义段落组件相对于挂载组件的基线偏移量。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_CustomSpanDrawInfo* info | 自定义段落组件绘制信息指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 基线偏移量值，单位为px。若函数参数异常，返回0.0f。 异常返回原因：传入参数验证失败，参数不能为空。 |
