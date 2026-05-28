# @ohos.app.ability.Ability (Ability基类)

更新时间：2026-03-19 08:47:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Ability类是应用生命周期调度的基本单元，是[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)和[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)的基类，提供系统配置更新回调和系统内存级别变化回调能力。该基类不支持开发者直接继承，开发者应根据具体的业务场景选择使用[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)，相关指南参见[Ability Kit简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitykit-overview)。

> [!NOTE]
> 本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { Ability } from '@kit.AbilityKit';
```



#### Ability的继承关系说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Ability基类及其子类的继承关系如下图所示。

> [!NOTE]
> 部分ExtensionAbility组件（例如 FormExtensionAbility 、 InputMethodExtensionAbility 等）与下图中的ExtensionAbility基类不存在继承关系，均未在图中列出。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/e2h3pLh5QW2YGgbiD6b61w/zh-cn_image_0000002581275600.png?HW-CC-KV=V1&HW-CC-Date=20260528T025634Z&HW-CC-Expire=86400&HW-CC-Sign=334218591A4B600350D0D67E63DC078AC861E7EDC446894A3BF75FBF4007A44E)




#### Ability.onConfigurationUpdate

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onConfigurationUpdate(newConfig: Configuration): void

当系统环境变量发生变化时，系统会触发该回调。开发者可以重写该回调实现对系统环境变量变化时的响应，例如当系统语言类型发生变化时，应用可以在回调中进行定制化的处理等。

> [!NOTE]
> 该回调方法在实际触发时存在一定限制。例如如果开发者通过 setLanguage 接口设置应用的语言，即便系统语言发生变化，系统也不再触发onConfigurationUpdate回调。详见 使用场景 。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newConfig | Configuration | 是 | 表示更新后的配置信息。 |


**示例：**

```json
// Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
import { UIAbility, Configuration } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onConfigurationUpdate(config: Configuration) {
    console.info(`onConfigurationUpdate, config: ${JSON.stringify(config)}`);
  }
}
```



#### Ability.onMemoryLevel

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

当整机可用内存变化到指定程度时，系统会触发该回调。开发者可以重写该回调实现对内存级别变化的响应，例如释放缓存数据等。

> [!NOTE]
> onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。


**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | AbilityConstant.MemoryLevel | 是 | 整机可用内存级别，对应的触发场景详见AbilityConstant.MemoryLevel。 |


**示例：**

```json
// Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(`onMemoryLevel, level: ${JSON.stringify(level)}`);
  }
}
```
