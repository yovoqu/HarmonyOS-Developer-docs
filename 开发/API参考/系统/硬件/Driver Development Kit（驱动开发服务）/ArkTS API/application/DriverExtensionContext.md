# DriverExtensionContext

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext
**支持设备：** PC/2in1

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。

DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。


## 导入模块
**支持设备：** PC/2in1


```ts
import { common } from '@kit.AbilityKit';
```


## 使用说明
**支持设备：** PC/2in1

在使用DriverExtensionContext的功能前，需要通过DriverExtensionAbility子类实例获取。


```ts
import {
  DriverExtensionAbility,
  DriverExtensionContext,
} from '@kit.DriverDevelopmentKit';

let context: DriverExtensionContext | undefined;
class EntryAbility extends DriverExtensionAbility {
  onInit() {
    context = this.context; // 获取DriverExtensionContext
  }
}
```


## DriverExtensionContext.updateDriverState
**支持设备：** PC/2in1

updateDriverState(): void

驱动状态上报。预留接口，暂不提供具体功能。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**


```ts
// 当前代码实现依赖上一节代码实现
if (context != null) {
  context.updateDriverState();
}
```
