# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-5051

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace backgroundProcessManager 差异内容：declare namespace backgroundProcessManager | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：export enum ProcessPriority 差异内容：export enum ProcessPriority | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ProcessPriority； API声明：PROCESS_BACKGROUND = 1 差异内容：PROCESS_BACKGROUND = 1 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ProcessPriority； API声明：PROCESS_INACTIVE = 2 差异内容：PROCESS_INACTIVE = 2 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：function setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>; 差异内容：function setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：function resetProcessPriority(pid: number): Promise<void>; 差异内容：function resetProcessPriority(pid: number): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.resourceschedule.backgroundProcessManager.d.ts 差异内容：BackgroundTasksKit | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
