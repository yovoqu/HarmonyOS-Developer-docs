# @ohos.app.ability.hyperSnapManager (应用快照管理)

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-hypersnapmanager
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

应用启动过程中的初始化流程可以提前制作成应用快照，从快照启动的应用不再重复执行初始化流程，从而起到加速启动的作用。hyperSnapManager模块提供应用快照管理的能力，包括启用或禁用应用的快照功能、请求重建应用快照等。


> [!NOTE]
> 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。


## 实现原理
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

应用快照只会制作一次，从应用快照启动可以省去应用初始化和AbilityStage创建所需的时间。

**图1** 快照启动流程

![](assets/ohos.app.ability.hyperSnapManager%20应用快照管理/file-20260514163714866-0.png)


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import { hyperSnapManager } from '@kit.AbilityKit';
```


## hyperSnapManager.setHyperSnapEnabled
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setHyperSnapEnabled(enableFlag: boolean): void

启用或禁用应用的快照功能。


**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enableFlag | boolean | 是 | 表示快照功能开关标志。          - true：表示启用快照功能（系统将最终决策是否创建快照）。          - false：禁用应用快照功能。 |


**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[元能力子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability)。


| 错误码ID | 错误信息 |
| --- | --- |
| 16000150 | Failed to send request to system service. |


**示例：**


```ts
import { hyperSnapManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 启用应用快照功能
  hyperSnapManager.setHyperSnapEnabled(true);
  console.info('Hyper Snap enabled successfully.');
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(
    `Failed to enable Hyper Snap. Code: ${code}, Message: ${message}`,
  );
}
```


## hyperSnapManager.requestRebuildHyperSnap
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

requestRebuildHyperSnap(): void

请求重建应用的快照。

此方法会销毁当前进程对应的快照，系统将在合适的时机生成新的快照。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**错误码**：

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[元能力子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability)。


| 错误码ID | 错误信息 |
| --- | --- |
| 16000150 | Failed to send request to system service. |


**示例：**


```ts
import { hyperSnapManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 请求重建应用快照
  hyperSnapManager.requestRebuildHyperSnap();
  console.info('Requested to rebuild Hyper Snap successfully.');
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(
    `Failed to request Hyper Snap rebuild. Code: ${code}, Message: ${message}`,
  );
}
```
