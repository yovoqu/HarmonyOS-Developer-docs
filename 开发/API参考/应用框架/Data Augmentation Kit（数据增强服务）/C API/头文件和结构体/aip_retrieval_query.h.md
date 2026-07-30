# aip_retrieval_query.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-query
**支持设备：** Phone | PC/2in1 | Tablet

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

提供与检索查询相关的接口。
 
**引用文件：** #include "dataaugmentation/retrieval/aip_retrieval_query.h"
 
**库：** libretrieval_ndk.so
 
**系统能力：** SystemCapability.DataAugmentation.Retrieval
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 类型定义

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| typedef struct OH_Retrieval_Query OH_Retrieval_Query | 定义检索词，当前只支持纯文本检索。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| OH_Retrieval_Query * OH_Retrieval_CreateQuery () | 创建检索词，作为检索接口的入参。 |
| int OH_Retrieval_DestroyQuery (OH_Retrieval_Query *query) | 销毁通过OH_Retrieval_CreateQuery获得的检索词。 |
| int OH_Retrieval_SetOriginalQuestion (OH_Retrieval_Query *query, const char *question) | 设置OH_Retrieval_Query中的检索词。其中，参数question为待检索的纯文本字符串，用于指定具体的检索内容。该参数不能为空，且长度不得超过512个字符。 |
