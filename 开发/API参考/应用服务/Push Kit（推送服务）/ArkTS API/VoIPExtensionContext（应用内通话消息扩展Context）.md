# VoIPExtensionContext（应用内通话消息扩展Context）

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-context
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

VoIPExtensionContext是VoIPExtensionAbility的上下文环境，继承自[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)。
 
**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Push.PushService
 
**起始版本：** 4.1.0(11)
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { VoIPExtensionContext } from '@kit.PushKit';
```
 
  

#### VoIPExtensionContext

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Push.PushService
 
**设备行为差异：** 对于6.1.0(23)以前版本，该属性在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。
 
**起始版本：** 4.1.0(11)
 
本类继承自[UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext)，未新增内容。
