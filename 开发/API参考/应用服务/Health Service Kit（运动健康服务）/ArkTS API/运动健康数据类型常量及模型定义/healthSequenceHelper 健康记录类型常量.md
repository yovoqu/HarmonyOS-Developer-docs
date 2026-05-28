# healthSequenceHelper (健康记录类型常量)

更新时间：2026-04-30 09:02:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper
**支持设备：** Phone | Tablet | Wearable

本模块提供健康记录数据类型常量及数据模型。
 
**起始版本：** 5.0.0(12)
  

#### 导入模块

**支持设备：** Phone | Tablet | Wearable

```text
import { healthStore } from '@kit.HealthServiceKit';
```
 
> [!NOTE]
> 此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

 
  

#### sleepRecord

**支持设备：** Phone | Tablet | Wearable

夜间睡眠数据类型常量及数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
 
  

#### 常量

**支持设备：** Phone | Tablet | Wearable

**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 夜间睡眠数据类型。 |
 
 
  

#### Model

**支持设备：** Phone | Tablet | Wearable

type Model = healthModels.SleepRecord
 
夜间睡眠健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthModels.SleepRecord | 夜间睡眠健康记录数据模型。 |
 
 
  

#### Fields

**支持设备：** Phone | Tablet | Wearable

type Fields = healthFields.Sleep
 
夜间睡眠健康记录数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthFields.Sleep | 夜间睡眠健康记录数据字段列表。 |
 
 
  

#### DetailFields

**支持设备：** Phone | Tablet | Wearable

type DetailFields = healthFields.SleepDetail
 
睡眠详情数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthFields.SleepDetail | 睡眠详情数据字段列表。 |
 
 
  

#### sleepNapRecord

**支持设备：** Phone | Tablet | Wearable

零星小睡数据类型常量及数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
 
  

#### 常量

**支持设备：** Phone | Tablet | Wearable

**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 零星小睡数据类型。 |
 
 
  

#### Model

**支持设备：** Phone | Tablet | Wearable

type Model = healthModels.SleepNapRecord
 
零星小睡健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthModels.SleepNapRecord | 零星小睡健康记录数据模型。 |
 
 
  

#### Fields

**支持设备：** Phone | Tablet | Wearable

type Fields = healthFields.SleepNap
 
零星小睡健康记录数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthFields.SleepNap | 零星小睡健康记录数据字段列表。 |
 
 
  

#### DetailFields

**支持设备：** Phone | Tablet | Wearable

type DetailFields = healthFields.SleepDetail
 
睡眠详情数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 5.0.0(12)
  
| 类型 | 说明 |
| --- | --- |
| healthFields.SleepDetail | 睡眠详情数据字段列表。 |
 
 
  

#### menstrualCycle

**支持设备：** Phone | Tablet | Wearable

生理周期数据类型常量及数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
  

#### 常量

**支持设备：** Phone | Tablet | Wearable

**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
  
| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 生理周期数据类型。 |
 
 
  

#### Model

**支持设备：** Phone | Tablet | Wearable

type Model = healthModels.MenstrualCycle
 
生理周期健康记录数据模型。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| healthModels.MenstrualCycle | 生理周期健康记录数据模型。 |
 
 
  

#### Fields

**支持设备：** Phone | Tablet | Wearable

type Fields = healthFields.MenstrualCycle
 
生理周期健康记录数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| healthFields.MenstrualCycle | 生理周期健康记录数据字段列表。 |
 
 
  

#### DetailFields

**支持设备：** Phone | Tablet | Wearable

type DetailFields = healthFields.MenstrualCycleDetail
 
生理周期详情数据字段列表。
 
**系统能力：** SystemCapability.Health.HealthStore
 
**起始版本：** 6.1.1(24)
 
**模型约束：** 此接口仅可在Stage模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| healthFields.MenstrualCycleDetail | 生理周期详情数据字段列表。 |
