# App Gallery Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-appgallerykit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace appInfoManager 差异内容： declare namespace appInfoManager | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager； API声明： export interface DynamicIconInfo 差异内容： export interface DynamicIconInfo | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo； API声明：readonly iconUrl: string; 差异内容：readonly iconUrl: string; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo； API声明：readonly iconId: string; 差异内容：readonly iconId: string; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：DynamicIconInfo； API声明：readonly enabled: boolean; 差异内容：readonly enabled: boolean; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager； API声明：function queryDynamicIcons(): Promise<DynamicIconInfo[]>; 差异内容：function queryDynamicIcons(): Promise<DynamicIconInfo[]>; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager； API声明：function selectDynamicIcon(iconId: string): Promise&lt;void&gt;; 差异内容：function selectDynamicIcon(iconId: string): Promise&lt;void&gt;; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| 新增API | NA | 类名：appInfoManager； API声明：function disableDynamicIcon(): Promise&lt;void&gt;; 差异内容：function disableDynamicIcon(): Promise&lt;void&gt;; | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
| kit变更 | NA | AppGalleryKit | api/@hms.core.appgalleryservice.appInfoManager.d.ts |
