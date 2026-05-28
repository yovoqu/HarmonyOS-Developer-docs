# Retrieval

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

智慧化数据平台（AIP）为应用提供构建端侧智慧化解决方案，提供向量化、知识检索和知识问答的能力。
 
**起始版本：** 6.0.0(20)
 
  

##### 汇总

  

##### 文件
 
| 名称 | 描述 |
| --- | --- |
| aip_retrieval.h | 提供知识检索相关的接口。 |
| aip_retrieval_condition.h | 提供与检索条件相关的接口。 |
| aip_retrieval_condition_vector.h | 提供与向量条件相关的接口。 |
| aip_retrieval_query.h | 提供与检索查询相关的接口。 |
| aip_retrieval_record.h | 提供与检索结果相关的接口。 |
 
 
  

##### 类型定义
 
| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Retriever OH_Retrieval_Retriever | 定义检索器类型，检索器是进行检索的句柄。 |
| typedef struct OH_Retrieval_Config OH_Retrieval_Config | 定义检索器配置。 |
| typedef struct OH_Retrieval_DbConfig OH_Retrieval_DbConfig | 定义一个用于打开数据库存储的数据库配置。 |
| typedef enum Retrieval_Channel_Type Retrieval_Channel_Type | 定义数据索引类型，目前仅包括向量索引数据。 |
| typedef void(* OH_Retrieval_Callback) (void *context, OH_Retrieval_Record *record, int errCode) | 检索结果记录的回调函数。 |
| typedef struct OH_Retrieval_Condition OH_Retrieval_Condition | 定义检索条件，可包含多个子检索条件等。 |
| typedef struct OH_Retrieval_SubCondition OH_Retrieval_SubCondition | 定义子检索条件，可以是向量检索。 |
| typedef struct OH_Retrieval_SubCondition OH_Retrieval_VectorCondition | 定义向量检索条件，包含检索的字段、检索参数、过滤条件等。 |
| typedef struct OH_Retrieval_Query OH_Retrieval_Query | 定义检索词，当前只支持纯文本检索。 |
| typedef struct OH_Retrieval_Record OH_Retrieval_Record | 定义检索结果，包含检索知识库得到的字段和字段取值。 |
| typedef struct OH_Retrieval_RecordItem OH_Retrieval_RecordItem | 定义检索结果中的数据库bucket数组。 |
 
 
  

##### 枚举
 
| 名称 | 描述 |
| --- | --- |
| Retrieval_Channel_Type { Retrieval_TYPE_VECTOR = 1 } | 定义数据索引类型，目前仅包括向量索引数据。 |
 
 
  

##### 函数
 
