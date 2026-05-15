# AgentHostProxy

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-agenthostproxy
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

AgentHostProxy用于从[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)服务端向客户端发送数据或安全认证请求。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { common } from '@kit.AbilityKit';
```


## AgentHostProxy
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### sendData
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

sendData(data: string): void

从[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)服务端给客户端发送数据。

**元服务API**：从 API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 待发送到[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)客户端的数据。 |


**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[元能力子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability)。


| 错误码ID | 错误信息 |
| --- | --- |
| 35600002 | Failed to send the IPC message. |


**示例：**


```ts
import { common, AgentExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[AgentExtensionAbility] ';

export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  // 数据发送处理
  onData(proxy: common.AgentHostProxy, data: string) {
    console.info(TAG + `onData ${data}`);
    try {
      // 发送数据到AgentExtensionAbility的客户端
      proxy.sendData('Hello Client');
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(
        `${TAG} sendData failed, err code: ${code}, err msg: ${msg}.`,
      );
    }
  }
}
```


### authorize
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

authorize(handshakeData: string): void

从[AgentExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-agent-agentextensionability)服务端给客户端发送安全认证请求。

**元服务API**：从 API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AgentRuntime.Core

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handshakeData | string | 是 | 待发送到客户端的安全认证数据。 |


**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[元能力子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability)。


| 错误码ID | 错误信息 |
| --- | --- |
| 35600002 | Failed to send the IPC message. |


**示例：**


```ts
import { common, AgentExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[AgentExtensionAbility] ';

export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  // 数据发送处理
  onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
    console.info(TAG + `onAuth ${handshakeData}`);
    try {
      // 发送认证数据到AgentExtensionAbility的客户端
      proxy.authorize('handshake_token');
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(
        `${TAG} authorize failed, err code: ${code}, err msg: ${msg}.`,
      );
    }
  }
}
```
