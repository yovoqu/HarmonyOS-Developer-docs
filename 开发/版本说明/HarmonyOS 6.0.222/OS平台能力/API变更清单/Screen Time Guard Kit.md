# Screen Time Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：appPicker； API声明：function startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>; 差异内容：function startAppForm(context: common.Context, appSelection: guardService.AppInfo, appSubTitle: string, displayTrustApp: boolean): Promise<void>; | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
| 新增API | NA | 类名：GuardServiceErrorCode； API声明：INVALID_PARAM = 1019000009 差异内容：INVALID_PARAM = 1019000009 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
| 新增API | NA | 类名：TimeStrategyType； API声明：INCLUSIVE_DURATION_TYPE = 3 差异内容：INCLUSIVE_DURATION_TYPE = 3 | api/@hms.utilityApplication.screenTimeGuard.guardService.d.ts |
