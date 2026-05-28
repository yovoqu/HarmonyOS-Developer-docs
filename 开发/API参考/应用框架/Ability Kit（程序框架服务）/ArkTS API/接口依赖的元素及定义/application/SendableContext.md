# SendableContext

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

SendableContext符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，继承自[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang#langisendable)。

> [!NOTE]
> 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { sendableContextManager } from '@kit.AbilityKit';
```



##### SendableContext

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

SendableContext符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。
