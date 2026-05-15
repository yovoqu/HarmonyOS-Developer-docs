# @system.notification (通知消息)

更新时间：2026-03-20 09:49:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-notification
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import notification from '@system.notification';
```


## ActionResult
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.Notification.Notification


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 单击通知后要重定向到的应用程序的Bundle名。 |
| abilityName | string | 是 | 单击通知后要重定向到的应用程序的Ability名称。 |
| uri | string | 否 | 要重定向到的页面的uri。 |


## ShowNotificationOptions
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.Notification.Notification


| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentTitle | string | 否 | 通知标题。 |
| contentText | string | 否 | 通知内容。 |
| clickAction(deprecated) | [ActionResult](#actionresult) | 否 | 通知被点击后触发的行为。 从API version 7开始不再维护。 |


## notification.show
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

show(options?: ShowNotificationOptions): void

显示通知。

**系统能力：** SystemCapability.Notification.Notification

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowNotificationOptions | 否 | 通知标题。 |


**示例：**


```ts
let notificationObj: notification = {
  show() {
    notification.show({
      contentTitle: 'title info',
      contentText: 'text',
      clickAction: {
        bundleName: 'com.example.testapp',
        abilityName: 'notificationDemo',
        uri: '/path/to/notification',
      },
    });
  },
};
```
