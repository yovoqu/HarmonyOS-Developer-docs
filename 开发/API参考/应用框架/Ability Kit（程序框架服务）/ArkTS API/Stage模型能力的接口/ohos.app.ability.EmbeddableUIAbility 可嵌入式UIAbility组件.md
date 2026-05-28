# @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

EmbeddableUIAbility组件是为元服务提供可嵌入式的UIAbility组件，继承自[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)。
 
开发者通过实现EmbeddableUIAbility，为其他应用提供跳出式启动和嵌入式启动元服务方式。
 
各类Ability的继承关系详见[继承关系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#ability的继承关系说明)。
 
> [!NOTE]
> 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。

  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { EmbeddableUIAbility } from '@kit.AbilityKit';
```
 
  

##### EmbeddableUIAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
 
**元服务API**：从API version 12 开始，该接口支持在元服务中使用。
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | EmbeddableUIAbilityContext | 否 | 否 | EmbeddableUIAbility组件的上下文。 |
