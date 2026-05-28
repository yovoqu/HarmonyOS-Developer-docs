# data_type.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-data-type-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明了张量的数据的类型。
 
**引用文件：** <mindspore/data_type.h>
 
**库：** libmindspore_lite_ndk.so
 
**系统能力：** SystemCapability.Ai.MindSpore
 
**起始版本：** 9
 
**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AI_DataType | OH_AI_DataType | MSTensor保存的数据支持的类型。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AI_DataType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AI_DataType
```
 
**描述**
 
MSTensor保存的数据支持的类型。
 
**起始版本：** 9
  
| 枚举项 | 描述 |
| --- | --- |
| OH_AI_DATATYPE_UNKNOWN = 0 | 未知的数据类型。 |
| OH_AI_DATATYPE_OBJECTTYPE_STRING = 12 | String数据类型。 |
| OH_AI_DATATYPE_OBJECTTYPE_LIST = 13 | List数据类型。 |
| OH_AI_DATATYPE_OBJECTTYPE_TUPLE = 14 | Tuple数据类型。 |
| OH_AI_DATATYPE_OBJECTTYPE_TENSOR = 17 | TensorList数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_BEGIN = 29 | Number类型的起始。 |
| OH_AI_DATATYPE_NUMBERTYPE_BOOL = 30 | Bool数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_INT8 = 32 | Int8数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_INT16 = 33 | Int16数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_INT32 = 34 | Int32数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_INT64 = 35 | Int64数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_UINT8 = 37 | UInt8数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_UINT16 = 38 | UInt16数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_UINT32 = 39 | UInt32数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_UINT64 = 40 | UInt64数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_FLOAT16 = 42 | Float16数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_FLOAT32 = 43 | Float32数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_FLOAT64 = 44 | Float64数据类型。 |
| OH_AI_DATATYPE_NUMBERTYPE_END = 46 | Number类型的结尾。 |
| OH_AI_DataTypeInvalid = INT32_MAX | 无效的数据类型。 |
