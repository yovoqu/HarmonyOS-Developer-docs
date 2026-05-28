# Desktop Extension Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：quickBarManager； API声明：interface QuickBarGroup 差异内容：interface QuickBarGroup | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickBarGroup； API声明：groupKey: string; 差异内容：groupKey: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickBarGroup； API声明：groupIcon: image.PixelMap; 差异内容：groupIcon: image.PixelMap; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise&lt;void&gt;; 差异内容：function addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function deleteQuickBarGroup(context: common.Context, groupKey: string): Promise&lt;void&gt;; 差异内容：function deleteQuickBarGroup(context: common.Context, groupKey: string): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>; 差异内容：function getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager； API声明：function setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise&lt;void&gt;; 差异内容：function setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise&lt;void&gt;; | api/@hms.pcService.quickBarManager.d.ets |
