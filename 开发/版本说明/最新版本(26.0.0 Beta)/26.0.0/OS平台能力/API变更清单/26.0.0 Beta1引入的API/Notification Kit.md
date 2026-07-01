# Notification Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-7001

## Notification Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：export interface UserGrantSetting 差异内容：export interface UserGrantSetting | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：UserGrantSetting； API声明：readonly userGrantEnabled: boolean; 差异内容：readonly userGrantEnabled: boolean; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：UserGrantSetting； API声明：readonly grantedBundleInfos?: Array&lt;GrantedBundleInfo&gt;; 差异内容：readonly grantedBundleInfos?: Array&lt;GrantedBundleInfo&gt;; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription； API声明：function openSubscriptionSettingsWithResult(context: UIAbilityContext): Promise&lt;UserGrantSetting&gt;; 差异内容：function openSubscriptionSettingsWithResult(context: UIAbilityContext): Promise&lt;UserGrantSetting&gt;; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription； API声明：export type UserGrantSetting = _UserGrantSetting; 差异内容：export type UserGrantSetting = _UserGrantSetting; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationManager； API声明：function openNotificationSettingsWithResult(context: UIAbilityContext): Promise&lt;NotificationSetting&gt;; 差异内容：function openNotificationSettingsWithResult(context: UIAbilityContext): Promise&lt;NotificationSetting&gt;; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting； API声明：lockScreenEnabled?: boolean; 差异内容：lockScreenEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting； API声明：bannerEnabled?: boolean; 差异内容：bannerEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting； API声明：badgeNumberEnabled?: boolean; 差异内容：badgeNumberEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting； API声明：notificationEnabled?: boolean; 差异内容：notificationEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
