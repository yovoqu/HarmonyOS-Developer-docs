# ArkUI_ContextCallback

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_ContextCallback
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

事件回调类型，用于定义回调函数及其用户自定义数据。使用该类型的接口触发回调时，会调用callback，并将userData作为参数传入。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void* userData | 用户自定义数据，在回调时作为参数传入。 |
 
 
  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void (*callback)(void* userData) | 事件触发时执行的回调函数，调用时会传入userData指向的用户自定义数据。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### callback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*callback)(void* userData)
```
 
**描述：**
 
事件触发时执行的回调函数，无返回值。触发该回调时，会将userData指向的用户自定义数据作为参数传入，用于执行自定义处理逻辑。具体触发时机由使用该类型的接口定义。
