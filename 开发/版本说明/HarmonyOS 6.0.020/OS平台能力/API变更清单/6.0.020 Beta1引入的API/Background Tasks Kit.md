# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：reminderAgentManager； API声明：function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise&lt;void&gt;; 差异内容：function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise&lt;void&gt;; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：export enum RingChannel 差异内容：export enum RingChannel | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel； API声明：RING_CHANNEL_ALARM = 0 差异内容：RING_CHANNEL_ALARM = 0 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel； API声明：RING_CHANNEL_MEDIA = 1 差异内容：RING_CHANNEL_MEDIA = 1 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：interface TransientTaskInfo 差异内容：interface TransientTaskInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：TransientTaskInfo； API声明：remainingQuota: number; 差异内容：remainingQuota: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：TransientTaskInfo； API声明：transientTasks: DelaySuspendInfo[]; 差异内容：transientTasks: DelaySuspendInfo[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：interface ContinuousTaskActiveInfo 差异内容：interface ContinuousTaskActiveInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskActiveInfo； API声明：id: number; 差异内容：id: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：interface ContinuousTaskInfo 差异内容：interface ContinuousTaskInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：abilityName: string; 差异内容：abilityName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：uid: number; 差异内容：uid: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：pid: number; 差异内容：pid: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：isFromWebView: boolean; 差异内容：isFromWebView: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：backgroundModes: string[]; 差异内容：backgroundModes: string[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：backgroundSubModes: string[]; 差异内容：backgroundSubModes: string[]; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：notificationId: number; 差异内容：notificationId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：continuousTaskId: number; 差异内容：continuousTaskId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：abilityId: number; 差异内容：abilityId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：wantAgentBundleName: string; 差异内容：wantAgentBundleName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：wantAgentAbilityName: string; 差异内容：wantAgentAbilityName: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：interface ContinuousTaskSuspendInfo 差异内容：interface ContinuousTaskSuspendInfo | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo； API声明：continuousTaskId: number; 差异内容：continuousTaskId: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo； API声明：suspendState: boolean; 差异内容：suspendState: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendInfo； API声明：suspendReason: ContinuousTaskSuspendReason; 差异内容：suspendReason: ContinuousTaskSuspendReason; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function getTransientTaskInfo(): Promise&lt;TransientTaskInfo&gt;; 差异内容：function getTransientTaskInfo(): Promise&lt;TransientTaskInfo&gt;; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>; 差异内容：function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function on(type: 'continuousTaskSuspend', callback: Callback&lt;ContinuousTaskSuspendInfo&gt;): void; 差异内容：function on(type: 'continuousTaskSuspend', callback: Callback&lt;ContinuousTaskSuspendInfo&gt;): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function off(type: 'continuousTaskSuspend', callback?: Callback&lt;ContinuousTaskSuspendInfo&gt;): void; 差异内容：function off(type: 'continuousTaskSuspend', callback?: Callback&lt;ContinuousTaskSuspendInfo&gt;): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function on(type: 'continuousTaskActive', callback: Callback&lt;ContinuousTaskActiveInfo&gt;): void; 差异内容：function on(type: 'continuousTaskActive', callback: Callback&lt;ContinuousTaskActiveInfo&gt;): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function off(type: 'continuousTaskActive', callback?: Callback&lt;ContinuousTaskActiveInfo&gt;): void; 差异内容：function off(type: 'continuousTaskActive', callback?: Callback&lt;ContinuousTaskActiveInfo&gt;): void; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：export enum ContinuousTaskSuspendReason 差异内容：export enum ContinuousTaskSuspendReason | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_DATA_TRANSFER_LOW_SPEED = 4 差异内容：SYSTEM_SUSPEND_DATA_TRANSFER_LOW_SPEED = 4 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 差异内容：SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_RUNNING = 6 差异内容：SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_RUNNING = 6 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_AUDIO_RECORDING_NOT_RUNNING = 7 差异内容：SYSTEM_SUSPEND_AUDIO_RECORDING_NOT_RUNNING = 7 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_LOCATION_NOT_USED = 8 差异内容：SYSTEM_SUSPEND_LOCATION_NOT_USED = 8 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_BLUETOOTH_NOT_USED = 9 差异内容：SYSTEM_SUSPEND_BLUETOOTH_NOT_USED = 9 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_MULTI_DEVICE_NOT_USED = 10 差异内容：SYSTEM_SUSPEND_MULTI_DEVICE_NOT_USED = 10 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_USED_ILLEGALLY = 11 差异内容：SYSTEM_SUSPEND_USED_ILLEGALLY = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskSuspendReason； API声明：SYSTEM_SUSPEND_SYSTEM_LOAD_WARNING = 12 差异内容：SYSTEM_SUSPEND_SYSTEM_LOAD_WARNING = 12 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：ReminderRequest； API声明：ringChannel?: RingChannel; 差异内容：ringChannel?: RingChannel; | api/@ohos.reminderAgentManager.d.ts |