| 名称 | 描述 |
| --- | --- |
| int OH_Retrieval_CreateRetriever (const OH_Retrieval_Config *config, OH_Retrieval_Retriever **retriever) | 获取检索器。 |
| int OH_Retrieval_DestroyRetriever (OH_Retrieval_Retriever *retriever) | 销毁通过OH_Retrieval_CreateRetriever获得的检索器。 |
| OH_Retrieval_Config * OH_Retrieval_CreateConfig () | 获取检索器配置。 |
| int OH_Retrieval_DestroyConfig (OH_Retrieval_Config *config) | 销毁通过OH_Retrieval_CreateConfig获得的检索配置。 |
| OH_Retrieval_DbConfig * OH_Retrieval_CreateDbConfig () | 创建一个配置项以打开数据库。 |
| int OH_Retrieval_DestroyDbConfig (OH_Retrieval_DbConfig *dbConfig) | 销毁OH_Retrieval_CreateDbConfig创建的OH_Retrieval_DbConfig。 |
| int OH_Retrieval_SetDbConfig (OH_Retrieval_DbConfig *dbConfig, OH_Rdb_ConfigV2*rdbConfig) | 设置OH_Retrieval_DbConfig中的数据库配置。 |
| int OH_Retrieval_AddConfig (OH_Retrieval_Config *config, Retrieval_Channel_Type channelType, OH_Retrieval_DbConfig *dbConfig) | 设置OH_Retrieval_Config中的数据库配置。 |
| int OH_Retrieval_Retrieve (const OH_Retrieval_Retriever *retriever, const OH_Retrieval_Query *query, const OH_Retrieval_Condition *condition, void *context, const OH_Retrieval_Callback *callback) | 执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。 |
| OH_Retrieval_Condition * OH_Retrieval_CreateCondition () | 创建检索条件，作为检索接口的入参。 |
| int OH_Retrieval_DestroyCondition (OH_Retrieval_Condition *condition) | 销毁通过OH_Retrieval_CreateCondition获得的检索条件。 |
| int OH_Retrieval_DestroySubCondition (OH_Retrieval_SubCondition *condition) | 销毁OH_Retrieval_SubCondition对象。 |
| int OH_Retrieval_AddSubCondition (OH_Retrieval_Condition *condition, OH_Retrieval_SubCondition *subCondition) | 在检索条件中，增加子检索条件。 |
| OH_Retrieval_VectorCondition * OH_Retrieval_CreateVectorCondition () | 创建向量检索条件。 |
| int OH_Retrieval_DestroyVectorCondition (OH_Retrieval_VectorCondition *condition) | 销毁通过OH_Retrieval_CreateVectorCondition获得的检索条件。 |
| int OH_Retrieval_SetVectorRecallLimit (OH_Retrieval_VectorCondition *condition, uint32_t limit) | 在检索条件中，设置向量检索结果数量上限1000。 |
| int OH_Retrieval_SetSimilarityThreshold (OH_Retrieval_VectorCondition *condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |
| OH_Retrieval_Query * OH_Retrieval_CreateQuery () | 创建检索词，作为检索接口的入参。 |
| int OH_Retrieval_DestroyQuery (OH_Retrieval_Query *query) | 销毁通过OH_Retrieval_CreateQuery获得的检索词。 |
| int OH_Retrieval_SetOriginalQuestion (OH_Retrieval_Query *query, const char *question) | 设置OH_Retrieval_Query中的检索词。 |
| int OH_Retrieval_DestroyRecord (OH_Retrieval_Record *record) | 销毁通过检索接口OH_Retrieval_Retrieve获得的检索结果。 |
| int OH_Retrieval_GetRecordLength (const OH_Retrieval_Record *record, uint32_t *length) | 获取检索结果OH_Retrieval_Record中的数据库bucket数组长度。 |
| int OH_Retrieval_GetRecordItem (const OH_Retrieval_Record *record, uint32_t index, const OH_Retrieval_RecordItem **item) | 获取检索结果OH_Retrieval_Record中的数据库bucket数组。 |
| int OH_Retrieval_GetItemSize (const OH_Retrieval_RecordItem *items, const char *fieldName, size_t *size) | 获取数据库bucket数组OH_Retrieval_RecordItem中指定字段的值的size。size值包含结束符。 |
| int OH_Retrieval_GetItemText (const OH_Retrieval_RecordItem *items, const char *fieldName, char *value, size_t size) | 获取数据库bucket数组OH_Retrieval_RecordItem中指定字段的值。 |
 
 
  

##### 类型定义说明

  

##### OH_Retrieval_Callback

```text
typedef void (*OH_Retrieval_Callback)(void *context, OH_Retrieval_Record *record, int errCode)
```
 
**描述**
 
检索结果记录的回调函数。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| context | 表示用户提供的上下文数据。 |
| record | 表示指向 OH_Retrieval_Record 实例的指针。 |
| errCode | 表示返回的错误码。 |
 
 
  

##### OH_Retrieval_Condition

```text
typedef struct OH_Retrieval_Condition OH_Retrieval_Condition
```
 
**描述**
 
定义检索条件，可包含多个子检索条件。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_Config

```text
typedef struct OH_Retrieval_Config OH_Retrieval_Config
```
 
**描述**
 
定义检索器配置，包括数据库路径、数据库名称、包名等。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_DbConfig

```text
typedef struct OH_Retrieval_DbConfig OH_Retrieval_DbConfig
```
 
**描述**
 
定义一个用于打开数据库存储的数据库配置。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_Query

```text
typedef struct OH_Retrieval_Query OH_Retrieval_Query
```
 
**描述**
 
定义检索词，当前只支持纯文本检索，不支持图片、视频等。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_Record

```text
typedef struct OH_Retrieval_Record OH_Retrieval_Record
```
 
**描述**
 
定义检索结果，包含检索知识库得到的字段和字段取值。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_RecordItem

```text
typedef struct OH_Retrieval_RecordItem OH_Retrieval_RecordItem
```
 
**描述**
 
定义检索结果中的数据库bucket数组。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_Retriever

```text
typedef struct OH_Retrieval_Retriever OH_Retrieval_Retriever
```
 
**描述**
 
定义检索器类型，检索器是进行检索的句柄。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_SubCondition

```text
typedef struct OH_Retrieval_SubCondition OH_Retrieval_SubCondition
```
 
**描述**
 
定义子检索条件，目前支持向量检索。
 
**起始版本：** 6.0.0(20)
 
  

##### OH_Retrieval_VectorCondition

```text
typedef struct OH_Retrieval_SubCondition OH_Retrieval_VectorCondition
```
 
**描述**
 
定义向量检索条件，包含检索的字段、检索参数、过滤条件等。
 
**起始版本：** 6.0.0(20)
 
  

##### Retrieval_Channel_Type

```text
typedef enum Retrieval_Channel_Type Retrieval_Channel_Type
```
 
**描述**
 
定义数据索引类型，目前仅包括向量索引数据。
 
**起始版本：** 6.0.0(20)
 
  

##### 枚举类型说明

  

##### Retrieval_Channel_Type

```text
enum Retrieval_Channel_Type
```
 
**描述**
 
定义数据索引类型，目前仅包括向量索引数据。
 
**起始版本：** 6.0.0(20)
  
| 枚举值 | 描述 |
| --- | --- |
| Retrieval_TYPE_VECTOR | 表示向量索引。 |
 
 
  

##### 函数说明

  

##### OH_Retrieval_AddConfig()

```text
int OH_Retrieval_AddConfig(OH_Retrieval_Config *config, Retrieval_Channel_Type channelType, OH_Retrieval_DbConfig *dbConfig)
```
 
**描述**
 
设置[OH_Retrieval_Config](#oh_retrieval_config)中的数据库配置。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向检索配置 OH_Retrieval_Config 实例的指针。 |
| channelType | 表示一种数据索引类型，目前仅支持向量查询。 |
| dbConfig | 指向数据库配置实例的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Config](#oh_retrieval_config)、[Retrieval_Channel_Type](#retrieval_channel_type)、[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_AddSubCondition()

```text
int OH_Retrieval_AddSubCondition(OH_Retrieval_Condition *condition, OH_Retrieval_SubCondition *subCondition)
```
 
**描述**
 
在检索条件中，增加子检索条件。当前仅支持增加一个子检索条件。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件OH_Retrieval_Condition实例的指针。 |
| subCondition | 指向子检索条件实例的指针，可以是向量检索条件OH_Retrieval_VectorCondition。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200009 | 条件数量超过上限1 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Condition](#oh_retrieval_condition)、[OH_Retrieval_SubCondition](#oh_retrieval_subcondition)、[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_CreateCondition()

```text
OH_Retrieval_Condition *OH_Retrieval_CreateCondition()
```
 
**描述**
 
创建检索条件，作为检索接口的入参。
 
**起始版本：** 6.0.0(20)
 
**返回：**
 
函数执行成功时，返回指向检索条件[OH_Retrieval_Condition](#oh_retrieval_condition)实例的指针。当函数执行失败时，该指针为空指针。
 
**参见：**
 
[OH_Retrieval_Condition](#oh_retrieval_condition)
 
  

##### OH_Retrieval_CreateConfig()

```text
OH_Retrieval_Config *OH_Retrieval_CreateConfig()
```
 
**描述**
 
获取检索器配置。用于初始化检索器。
 
**起始版本：** 6.0.0(20)
 
**返回：**
 
函数执行成功时，返回指向检索器配置[OH_Retrieval_Config](#oh_retrieval_config)实例的指针。当函数执行失败时，该指针为空指针。
 
**参见：**
 
[OH_Retrieval_Config](#oh_retrieval_config)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_CreateDbConfig()

```text
OH_Retrieval_DbConfig *OH_Retrieval_CreateDbConfig()
```
 
**描述**
 
创建一个数据库相关配置项。
 
**起始版本：** 6.0.0(20)
 
**返回：**
 
返回指向[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)实例的指针。当函数执行失败时，该指针为空指针。
 
**参见：**
 
[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_CreateQuery()

```text
OH_Retrieval_Query *OH_Retrieval_CreateQuery()
```
 
**描述**
 
创建检索词，作为检索接口的入参。
 
**起始版本：** 6.0.0(20)
 
**返回：**
 
函数执行成功时，返回指向[OH_Retrieval_Query](#oh_retrieval_query)实例的指针。当函数执行失败时，该指针为空指针。
 
**参见：**
 
[OH_Retrieval_Query](#oh_retrieval_query)
 
  

##### OH_Retrieval_CreateRetriever()

```text
int OH_Retrieval_CreateRetriever(const OH_Retrieval_Config *config, OH_Retrieval_Retriever **retriever)
```
 
**描述**
 
读取检索配置，初始化检索器。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| config | 创建检索器时，需要输入检索器的配置项OH_Retrieval_Config。 |
| retriever | 返回指向检索器OH_Retrieval_Retriever实例的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Retriever](#oh_retrieval_retriever)、[OH_Retrieval_Config](#oh_retrieval_config)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_CreateVectorCondition()

```text
OH_Retrieval_VectorCondition *OH_Retrieval_CreateVectorCondition()
```
 
**描述**
 
创建向量检索条件。
 
**起始版本：** 6.0.0(20)
 
**返回：**
 
函数执行成功时，返回指向检索条件[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)实例的指针。当函数执行失败时，该指针为空指针。
 
**参见：**
 
[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)
 
  

##### OH_Retrieval_DestroyCondition()

```text
int OH_Retrieval_DestroyCondition(OH_Retrieval_Condition *condition)
```
 
**描述**
 
销毁通过[OH_Retrieval_CreateCondition](#oh_retrieval_createcondition)获得的检索条件。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件OH_Retrieval_Condition的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Condition](#oh_retrieval_condition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateCondition](#oh_retrieval_createcondition)
 
  

##### OH_Retrieval_DestroyConfig()

```text
int OH_Retrieval_DestroyConfig(OH_Retrieval_Config *config)
```
 
**描述**
 
销毁通过OH_Retriever_CreateConfig获得的检索配置。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| config | 指向检索配置OH_Retrieval_Config的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Config](#oh_retrieval_config)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateConfig](#oh_retrieval_createconfig)
 
  

##### OH_Retrieval_DestroyDbConfig()

```text
int OH_Retrieval_DestroyDbConfig(OH_Retrieval_DbConfig *dbConfig)
```
 
**描述**
 
销毁[OH_Retrieval_CreateDbConfig](#oh_retrieval_createdbconfig)创建的[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| dbConfig | 表示指向OH_Retrieval_DbConfig实例的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateDbConfig](#oh_retrieval_createdbconfig)
 
  

##### OH_Retrieval_DestroyQuery()

```text
int OH_Retrieval_DestroyQuery(OH_Retrieval_Query *query)
```
 
**描述**
 
销毁通过[OH_Retrieval_CreateQuery](#oh_retrieval_createquery)获得的检索词。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| query | 指向检索词OH_Retrieval_Query的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Query](#oh_retrieval_query)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateQuery](#oh_retrieval_createquery)
 
  

##### OH_Retrieval_DestroyRecord()

```text
int OH_Retrieval_DestroyRecord(OH_Retrieval_Record *record)
```
 
**描述**
 
销毁通过检索接口[OH_Retrieval_Retrieve](#oh_retrieval_retrieve)获得的检索结果。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果OH_Retrieval_Record的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Record](#oh_retrieval_record)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_Retrieve](#oh_retrieval_retrieve)
 
  

##### OH_Retrieval_DestroyRetriever()

```text
int OH_Retrieval_DestroyRetriever(OH_Retrieval_Retriever *retriever)
```
 
**描述**
 
销毁通过[OH_Retrieval_CreateRetriever](#oh_retrieval_createretriever)获得的检索器。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| retriever | 指向检索器OH_Retrieval_Retriever的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Retriever](#oh_retrieval_retriever)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateRetriever](#oh_retrieval_createretriever)
 
  

##### OH_Retrieval_DestroySubCondition()

```text
int OH_Retrieval_DestroySubCondition(OH_Retrieval_SubCondition *condition)
```
 
**描述**
 
销毁通过[OH_Retrieval_SubCondition](#oh_retrieval_subcondition)。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件OH_Retrieval_SubCondition的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_SubCondition](#oh_retrieval_subcondition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_DestroyVectorCondition()

```text
int OH_Retrieval_DestroyVectorCondition(OH_Retrieval_VectorCondition *condition)
```
 
**描述**
 
销毁通过[OH_Retrieval_CreateVectorCondition](#oh_retrieval_createvectorcondition)获得的检索条件。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向向量检索条件OH_Retrieval_VectorCondition的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)、[OH_Retrieval_CreateVectorCondition](#oh_retrieval_createvectorcondition)
 
  

##### OH_Retrieval_GetItemSize()

```text
int OH_Retrieval_GetItemSize(const OH_Retrieval_RecordItem *items, const char *fieldName, size_t *size)
```
 
**描述**
 
获取数据库bucket数组[OH_Retrieval_RecordItem](#oh_retrieval_recorditem)中指定字段的值的size。size值包含结束符。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| items | 指向数据库bucket数组OH_Retrieval_RecordItem实例的指针。 |
| fieldName | 数据库bucket的字段名。 |
| size | 数据库bucket相应字段的值的大小。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200007 | 不存在该字段 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_RecordItem](#oh_retrieval_recorditem)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_GetItemText()

```text
int OH_Retrieval_GetItemText(const OH_Retrieval_RecordItem *items, const char *fieldName, char *value, size_t size)
```
 
**描述**
 
获取数据库bucket数组[OH_Retrieval_RecordItem](#oh_retrieval_recorditem)中指定字段的值。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| items | 指向数据库bucket数组OH_Retrieval_RecordItem实例的指针。 |
| fieldName | 数据库bucket的字段名。 |
| value | 数据库bucket相应字段的值。 |
| size | 数据库bucket相应字段的值的大小。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200007 | 不存在该字段 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_RecordItem](#oh_retrieval_recorditem)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_GetRecordItem()

```text
int OH_Retrieval_GetRecordItem(const OH_Retrieval_Record *record, uint32_t index, const OH_Retrieval_RecordItem **item)
```
 
**描述**
 
获取检索结果[OH_Retrieval_Record](#oh_retrieval_record)中的数据库bucket数组。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果OH_Retrieval_Record实例的指针。 |
| index | record数组的索引值。最大值为999。 |
| item | 指向record数组中单个元素OH_Retrieval_RecordItem的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200006 | 下标越界 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Record](#oh_retrieval_record)、[OH_Retrieval_RecordItem](#oh_retrieval_recorditem)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_GetRecordLength()

```text
int OH_Retrieval_GetRecordLength(const OH_Retrieval_Record *record, uint32_t *length)
```
 
**描述**
 
获取检索结果[OH_Retrieval_Record](#oh_retrieval_record)中的数据库bucket数组。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| record | 指向检索结果OH_Retrieval_Record实例的指针。 |
| length | 数据库bucket数组的长度。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Record](#oh_retrieval_record)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_Retrieve()

```text
int OH_Retrieval_Retrieve(const OH_Retrieval_Retriever *retriever, const OH_Retrieval_Query *query, const OH_Retrieval_Condition *condition, void *context, const OH_Retrieval_Callback *callback)
```
 
**描述**
 
执行检索。获得检索器句柄后，输入检索查询词，根据检索条件执行检索，得到检索结果。接口执行时，会在“/data/storage/el2/base/cache”路径下生成临时存储缓存文件。当设备类型为phone、tablet时，该接口仅支持倒排，不支持向量。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| retriever | 检索器句柄，指向OH_Retrieval_Retriever实例的指针。 |
| query | 检索的查询词，指向OH_Retrieval_Query实例的指针。 |
| condition | 检索条件，指向OH_Retrieval_Condition实例的指针。 |
| context | 表示用户提供的上下文数据，这些数据将在后续调用函数时传递回函数中。 |
| callback | 表示指向OH_Retrieval_Callback实例的指针。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200005 | 执行报错 |
| 1021200010 | 无效参数 |
| 1021200012 | 无法生成嵌入向量 |
 
 
**参见：**
 
[OH_Retrieval_Retriever](#oh_retrieval_retriever)、[OH_Retrieval_Query](#oh_retrieval_query)、[OH_Retrieval_Condition](#oh_retrieval_condition)、[OH_Retrieval_Callback](#oh_retrieval_callback)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_SetDbConfig()

```text
int OH_Retrieval_SetDbConfig(OH_Retrieval_DbConfig *dbConfig, OH_Rdb_ConfigV2 *rdbConfig)
```
 
**描述**
 
在[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)中设置数据库配置。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| dbConfig | 表示指向OH_Retrieval_DbConfig实例的指针。 |
| rdbConfig | 表示指向数据库配置实例的指针，可能是OH_Rdb_ConfigV2实例。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_DbConfig](#oh_retrieval_dbconfig)、[OH_Rdb_ConfigV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-configv2)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_SetOriginalQuestion()

```text
int OH_Retrieval_SetOriginalQuestion(OH_Retrieval_Query *query, const char *question)
```
 
**描述**
 
设置[OH_Retrieval_Query](#oh_retrieval_query)中的检索词。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| query | 指向检索词OH_Retrieval_Query实例的指针。 |
| question | 纯文本的问题。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200008 | 数组超过最大长度512字节 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_Query](#oh_retrieval_query)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_SetSimilarityThreshold()

```text
int OH_Retrieval_SetSimilarityThreshold(OH_Retrieval_VectorCondition *condition, double threshold)
```
 
**描述**
 
在检索条件中，设置向量检索的相似度阈值。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件OH_Retrieval_VectorCondition实例的指针。 |
| threshold | 向量检索的余弦相似度阈值，取值范围[0, 1]。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
 
  

##### OH_Retrieval_SetVectorRecallLimit()

```text
int OH_Retrieval_SetVectorRecallLimit(OH_Retrieval_VectorCondition *condition, uint32_t limit)
```
 
**描述**
 
在检索条件中，设置向量检索结果数量上限。
 
**起始版本：** 6.0.0(20)
 
**参数:**
  
| 名称 | 描述 |
| --- | --- |
| condition | 指向检索条件OH_Retrieval_VectorCondition实例的指针。 |
| limit | 向量检索结果的数量上限，最大值1000。 |
 
 
**返回：**
 
返回函数的执行状态。执行成功返回AIP_OK。
  
| 错误码ID | 错误信息 |
| --- | --- |
| 0 | 操作成功 |
| 1021200010 | 无效参数 |
 
 
**参见：**
 
[OH_Retrieval_VectorCondition](#oh_retrieval_vectorcondition)、[OH_Aip_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-aip#oh_aip_errcode-1)
