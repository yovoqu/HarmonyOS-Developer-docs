# JSVM_DefineClassOptions

更新时间：2026-03-12 02:57:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-defineclassoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_DefineClassOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

定义Class的选项。
 
**起始版本：** 18
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| JSVM_DefineClassOptionsId id | 定义Class的选项ID。 |
| content | id对应的定义Class选项值联合体。 |
| content.ptr | 指向定义Class选项值的指针。 |
| content.num | 存储整数类型的定义Class选项值。 |
| content.boolean | 存储布尔类型的定义Class选项值。 |
