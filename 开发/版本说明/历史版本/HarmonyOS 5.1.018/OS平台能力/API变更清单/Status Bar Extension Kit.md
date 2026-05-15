# Status Bar Extension Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-statusbarextensionkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void; 差异内容：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void; 差异内容：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 删除同名函数 | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem): void; 差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem): void; | 类名：global； API声明： 差异内容：NA | api/@hms.pcService.statusBarManager.d.ts |
| 删除同名函数 | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void; 差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void; | 类名：global； API声明： 差异内容：NA | api/@hms.pcService.statusBarManager.d.ts |
