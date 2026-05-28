# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global； API声明：declare class WorkSchedulerExtensionAbility 差异内容：NA | 类名：global； API声明：declare class WorkSchedulerExtensionAbility 差异内容：stagemodelonly | api/@ohos.WorkSchedulerExtensionAbility.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; 差异内容：function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise&lt;void&gt;; 差异内容：function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise&lt;void&gt;; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export class ContinuousTaskRequest 差异内容：export class ContinuousTaskRequest | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：backgroundTaskModes: BackgroundTaskMode[]; 差异内容：backgroundTaskModes: BackgroundTaskMode[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：backgroundTaskSubmodes: BackgroundTaskSubmode[]; 差异内容：backgroundTaskSubmodes: BackgroundTaskSubmode[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：wantAgent: WantAgent; 差异内容：wantAgent: WantAgent; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：combinedTaskNotification?: boolean; 差异内容：combinedTaskNotification?: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：continuousTaskId?: number; 差异内容：continuousTaskId?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskRequest； API声明：isModeSupported(): boolean; 差异内容：isModeSupported(): boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskMode 差异内容：export enum BackgroundTaskMode | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_DATA_TRANSFER = 1 差异内容：MODE_DATA_TRANSFER = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_AUDIO_PLAYBACK = 2 差异内容：MODE_AUDIO_PLAYBACK = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_AUDIO_RECORDING = 3 差异内容：MODE_AUDIO_RECORDING = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_LOCATION = 4 差异内容：MODE_LOCATION = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_BLUETOOTH_INTERACTION = 5 差异内容：MODE_BLUETOOTH_INTERACTION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_MULTI_DEVICE_CONNECTION = 6 差异内容：MODE_MULTI_DEVICE_CONNECTION = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_VOIP = 8 差异内容：MODE_VOIP = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskMode； API声明：MODE_TASK_KEEPING = 9 差异内容：MODE_TASK_KEEPING = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export enum BackgroundTaskSubmode 差异内容：export enum BackgroundTaskSubmode | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1 差异内容：SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_NORMAL_NOTIFICATION = 2 差异内容：SUBMODE_NORMAL_NOTIFICATION = 2 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_LIVE_VIEW_NOTIFICATION = 3 差异内容：SUBMODE_LIVE_VIEW_NOTIFICATION = 3 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
