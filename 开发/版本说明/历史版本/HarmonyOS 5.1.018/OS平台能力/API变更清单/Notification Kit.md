# Notification Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：801 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number): Promise&lt;void&gt;; 差异内容：NA | 类名：notificationManager； API声明：function setBadgeNumber(badgeNumber: number): Promise&lt;void&gt;; 差异内容：801 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager； API声明：function openNotificationSettings(context: UIAbilityContext): Promise&lt;void&gt;; 差异内容：NA | 类名：notificationManager； API声明：function openNotificationSettings(context: UIAbilityContext): Promise&lt;void&gt;; 差异内容：801 | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function cancelAll(): Promise&lt;void&gt;; 差异内容：401 | 类名：notificationManager； API声明：function cancelAll(): Promise&lt;void&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function getSlots(): Promise<Array&lt;NotificationSlot&gt;>; 差异内容：401 | 类名：notificationManager； API声明：function getSlots(): Promise<Array&lt;NotificationSlot&gt;>; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function removeAllSlots(): Promise&lt;void&gt;; 差异内容：401 | 类名：notificationManager； API声明：function removeAllSlots(): Promise&lt;void&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function isNotificationEnabled(): Promise&lt;boolean&gt;; 差异内容：401 | 类名：notificationManager； API声明：function isNotificationEnabled(): Promise&lt;boolean&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function getActiveNotificationCount(): Promise&lt;number&gt;; 差异内容：401 | 类名：notificationManager； API声明：function getActiveNotificationCount(): Promise&lt;number&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function getActiveNotifications(): Promise<Array&lt;NotificationRequest&gt;>; 差异内容：401 | 类名：notificationManager； API声明：function getActiveNotifications(): Promise<Array&lt;NotificationRequest&gt;>; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function requestEnableNotification(): Promise&lt;void&gt;; 差异内容：401 | 类名：notificationManager； API声明：function requestEnableNotification(): Promise&lt;void&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager； API声明：function isDistributedEnabled(): Promise&lt;boolean&gt;; 差异内容：401 | 类名：notificationManager； API声明：function isDistributedEnabled(): Promise&lt;boolean&gt;; 差异内容：NA | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：global； API声明：export interface NotificationIconButton 差异内容：export interface NotificationIconButton | api/notification/notificationContent.d.ts |
| 起始版本有变化 | 类名：notificationManager； API声明：function isNotificationEnabled(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：9 | 类名：notificationManager； API声明：function isNotificationEnabled(callback: AsyncCallback&lt;boolean&gt;): void; 差异内容：11 | api/@ohos.notificationManager.d.ts |
| 起始版本有变化 | 类名：notificationManager； API声明：function isNotificationEnabled(): Promise&lt;boolean&gt;; 差异内容：9 | 类名：notificationManager； API声明：function isNotificationEnabled(): Promise&lt;boolean&gt;; 差异内容：11 | api/@ohos.notificationManager.d.ts |
| 起始版本有变化 | 类名：global； API声明：export enum NotificationFlagStatus 差异内容：8 | 类名：global； API声明：export enum NotificationFlagStatus 差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus； API声明：TYPE_NONE = 0 差异内容：8 | 类名：NotificationFlagStatus； API声明：TYPE_NONE = 0 差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus； API声明：TYPE_OPEN = 1 差异内容：8 | 类名：NotificationFlagStatus； API声明：TYPE_OPEN = 1 差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus； API声明：TYPE_CLOSE = 2 差异内容：8 | 类名：NotificationFlagStatus； API声明：TYPE_CLOSE = 2 差异内容：11 | api/notification/notificationFlags.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：NotificationRequest； API声明：updateOnly?: boolean; 差异内容：updateOnly?: boolean; | api/notification/notificationRequest.d.ts |
| 新增导出符号 | 类名：global； API声明：export interface NotificationIconButton 差异内容：NA | 类名：global； API声明： 差异内容：export interface NotificationIconButton | api/notification/notificationContent.d.ts |
