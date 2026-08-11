# embedded_component.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-embedded-component-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明EmbeddedComponent组件选项（ArkUI_EmbeddedComponentOption）相关的结构体和方法。开发者可通过这些方法创建、销毁组件选项对象，并为EmbeddedComponent组件设置运行异常回调（onError）和正常退出回调（onTerminated）。
 
**引用文件：** <arkui/node_attributes/embedded_component.h>
 
**库：** libace_ndk.z.so
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**相关示例：** [embedded_component_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/UIExtensionAndAccessibility)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AbilityBase_Want | AbilityBase_Want | 声明元能力Want结构。 |
| ArkUI_EmbeddedComponentOption | ArkUI_EmbeddedComponentOption | 为EmbeddedComponent定义参数EmbeddedComponentOption。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create() | - | 创建EmbeddedComponent组件选项的对象。 |
| void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option) | - | 删除EmbeddedComponent组件选项的对象。 |
| void OH_ArkUI_EmbeddedComponentOption_SetOnError(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message)) | - | 设置EmbeddedComponent组件的onError回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。 |
| void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want)) | - | 设置EmbeddedComponent组件的onTerminated回调。EmbeddedComponent组件正常退出时触发本回调。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_ArkUI_EmbeddedComponentOption_Create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create()
```
 
**描述：**
 
创建EmbeddedComponent组件选项的对象。
 
**起始版本：** 20
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* | 返回指向EmbeddedComponent组件选项的对象的指针。 |
 
 
  

#### OH_ArkUI_EmbeddedComponentOption_Dispose()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option)
```
 
**描述：**
 
删除EmbeddedComponent组件选项的对象。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | 要销毁的EmbeddedComponent组件选项的对象的指针。 |
 
 
  

#### OH_ArkUI_EmbeddedComponentOption_SetOnError()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_EmbeddedComponentOption_SetOnError(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message))
```
 
**描述：**
 
设置EmbeddedComponent组件的[onError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component#onerror)回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | EmbeddedComponent组件选项的对象的指针。 |
| void (*callback)(int32_t code, const char* name, const char* message) | 开发者自定义回调函数。 - code：接口调用失败返回的错误码信息。错误码的详细介绍请参考UIExtension错误码。 - name：接口调用失败返回的名称信息。 - message：接口调用失败返回的详细信息。 |
 
 
  

#### OH_ArkUI_EmbeddedComponentOption_SetOnTerminated()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want))
```
 
**描述：**
 
设置EmbeddedComponent组件的[onTerminated](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component#onterminated)回调。EmbeddedComponent组件正常退出时触发本回调。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ArkUI_EmbeddedComponentOption* option | EmbeddedComponent组件选项的对象的指针。 |
| void (*callback)(int32_t code, AbilityBase_Want* want) | 开发者自定义回调函数。 - code：被拉起EmbeddedUIExtensionAbility退出时返回的结果码。若EmbeddedUIExtensionAbility通过调用terminateSelfWithResult退出，结果码为EmbeddedUIExtensionAbility设置的值。若EmbeddedUIExtensionAbility通过调用terminateSelf退出，结果码为默认值"0"。 - want：被拉起EmbeddedUIExtensionAbility退出时返回的数据。 |
