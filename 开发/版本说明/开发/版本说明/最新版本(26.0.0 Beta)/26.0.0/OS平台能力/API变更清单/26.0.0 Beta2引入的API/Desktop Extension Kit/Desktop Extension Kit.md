# Desktop Extension Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：quickBarManager； API声明：function setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise&lt;void&gt;; 差异内容：function setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise&lt;void&gt;; 差异内容：function setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：export enum ProgressState 差异内容：export enum ProgressState | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState； API声明：NO_PROGRESS = 0 差异内容：NO_PROGRESS = 0 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState； API声明：NORMAL = 1 差异内容：NORMAL = 1 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState； API声明：PAUSED = 2 差异内容：PAUSED = 2 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState； API声明：ERROR = 3 差异内容：ERROR = 3 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function setProgressState(context: common.Context, state: ProgressState): Promise&lt;void&gt;; 差异内容：function setProgressState(context: common.Context, state: ProgressState): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function setProgressValue(context: common.Context, completed: number, total: number): Promise&lt;void&gt;; 差异内容：function setProgressValue(context: common.Context, completed: number, total: number): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function isQuickBarCapabilitySupported(context: common.Context): Promise&lt;boolean&gt;; 差异内容：function isQuickBarCapabilitySupported(context: common.Context): Promise&lt;boolean&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：statusBarManager； API声明：function onIconHover(callback: Callback<emitter.EventData>): void; 差异内容：function onIconHover(callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function offIconHover(callback?: Callback<emitter.EventData>): void; 差异内容：function offIconHover(callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function isStatusBarCapabilitySupported(context: common.Context): Promise&lt;boolean&gt;; 差异内容：function isStatusBarCapabilitySupported(context: common.Context): Promise&lt;boolean&gt;; | api/@hms.pcService.statusBarManager.d.ts |
