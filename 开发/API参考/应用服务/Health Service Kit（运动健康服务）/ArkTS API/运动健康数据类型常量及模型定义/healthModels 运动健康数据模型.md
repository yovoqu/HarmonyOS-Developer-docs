# healthModels (运动健康数据模型)

更新时间：2026-04-30 09:02:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels
**支持设备：** Phone | Tablet | Wearable

本模块提供运动健康数据模型。
 
**起始版本：** 5.0.0(12)
  

##### 导入模块

**支持设备：** Phone | Tablet | Wearable

```text
import { healthStore } from '@kit.HealthServiceKit';
```
 
> [!NOTE]
> 此模块为healthStore子模块，需通过healthStore.healthModels方式使用。

 
  

##### Adventures

**支持设备：** Phone | Tablet | Wearable

type Adventures = healthStore.ExerciseSequence<healthFields.AdventuresSummary, healthFields.AdventuresDetail>
 
户外探险锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.AdventuresSummary, healthFields.AdventuresDetail> | 户外探险锻炼记录数据模型。 |
 
 
  

##### Basketball

**支持设备：** Phone | Tablet | Wearable

type Basketball = healthStore.ExerciseSequence<healthFields.BasketballSummary, healthFields.BasketballDetail>
 
篮球锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.BasketballSummary, healthFields.BasketballDetail> | 篮球锻炼记录数据模型。 |
 
 
  

##### Biathlon

**支持设备：** Phone | Tablet | Wearable

type Biathlon = healthStore.ExerciseSequence<healthFields.BiathlonSummary, healthFields.BiathlonDetail>
 
冬季两项锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.BiathlonSummary, healthFields.BiathlonDetail> | 冬季两项锻炼记录数据模型。 |
 
 
  

##### BloodOxygenSaturation

**支持设备：** Phone | Tablet | Wearable

type BloodOxygenSaturation = healthStore.SamplePoint<healthFields.BloodOxygenSaturation>
 
血氧采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.BloodOxygenSaturation> | 血氧采样数据模型。 |
 
 
  

##### BloodOxygenSaturationAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type BloodOxygenSaturationAggregateRequest = healthStore.AggregateRequest<healthFields.BloodOxygenSaturationAggregation>
 
血氧采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.BloodOxygenSaturationAggregation> | 血氧采样数据聚合统计请求模型。 |
 
 
  

##### BloodOxygenSaturationAggregateResult

**支持设备：** Phone | Tablet | Wearable

type BloodOxygenSaturationAggregateResult = healthStore.AggregateResult<healthFields.BloodOxygenSaturationAggregation>
 
血氧聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.BloodOxygenSaturationAggregation> | 血氧聚合结果数据模型。 |
 
 
  

##### BloodPressure

**支持设备：** Phone | Tablet | Wearable

type BloodPressure = healthStore.SamplePoint<healthFields.BloodPressure>
 
血压采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.BloodPressure> | 血压采样数据模型。 |
 
 
  

##### Bmx

**支持设备：** Phone | Tablet | Wearable

type Bmx = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>
 
BMX自行车锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail> | BMX自行车锻炼记录数据模型。 |
 
 
  

##### BodyTemperature

**支持设备：** Phone | Tablet | Wearable

type BodyTemperature = healthStore.SamplePoint<healthFields.BodyTemperature>
 
体温采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.BodyTemperature> | 体温采样数据模型。 |
 
 
  

##### BodyTemperatureAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type BodyTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.BodyTemperatureAggregation>
 
体温采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.BodyTemperatureAggregation> | 体温采样数据聚合统计请求模型。 |
 
 
  

##### BodyTemperatureAggregateResult

**支持设备：** Phone | Tablet | Wearable

type BodyTemperatureAggregateResult = healthStore.AggregateResult<healthFields.BodyTemperatureAggregation>
 
体温聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.BodyTemperatureAggregation> | 体温聚合结果数据模型。 |
 
 
  

##### BreathHoldingTest

**支持设备：** Phone | Tablet | Wearable

type BreathHoldingTest = healthStore.ExerciseSequence<healthFields.BreathHoldingTestSummary, healthFields.BreathHoldingTestDetail>
 
闭气测试锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.BreathHoldingTestSummary, healthFields.BreathHoldingTestDetail> | 闭气测试锻炼记录数据模型。 |
 
 
  

##### BreathHoldingTrain

**支持设备：** Phone | Tablet | Wearable

