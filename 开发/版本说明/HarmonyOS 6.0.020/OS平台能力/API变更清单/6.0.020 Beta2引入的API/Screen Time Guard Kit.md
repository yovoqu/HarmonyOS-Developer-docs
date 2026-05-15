# Screen Time Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-screentimeguardkit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：appPicker； API声明：function startAppPicker(context: common.Context, appSelection: AppInfo): Promise<string[]>; 差异内容：appSelection: AppInfo | 类名：appPicker； API声明：function startAppPicker(context: common.Context, appSelection: guardService.AppInfo): Promise<string[]>; 差异内容：appSelection: guardService.AppInfo | api/@hms.utilityApplication.screenTimeGuard.appPicker.d.ts |
