# @ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AppServiceExtensionAbility模块提供后台服务相关扩展能力，包括后台服务的创建、销毁、连接、断开等生命周期回调。

> [!NOTE]
> 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

 - 当前仅支持2in1设备。
 - 应用集成AppServiceExtensionAbility的组件需要申请ACL权限（ohos.permission.SUPPORT_APP_SERVICE_EXTENSION）。该ACL权限当前只对企业普通应用开放申请，申请方式参考[权限申请指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。




#### 生命周期

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AppServiceExtensionAbility提供了[onCreate()](#oncreate)、[onRequest()](#onrequest)、[onConnect()](#onconnect)、[onDisconnect()](#ondisconnect)和[onDestroy()](#ondestroy)生命周期回调，开发者可根据需要重写对应的回调方法。下图展示了AppServiceExtensionAbility的生命周期。


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/CJC-3m7QRmmDqt7stj20-w/zh-cn_image_0000002611755457.png?HW-CC-KV=V1&HW-CC-Date=20260528T025638Z&HW-CC-Expire=86400&HW-CC-Sign=873C5F1FD4008EE6E0F39697154A86332875670A6CFB8BF6C140DFD38006FE00)


 - **onCreate**

  在AppServiceExtensionAbility实例创建时，系统会触发该回调。
 - **onDestroy**

  在AppServiceExtensionAbility实例销毁时，系统会触发该回调。
 - **onRequest**

  调用方使用[startAppServiceExtensionAbility()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startappserviceextensionability20)拉起AppServiceExtensionAbility实例时，系统会触发该回调。
 - **onConnect**

  调用方使用[connectAppServiceExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectappserviceextensionability20)连接AppServiceExtensionAbility实例时，系统会触发该回调。
 - **onDisconnect**

  当所有连接方断开与AppServiceExtensionAbility实例的连接时，系统会触发该回调。




#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { AppServiceExtensionAbility } from '@kit.AbilityKit';
```



#### AppServiceExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AppServiceExtensionAbility模块提供后台服务相关扩展能力，包括后台服务的创建、销毁、连接、断开等生命周期回调。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | AppServiceExtensionContext | 否 | 否 | AppServiceExtensionAbility的上下文环境，继承自ExtensionContext。 |




#### onCreate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCreate(want: Want): void

在AppServiceExtensionAbility实例创建时，系统会触发该回调。应用可以在该接口中执行自己的业务逻辑初始化操作，例如注册公共事件监听等。

> [!NOTE]
> 如果AppServiceExtensionAbility实例已创建，再次启动或连接该实例时不会触发onCreate()回调。


**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |


**示例：**

```text
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    hilog.info(0x0000, TAG, `onCreate, want: ${want.abilityName}`);
  }
}
```



#### onDestroy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDestroy(): void

在AppServiceExtensionAbility实例销毁时，系统会触发该回调。应用可以在该接口中执行资源清理等操作，如注销监听等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```text
import { AppServiceExtensionAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onDestroy() {
    hilog.info(0x0000, TAG, `onDestroy`);
  }
}
```



#### onRequest

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onRequest(want: Want, startId: number): void

调用方每次使用[startAppServiceExtensionAbility()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startappserviceextensionability20)拉起AppServiceExtensionAbility实例时，系统都会触发该回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |
| startId | number | 是 | 返回拉起次数。首次拉起初始值返回1，多次拉起时自动递增。 |


**示例：**

```text
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onRequest(want: Want, startId: number) {
    hilog.info(0x0000, TAG, `onRequest, want: ${want.abilityName}, startId: ${startId}`);
  }
}
```



#### onConnect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onConnect(want: Want): rpc.RemoteObject

调用方使用[connectAppServiceExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectappserviceextensionability20)连接AppServiceExtensionAbility实例时，系统会触发该回调。

应用需要在该接口中返回一个RemoteObject对象，用于客户端和服务端进行通信。当AppServiceExtensionAbility实例处于连接状态时，如果调用方发起新的连接，系统会返回缓存的RemoteObject对象，而不会重复回调onConnect()接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |


**返回值：**

| 类型 | 说明 |
| --- | --- |
| rpc.RemoteObject | 一个RemoteObject对象，用于客户端和服务端进行通信。 |


**示例：**

```text
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

class StubTest extends rpc.RemoteObject {
  constructor(des: string) {
    super(des);
  }

  onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
  }
}

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onConnect(want: Want) {
    hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```



#### onDisconnect

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDisconnect(want: Want): void

当所有连接方断开与AppServiceExtensionAbility实例的连接时，系统会触发该回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | AppServiceExtensionAbility实例最近一次被拉起或者连接时，调用方传递的Want类型信息，包括Ability名称、Bundle名称等。 |


**示例：**

```text
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onDisconnect(want: Want) {
    hilog.info(0x0000, TAG, `onDisconnect, want: ${want.abilityName}`);
  }
}
```
