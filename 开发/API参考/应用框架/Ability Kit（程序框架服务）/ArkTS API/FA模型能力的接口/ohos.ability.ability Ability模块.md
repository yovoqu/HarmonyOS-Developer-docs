# @ohos.ability.ability (Ability模块)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Ability模块将二级模块API组织在一起方便开发者进行导出。
 
> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { ability } from '@kit.AbilityKit';
```
 
  

#### DataAbilityHelper

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type DataAbilityHelper = _DataAbilityHelper
 
DataAbilityHelper二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _DataAbilityHelper | DataAbilityHelper二级模块。 |
 
 
  

#### PacMap

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type PacMap = _PacMap
 
PacMap二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
  
| 类型 | 说明 |
| --- | --- |
| _PacMap | DataAbilityHelper二级模块。 |
 
 
  

#### DataAbilityOperation

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type DataAbilityOperation = _DataAbilityOperation
 
DataAbilityOperation二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _DataAbilityOperation | DataAbilityOperation二级模块。 |
 
 
  

#### DataAbilityResult

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type DataAbilityResult = _DataAbilityResult
 
DataAbilityResult二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _DataAbilityResult | DataAbilityResult二级模块。 |
 
 
  

#### AbilityResult

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AbilityResult = _AbilityResult
 
AbilityResult二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityBase
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _AbilityResult | AbilityResult二级模块。 |
 
 
  

#### ConnectOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type ConnectOptions = _ConnectOptions
 
ConnectOptions二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _ConnectOptions | ConnectOptions二级模块。 |
 
 
  

#### StartAbilityParameter

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type StartAbilityParameter = _StartAbilityParameter
 
StartAbilityParameter二级模块。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel
 
**模型约束**：此接口仅可在FA模型下使用。
  
| 类型 | 说明 |
| --- | --- |
| _StartAbilityParameter | StartAbilityParameter二级模块。 |
 
 
**示例：**
 
```text
import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;
let startAbilityParameter: ability.StartAbilityParameter;
```
