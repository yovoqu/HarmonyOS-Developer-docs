# @ohos.app.agent.agentConstant (Agent常量)

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentconstant
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

agentConstant模块提供Agent相关的常量。
 
**起始版本：** 26.0.0
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { agentConstant } from '@kit.AbilityKit';
```
 
  

#### agentConstant.AgentCardType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Agent卡片的类型。
 
**起始版本：** 26.0.0
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API**：从API版本26.0.0开始，该枚举支持在元服务中使用。
 
**系统能力**：SystemCapability.Ability.AgentRuntime.Core
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP | 0 | 应用型Agent卡片，适用于传统安装应用，Agent能力随应用一起安装和卸载，需要用户主动安装应用后才能使用。 |
| ATOMIC_SERVICE | 1 | 元服务型Agent卡片，适用于免安装的元服务，Agent能力可以即用即离，无需预先安装，支持快速体验和分享。 |
