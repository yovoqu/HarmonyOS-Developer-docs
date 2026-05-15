# healthModels (运动健康数据模型)(Lite)

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels-lite
**支持设备：** lite_wearable

本模块提供运动健康数据模型。

**起始版本：** 6.1.1(24)


## 导入模块
**支持设备：** lite_wearable


```java
import healthStore from '@hms.health.store';
```


> [!NOTE]
> 此模块为healthStore子模块，需通过healthStore.healthModels方式使用。


## Badminton
**支持设备：** lite_wearable

type Badminton = healthStore.ExerciseSequence<healthFields.BadmintonSummary, healthFields.BadmintonDetail>

羽毛球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;[healthFields.BadmintonSummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#badmintonsummary), [healthFields.BadmintonDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#badmintondetail)&gt; | 羽毛球锻炼记录数据模型。 |


## Tennis
**支持设备：** lite_wearable

type Tennis = healthStore.ExerciseSequence<healthFields.TennisSummary, healthFields.TennisDetail>

网球数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;healthFields.TennisSummary, healthFields.TennisDetail&gt; | 网球锻炼记录数据模型。 |


## StairClimb
**支持设备：** lite_wearable

type StairClimb = healthStore.ExerciseSequence<healthFields.StairClimbSummary, healthFields.StairClimbDetail>

爬楼锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;healthFields.StairClimbSummary, healthFields.StairClimbDetail&gt; | 爬楼锻炼记录数据模型。 |


## Soccer
**支持设备：** lite_wearable

type Soccer = healthStore.ExerciseSequence<healthFields.SoccerSummary, healthFields.SoccerDetail>

足球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;healthFields.SoccerSummary, healthFields.SoccerDetail; | 足球锻炼记录数据模型。 |


## PickleBall
**支持设备：** lite_wearable

type PickleBall = healthStore.ExerciseSequence<healthFields.PickleBallSummary, healthFields.PickleBallDetail>

匹克球锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;healthFields.PickleBallSummary, healthFields.PickleBallDetail&gt; | 匹克球锻炼记录数据模型。 |


## StrengthTraining
**支持设备：** lite_wearable

type StrengthTraining = healthStore.ExerciseSequence<healthFields.StrengthTrainingSummary, healthFields.StrengthTrainingDetail>

力量训练锻炼记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore.Lite

**起始版本：** 6.1.1(24)

**模型约束：** 此接口仅可在FA模型下使用。


| 类型 | 说明 |
| --- | --- |
| [healthStore.ExerciseSequence](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore-lite#exercisesequence)&lt;[healthFields.StrengthTrainingSummary](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#strengthtrainingsummary), [healthFields.StrengthTrainingDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields-lite#strengthtrainingdetail)&gt; | 力量训练锻炼记录数据模型。 |
