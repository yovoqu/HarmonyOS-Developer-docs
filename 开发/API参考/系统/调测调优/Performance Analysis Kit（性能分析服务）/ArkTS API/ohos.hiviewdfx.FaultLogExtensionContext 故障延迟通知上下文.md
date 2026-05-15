# @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

FaultLogExtensionContext是[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

FaultLogExtensionContext模块提供访问[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。


## 使用说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通过FaultLogExtensionAbility子类实例来获取。


```ts
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
  onFaultReportReady() {
    let context = this.context; // 获取FaultLogExtensionContext
    console.info('cache dir is ' + context.cacheDir); // 访问context中的成员
  }
}
```


## FaultLogExtensionContext
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

FaultLogExtensionContext是[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的上下文环境。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger
