# JSVM_PropertyHandlerConfigurationStruct

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。
 
**使用场景：** 需要拦截和处理JavaScript对象属性操作的场景，实现动态属性访问控制，构建代理对象或属性监听机制。
 
**解决的问题：** 提供了一种机制来拦截和自定义对象的属性操作行为，允许在属性读写删除等操作时执行自定义逻辑。
 
**收益：** 增强对象操作的灵活性和可控性，简化属性拦截的实现逻辑。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 12
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| JSVM_Value namedPropertyData | 命名属性回调使用的数据。 |
| JSVM_Value indexedPropertyData | 索引属性回调使用的数据。 |
 
 
  

#### 回调函数成员

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData) | 通过获取实例对象的命名属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData) | 通过设置实例对象的命名属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData) | 通过删除实例对象的命名属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData) | 通过获取对象上的所有命名属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData) | 通过获取实例对象的索引属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData) | 通过设置实例对象的索引属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData) | 通过删除实例对象的索引属性而触发的回调函数。 |
| JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData) | 通过获取对象上的所有索引属性而触发的回调函数。 |
 
 
  

#### 回调函数成员说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### genericNamedPropertyGetterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过获取实例对象的命名属性而触发的回调函数。
 
  

#### genericNamedPropertySetterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过设置实例对象的命名属性而触发的回调函数。
 
  

#### genericNamedPropertyDeleterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过删除实例对象的命名属性而触发的回调函数。
 
  

#### genericNamedPropertyEnumeratorCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过获取对象上的所有命名属性而触发的回调函数。
 
  

#### genericIndexedPropertyGetterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过获取实例对象的索引属性而触发的回调函数。
 
  

#### genericIndexedPropertySetterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过设置实例对象的索引属性而触发的回调函数。
 
  

#### genericIndexedPropertyDeleterCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过删除实例对象的索引属性而触发的回调函数。
 
  

#### genericIndexedPropertyEnumeratorCallback()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过获取对象上的所有索引属性而触发的回调函数。
