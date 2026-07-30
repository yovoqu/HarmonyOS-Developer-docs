# @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

开发者通过实现EmbeddedUIExtensionAbility，为本应用提供跨进程界面嵌入能力。例如，开发者可以在[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)的页面中通过[EmbeddedComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component)嵌入本应用的EmbeddedUIExtensionAbility提供的界面。

各类Ability的继承关系详见[继承关系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#ability的继承关系说明)。

> [!NOTE]
> 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { EmbeddedUIExtensionAbility } from '@kit.AbilityKit';
```



#### EmbeddedUIExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

> [!NOTE]
> EmbeddedUIExtensionAbility只能被同应用的UIAbility拉起。从API版本26.0.0开始，满足以下条件时则允许EmbeddedComponent跨应用拉起EmbeddedUIExtensionAbility： EmbeddedComponent所属应用已申请ohos.permission.SUPPORT_CROSS_APP_EMBED_FOR_OA权限（该权限仅企业普通应用可申请）。 该应用的 appIdentifier 在EmbeddedUIExtensionAbility支持的应用清单（即 extensionAbilities标签 的appIdentifierAllowList属性）中。


**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
