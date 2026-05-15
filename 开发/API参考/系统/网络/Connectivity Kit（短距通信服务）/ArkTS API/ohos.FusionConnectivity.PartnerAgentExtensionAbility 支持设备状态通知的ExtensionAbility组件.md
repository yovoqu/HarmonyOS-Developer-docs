# @ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-fusionconnectivity-partneragentextensionability
**支持设备：** Phone / PC/2in1 / Tablet

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。应用模块级配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file) 中的[extensionabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#extensionabilities标签)的type属性应该配置为partnerAgent。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet


```ts
import {
  PartnerAgentExtensionAbility,
  partnerAgent,
} from '@kit.ConnectivityKit';
```


## PartnerDeviceAddress
**支持设备：** Phone / PC/2in1 / Tablet

type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress

描述设备地址信息。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。


| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerDeviceAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent#partneragentpartnerdeviceaddress) | 信息互通设备的地址信息。 |


## PartnerAgentExtensionAbilityDestroyReason
**支持设备：** Phone / PC/2in1 / Tablet

type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason

描述PartnerAgentExtensionAbility被销毁的原因。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。


| 类型 | 说明 |
| --- | --- |
| [partnerAgent.PartnerAgentExtensionAbilityDestroyReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent#partneragentpartneragentextensionabilitydestroyreason) | PartnerAgentExtensionAbility被销毁的原因。 |


## PartnerAgentExtensionAbility
**支持设备：** Phone / PC/2in1 / Tablet

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。本能力继承自[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)。


### 属性
**支持设备：** Phone / PC/2in1 / Tablet

**系统能力**： SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [PartnerAgentExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-fusionconnectivity-partneragentextensioncontext) | 否 | 否 | PartnerAgentExtensionAbility的上下文。 |


### onDestroyWithReason
**支持设备：** Phone / PC/2in1 / Tablet

onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void

外设互通扩展能力被销毁时触发的方法回调。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [PartnerAgentExtensionAbilityDestroyReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent#partneragentpartneragentextensionabilitydestroyreason) | 是 | 通知销毁该应用的原因。 |


**示例：**


```ts
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDestroyWithReason(
    reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason,
  ): void {
    console.info(`onDestroyWithReason is: ${reason}`);
  }
}
```


### onDeviceDiscovered
**支持设备：** Phone / PC/2in1 / Tablet

onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void

当已注册的设备被发现时，系统会调用此回调方法。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragent#partneragentpartnerdeviceaddress) | 是 | 应用注册的设备地址信息。          应用需在PartnerDeviceAddress类型中设置bluetoothAddress选项。 |


**示例：**


```ts
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
    console.info(
      `onDeviceDiscovered success: ${deviceAddress.bluetoothAddress}`,
    );
  }
}
```
