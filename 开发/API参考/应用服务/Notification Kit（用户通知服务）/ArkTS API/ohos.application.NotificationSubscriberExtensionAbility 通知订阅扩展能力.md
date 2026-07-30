# @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

NotificationSubscriberExtensionAbility是通知订阅者扩展能力的基类，提供通知订阅的相关功能。三方穿戴类应用（如手表配套应用）通过继承此类实现回调逻辑，在本机发布通知时接收通知信息并通过蓝牙转发给穿戴设备，在本机通知被取消时接收取消通知的回调并转发给穿戴设备删除对应通知。
 
当穿戴类应用需要获取本机通知并同步到配对的穿戴设备时，使用本模块。本模块与notificationExtensionSubscription模块配合使用，本模块负责在回调中接收和处理通知数据，notificationExtensionSubscription模块负责授权、订阅和取消订阅等管理操作。
 
> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
```
 
  

#### NotificationSubscriberExtensionAbility

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力**：SystemCapability.Notification.Notification
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | NotificationSubscriberExtensionContext | 否 | 否 | NotificationSubscriberExtensionAbility的上下文环境。 |
 
 
  

#### onDestroy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onDestroy(): void
 
通知订阅扩展被销毁时的回调。
 
**系统能力**：SystemCapability.Notification.Notification
 
**示例：**
 
```text
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onDestroy(): void {
    console.info(`${TAG} onDestroy`);
  }
}
```
 
  

#### onReceiveMessage

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onReceiveMessage(notificationInfo: NotificationInfo): void
 
收到通知时回调。
 
**系统能力**：SystemCapability.Notification.Notification
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| notificationInfo | NotificationInfo | 是 | 通知订阅扩展能力中收到通知的回调信息。 |
 
 
**示例：**
 
```json
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
    console.info(`${TAG} onReceiveMessage. notificationInfo: ${JSON.stringify(notificationInfo)}`);
  }
}
```
 
  

#### onCancelMessages

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

onCancelMessages(hashCodes: Array&lt;string&gt;): void
 
取消通知时的回调。
 
**系统能力**：SystemCapability.Notification.Notification
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hashCodes | Array&lt;string&gt; | 是 | 要取消的通知的哈希码列表。通过onReceiveMessage获取。 |
 
 
**示例：**
 
```json
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onCancelMessages(hashCodes: Array<string>): void {
    console.info(`${TAG} onCancelMessages. hashCodes: ${JSON.stringify(hashCodes)}`);
  }
}
```
