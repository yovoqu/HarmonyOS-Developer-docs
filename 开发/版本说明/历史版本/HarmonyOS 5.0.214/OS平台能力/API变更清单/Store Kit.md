# Store Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-storekit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global； API声明： declare namespace updateManager 差异内容：NA | 类名：global； API声明： declare namespace updateManager 差异内容：stagemodelonly | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API模型切换 | 类名：updateManager； API声明： export enum UpdateAvailableCode 差异内容：NA | 类名：updateManager； API声明： export enum UpdateAvailableCode 差异内容：stagemodelonly | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API模型切换 | 类名：updateManager； API声明： export enum ShowUpdateResultCode 差异内容：NA | 类名：updateManager； API声明： export enum ShowUpdateResultCode 差异内容：stagemodelonly | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API模型切换 | 类名：updateManager； API声明： export interface CheckUpdateResult 差异内容：NA | 类名：updateManager； API声明： export interface CheckUpdateResult 差异内容：stagemodelonly | api/@hms.core.appgalleryservice.updateManager.d.ts |
| API模型切换 | 类名：CheckUpdateResult； API声明：readonly updateAvailable: UpdateAvailableCode; 差异内容：NA | 类名：CheckUpdateResult； API声明：readonly updateAvailable: UpdateAvailableCode; 差异内容：stagemodelonly | api/@hms.core.appgalleryservice.updateManager.d.ts |
| 新增API | NA | 类名：AppPrivacyLink； API声明：readonly name?: string; 差异内容：readonly name?: string; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：AppPrivacyResult； API声明：readonly signingTimestamp?: number; 差异内容：readonly signingTimestamp?: number; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：RequestErrorCode； API声明：MODULE_DEBUG_FILES_SIZE_OVER_LIMIT = -10 差异内容：MODULE_DEBUG_FILES_SIZE_OVER_LIMIT = -10 | api/@hms.core.appgalleryservice.moduleInstallManager.d.ts |
| 新增API | NA | 类名：RequestErrorCode； API声明：MODULE_DEBUG_FILES_NOT_EXIST = -9 差异内容：MODULE_DEBUG_FILES_NOT_EXIST = -9 | api/@hms.core.appgalleryservice.moduleInstallManager.d.ts |
| 新增API | NA | 类名：ServiceViewCallback； API声明：onAppear?: Callback&lt;void&gt;; 差异内容：onAppear?: Callback&lt;void&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：ServiceViewCallback； API声明：onDisappear?: Callback&lt;void&gt;; 差异内容：onDisappear?: Callback&lt;void&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：privacyManager； API声明： export interface ConsentResult 差异内容： export interface ConsentResult | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：ConsentResult； API声明：readonly results: AppPrivacyResult[]; 差异内容：readonly results: AppPrivacyResult[]; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：privacyManager； API声明：function requestAppPrivacyConsent(context: common.UIAbilityContext): Promise&lt;ConsentResult&gt;; 差异内容：function requestAppPrivacyConsent(context: common.UIAbilityContext): Promise&lt;ConsentResult&gt;; | api/@hms.core.appgalleryservice.privacyManager.d.ts |
| 新增API | NA | 类名：ProductViewCallback； API声明：onAppear?: Callback&lt;void&gt;; 差异内容：onAppear?: Callback&lt;void&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：ProductViewCallback； API声明：onDisappear?: Callback&lt;void&gt;; 差异内容：onDisappear?: Callback&lt;void&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager； API声明： export interface CheckShortcutResult 差异内容： export interface CheckShortcutResult | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：CheckShortcutResult； API声明：tid?: string; 差异内容：tid?: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：CheckShortcutResult； API声明：expired?: number; 差异内容：expired?: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：CheckShortcutResult； API声明：code: number; 差异内容：code: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：CheckShortcutResult； API声明：limit?: number; 差异内容：limit?: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager； API声明： export interface SKExposure 差异内容： export interface SKExposure | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：adTechId: string; 差异内容：adTechId: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：campaignId: string; 差异内容：campaignId: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：destinationId: string; 差异内容：destinationId: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：mmpIds?: string[]; 差异内容：mmpIds?: string[]; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：serviceTag?: string; 差异内容：serviceTag?: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：nonce: string; 差异内容：nonce: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：timestamp: number; 差异内容：timestamp: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：SKExposure； API声明：signature: string; 差异内容：signature: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager； API声明：function checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise&lt;CheckShortcutResult&gt;; 差异内容：function checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise&lt;CheckShortcutResult&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager； API声明：function checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise&lt;CheckShortcutResult&gt;; 差异内容：function checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise&lt;CheckShortcutResult&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager； API声明：function requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise&lt;void&gt;; 差异内容：function requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise&lt;void&gt;; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
