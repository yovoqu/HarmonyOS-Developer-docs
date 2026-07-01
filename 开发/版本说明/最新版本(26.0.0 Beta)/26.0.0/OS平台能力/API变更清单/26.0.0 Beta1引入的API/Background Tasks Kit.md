# Background Tasks Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：201 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增错误码 | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context): Promise&lt;void&gt;; 差异内容：NA | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context): Promise&lt;void&gt;; 差异内容：201 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskCancelInfo； API声明：detailedReason?: ContinuousTaskDetailedCancelReason; 差异内容：detailedReason?: ContinuousTaskDetailedCancelReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo； API声明：suspendMessage?: SuspendMessage; 差异内容：suspendMessage?: SuspendMessage; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：interface SuspendMessage 差异内容：interface SuspendMessage | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：SuspendMessage； API声明：message: string; 差异内容：message: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：SuspendMessage； API声明：reason: ContinuousTaskSuspendReason; 差异内容：reason: ContinuousTaskSuspendReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_NEARLINK = 14 差异内容：MODE_NEARLINK = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export enum ContinuousTaskDetailedCancelReason 差异内容：export enum ContinuousTaskDetailedCancelReason | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：USER_CANCEL_REMOVE_NOTIFICATION = 3 差异内容：USER_CANCEL_REMOVE_NOTIFICATION = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4 差异内容：SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 差异内容：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6 差异内容：SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7 差异内容：SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_LOCATION = 8 差异内容：SYSTEM_CANCEL_NOT_USE_LOCATION = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9 差异内容：SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10 差异内容：SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_USE_ILLEGALLY = 11 差异内容：SYSTEM_CANCEL_USE_ILLEGALLY = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_DATA_TRANSFER_NOT_UPDATE = 12 差异内容：SYSTEM_CANCEL_DATA_TRANSFER_NOT_UPDATE = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_VOIP_NOT_RUNNING = 13 差异内容：SYSTEM_CANCEL_VOIP_NOT_RUNNING = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskDetailedCancelReason； API声明：SYSTEM_CANCEL_USER_UNAUTHORIZED = 14 差异内容：SYSTEM_CANCEL_USER_UNAUTHORIZED = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_VOIP_NOT_USED = 13 差异内容：SYSTEM_SUSPEND_VOIP_NOT_USED = 13 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_BLUETOOTH_DATA_NOT_EXIST = 14 差异内容：SYSTEM_SUSPEND_BLUETOOTH_DATA_NOT_EXIST = 14 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_POSITION_NOT_MOVED = 15 差异内容：SYSTEM_SUSPEND_POSITION_NOT_MOVED = 15 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_AUDIO_PLAYBACK_MUTE = 16 差异内容：SYSTEM_SUSPEND_AUDIO_PLAYBACK_MUTE = 16 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_NEARLINK_NOT_USED = 17 差异内容：SYSTEM_SUSPEND_NEARLINK_NOT_USED = 17 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_NEARLINK_DATA_NOT_EXIST = 18 差异内容：SYSTEM_SUSPEND_NEARLINK_DATA_NOT_EXIST = 18 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_USER_UNAUTHORIZED = 19 差异内容：SYSTEM_SUSPEND_USER_UNAUTHORIZED = 19 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ReminderRequestTimer； API声明：repeatInterval?: number; 差异内容：repeatInterval?: number; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderRequestTimer； API声明：repeatCount?: number; 差异内容：repeatCount?: number; | api/@ohos.reminderAgentManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：export class ContinuousTaskRequest 差异内容：NA | 类名：backgroundTaskManager； API声明：export class ContinuousTaskRequest 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：get backgroundTaskModes(): BackgroundTaskMode[]; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：get backgroundTaskModes(): BackgroundTaskMode[]; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：get backgroundTaskSubmodes(): BackgroundTaskSubmode[]; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：get backgroundTaskSubmodes(): BackgroundTaskSubmode[]; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：get wantAgent(): WantAgent; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：get wantAgent(): WantAgent; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：combinedTaskNotification?: boolean; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：combinedTaskNotification?: boolean; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：continuousTaskId?: number; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：continuousTaskId?: number; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskRequest； API声明：isModeSupported(): boolean; 差异内容：NA | 类名：ContinuousTaskRequest； API声明：isModeSupported(): boolean; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContinuousTaskNotification； API声明：continuousTaskId?: number; 差异内容：NA | 类名：ContinuousTaskNotification； API声明：continuousTaskId?: number; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：NA | 类名：backgroundTaskManager； API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：NA | 类名：backgroundTaskManager； API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise&lt;void&gt;; 差异内容：NA | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise&lt;void&gt;; 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundMode； API声明：LOCATION = 4 差异内容：NA | 类名：BackgroundMode； API声明：LOCATION = 4 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskMode 差异内容：NA | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskMode 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode； API声明：MODE_AUDIO_PLAYBACK = 2 差异内容：NA | 类名：BackgroundTaskMode； API声明：MODE_AUDIO_PLAYBACK = 2 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode； API声明：MODE_LOCATION = 4 差异内容：NA | 类名：BackgroundTaskMode； API声明：MODE_LOCATION = 4 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode； API声明：MODE_MULTI_DEVICE_CONNECTION = 6 差异内容：NA | 类名：BackgroundTaskMode； API声明：MODE_MULTI_DEVICE_CONNECTION = 6 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskMode； API声明：MODE_AV_PLAYBACK_AND_RECORD = 12 差异内容：NA | 类名：BackgroundTaskMode； API声明：MODE_AV_PLAYBACK_AND_RECORD = 12 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskSubmode 差异内容：NA | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskSubmode 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode； API声明：SUBMODE_NORMAL_NOTIFICATION = 2 差异内容：NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_NORMAL_NOTIFICATION = 2 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4 差异内容：NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| API从不支持元服务到支持元服务 | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5 差异内容：NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5 差异内容：atomicservice | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
