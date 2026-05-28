# @ohos.app.agent.AgentExtensionAbility (智能体扩展组件)

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AgentExtensionAbility继承自[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)，提供智能体扩展能力，包括智能体服务的创建、销毁、连接、断开的生命周期回调接口，以及接收客户端所发送数据和安全认证的回调接口。

本文将AgentExtensionAbility组件提供方称为服务端，将AgentExtensionAbility组件使用方称为客户端。

> [!NOTE]
> 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。 本模块接口不支持在 har 包中使用。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { AgentExtensionAbility } from '@kit.AbilityKit';
```



#### 生命周期

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**图1** AgentExtensionAbility生命周期


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/yf5tXnADTRqhIJWQa6xQAg/zh-cn_image_0000002581275602.png?HW-CC-KV=V1&HW-CC-Date=20260528T025639Z&HW-CC-Expire=86400&HW-CC-Sign=0FCBF8503A58BB6CB1635AB872EC8E1B6416ABF67F4963CB152DD72D178DAB11)


 - **onCreate**

  当AgentExtensionAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。
 - **onConnect**

  当客户端连接AgentExtensionAbility成功后，系统会触发该回调。
 - **onDisconnect**

  当客户端与AgentExtensionAbility断开连接时，系统会触发该回调。
 - **onDestroy**

  当AgentExtensionAbility被销毁时，系统会触发该回调。




#### AgentExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**元服务API：** 从API version 24开始，该属性支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | AgentExtensionContext | 否 | 否 | AgentExtensionAbility的上下文环境，继承自ExtensionContext。 |




#### onCreate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCreate(want: Want): void

当AgentExtensionAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前AgentExtensionAbility相关的Want类型信息，包括Ability名称、Bundle名称等。 |


**示例：**

```text
import { AgentExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AgentExt extends AgentExtensionAbility {
  // 创建AgentExtensionAbility
  onCreate(want: Want) {
    hilog.info(0x0000, TAG, `onCreate, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
  }
}
```



#### onConnect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onConnect(want: Want, proxy: AgentHostProxy): void

当客户端连接AgentExtensionAbility成功后，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前AgentExtensionAbility相关的Want类型信息，包括Ability名称、Bundle名称等。 |
| proxy | AgentHostProxy | 是 | AgentHostProxy对象，用于与客户端进行通信。 |


**示例：**

```text
import { AgentExtensionAbility, Want, common} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AgentExtensionAbility]';

export default class AgentExt extends AgentExtensionAbility {
  onConnect(want: Want, proxy: common.AgentHostProxy){
    hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
  }
}
```



#### onDisconnect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDisconnect(want: Want, proxy: AgentHostProxy): void

当客户端与AgentExtensionAbility断开连接时，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 当前AgentExtensionAbility相关的Want类型信息，包括Ability名称、Bundle名称等。 |
| proxy | AgentHostProxy | 是 | AgentHostProxy对象，用于与客户端进行通信。 |


**示例：**

```text
import { AgentExtensionAbility, Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AgentExtensionAbility]';

export default class AgentExt extends AgentExtensionAbility {
  onDisconnect(want: Want, proxy: common.AgentHostProxy) {
    hilog.info(0x0000, TAG, `onDisconnect, want: ${want.abilityName}, bundlename: ${want.bundleName}`);
  }
}
```



#### onData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onData(proxy: AgentHostProxy, data: string): void

当AgentExtensionAbility接收到客户端发送的数据时，系统会触发该回调。服务端可以在此回调中通过[AgentHostProxy.senddata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agenthostproxy#senddata)向客户端发送数据。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | AgentHostProxy | 是 | AgentHostProxy对象，用于与客户端进行通信。 |
| data | string | 是 | 表示接收到的数据。 |


**示例：**

```text
import { AgentExtensionAbility, common} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AgentExtensionAbility]';

export default class AgentExt extends AgentExtensionAbility {
  onData(proxy : common.AgentHostProxy, data : string ){
    hilog.info(0x0000, TAG, `onData, data: ${data}`);
  }
}
```



#### onAuth

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onAuth(proxy: AgentHostProxy, handshakeData: string): void

当AgentExtensionAbility接收到客户端发送的安全认证请求时，系统会触发该回调。服务端可以在此回调中处理接收到的安全认证请求，并通过[AgentHostProxy.authorize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agenthostproxy#authorize)向客户端发送安全认证请求。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | AgentHostProxy | 是 | AgentHostProxy对象，用于向客户端发送安全认证请求。 |
| handshakeData | string | 是 | 表示接收到的安全认证数据。 |


**示例：**

```text
import { AgentExtensionAbility, common} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AgentExtensionAbility]';

export default class AgentExt extends AgentExtensionAbility {
  onAuth(proxy : common.AgentHostProxy, handshakeData : string ){
    hilog.info(0x0000, TAG, `onAuth, handshakeData: ${handshakeData}`);
  }
}
```



#### onDestroy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDestroy(): void

当AgentExtensionAbility被销毁时，系统会触发该回调。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**示例：**

```text
import { AgentExtensionAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AgentExtensionAbility]';

export default class AgentExt extends AgentExtensionAbility {
  onDestroy() {
    hilog.info(0x0000, TAG, `onDestroy`);
  }
}
```
