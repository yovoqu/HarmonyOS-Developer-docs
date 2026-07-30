# Background Tasks Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：requestAuthFromUserByDialog(context: Context, callback: Callback&lt;UserAuthResult&gt;): void; 差异内容：requestAuthFromUserByDialog(context: Context, callback: Callback&lt;UserAuthResult&gt;): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：checkSpecialScenarioAuthResult(context: Context): Promise&lt;UserAuthResult&gt;; 差异内容：checkSpecialScenarioAuthResult(context: Context): Promise&lt;UserAuthResult&gt;; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：export enum TimeZoneType 差异内容：export enum TimeZoneType | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType； API声明：FIXED_TIME_ZONE = 1 差异内容：FIXED_TIME_ZONE = 1 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：TimeZoneType； API声明：SYSTEM_TIME_ZONE = 2 差异内容：SYSTEM_TIME_ZONE = 2 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：interface NotificationRequestProxy 差异内容：interface NotificationRequestProxy | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：NotificationRequestProxy； API声明：appMessageId?: string; 差异内容：appMessageId?: string; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：NotificationRequestProxy； API声明：isAlertOnce?: boolean; 差异内容：isAlertOnce?: boolean; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequest； API声明：fixedTimeZone?: TimeZoneType; 差异内容：fixedTimeZone?: TimeZoneType; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequest； API声明：notificationRequestProxy?: NotificationRequestProxy; 差异内容：notificationRequestProxy?: NotificationRequestProxy; | api/@ohos.reminderAgentManager.d.ts |
| 删除API | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 差异内容：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 | NA | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