type BreathHoldingTrain = healthStore.ExerciseSequence<healthFields.BreathHoldingTrainSummary, healthFields.BreathHoldingTrainDetail>
 
闭气训练锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.BreathHoldingTrainSummary, healthFields.BreathHoldingTrainDetail> | 闭气训练锻炼记录数据模型。 |
 
 
  

##### Cycling

**支持设备：** Phone | Tablet | Wearable

type Cycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>
 
户外骑行锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail> | 户外骑行锻炼记录数据模型。 |
 
 
  

##### DailyActivities

**支持设备：** Phone | Tablet | Wearable

type DailyActivities = healthStore.SamplePoint<healthFields.DailyActivities>
 
日常活动采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.DailyActivities> | 日常活动采样数据模型。 |
 
 
  

##### DailyActivitiesAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type DailyActivitiesAggregateRequest = healthStore.AggregateRequest<healthFields.DailyActivitiesAggregation>
 
日常活动采样数据聚合统计请求模型。
 
**元服务API**：从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.DailyActivitiesAggregation> | 日常活动采样数据聚合统计请求模型。 |
 
 
  

##### DailyActivitiesAggregateResult

**支持设备：** Phone | Tablet | Wearable

type DailyActivitiesAggregateResult = healthStore.AggregateResult<healthFields.DailyActivitiesAggregation>
 
日常活动聚合结果数据模型。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.DailyActivitiesAggregation> | 日常活动聚合结果数据模型。 |
 
 
  

##### Diving

**支持设备：** Phone | Tablet | Wearable

type Diving = healthStore.ExerciseSequence<healthFields.DivingSummary, healthFields.DivingDetail>
 
自由潜水锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.DivingSummary, healthFields.DivingDetail> | 自由潜水锻炼记录数据模型。 |
 
 
  

##### Elliptical

**支持设备：** Phone | Tablet | Wearable

type Elliptical = healthStore.ExerciseSequence<healthFields.EllipticalSummary, healthFields.EllipticalDetail>
 
椭圆机锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.EllipticalSummary, healthFields.EllipticalDetail> | 椭圆机锻炼记录数据模型。 |
 
 
  

##### Emotion

**支持设备：** Phone | Tablet | Wearable

type Emotion = healthStore.SamplePoint<healthFields.Emotion>
 
情绪采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.1.0(18)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.Emotion> | 情绪采样数据模型。 |
 
 
  

##### GolfCourseModel

**支持设备：** Phone | Tablet | Wearable

type GolfCourseModel = healthStore.ExerciseSequence<healthFields.GolfCourseModelSummary, healthFields.GolfCourseModelDetail>
 
高尔夫场地模式锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.GolfCourseModelSummary, healthFields.GolfCourseModelDetail> | 高尔夫场地模式锻炼记录数据模型。 |
 
 
  

##### GolfPractice

**支持设备：** Phone | Tablet | Wearable

type GolfPractice = healthStore.ExerciseSequence<healthFields.GolfPracticeSummary, healthFields.GolfPracticeDetail>
 
高尔夫练习场模式锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.GolfPracticeSummary, healthFields.GolfPracticeDetail> | 高尔夫练习场模式锻炼记录数据模型。 |
 
 
  

##### HeartRate

**支持设备：** Phone | Tablet | Wearable

type HeartRate = healthStore.SamplePoint<healthFields.HeartRate>
 
动态心率采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.HeartRate> | 动态心率采样数据模型。 |
 
 
  

##### HeartRateAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type HeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.HeartRateAggregation>
 
动态心率采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.HeartRateAggregation> | 动态心率采样数据聚合统计请求模型。 |
 
 
  

##### HeartRateAggregateResult

**支持设备：** Phone | Tablet | Wearable

type HeartRateAggregateResult = healthStore.AggregateResult<healthFields.HeartRateAggregation>
 
动态心率聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.HeartRateAggregation> | 动态心率聚合结果数据模型。 |
 
 
  

##### HeartRateVariability

**支持设备：** Phone | Tablet | Wearable

type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>
 
心率变异性采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.1.0(18)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.HeartRateVariability> | 心率变异性采样数据模型。 |
 
 
  

##### Height

**支持设备：** Phone | Tablet | Wearable

type Height = healthStore.SamplePoint<healthFields.Height>
 
身高采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.Height> | 身高采样数据模型。 |
 
 
  

##### Hiking

**支持设备：** Phone | Tablet | Wearable

type Hiking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>
 
徒步锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail> | 徒步锻炼记录数据模型。 |
 
 
  

