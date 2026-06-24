# VoIPExtensionAbility（应用内通话消息扩展Ability）（废弃）

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-ability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

VoIPExtensionAbility为应用内通话消息扩展Ability，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)，增加获取场景化消息数据的回调。有如下约束：
 
- VoIPExtensionAbility为独立子进程，轻量级。
- 不允许调用卡片API。

 
执行ExtensionAbility失败可能会返回错误，请按具体报错信息排查，详请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Push.PushService
 
**起始版本：** 4.1.0(11)
 
**废弃版本：** 26.0.0
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { VoIPExtensionAbility } from '@kit.PushKit';
```
 
  

#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**模型约束：** 属性仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Push.PushService
 
**起始版本：** 4.1.0(11)
 
**废弃版本：** 26.0.0
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | VoIPExtensionContext(deprecated) | 否 | 否 | VoIPExtensionAbility的上下文环境，继承自UIExtensionContext。 |
 
 
  

#### onReceiveMessage(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void
 
应用继承VoIPExtensionAbility后接收应用内通话消息的接口。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.Push.PushService
 
**起始版本：** 4.1.0(11)
 
**废弃版本：** 26.0.0
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| voipInfo | pushCommon.VoIPInfo | 是 | 网络音视频通话消息数据。 |
 
 
**示例：**
 
```text
import { VoIPExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'VoIPExtensionAbility';

export default class VoipExtAbility extends VoIPExtensionAbility {
  // voipInfo为场景化消息数据
  onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'VoipExtAbility onReceiveMessage');
  }
}
```
