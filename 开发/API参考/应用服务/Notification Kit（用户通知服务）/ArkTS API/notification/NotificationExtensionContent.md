# NotificationExtensionContent

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-inner-notification-notificationextensioncontent
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

通知扩展内容。


> [!NOTE]
> 本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。


## NotificationExtensionContent
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.Notification.Notification


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 通知标题。不能为空且不能超过1024字节，超出内容将被截断。 |
| text | string | 否 | 否 | 通知内容。不能为空且不能超过3072字节，超出内容将被截断。 |
