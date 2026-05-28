# Desktop Extension Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：statusBarManager； API声明：function removeFromStatusBar(context: common.Context): void; 差异内容：NA | 类名：statusBarManager； API声明：function removeFromStatusBar(context: common.Context): void; 差异内容：1010710003,1010710004,401 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function removeFromStatusBar(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：statusBarManager； API声明：function removeFromStatusBar(context: common.Context, callback: AsyncCallback&lt;void&gt;): void; 差异内容：1010710003,1010710004,401 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void; 差异内容：NA | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：statusBarManager； API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback&lt;void&gt;): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function updateQuickOperationHeight(context: common.Context, height: number): void; 差异内容：NA | 类名：statusBarManager； API声明：function updateQuickOperationHeight(context: common.Context, height: number): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：statusBarManager； API声明：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void; 差异内容：NA | 类名：statusBarManager； API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager； API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：statusBarManager； API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback&lt;void&gt;): void; 差异内容：1010710003 | api/@hms.pcService.statusBarManager.d.ts |
| 属性变更 | 类名：StatusBarItem； API声明：statusBarGroupMenu?: Array&lt;StatusBarGroupMenu&gt;; 差异内容：Array&lt;StatusBarGroupMenu&gt; | 类名：StatusBarItem； API声明：statusBarGroupMenu?: StatusBarGroupMenu[]; 差异内容：StatusBarGroupMenu[] | api/@hms.pcService.statusBarManager.d.ts |
| 属性变更 | 类名：StatusBarMenuItem； API声明：subMenu?: Array&lt;StatusBarSubMenuItem&gt;; 差异内容：Array&lt;StatusBarSubMenuItem&gt; | 类名：StatusBarMenuItem； API声明：subMenu?: StatusBarSubMenuItem[]; 差异内容：StatusBarSubMenuItem[] | api/@hms.pcService.statusBarManager.d.ts |
| 自定义类型变更 | 类名：statusBarManager； API声明：type StatusBarGroupMenu = Array&lt;StatusBarMenuItem&gt;; 差异内容：Array&lt;StatusBarMenuItem&gt; | 类名：statusBarManager； API声明：type StatusBarGroupMenu = StatusBarMenuItem[]; 差异内容：StatusBarMenuItem[] | api/@hms.pcService.statusBarManager.d.ts |
| kit变更 | StatusBarExtensionKit | DesktopExtensionKit | api/@hms.pcService.statusBarManager.d.ts |
| kit变更 | StatusBarExtensionKit | DesktopExtensionKit | api/@hms.pcService.StatusBarViewExtensionAbility.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：kits@kit.DeskTopExtensionKit.d.ts 差异内容：DesktopExtensionKit | kits/@kit.DeskTopExtensionKit.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：QuickOperation； API声明：loadingStatus?: boolean; 差异内容：loadingStatus?: boolean; | api/@hms.pcService.statusBarManager.d.ts |
