# aip_retrieval_condition_vector.h

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition-vector
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

提供与向量条件相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip_retrieval_condition_vector.h"

**库：** libretrieval_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 类型定义


| 名称 | 描述 |
| --- | --- |
| typedef struct [OH_Retrieval_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) [OH_Retrieval_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) | 定义向量检索条件，包含检索的字段、检索参数、过滤条件等。 |


### 函数


| 名称 | 描述 |
| --- | --- |
| [OH_Retrieval_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) * [OH_Retrieval_CreateVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createvectorcondition) () | 创建向量检索条件。 |
| int [OH_Retrieval_DestroyVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_destroyvectorcondition) ([OH_Retrieval_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) *condition) | 销毁通过[OH_Retrieval_CreateVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createvectorcondition)获得的检索条件。 |
| int [OH_Retrieval_SetVectorRecallLimit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_setvectorrecalllimit) ([OH_Retrieval_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) *condition, uint32_t limit) | 在检索条件中，设置向量检索结果数量上限。 |
| int [OH_Retrieval_SetSimilarityThreshold](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_setsimilaritythreshold) ([OH_Retrieval_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) *condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |
