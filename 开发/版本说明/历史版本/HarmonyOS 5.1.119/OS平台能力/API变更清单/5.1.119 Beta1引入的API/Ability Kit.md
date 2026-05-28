# Ability Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：continueManager； API声明：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback&lt;ContinueResultInfo&gt;): void; 差异内容：401 | 类名：continueManager； API声明：function on(type: 'prepareContinue', context: Context, callback: AsyncCallback&lt;ContinueResultInfo&gt;): void; 差异内容：NA | api/@ohos.app.ability.continueManager.d.ts |
| 删除错误码 | 类名：continueManager； API声明：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback&lt;ContinueResultInfo&gt;): void; 差异内容：401 | 类名：continueManager； API声明：function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback&lt;ContinueResultInfo&gt;): void; 差异内容：NA | api/@ohos.app.ability.continueManager.d.ts |
| 删除错误码 | 类名：UIExtensionContentSession； API声明：loadContentByName(name: string, storage?: LocalStorage): void; 差异内容：401 | 类名：UIExtensionContentSession； API声明：loadContentByName(name: string, storage?: LocalStorage): void; 差异内容：NA | api/@ohos.app.ability.UIExtensionContentSession.d.ts |
| 删除错误码 | 类名：Context； API声明：createAreaModeContext(areaMode: contextConstant.AreaMode): Context; 差异内容：401 | 类名：Context； API声明：createAreaModeContext(areaMode: contextConstant.AreaMode): Context; 差异内容：NA | api/application/Context.d.ts |
| 删除错误码 | 类名：UIAbilityContext； API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; 差异内容：401 | 类名：UIAbilityContext； API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; 差异内容：NA | api/application/UIAbilityContext.d.ts |
| 删除错误码 | 类名：UIExtensionContext； API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; 差异内容：401 | 类名：UIExtensionContext； API声明：setColorMode(colorMode: ConfigurationConstant.ColorMode): void; 差异内容：NA | api/application/UIExtensionContext.d.ts |
| 新增API | NA | 类名：application； API声明：export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise&lt;Context&gt;; 差异内容：export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise&lt;Context&gt;; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：Params； API声明：APP_LAUNCH_TRUSTLIST = 'ohos.params.appLaunchTrustList' 差异内容：APP_LAUNCH_TRUSTLIST = 'ohos.params.appLaunchTrustList' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：Params； API声明：DESTINATION_PLUGIN_ABILITY = 'ohos.params.pluginAbility' 差异内容：DESTINATION_PLUGIN_ABILITY = 'ohos.params.pluginAbility' | api/@ohos.app.ability.wantConstant.d.ts |
| 新增API | NA | 类名：ExtensionAbilityType； API声明：CALLER_INFO_QUERY = 25 差异内容：CALLER_INFO_QUERY = 25 | api/@ohos.bundle.bundleManager.d.ts |
