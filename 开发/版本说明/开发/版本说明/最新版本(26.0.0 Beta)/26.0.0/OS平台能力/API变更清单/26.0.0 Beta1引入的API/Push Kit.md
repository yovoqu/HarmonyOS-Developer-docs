# Push Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global； API声明：export default class VoIPExtensionAbility 差异内容：NA | 类名：global； API声明：export default class VoIPExtensionAbility 差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：VoIPExtensionAbility； API声明：context: VoIPExtensionContext; 差异内容：NA | 类名：VoIPExtensionAbility； API声明：context: VoIPExtensionContext; 差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：VoIPExtensionAbility； API声明：onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void; 差异内容：NA | 类名：VoIPExtensionAbility； API声明：onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void; 差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：global； API声明：export default class VoIPExtensionContext 差异内容：NA | 类名：global； API声明：export default class VoIPExtensionContext 差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionContext.d.ts |
| 新增API | NA | 类名：serviceNotification； API声明：function querySubscribeNotificationSetting(): Promise&lt;SubscribeNotificationSetting&gt;; 差异内容：function querySubscribeNotificationSetting(): Promise&lt;SubscribeNotificationSetting&gt;; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification； API声明：export interface SubscribeNotificationSetting 差异内容：export interface SubscribeNotificationSetting | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting； API声明：bundleName: string; 差异内容：bundleName: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting； API声明：enable?: boolean; 差异内容：enable?: boolean; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting； API声明：entitySettings?: Array&lt;EntitySetting&gt;; 差异内容：entitySettings?: Array&lt;EntitySetting&gt;; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification； API声明：export interface EntitySetting 差异内容：export interface EntitySetting | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting； API声明：entityId: string; 差异内容：entityId: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting； API声明：entityName: string; 差异内容：entityName: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting； API声明：enable?: boolean; 差异内容：enable?: boolean; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting； API声明：entityType: EntityType; 差异内容：entityType: EntityType; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification； API声明：export enum EntityType 差异内容：export enum EntityType | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntityType； API声明：ONCE = 0 差异内容：ONCE = 0 | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntityType； API声明：PERIOD = 1 差异内容：PERIOD = 1 | api/@hms.core.push.serviceNotification.d.ts |
