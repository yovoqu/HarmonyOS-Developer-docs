# Status Bar Extension Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-statusbarextensionkit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function removeFromStatusBar(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function removeFromStatusBar(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: Array&lt;StatusBarGroupMenu&gt;, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: Array&lt;StatusBarGroupMenu&gt;, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuAction； API声明：notifyOnly?: boolean; 差异内容：notifyOnly?: boolean; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuAction； API声明：menuCode?: string; 差异内容：menuCode?: string; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void; 差异内容：function on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void; 差异内容：function off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void; 差异内容：function on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void; 差异内容：function off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
