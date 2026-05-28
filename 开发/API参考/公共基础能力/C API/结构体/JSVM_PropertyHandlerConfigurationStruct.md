# JSVM_PropertyHandlerConfigurationStruct

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```
  

##### 概述

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。
 
**起始版本：** 12
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| JSVM_Value namedPropertyData | 命名属性回调使用的数据。 |
| JSVM_Value indexedPropertyData | 索引属性回调使用的数据。 |
 
 
  

##### 成员函数
 
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
 
 
  

##### 成员函数说明

  

##### genericNamedPropertyGetterCallback()

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过获取实例对象的命名属性而触发的回调函数。
 
  

##### genericNamedPropertySetterCallback()

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过设置实例对象的命名属性而触发的回调函数。
 
  

##### genericNamedPropertyDeleterCallback()

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过删除实例对象的命名属性而触发的回调函数。
 
  

##### genericNamedPropertyEnumeratorCallback()

```text
JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```
 
**描述**
 
通过获取对象上的所有命名属性而触发的回调函数。
 
  

##### genericIndexedPropertyGetterCallback()

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过获取实例对象的索引属性而触发的回调函数。
 
  

##### genericIndexedPropertySetterCallback()

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过设置实例对象的索引属性而触发的回调函数。
 
  

##### genericIndexedPropertyDeleterCallback()

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过删除实例对象的索引属性而触发的回调函数。
 
  

##### genericIndexedPropertyEnumeratorCallback()

```text
JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```
 
**描述**
 
通过获取对象上的所有索引属性而触发的回调函数。
