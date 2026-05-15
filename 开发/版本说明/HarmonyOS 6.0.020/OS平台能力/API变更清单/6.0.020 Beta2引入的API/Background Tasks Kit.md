# Background Tasks Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：backgroundProcessManager； API声明：export enum PowerSaveMode 差异内容：export enum PowerSaveMode | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：PowerSaveMode； API声明：EFFICIENCY_MODE = 1 差异内容：EFFICIENCY_MODE = 1 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：PowerSaveMode； API声明：DEFAULT_MODE = 2 差异内容：DEFAULT_MODE = 2 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>; 差异内容：function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager； API声明：function isPowerSaveMode(pid: number): Promise<boolean>; 差异内容：function isPowerSaveMode(pid: number): Promise<boolean>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
