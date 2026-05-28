# JSVM_CallbackStruct

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_CallbackStruct
```
  

##### 概述

用户提供的Native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。
 
**起始版本：** 11
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| void* data | 用户提供的Native回调函数的数据。 |
 
 
  

##### 成员函数
 
| 名称 | 描述 |
| --- | --- |
| JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info) | 用户提供的Native回调函数的指针。 |
 
 
  

##### 成员函数说明

  

##### callback()

```text
JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info)
```
 
**描述**
 
用户提供的Native回调函数的指针。
