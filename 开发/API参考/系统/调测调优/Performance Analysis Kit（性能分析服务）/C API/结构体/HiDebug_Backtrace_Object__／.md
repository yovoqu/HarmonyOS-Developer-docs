# HiDebug_Backtrace_Object__*

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-backtrace-object--8h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HiDebug_Backtrace_Object__* HiDebug_Backtrace_Object
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于栈回溯及栈解析的对象。该对象封装了栈回溯所需的上下文信息，包括调用栈地址、线程状态等数据，通过相关接口可获取详细的栈帧信息和符号解析结果。该对象通过HiDebug相关接口创建，使用后需要调用对应的销毁接口释放资源。
 
**起始版本：** 20
 
**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
 
**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
