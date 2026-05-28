# NotificationExtensionSubscriptionInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于描述通知扩展订阅的信息。
 
> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### NotificationExtensionSubscriptionInfo

**系统能力：** SystemCapability.Notification.Notification
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | notificationExtensionSubscription.SubscribeType | 否 | 否 | 表示订阅的类型，包括通过蓝牙订阅通知。 |
| addr | string | 否 | 否 | 表示设备的唯一标识符。例如："11:22:33:AA:BB:FF" |
