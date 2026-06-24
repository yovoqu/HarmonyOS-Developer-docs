# JSVM_CompileProfile

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef const struct {...} JSVM_CompileProfile
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

与JSVM_COMPILE_COMPILE_PROFILE一起传递的编译采样文件。
 
**使用场景：** 用于应用二次启动时的预编译优化，可提升应用启动速度和运行性能。适用于需要优化启动性能的应用场景。
 
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
| int *profile | 编译采样文件的指针。 |
| size_t length | 编译采样文件的大小。 |
