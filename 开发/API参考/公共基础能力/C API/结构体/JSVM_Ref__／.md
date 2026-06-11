# JSVM_Ref__*

更新时间：2026-06-09 02:58:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-ref--8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct JSVM_Ref__* JSVM_Ref
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

表示JavaScript值的引用。
 
**使用场景：** 在Native与JavaScript交互场景中，需要持有JavaScript对象引用时使用。
 
**功能特点：** 提供对JavaScript值的稳定引用，防止被垃圾回收。支持跨函数、跨作用域传递JavaScript值。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
