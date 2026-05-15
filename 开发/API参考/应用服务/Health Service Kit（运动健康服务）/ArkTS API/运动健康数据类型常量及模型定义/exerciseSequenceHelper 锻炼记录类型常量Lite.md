# exerciseSequenceHelper (锻炼记录类型常量)(Lite)

更新时间：2026-05-12 09:31:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper-lite
**支持设备：** lite_wearable

本模块提供锻炼记录数据类型常量及数据模型。

**起始版本：** 6.1.1(24)


## 导入模块
**支持设备：** lite_wearable


```java
import healthStore from '@hms.health.store';
```


> [!NOTE]
> 此模块为healthStore子模块，需通过healthStore.exerciseSequenceHelper方式使用。


## 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 锻炼记录数据类型。 |


## badminton
**支持设备：** lite_wearable

羽毛球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 羽毛球子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.Badminton

羽毛球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.Badminton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#badminton) | 羽毛球锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.BadmintonSummary

羽毛球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.BadmintonSummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#badmintonsummary) | 羽毛球统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.BadmintonDetail

羽毛球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.BadmintonDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#badmintondetail) | 羽毛球详情数据字段列表。 |


## tennis
**支持设备：** lite_wearable

网球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 网球子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.Tennis

网球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.Tennis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#tennis) | 网球锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.TennisSummary

网球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.TennisSummary | 网球统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.TennisDetail

网球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.TennisDetail | 网球详情数据字段列表。 |


## stairClimb
**支持设备：** lite_wearable

爬楼数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 爬楼子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.StairClimb

爬楼锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.StairClimb](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#stairclimb) | 爬楼锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.StairClimbSummary

爬楼统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.StairClimbSummary | 爬楼统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.StairClimbDetail

爬楼详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.StairClimbDetail | 爬楼详情数据字段列表。 |


## soccer
**支持设备：** lite_wearable

足球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 足球子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.Soccer

足球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.Soccer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#soccer) | 足球锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.SoccerSummary

足球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.SoccerSummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#soccersummary) | 足球统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.SoccerDetail

足球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.SoccerDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#soccerdetail) | 足球详情数据字段列表。 |


## pickleBall
**支持设备：** lite_wearable

匹克球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 匹克球子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.PickleBall

匹克球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.PickleBall](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#pickleball) | 匹克球锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.PickleBallSummary

匹克球统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.PickleBallSummary | 匹克球统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.PickleBallDetail

匹克球详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| healthFields.PickleBallDetail | 匹克球详情数据字段列表。 |


## strengthTraining
**支持设备：** lite_wearable

力量训练数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


### 常量
**支持设备：** lite_wearable

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | [healthStore.SubDataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#subdatatype) | 力量训练子数据类型。 |


### Model
**支持设备：** lite_wearable

type Model = healthModels.StrengthTraining

力量训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthModels.StrengthTraining](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite#strengthtraining) | 力量训练锻炼记录数据模型。 |


### SummaryFields
**支持设备：** lite_wearable

type SummaryFields = healthFields.StrengthTrainingSummary

力量训练统计数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.StrengthTrainingSummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#strengthtrainingsummary) | 力量训练统计数据字段列表。 |


### DetailFields
**支持设备：** lite_wearable

type DetailFields = healthFields.StrengthTrainingDetail

力量训练详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthFields.StrengthTrainingDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#strengthtrainingdetail) | 力量训练详情数据字段列表。 |
