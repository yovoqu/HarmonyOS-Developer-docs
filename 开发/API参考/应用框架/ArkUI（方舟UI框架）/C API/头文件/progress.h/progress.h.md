# progress.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-progress-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义Progress相关的枚举和接口。
 
**引用文件：** <arkui/node_attributes/progress.h>
 
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
| ArkUI_ProgressLinearStyleOption | ArkUI_ProgressLinearStyleOption | 定义线性进度条的样式选项，适用于需要自定义线性进度条显示样式的场景。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_ProgressType | ArkUI_ProgressType | 定义进度条类型枚举值。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void) | 创建线性进度条样式信息。 |
| void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option) | 销毁线性进度条样式信息。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled) | 设置进度平滑动效的开关。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled) | 设置扫光效果的开关。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth) | 设置进度条宽度。 |
| void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius) | 设置进度条圆角半径。 |
| bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option) | 获取进度平滑动效的开关信息。 |
| bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option) | 获取扫光效果的开关信息。 |
| float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option) | 获取进度条宽度。 |
| float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option) | 获取进度条圆角半径值。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ArkUI_ProgressType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum ArkUI_ProgressType
```
 
**描述**
 
定义进度条类型枚举值。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| ARKUI_PROGRESS_TYPE_LINEAR = 0 | 线性样式。 |
| ARKUI_PROGRESS_TYPE_RING = 1 | 环形无刻度样式。 |
| ARKUI_PROGRESS_TYPE_ECLIPSE = 2 | 圆形样式。 |
| ARKUI_PROGRESS_TYPE_SCALE_RING = 3 | 环形有刻度样式。 |
| ARKUI_PROGRESS_TYPE_CAPSULE = 4 | 胶囊样式。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_ProgressLinearStyleOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void)
```
 
**描述**
 
创建线性进度条样式信息。
 
**起始版本：** 15
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* | ProgressLinearStyleOption实例。 如果返回空指针，可能是因为内存不足。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_Destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option)
```
 
**描述**
 
销毁线性进度条样式信息。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```
 
**描述**
 
设置进度平滑动效的开关。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| bool enabled | 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。 true：表示开启进度平滑动效。 false：表示关闭进度平滑动效。 默认值：true。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```
 
**描述**
 
设置扫光效果的开关。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| bool enabled | 扫光效果的开关。 true：表示开启扫光效果。 false：表示关闭扫光效果。 默认值：false。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth)
```
 
**描述**
 
设置进度条宽度。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| float strokeWidth | 进度条宽度值（不支持百分比设置），单位为vp，默认值：4.0vp。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius)
```
 
**描述**
 
设置进度条圆角半径。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
| float strokeRadius | 进度条圆角半径值，单位为vp，取值范围[0, strokeWidth/2]。默认值：strokeWidth/2。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```
 
**描述**
 
获取进度平滑动效的开关信息。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| bool | 是否开启平滑动效。true：表示开启进度平滑动效。false：表示关闭进度平滑动效。默认值：true。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```
 
**描述**
 
获取扫光效果的开关信息。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| bool | 是否开启扫光效果。true：表示开启扫光效果。false：表示关闭扫光效果。默认值：false。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option)
```
 
**描述**
 
获取进度条宽度。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 进度条宽度值，单位为vp。 |
 
 
  

#### OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option)
```
 
**描述**
 
获取进度条圆角半径值。
 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_ProgressLinearStyleOption* option | 线性进度条样式信息。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| float | 进度条圆角半径值，单位为vp。 |
