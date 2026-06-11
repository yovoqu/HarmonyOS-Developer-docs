# JSVM_CallbackStruct

更新时间：2026-06-09 02:58:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_CallbackStruct
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

用户提供的Native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。
 
**使用场景：** 在Native层实现JavaScript可调用的函数，将C/C++函数封装为JavaScript回调，实现Native与JavaScript之间的双向交互。
 
**功能特点：** 支持传递自定义数据到回调函数，提供标准的回调函数签名，跨语言调用的基础设施。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| void* data | 用户提供的Native回调函数的数据。 |
 
 
  

#### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env, JSVM_CallbackInfo info) | 用户提供的Native回调函数的指针。 |
 
 
  

#### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### callback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env, JSVM_CallbackInfo info)
```
 
**描述**
 
用户提供的Native回调函数的指针。
