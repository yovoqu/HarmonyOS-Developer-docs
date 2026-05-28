# Ability Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-abilitykit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare enum FailureCode 差异内容：declare enum FailureCode | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：FailureCode； API声明：FAILURE_CODE_SYSTEM_MALFUNCTION = 0 差异内容：FAILURE_CODE_SYSTEM_MALFUNCTION = 0 | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：FailureCode； API声明：FAILURE_CODE_USER_CANCEL = 1 差异内容：FAILURE_CODE_USER_CANCEL = 1 | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：FailureCode； API声明：FAILURE_CODE_USER_REFUSE = 2 差异内容：FAILURE_CODE_USER_REFUSE = 2 | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：global； API声明：declare class CompletionHandlerForAtomicService 差异内容：declare class CompletionHandlerForAtomicService | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：CompletionHandlerForAtomicService； API声明：onAtomicServiceRequestSuccess(appId: string): void; 差异内容：onAtomicServiceRequestSuccess(appId: string): void; | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：CompletionHandlerForAtomicService； API声明：onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string): void; 差异内容：onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string): void; | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 新增API | NA | 类名：LaunchReason； API声明：PRELOAD = 11 差异内容：PRELOAD = 11 | api/@ohos.app.ability.AbilityConstant.d.ts |
| 新增API | NA | 类名：application； API声明：export function promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise&lt;void&gt;; 差异内容：export function promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise&lt;void&gt;; | api/@ohos.app.ability.application.d.ts |
| 新增API | NA | 类名：application； API声明：export function demoteCurrentFromCandidateMasterProcess(): Promise&lt;void&gt;; 差异内容：export function demoteCurrentFromCandidateMasterProcess(): Promise&lt;void&gt;; | api/@ohos.app.ability.application.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.app.ability.CompletionHandlerForAtomicService.d.ts 差异内容：AbilityKit | api/@ohos.app.ability.CompletionHandlerForAtomicService.d.ts |
| 类新增可选成员 | 类名：global； API声明： 差异内容：NA | 类名：AtomicServiceOptions； API声明：completionHandlerForAtomicService?: CompletionHandlerForAtomicService; 差异内容：completionHandlerForAtomicService?: CompletionHandlerForAtomicService; | api/@ohos.app.ability.AtomicServiceOptions.d.ts |
| 类新增可选成员 | 类名：global； API声明： 差异内容：NA | 类名：StartOptions； API声明：hideStartWindow?: boolean; 差异内容：hideStartWindow?: boolean; | api/@ohos.app.ability.StartOptions.d.ts |
| 类新增可选成员 | 类名：global； API声明： 差异内容：NA | 类名：StartOptions； API声明：windowCreateParams?: window.WindowCreateParams; 差异内容：windowCreateParams?: window.WindowCreateParams; | api/@ohos.app.ability.StartOptions.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：ApplicationInfo； API声明：readonly cloudStructuredDataSyncEnabled?: boolean; 差异内容：readonly cloudStructuredDataSyncEnabled?: boolean; | api/bundleManager/ApplicationInfo.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class AbilityStageContext 差异内容：export default class AbilityStageContext | 类名：global； API声明：declare class AbilityStageContext 差异内容：NA | api/application/AbilityStageContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class ApplicationContext 差异内容：export default class ApplicationContext | 类名：global； API声明：declare class ApplicationContext 差异内容：NA | api/application/ApplicationContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class ExtensionContext 差异内容：export default class ExtensionContext | 类名：global； API声明：declare class ExtensionContext 差异内容：NA | api/application/ExtensionContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class UIAbilityContext 差异内容：export default class UIAbilityContext | 类名：global； API声明：declare class UIAbilityContext 差异内容：NA | api/application/UIAbilityContext.d.ts |
| 删除导出符号 | 类名：global； API声明：export default class UIExtensionContext 差异内容：export default class UIExtensionContext | 类名：global； API声明：declare class UIExtensionContext 差异内容：NA | api/application/UIExtensionContext.d.ts |
