# Screen Time Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace appPicker 差异内容：declare namespace appPicker | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：appPicker； API声明：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>; 差异内容：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>; | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace guardService 差异内容：declare namespace guardService | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：enum GuardServiceErrorCode 差异内容：enum GuardServiceErrorCode | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：INTERNAL_ERROR = 1019000001 差异内容：INTERNAL_ERROR = 1019000001 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：USER_NOT_AUTHORIZED = 1019000002 差异内容：USER_NOT_AUTHORIZED = 1019000002 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：USER_CANCELED = 1019000003 差异内容：USER_CANCELED = 1019000003 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：STRATEGIES_EXCEED_LIMIT = 1019000004 差异内容：STRATEGIES_EXCEED_LIMIT = 1019000004 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：STRATEGY_NAME_ALREADY_EXIST = 1019000005 差异内容：STRATEGY_NAME_ALREADY_EXIST = 1019000005 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：NONEXISTENT_STRATEGY = 1019000006 差异内容：NONEXISTENT_STRATEGY = 1019000006 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：STRATEGY_ALREADY_EXECUTED = 1019000007 差异内容：STRATEGY_ALREADY_EXECUTED = 1019000007 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：STRATEGY_NOT_STARTED = 1019000008 差异内容：STRATEGY_NOT_STARTED = 1019000008 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：enum RestrictionType 差异内容：enum RestrictionType | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：RestrictionType； API声明：TRUSTLIST_TYPE = 1 差异内容：TRUSTLIST_TYPE = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：RestrictionType； API声明：BLOCKLIST_TYPE = 2 差异内容：BLOCKLIST_TYPE = 2 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：enum TimeStrategyType 差异内容：enum TimeStrategyType | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType； API声明：START_END_TIME_TYPE = 1 差异内容：START_END_TIME_TYPE = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType； API声明：TOTAL_DURATION_TYPE = 2 差异内容：TOTAL_DURATION_TYPE = 2 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：enum AuthStatus 差异内容：enum AuthStatus | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus； API声明：AUTH_INIT = -1 差异内容：AUTH_INIT = -1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus； API声明：AUTH_GRANTED = 0 差异内容：AUTH_GRANTED = 0 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AuthStatus； API声明：AUTH_DENIED = 1 差异内容：AUTH_DENIED = 1 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：interface AppInfo 差异内容：interface AppInfo | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：AppInfo； API声明：appTokens: string[]; 差异内容：appTokens: string[]; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：interface TimeStrategy 差异内容：interface TimeStrategy | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy； API声明：type: TimeStrategyType; 差异内容：type: TimeStrategyType; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy； API声明：startTime?: string; 差异内容：startTime?: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy； API声明：endTime?: string; 差异内容：endTime?: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy； API声明：totalDuration?: number; 差异内容：totalDuration?: number; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategy； API声明：repeat?: number[]; 差异内容：repeat?: number[]; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：interface GuardStrategy 差异内容：interface GuardStrategy | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy； API声明：name: string; 差异内容：name: string; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy； API声明：timeStrategy: TimeStrategy; 差异内容：timeStrategy: TimeStrategy; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy； API声明：appInfo: AppInfo; 差异内容：appInfo: AppInfo; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategy； API声明：appRestrictionType: RestrictionType; 差异内容：appRestrictionType: RestrictionType; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function requestUserAuth(context: common.UIAbilityContext): Promise&lt;void&gt;; 差异内容：function requestUserAuth(context: common.UIAbilityContext): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function revokeUserAuth(): Promise&lt;void&gt;; 差异内容：function revokeUserAuth(): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function getUserAuthStatus(): Promise&lt;AuthStatus&gt;; 差异内容：function getUserAuthStatus(): Promise&lt;AuthStatus&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function addGuardStrategy(guardStrategy: GuardStrategy): Promise&lt;void&gt;; 差异内容：function addGuardStrategy(guardStrategy: GuardStrategy): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise&lt;void&gt;; 差异内容：function updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function queryGuardStrategies(): Promise<GuardStrategy[]>; 差异内容：function queryGuardStrategies(): Promise<GuardStrategy[]>; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function removeGuardStrategy(strategyName: string): Promise&lt;void&gt;; 差异内容：function removeGuardStrategy(strategyName: string): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function startGuardStrategy(strategyName: string): Promise&lt;void&gt;; 差异内容：function startGuardStrategy(strategyName: string): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function stopGuardStrategy(strategyName: string): Promise&lt;void&gt;; 差异内容：function stopGuardStrategy(strategyName: string): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise&lt;void&gt;; 差异内容：function setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise&lt;void&gt;; 差异内容：function releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：global； API声明：export default class TimeGuardExtensionAbility 差异内容：export default class TimeGuardExtensionAbility | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility； API声明：context: TimeGuardExtensionContext; 差异内容：context: TimeGuardExtensionContext; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility； API声明：onStart(strategyName: string): Promise&lt;void&gt;; 差异内容：onStart(strategyName: string): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility； API声明：onStop(strategyName: string): Promise&lt;void&gt;; 差异内容：onStop(strategyName: string): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility； API声明：onUserAuthSwitchOn(): Promise&lt;void&gt;; 差异内容：onUserAuthSwitchOn(): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：TimeGuardExtensionAbility； API声明：onUserAuthSwitchOff(): Promise&lt;void&gt;; 差异内容：onUserAuthSwitchOff(): Promise&lt;void&gt;; | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增API | NA | 类名：global； API声明：export default class TimeGuardExtensionContext 差异内容：export default class TimeGuardExtensionContext | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.utilityApplication.screenTimeGuard.appPicker.d.ts 差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.utilityApplication.screenTimeGuard.guardService.d.ts 差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts 差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts 差异内容：ScreenTimeGuardKit | api/@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：kits@kit.ScreenTimeGuardKit.d.ts 差异内容：ScreenTimeGuardKit | kits/@kit.ScreenTimeGuardKit.d.ts |
