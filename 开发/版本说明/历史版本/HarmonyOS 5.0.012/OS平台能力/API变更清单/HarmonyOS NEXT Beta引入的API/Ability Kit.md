# Ability Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：Context； API声明：createModuleContext(moduleName: string): Context; 差异内容：NA | 类名：Context； API声明：createModuleContext(moduleName: string): Context; 差异内容：12 | api/application/Context.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace application 差异内容： declare namespace application | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：application； API声明：export function createModuleContext(context: Context, moduleName: string): Promise&lt;Context&gt;; 差异内容：export function createModuleContext(context: Context, moduleName: string): Promise&lt;Context&gt;; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：LaunchReason； API声明：PREPARE_CONTINUATION = 10 差异内容：PREPARE_CONTINUATION = 10 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：Params； API声明：CALLER_REQUEST_CODE = 'ohos.extra.param.key.callerRequestCode' 差异内容：CALLER_REQUEST_CODE = 'ohos.extra.param.key.callerRequestCode' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：UIAbilityContext； API声明：backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise&lt;void&gt;; 差异内容：backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise&lt;void&gt;; | api/application/UIAbilityContext.d.ts |
| 新增API | NA | 类名：ApplicationInfo； API声明：readonly cloudFileSyncEnabled: boolean; 差异内容：readonly cloudFileSyncEnabled: boolean; | api/bundleManager/ApplicationInfo.d.ts |
