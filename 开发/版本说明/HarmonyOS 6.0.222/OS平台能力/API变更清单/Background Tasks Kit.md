# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void; 差异内容：requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>; 差异内容：checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_AV_PLAYBACK_AND_RECORD = 12 差异内容：MODE_AV_PLAYBACK_AND_RECORD = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_SPECIAL_SCENARIO_PROCESSING = 13 差异内容：MODE_SPECIAL_SCENARIO_PROCESSING = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4 差异内容：SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5 差异内容：SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6 差异内容：SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7 差异内容：SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8 差异内容：SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9 差异内容：SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10 差异内容：SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export enum UserAuthResult 差异内容：export enum UserAuthResult | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult； API声明：NOT_SUPPORTED = 0 差异内容：NOT_SUPPORTED = 0 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult； API声明：NOT_DETERMINED = 1 差异内容：NOT_DETERMINED = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult； API声明：DENIED = 2 差异内容：DENIED = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult； API声明：GRANTED_ONCE = 3 差异内容：GRANTED_ONCE = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：UserAuthResult； API声明：GRANTED_ALWAYS = 4 差异内容：GRANTED_ALWAYS = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：WorkInfo； API声明：earliestStartTime?: number; 差异内容：earliestStartTime?: number; | api/@ohos.resourceschedule.workScheduler.d.ts |