##### IndoorCycling

**支持设备：** Phone | Tablet | Wearable

type IndoorCycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>
 
室内单车锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail> | 室内单车锻炼记录数据模型。 |
 
 
  

##### IndoorRunning

**支持设备：** Phone | Tablet | Wearable

type IndoorRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>
 
室内跑步锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail> | 室内跑步锻炼记录数据模型。 |
 
 
  

##### IndoorWalking

**支持设备：** Phone | Tablet | Wearable

type IndoorWalking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>
 
室内步行锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail> | 室内步行锻炼记录数据模型。 |
 
 
  

##### JumpingRope

**支持设备：** Phone | Tablet | Wearable

type JumpingRope = healthStore.ExerciseSequence<healthFields.JumpingRopeSummary, healthFields.JumpingRopeDetail>
 
跳绳锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.JumpingRopeSummary, healthFields.JumpingRopeDetail> | 跳绳锻炼记录数据模型。 |
 
 
  

##### MenstrualCycle

**支持设备：** Phone | Tablet | Wearable

type MenstrualCycle = healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail>
 
生理周期健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| healthStore.HealthSequence<healthFields.MenstrualCycle, healthFields.MenstrualCycleDetail> | 生理周期健康记录数据模型。 |
 
 
  

##### MountainHike

**支持设备：** Phone | Tablet | Wearable

type MountainHike = healthStore.ExerciseSequence<healthFields.MountainHikeSummary, healthFields.MountainHikeDetail>
 
登山锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.MountainHikeSummary, healthFields.MountainHikeDetail> | 登山锻炼记录数据模型。 |
 
 
  

##### OpenWaterSwim

**支持设备：** Phone | Tablet | Wearable

type OpenWaterSwim = healthStore.ExerciseSequence<healthFields.OpenWaterSwimSummary, healthFields.OpenWaterSwimDetail>
 
开放水域游泳锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.OpenWaterSwimSummary, healthFields.OpenWaterSwimDetail> | 开放水域游泳锻炼记录数据模型。 |
 
 
  

##### PoolSwim

**支持设备：** Phone | Tablet | Wearable

type PoolSwim = healthStore.ExerciseSequence<healthFields.PoolSwimSummary, healthFields.PoolSwimDetail>
 
泳池游泳锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.PoolSwimSummary, healthFields.PoolSwimDetail> | 泳池游泳锻炼记录数据模型。 |
 
 
  

##### RestingHeartRate

**支持设备：** Phone | Tablet | Wearable

type RestingHeartRate = healthStore.SamplePoint<healthFields.RestingHeartRate>
 
静息心率采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.RestingHeartRate> | 静息心率采样数据模型。 |
 
 
  

##### RestingHeartRateAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type RestingHeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.RestingHeartRateAggregation>
 
静息心率采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.RestingHeartRateAggregation> | 静息心率采样数据聚合统计请求模型。 |
 
 
  

##### RestingHeartRateAggregateResult

**支持设备：** Phone | Tablet | Wearable

type RestingHeartRateAggregateResult = healthStore.AggregateResult<healthFields.RestingHeartRateAggregation>
 
静息心率聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.RestingHeartRateAggregation> | 静息心率聚合结果数据模型。 |
 
 
  

##### Rower

**支持设备：** Phone | Tablet | Wearable

type Rower = healthStore.ExerciseSequence<healthFields.RowerSummary, healthFields.RowerDetail>
 
划船机锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.RowerSummary, healthFields.RowerDetail> | 划船机锻炼记录数据模型。 |
 
 
  

##### Rowing

**支持设备：** Phone | Tablet | Wearable

type Rowing = healthStore.ExerciseSequence<healthFields.RowingSummary, healthFields.RowingDetail>
 
赛艇锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.RowingSummary, healthFields.RowingDetail> | 赛艇锻炼记录数据模型。 |
 
 
  

##### Running

**支持设备：** Phone | Tablet | Wearable

type Running = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>
 
户外跑步锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail> | 户外跑步锻炼记录数据模型。 |
 
 
  

##### ScubaDiving

**支持设备：** Phone | Tablet | Wearable

type ScubaDiving = healthStore.ExerciseSequence<healthFields.ScubaDivingSummary, healthFields.ScubaDivingDetail>
 
水肺潜水锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.ScubaDivingSummary, healthFields.ScubaDivingDetail> | 水肺潜水锻炼记录数据模型。 |
 
 
  

##### Skiing

**支持设备：** Phone | Tablet | Wearable

