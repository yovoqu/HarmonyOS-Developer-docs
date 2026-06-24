# JSVM_CallbackStruct*

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef JSVM_CallbackStruct* JSVM_Callback
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

用户提供的native函数的函数指针类型，这些函数通过JSVM-API接口暴露给JavaScript。
 
**使用场景：** 在Native层实现JavaScript可调用的函数时使用，适用于JSVM扩展开发场景。
 
**解决的问题：** 定义标准化的函数指针类型，便于将C/C++函数暴露给JavaScript环境。
 
**功能特点：** 提供类型安全的函数指针定义，支持Native与JavaScript的交互。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
