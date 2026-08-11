# AutoFillRequest

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofillrequest
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供自动填充与自动保存场景下的页面请求数据，以及自动填充失败时的返回结果。
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { autoFillManager } from '@kit.AbilityKit';
```
 
  

#### FillRequest

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自动填充请求信息。
 
**起始版本：** 26.0.0
 
**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
 
**模型约束**：此接口仅可在Stage模型下使用。
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | AutoFillType | 否 | 否 | 自动填充类型。 |
| viewData | ViewData | 否 | 否 | 页面数据。 |
| triggerType | AutoFillTriggerType | 否 | 是 | 自动填充服务的拉起类型。 |
 
 
  

#### SaveRequest

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自动保存请求信息。
 
**起始版本：** 26.0.0
 
**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
 
**模型约束**：此接口仅可在Stage模型下使用。
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| viewData | ViewData | 否 | 否 | 页面数据。 |
 
 
  

#### FillFailureResult

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自动填充失败结果。
 
**起始版本：** 26.0.0
 
**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
 
**模型约束**：此接口仅可在Stage模型下使用。
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errCode | number | 否 | 否 | 错误码。 |