type Skiing = healthStore.ExerciseSequence<healthFields.SkiingSummary, healthFields.SkiingDetail>
 
滑雪锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.SkiingSummary, healthFields.SkiingDetail> | 滑雪锻炼记录数据模型。 |
 
 
  

##### SkinTemperature

**支持设备：** Phone | Tablet | Wearable

type SkinTemperature = healthStore.SamplePoint<healthFields.SkinTemperature>
 
皮肤体温采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.SkinTemperature> | 皮肤体温采样数据模型。 |
 
 
  

##### SkinTemperatureAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type SkinTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.SkinTemperatureAggregation>
 
皮肤体温采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.SkinTemperatureAggregation> | 皮肤体温采样数据聚合统计请求模型。 |
 
 
  

##### SkinTemperatureAggregateResult

**支持设备：** Phone | Tablet | Wearable

type SkinTemperatureAggregateResult = healthStore.AggregateResult<healthFields.SkinTemperatureAggregation>
 
皮肤体温聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.SkinTemperatureAggregation> | 皮肤体温聚合结果数据模型。 |
 
 
  

##### Sled

**支持设备：** Phone | Tablet | Wearable

type Sled = healthStore.ExerciseSequence<healthFields.SledSummary, healthFields.SledDetail>
 
滑雪橇锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.SledSummary, healthFields.SledDetail> | 滑雪橇锻炼记录数据模型。 |
 
 
  

##### SleepNapRecord

**支持设备：** Phone | Tablet | Wearable

type SleepNapRecord = healthStore.HealthSequence<healthFields.SleepNap, healthFields.SleepDetail>
 
零星小睡健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.HealthSequence<healthFields.SleepNap, healthFields.SleepDetail> | 零星小睡健康记录数据模型。 |
 
 
  

##### SleepRecord

**支持设备：** Phone | Tablet | Wearable

type SleepRecord = healthStore.HealthSequence<healthFields.Sleep, healthFields.SleepDetail>
 
夜间睡眠健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.HealthSequence<healthFields.Sleep, healthFields.SleepDetail> | 夜间睡眠健康记录数据模型。 |
 
 
  

##### Snowboarding

**支持设备：** Phone | Tablet | Wearable

type Snowboarding = healthStore.ExerciseSequence<healthFields.SnowboardingSummary, healthFields.SnowboardingDetail>
 
单板滑雪锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.SnowboardingSummary, healthFields.SnowboardingDetail> | 单板滑雪锻炼记录数据模型。 |
 
 
  

##### Spinning

**支持设备：** Phone | Tablet | Wearable

type Spinning = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>
 
动感单车锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail> | 动感单车锻炼记录数据模型。 |
 
 
  

##### Sports

**支持设备：** Phone | Tablet | Wearable

type Sports = healthStore.ExerciseSequence<healthFields.SportsSummary, healthFields.SportsDetail>
 
通用锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.SportsSummary, healthFields.SportsDetail> | 通用锻炼记录数据模型。 |
 
 
  

##### Stress

**支持设备：** Phone | Tablet | Wearable

type Stress = healthStore.SamplePoint<healthFields.Stress>
 
压力采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.Stress> | 压力采样数据模型。 |
 
 
  

##### StressAggregateRequest

**支持设备：** Phone | Tablet | Wearable

type StressAggregateRequest = healthStore.AggregateRequest<healthFields.StressAggregation>
 
压力采样数据聚合统计请求模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateRequest<healthFields.StressAggregation> | 压力采样数据聚合统计请求模型。 |
 
 
  

##### StressAggregateResult

**支持设备：** Phone | Tablet | Wearable

type StressAggregateResult = healthStore.AggregateResult<healthFields.StressAggregation>
 
压力聚合结果数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.AggregateResult<healthFields.StressAggregation> | 压力聚合结果数据模型。 |
 
 
  

##### TrailRunning

**支持设备：** Phone | Tablet | Wearable

type TrailRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>
 
越野跑锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail> | 越野跑锻炼记录数据模型。 |
 
 
  

##### Walking

**支持设备：** Phone | Tablet | Wearable

type Walking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>
 
户外步行锻炼记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail> | 户外步行锻炼数据模型记录。 |
 
 
  

##### Weight

**支持设备：** Phone | Tablet | Wearable

type Weight = healthStore.SamplePoint<healthFields.Weight>
 
体重采样数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthStore.SamplePoint<healthFields.Weight> | 体重采样数据模型。 |
