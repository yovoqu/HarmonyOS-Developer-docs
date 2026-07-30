# AbilityStateData

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystatedata
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AbilityStateData是Ability状态信息的数据结构。使用[on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager#appmanageronapplicationstate14)注册生命周期变化监听后，可以通过[ApplicationStateObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver)的onAbilityStateChanged回调的入参获取该数据结构。

> [!NOTE]
> 本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { appManager } from '@kit.AbilityKit';
```



#### AbilityStateData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 |
| bundleName | string | 否 | 否 | 应用Bundle名称。 |
| abilityName | string | 否 | 否 | Ability名称。 |
| uid | number | 否 | 否 | 所属应用程序的UID。 |
| state | number | 否 | 否 | Ability状态。 - Stage模型：UIAbility的状态参见UIAbility状态；ExtensionAbility的状态参见ExtensionAbility状态；UIExtensionAbility的状态参见UIExtensionAbility状态。 - FA模型：参见Ability状态。 |
| moduleName | string | 否 | 否 | Ability所属的模块名称。 |
| abilityType | number | 否 | 否 | Ability类型：UIAbility或ExtensionAbility等。 |
| isAtomicService | boolean | 否 | 否 | 判断Ability所属应用是否为元服务。 true: 是元服务。 false: 不是元服务。 |
| appCloneIndex | number | 否 | 是 | 应用包的分身索引标识。 |
| callerBundleName23+ | string | 否 | 是 | Ability创建时的拉起方Bundle名称。 |




#### UIAbility状态

| 值 | 说明 |
| --- | --- |
| 0 | UIAbility正在创建中。 |
| 1 | UIAbility已创建完成。 |
| 2 | UIAbility处于前台。 |
| 3 | UIAbility已获得焦点。 |
| 4 | UIAbility处于后台。 |
| 5 | UIAbility已经销毁。 |




#### ExtensionAbility状态

| 值 | 说明 |
| --- | --- |
| 0 | ExtensionAbility正在创建中。 |
| 1 | ExtensionAbility已创建完成。 |
| 2 | ExtensionAbility已与客户端建立连接。 |
| 3 | ExtensionAbility与客户端断开连接。 |
| 4 | 所有客户端断连导致ExtensionAbility正常销毁。 |
| 5 | ExtensionAbility已销毁。涵盖正常销毁（含所有客户端断连触发）及异常销毁（如所在进程被杀死等）。 |




#### UIExtensionAbility状态

| 值 | 说明 |
| --- | --- |
| 0 | UIExtensionAbility正在创建中。 |
| 1 | UIExtensionAbility已创建完成。 |
| 2 | UIExtensionAbility处于前台。 |
| 4 | UIExtensionAbility处于后台。 |
| 5 | UIExtensionAbility已经销毁。 |




#### Ability状态

| 值 | 说明 |
| --- | --- |
| 0 | Ability正在创建中。 |
| 1 | Ability已创建完成。 |
| 2 | Ability处于前台。 |
| 3 | Ability已获得焦点。 |
| 4 | Ability处于后台。 |
| 5 | Ability已经销毁。 |
| 7 | 后台服务已被客户端连接。 |
| 8 | 后台服务与客户端断开连接。 |




#### Ability类型

| 值 | 说明 |
| --- | --- |
| 0 | 未知类型。（系统错误） |
| 1 | UI界面类型的Ability，即UIAbility。 |
| 2 | 后台服务类型的Ability。（FA模型） |
| 3 | 数据类型的Ability。（FA模型） |
| 4 | 卡片类型的Ability。（FA模型） |
| 5 | 扩展类型的Ability。（Stage模型） |
