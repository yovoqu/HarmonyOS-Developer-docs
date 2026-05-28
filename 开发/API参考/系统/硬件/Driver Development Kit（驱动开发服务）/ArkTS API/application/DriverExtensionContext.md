# DriverExtensionContext

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext
**支持设备：** PC/2in1

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。
 
DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。
 
> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。

  

#### 导入模块

**支持设备：** PC/2in1

```text
import { common } from '@kit.AbilityKit';
```
 
  

#### 使用说明

**支持设备：** PC/2in1

在使用DriverExtensionContext的功能前，需要通过DriverExtensionAbility子类实例获取。
 
```text
import { DriverExtensionAbility, DriverExtensionContext } from '@kit.DriverDevelopmentKit';

  let context : DriverExtensionContext | undefined;
  class EntryAbility extends DriverExtensionAbility {
    onInit() {
      context = this.context; // 获取DriverExtensionContext
    }
  }
```
 
  

#### DriverExtensionContext.updateDriverState

**支持设备：** PC/2in1

updateDriverState(): void
 
驱动状态上报。预留接口，暂不提供具体功能。
 
**系统能力**：SystemCapability.Driver.ExternalDevice
 
**示例：**
 
```text
// 当前代码实现依赖上一节代码实现
if (context != null) {
  context.updateDriverState();
}
```
