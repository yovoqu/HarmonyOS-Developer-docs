# @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitydelegatorregistry
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AbilityDelegatorRegistry是自动化测试框架的注册模块，用于获取[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)和[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象。通过该模块，开发者可以利用[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)对象添加[AbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor#abilitymonitor-1)对象，实现对指定Ability生命周期状态变化的监视；同时，借助[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象便捷地读取当前运行的测试参数。

> [!NOTE]
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在 单元测试框架 中使用。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { abilityDelegatorRegistry } from '@kit.TestKit';
```



#### AbilityLifecycleState

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Ability生命周期状态，可配合[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)的[getAbilityState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#getabilitystate9)方法返回对应Ability的生命周期状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示Ability处于无效状态。 |
| CREATE | 1 | 表示Ability处于已创建状态。 |
| FOREGROUND | 2 | 表示Ability处于前台状态。 |
| BACKGROUND | 3 | 表示Ability处于后台状态。 |
| DESTROY | 4 | 表示Ability处于已销毁状态。 |




#### abilityDelegatorRegistry.getAbilityDelegator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getAbilityDelegator(): AbilityDelegator

获取应用程序的[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)对象，该对象可用于调度测试框架，执行相关测试功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AbilityDelegator | 用来调度测试框架相关功能。 |


**示例：**

```json
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

// 获取应用程序的AbilityDelegator对象
let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 构造Want参数，指定目标Ability
let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};

// 启动指定Ability
abilityDelegator.startAbility(want, (err) => {
  if (err) {
    console.error(`Failed start ability, error: ${JSON.stringify(err)}`);
  } else {
    console.info('Success start ability.');
  }
});
```



#### abilityDelegatorRegistry.getArguments

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

getArguments(): AbilityDelegatorArgs

获取单元测试参数[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AbilityDelegatorArgs | AbilityDelegatorArgs对象。可以用来获取测试参数。 |


**示例：**

```json
import { abilityDelegatorRegistry } from '@kit.TestKit';

// 获取单元测试参数AbilityDelegatorArgs对象
let args = abilityDelegatorRegistry.getArguments();
// 打印测试参数信息
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```



#### AbilityDelegator

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AbilityDelegator = _AbilityDelegator

提供通过[AbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor)实例来监听和管理[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)生命周期变化的能力。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _AbilityDelegator | AbilityDelegator模块。 |




#### AbilityDelegatorArgs

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AbilityDelegatorArgs = _AbilityDelegatorArgs

提供在应用程序执行测试用例期间，获取测试用例参数AbilityDelegatorArgs对象的能力。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _AbilityDelegatorArgs | AbilityDelegatorArgs模块。 |




#### AbilityMonitor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AbilityMonitor = _AbilityMonitor

作为[addAbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#addabilitymonitor9)的入参，用于监听指定UIAbility的生命周期变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _AbilityMonitor | AbilityMonitor模块。 |




#### ShellCmdResult

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type ShellCmdResult = _ShellCmdResult

提供获取Shell命令执行结果的能力，可用于在自动化测试中执行Shell命令并获取命令的返回结果，包括命令的返回码和标准输出内容等信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _ShellCmdResult | ShellCmdResult模块。 |




#### AbilityStageMonitor14+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type AbilityStageMonitor = _AbilityStageMonitor

提供监听指定[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)对象的能力。开发者可以将AbilityStageMonitor作为[abilityDelegator.waitAbilityStageMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#waitabilitystagemonitor9)的入参来注册监听。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| _AbilityStageMonitor | AbilityStageMonitor模块。 |
