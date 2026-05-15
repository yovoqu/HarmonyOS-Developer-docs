# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global； API声明：export default class WorkSchedulerExtensionAbility 差异内容：stagemodelonly | 类名：global； API声明：declare class WorkSchedulerExtensionAbility 差异内容：NA | api/@ohos.WorkSchedulerExtensionAbility.d.ts |
| 新增API | NA | 类名：backgroundTaskManager； API声明：function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>; 差异内容：function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 接口新增必选属性 | 类名：global； API声明： 差异内容：NA | 类名：ContinuousTaskInfo； API声明：suspendState: boolean; 差异内容：suspendState: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
