# JSVM_CompileOptions

更新时间：2026-03-12 02:57:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_CompileOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

配合[OH_JSVM_CompileScriptWithOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilescriptwithoptions)接口使用，是其参数中options数组的元素类型。
 
**起始版本：** 12
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| JSVM_CompileOptionId id | 编译选项对应的ID。 |
| content | id对应的编译选项值联合体。 |
| content.ptr | 指向编译选项值的指针。 |
| content.num | 存储整数类型的编译选项值。 |
| content.boolean | 存储布尔类型的编译选项值。 |
