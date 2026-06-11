# JSVM_EscapableHandleScope__*

更新时间：2026-06-09 02:58:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-escapablehandlescope--8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct JSVM_EscapableHandleScope__* JSVM_EscapableHandleScope
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

表示一种特殊类型的handle scope，用于将在特定handle scope内创建的值返回到父作用域。
 
**使用场景：** 当需要在子函数中创建JS对象并将其返回给父函数或更上层作用域时使用，在JSVM API开发中，需要将局部创建的JS值传递出当前作用域的场景。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**支持设备类型：** Phone | PC/2in1 | Tablet | Wearable。具体支持情况可通过对应的API接口进行判断。
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
