# Ability Kit

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：UIAbilityContext； API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number; 差异内容：NA | 类名：UIAbilityContext； API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number; 差异内容：16000012,16000013 | api/application/UIAbilityContext.d.ts |
| 新增错误码 | 类名：UIExtensionContext； API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number; 差异内容：NA | 类名：UIExtensionContext； API声明：connectServiceExtensionAbility(want: Want, options: ConnectOptions): number; 差异内容：16000012,16000013 | api/application/UIExtensionContext.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace hyperSnapManager 差异内容：declare namespace hyperSnapManager | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager； API声明：function setHyperSnapEnabled(enableFlag: boolean): void; 差异内容：function setHyperSnapEnabled(enableFlag: boolean): void; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：hyperSnapManager； API声明：function requestRebuildHyperSnap(): void; 差异内容：function requestRebuildHyperSnap(): void; | api/@ohos.app.ability.hyperSnapManager.d.ts |
| 新增API | NA | 类名：AbilityStage； API声明：onLaunchFromHyperSnap(): void; 差异内容：onLaunchFromHyperSnap(): void; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：AbilityStage； API声明：onAboutToCreateAbility(): void; 差异内容：onAboutToCreateAbility(): void; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.app.ability.hyperSnapManager.d.ts 差异内容：AbilityKit | api/@ohos.app.ability.hyperSnapManager.d.ts |
