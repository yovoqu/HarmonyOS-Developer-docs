# Ability Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：appManager； API声明：function off(type: 'applicationState', observerId: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：function off(type: 'applicationState', observerId: number, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.app.ability.appManager.d.ts |
| 新增API | NA | 类名：AbilityConstant； API声明： export enum PrepareTermination 差异内容： export enum PrepareTermination | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：PrepareTermination； API声明：TERMINATE_IMMEDIATELY = 0 差异内容：TERMINATE_IMMEDIATELY = 0 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：PrepareTermination； API声明：CANCEL = 1 差异内容：CANCEL = 1 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：AbilityStage； API声明：onPrepareTermination(): AbilityConstant.PrepareTermination; 差异内容：onPrepareTermination(): AbilityConstant.PrepareTermination; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：AbilityStage； API声明：onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>; 差异内容：onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>; | api/@ohos.app.ability.AbilityStage.d.ts |
| 新增API | NA | 类名：UIAbility； API声明：onPrepareToTerminateAsync(): Promise&lt;boolean&gt;; 差异内容：onPrepareToTerminateAsync(): Promise&lt;boolean&gt;; | api/@ohos.app.ability.UIAbility.d.ts |
| 新增API | NA | 类名：Context； API声明：createDisplayContext(displayId: number): Context; 差异内容：createDisplayContext(displayId: number): Context; | api/application/Context.d.ts |
| 新增API | NA | 类名：UIAbilityContext； API声明：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise&lt;void&gt;; 差异内容：setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise&lt;void&gt;; | api/application/UIAbilityContext.d.ts |
