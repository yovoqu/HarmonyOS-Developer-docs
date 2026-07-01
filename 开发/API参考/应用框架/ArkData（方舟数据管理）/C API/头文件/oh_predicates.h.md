# oh_predicates.h

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-predicates-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示关系型数据库（RDB）的谓词。
 
**引用文件：** <database/rdb/oh_predicates.h>
 
**库：** libnative_rdb_ndk.z.so
 
**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core
 
**起始版本：** 10
 
**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Predicates | OH_Predicates | 表示谓词。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_OrderType | OH_OrderType | 排序方式。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int OH_Predicates_NotLike(OH_Predicates *predicates, const char *field, const char *pattern) | 设置OH_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。 此方法类似于SQL语句中的“Not like”。 |
| int OH_Predicates_Glob(OH_Predicates *predicates, const char *field, const char *pattern) | 设置OH_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。 与like方法不同，此方法的输入参数区分大小写。 |
| int OH_Predicates_NotGlob(OH_Predicates *predicates, const char *field, const char *pattern) | 设置OH_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。 与Not Like方法不同，此方法的输入参数区分大小写。 |
| int OH_Predicates_Having(OH_Predicates *predicates, const char *conditions, const OH_Data_Values *values) | 设置OH_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_OrderType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_OrderType
```
 
**描述**
 
排序方式。
 
**起始版本：** 10
  
| 枚举项 | 描述 |
| --- | --- |
| ASC = 0 | 升序排列。 |
| DESC = 1 | 降序排列。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_Predicates_NotLike()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int OH_Predicates_NotLike(OH_Predicates *predicates, const char *field, const char *pattern)
```
 
**描述**
 
设置OH_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。
 
此方法类似于SQL语句中的“Not like”。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Predicates *predicates | 表示指向OH_Predicates实例的指针。 |
| const char *field | 表示数据库表中的列名，不能为空。 |
| const char *pattern | 表示谓词不匹配的模式，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。详细信息请参阅OH_Rdb_ErrCode。 |
 
 
  

#### OH_Predicates_Glob()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int OH_Predicates_Glob(OH_Predicates *predicates, const char *field, const char *pattern)
```
 
**描述**
 
设置OH_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。
 
与like方法不同，此方法的输入参数区分大小写。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Predicates *predicates | 表示指向OH_Predicates实例的指针。 |
| const char *field | 表示数据库表中的列名，不能为空。 |
| const char *pattern | 表示谓词匹配的样式，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。详细信息请参阅OH_Rdb_ErrCode。 |
 
 
  

#### OH_Predicates_NotGlob()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int OH_Predicates_NotGlob(OH_Predicates *predicates, const char *field, const char *pattern)
```
 
**描述**
 
设置OH_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。
 
与Not Like方法不同，此方法的输入参数区分大小写。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Predicates *predicates | 表示指向OH_Predicates实例的指针。 |
| const char *field | 表示数据库表中的列名，不能为空。 |
| const char *pattern | 表示谓词不匹配的样式，不能为空。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。详细信息请参阅OH_Rdb_ErrCode。 |
 
 
  

#### OH_Predicates_Having()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int OH_Predicates_Having(OH_Predicates *predicates, const char *conditions, const OH_Data_Values *values)
```
 
**描述**
 
设置OH_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Predicates *predicates | 表示指向OH_Predicates实例的指针。 |
| const char *conditions | 表示having子句中的过滤条件，不能为空且不能为空字符串。 |
| const OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。详细信息请参阅OH_Rdb_ErrCode。 |
