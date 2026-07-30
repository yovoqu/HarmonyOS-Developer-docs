# ArkUI_NativeDialogAPI_2

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_NativeDialogAPI_2
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArkUI提供的Native侧自定义弹窗接口集合，用于在Native层创建和管理自定义弹窗，支持设置弹窗避让键盘距离、显示层级、层级节点id和嵌入式弹窗蒙层显示区域等功能，适用于需要精细化控制弹窗行为的场景。
 
**起始版本：** 15
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeDialogAPI_1 nativeDialogAPI1 | ArkUI提供的Native侧自定义弹窗接口集合，范围是ArkUI_NativeDialogAPI_1。 起始版本： 15 |
 
 
  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit) | 设置弹窗避让键盘后，和键盘之间距离。 |
| int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode) | 设置弹窗的显示层级。 |
| int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId) | 设置弹窗显示层级页面下的节点id。 |
| int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode) | 设置嵌入式弹窗蒙层的显示区域。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### setKeyboardAvoidDistance()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```
 
**描述：**
 
设置弹窗避让键盘后，和键盘之间距离。
 
> [!NOTE]
> setKeyboardAvoidDistance方法需要在调用 show 方法之前调用。

 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float distance | 弹窗与键盘之间保持的避让距离，单位由unit参数指定。 |
| ArkUI_LengthMetricUnit unit | 避让距离的单位，参数类型ArkUI_LengthMetricUnit。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_CAPI_INIT_ERROR 接口初始化错误，请确保Native模块已正确初始化。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常，请检查参数是否有效。 |
 
 
  

#### setLevelMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```
 
**描述：**
 
设置弹窗的显示层级。
 
> [!NOTE]
> setLevelMode方法需要在调用 show 方法之前调用；若需配合 setLevelUniqueId 使用，则需要在调用setLevelUniqueId方法之后调用。

 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_LevelMode levelMode | 显示层级的枚举值，类型为ArkUI_LevelMode。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常，请检查参数是否有效。 |
 
 
  

#### setLevelUniqueId()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```
 
**描述：**
 
设置弹窗显示层级页面下的节点id。
 
> [!NOTE]
> setLevelUniqueId方法需要在调用 setLevelMode 方法之前调用，且需要在调用 show 方法之前调用。

 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t uniqueId | 指定节点ID，会查找该节点所在页面，并将弹窗显示在该页面下。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常，请检查参数是否有效。 |
 
 
  

#### setImmersiveMode()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```
 
**描述：**
 
设置嵌入式弹窗蒙层的显示区域。
 
> [!NOTE]
> setImmersiveMode方法需要在调用 show 方法之前调用。

 
**起始版本：** 15
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_ImmersiveMode immersiveMode | 显示区域类型的枚举值，类型为ArkUI_ImmersiveMode。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常，请检查参数是否有效。 |
