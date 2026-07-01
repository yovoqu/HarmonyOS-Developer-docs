# Screen Time Guard Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-7001

## Screen Time Guard Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：SYSCAP_UNSUPPORTED_STRATEGY_TYPE = 1019000011 差异内容：SYSCAP_UNSUPPORTED_STRATEGY_TYPE = 1019000011 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：interface GuardStrategyData 差异内容：interface GuardStrategyData | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：GuardStrategyData； API声明：usageDuration: number; 差异内容：usageDuration: number; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：guardService； API声明：function queryGuardStrategyData(strategyName: string): Promise&lt;GuardStrategyData&gt;; 差异内容：function queryGuardStrategyData(strategyName: string): Promise&lt;GuardStrategyData&gt;; | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
