# @ohos.FusionConnectivity.PartnerAgentExtensionAbility (支持设备状态通知的ExtensionAbility组件)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fusionconnectivity-partneragentextensionability
**支持设备：** Phone | PC/2in1 | Tablet

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。应用模块级配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file) 中的[extensionabilities](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#extensionabilities标签)的type属性应该配置为partnerAgent。

> [!NOTE]
> 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 约束限制

**支持设备：** Phone | PC/2in1 | Tablet

为保障系统安全性和稳定性，防止PartnerAgentExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](#附录)。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { PartnerAgentExtensionAbility, partnerAgent } from '@kit.ConnectivityKit';
```



#### PartnerDeviceAddress

**支持设备：** Phone | PC/2in1 | Tablet

type PartnerDeviceAddress = partnerAgent.PartnerDeviceAddress

描述设备地址信息。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| partnerAgent.PartnerDeviceAddress | 信息互通设备的地址信息。 |




#### PartnerAgentExtensionAbilityDestroyReason

**支持设备：** Phone | PC/2in1 | Tablet

type PartnerAgentExtensionAbilityDestroyReason = partnerAgent.PartnerAgentExtensionAbilityDestroyReason

描述PartnerAgentExtensionAbility被销毁的原因。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| partnerAgent.PartnerAgentExtensionAbilityDestroyReason | PartnerAgentExtensionAbility被销毁的原因。 |




#### PartnerAgentExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet

PartnerAgentExtensionAbility是外设互通扩展能力的基础类，提供设备发现与设备下线的通知功能，需要应用继承实现。本能力继承自[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet

**系统能力**： SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | PartnerAgentExtensionContext | 否 | 否 | PartnerAgentExtensionAbility的上下文。 |




#### onDestroyWithReason

**支持设备：** Phone | PC/2in1 | Tablet

onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void

外设互通扩展能力被销毁时触发的方法回调。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | PartnerAgentExtensionAbilityDestroyReason | 是 | 通知销毁该应用的原因。 |


**示例：**

```text
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
    console.info(`onDestroyWithReason is: ${reason}`);
  }
}
```



#### onDeviceDiscovered

**支持设备：** Phone | PC/2in1 | Tablet

onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void

当已注册的设备被发现时，系统会调用此回调方法。

**系统能力**：SystemCapability.Communication.FusionConnectivity.Core

**模型约束**： 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | PartnerDeviceAddress | 是 | 应用注册的设备地址信息。 应用需在PartnerDeviceAddress类型中设置bluetoothAddress选项。 |


**示例：**

```text
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
    console.info(`onDeviceDiscovered success: ${deviceAddress.bluetoothAddress}`);
  }
}
```



#### 附录

**支持设备：** Phone | PC/2in1 | Tablet

PartnerAgentExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | @ohos.backgroundTaskManager (后台任务管理) |
| Ability Kit | @ohos.resourceschedule.backgroundTaskManager (后台任务管理) |
| Camera Kit | @ohos.multimedia.cameraPicker (相机选择器) |
| Connectivity Kit | @ohos.connectedTag (有源标签) |
| Connectivity Kit | @ohos.nfc.cardEmulation (标准NFC-cardEmulation) |
| Connectivity Kit | @ohos.nfc.controller (标准NFC) |
| Connectivity Kit | @ohos.nfc.tag (标准NFC-Tag) |
| Connectivity Kit | tagSession (标准NFC-Tag TagSession) |
| Connectivity Kit | @ohos.wifiext (WLAN扩展接口) |
| Connectivity Kit | @ohos.wifiManager (WLAN) |
| Connectivity Kit | @ohos.wifiManagerExt (WLAN扩展接口) |
| Location Kit | @ohos.geolocation (位置服务) |
| Location Kit | @ohos.geoLocationManager (位置服务) |
| Media Library Kit | @ohos.multimedia.movingphotoview (动态照片) |
| Telephony Kit | @ohos.telephony.sim (SIM卡管理) |
| Telephony Kit | @ohos.telephony.sms (短信服务) |
