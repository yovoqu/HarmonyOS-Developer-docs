# JSVM_Deferred__*

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-deferred--8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct JSVM_Deferred__* JSVM_Deferred
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

表示Promise延迟对象。
 
**使用场景：** 在JSVM Native模块中需要创建Promise对象并延迟处理异步操作结果时，需要在Native层手动控制Promise的resolve或reject时机的场景，将Native层的异步操作结果封装为Promise返回给JavaScript层。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
