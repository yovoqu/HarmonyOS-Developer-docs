# Ability Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6012

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：ApplicationContext； API声明：setLanguage(language: string): void; 差异内容：NA | 类名：ApplicationContext； API声明：setLanguage(language: string): void; 差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：ApplicationContext； API声明：setFont(font: string): void; 差异内容：NA | 类名：ApplicationContext； API声明：setFont(font: string): void; 差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：ApplicationContext； API声明：setFontSizeScale(fontSizeScale: number): void; 差异内容：NA | 类名：ApplicationContext； API声明：setFontSizeScale(fontSizeScale: number): void; 差异内容：crossplatform | api/application/ApplicationContext.d.ts |
| API跨平台权限变更 | 类名：UIAbilityContext； API声明：windowStage: window.WindowStage; 差异内容：NA | 类名：UIAbilityContext； API声明：windowStage: window.WindowStage; 差异内容：crossplatform | api/application/UIAbilityContext.d.ts |
| 删除错误码 | 类名：ApplicationContext； API声明：setLanguage(language: string): void; 差异内容：401 | 类名：ApplicationContext； API声明：setLanguage(language: string): void; 差异内容：NA | api/application/ApplicationContext.d.ts |
| 删除错误码 | 类名：ApplicationContext； API声明：setFont(font: string): void; 差异内容：401 | 类名：ApplicationContext； API声明：setFont(font: string): void; 差异内容：NA | api/application/ApplicationContext.d.ts |
| 删除错误码 | 类名：ApplicationContext； API声明：setFontSizeScale(fontSizeScale: number): void; 差异内容：401 | 类名：ApplicationContext； API声明：setFontSizeScale(fontSizeScale: number): void; 差异内容：NA | api/application/ApplicationContext.d.ts |
| 新增API | NA | 类名：ChildProcessOptions； API声明：isolationUid?: boolean; 差异内容：isolationUid?: boolean; | api/@ohos.app.ability.ChildProcessOptions.d.ts |
