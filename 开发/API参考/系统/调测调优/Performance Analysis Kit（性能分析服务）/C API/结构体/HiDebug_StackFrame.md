# HiDebug_StackFrame

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

栈帧内容的定义。
 
**起始版本：** 20
 
**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
 
**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| HiDebug_StackFrameType type | 当前栈的类型。 |
| struct HiDebug_JsStackFrame js | 由HiDebug_JsStackFrame定义的js栈帧内容。 |
| struct HiDebug_NativeStackFrame native | 由HiDebug_NativeStackFrame定义的native栈帧内容。 |
