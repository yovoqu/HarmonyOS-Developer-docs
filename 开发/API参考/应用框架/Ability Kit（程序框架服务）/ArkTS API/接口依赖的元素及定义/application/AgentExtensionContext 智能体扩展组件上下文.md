# AgentExtensionContext (智能体扩展组件上下文)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentextensioncontext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

AgentExtensionContext模块是[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

AgentExtensionContext为开发者提供访问当前[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)智能体所配置的[AgentCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentcard)信息的能力。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { common } from '@kit.AbilityKit';
```


## AgentExtensionContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| agentCard | [AgentCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentcard) | 否 | 否 | 当前[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)所配置的[AgentCard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agentcard#agentcard-1)信息。 |


**示例：**


```ts
import { AgentExtensionAbility, common } from '@kit.AbilityKit';

export default class AgentExtension extends AgentExtensionAbility {
  onCreate(): void {
    let tmpContext: common.AgentExtensionContext = this.context; // 获取AgentExtensionContext
    console.info(
      `agentCard info data: ${JSON.stringify(tmpContext.agentCard)}.`,
    );
  }
}
```
