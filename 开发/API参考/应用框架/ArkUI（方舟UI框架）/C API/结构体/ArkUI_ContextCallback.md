# ArkUI_ContextCallback

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} ArkUI_ContextCallback
```
  

##### 概述

事件回调类型。
 
**起始版本：** 12
 
**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)
 
**所在头文件：** [native_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| void* userData | 自定义类型，开发者自定义类型的数据，在回调时作为参数传入。 |
 
 
  

##### 成员函数
 
| 名称 | 描述 |
| --- | --- |
| void (*callback)(void* userData) | 事件回调。 |
 
 
  

##### 成员函数说明

  

##### callback()

```text
void (*callback)(void* userData)
```
 
**描述：**
 
事件回调。
