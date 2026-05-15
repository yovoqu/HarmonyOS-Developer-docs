# Notification Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：export interface NotificationParameters 差异内容：export interface NotificationParameters | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters； API声明：wantAction?: string; 差异内容：wantAction?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters； API声明：wantUri?: string; 差异内容：wantUri?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationParameters； API声明：wantParameters?: Record<string, Object>; 差异内容：wantParameters?: Record<string, Object>; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：notificationManager； API声明：function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>; 差异内容：function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager； API声明：export type NotificationParameters = _NotificationParameters; 差异内容：export type NotificationParameters = _NotificationParameters; | api/@ohos.notificationManager.d.ts |
