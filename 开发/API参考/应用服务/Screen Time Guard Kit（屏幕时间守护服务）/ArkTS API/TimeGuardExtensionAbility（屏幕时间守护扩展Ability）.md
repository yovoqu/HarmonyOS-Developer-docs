# TimeGuardExtensionAbility（屏幕时间守护扩展Ability）

更新时间：2026-06-09 02:58:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensionability
**支持设备：** Phone | Tablet

TimeGuardExtensionAbility是屏幕时间守护扩展Ability，提供extension回调，支持开发者在策略管控生效和策略停止时执行特定逻辑，以及支持开发者用户授予应用权限和取消应用授权时执行特定逻辑。TimeGuardExtensionAbility继承自[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
  

#### 导入模块

**支持设备：** Phone | Tablet

```text
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
```
 
  

#### 属性

**支持设备：** Phone | Tablet

**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | TimeGuardExtensionContext | 否 | 否 | TimeGuardExtensionContext上下文环境，继承自ExtensionContext。 |
 
 
  

#### onStart

**支持设备：** Phone | Tablet

onStart(strategyName: string): Promise&lt;void&gt;
 
当管控应用启动的策略管控生效时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 生效的时间管控策略名称。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**示例：**
 
```text
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
 
let index = 0; // 用于自增操作
 
function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}
 
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStart(strategyName: string): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onStart:', strategyName, index);
  }
}
```
 
  

#### onStop

**支持设备：** Phone | Tablet

onStop(strategyName: string): Promise&lt;void&gt;
 
当管控应用启动的策略管控结束时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 结束的时间管控策略名称。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**示例：**
 
```text
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
 
let index = 0; // 用于自增操作
 
function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}
 
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStop(strategyName: string): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onStop:', strategyName, index);
  }
}
```
 
  

#### onUserAuthSwitchOn

**支持设备：** Phone | Tablet

onUserAuthSwitchOn(): Promise&lt;void&gt;
 
当用户在“健康使用设备”中授予管控应用权限时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**示例：**
 
```text
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
 
let index = 0; // 用于自增操作
 
function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}
 
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOn(): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onUserAuthSwitchOn:', index);
  }
}
```
 
  

#### onUserAuthSwitchOff

**支持设备：** Phone | Tablet

onUserAuthSwitchOff(): Promise&lt;void&gt;
 
当用户在“健康使用设备”中授予管控应用权限时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
 
 
**示例：**
 
```text
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
 
let index = 0; // 用于自增操作
 
function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}
 
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOff(): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onUserAuthSwitchOff:', index);
  }
}
```
