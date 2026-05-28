# Background Tasks Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：reminderAgentManager； API声明：function cancelReminderOnDisplay(reminderId: number): Promise&lt;void&gt;; 差异内容：function cancelReminderOnDisplay(reminderId: number): Promise&lt;void&gt;; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：function subscribeReminderState(callback: Callback<Array&lt;ReminderState&gt;>): Promise&lt;void&gt;; 差异内容：function subscribeReminderState(callback: Callback<Array&lt;ReminderState&gt;>): Promise&lt;void&gt;; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：function unsubscribeReminderState(callback?: Callback<Array&lt;ReminderState&gt;>): Promise&lt;void&gt;; 差异内容：function unsubscribeReminderState(callback?: Callback<Array&lt;ReminderState&gt;>): Promise&lt;void&gt;; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：RingChannel； API声明：RING_CHANNEL_NOTIFICATION = 2 差异内容：RING_CHANNEL_NOTIFICATION = 2 | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：reminderAgentManager； API声明：interface ReminderState 差异内容：interface ReminderState | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState； API声明：reminderId: number; 差异内容：reminderId: number; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState； API声明：buttonType: ActionButtonType; 差异内容：buttonType: ActionButtonType; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：ReminderState； API声明：isMessageResent: boolean; 差异内容：isMessageResent: boolean; | api/@ohos.reminderAgentManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：function getPowerSaveMode(pid: number): Promise&lt;PowerSaveMode&gt;; 差异内容：function getPowerSaveMode(pid: number): Promise&lt;PowerSaveMode&gt;; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：bundleName?: string; 差异内容：bundleName?: string; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：ContinuousTaskInfo； API声明：appIndex?: number; 差异内容：appIndex?: number; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 新增API | NA | 类名：BackgroundTaskSubmode； API声明：SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11 差异内容：SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11 | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
