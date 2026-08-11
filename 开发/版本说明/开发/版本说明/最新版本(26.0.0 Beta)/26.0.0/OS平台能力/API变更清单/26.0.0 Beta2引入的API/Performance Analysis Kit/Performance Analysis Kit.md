# Performance Analysis Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：hilog； API声明：function setOutputType(type: OutputType): OutputType; 差异内容：function setOutputType(type: OutputType): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function setOutputTypeByDomainID(type: OutputType, domainIDs: Array&lt;number&gt;, isExclude: boolean): OutputType; 差异内容：function setOutputTypeByDomainID(type: OutputType, domainIDs: Array&lt;number&gt;, isExclude: boolean): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function getOutputType(): OutputType; 差异内容：function getOutputType(): OutputType; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function getOutputDir(): string; 差异内容：function getOutputDir(): string; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function clean(): void; 差异内容：function clean(): void; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function flush(): void; 差异内容：function flush(): void; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：function getLogFile(latestSeconds: number): Array&lt;string&gt;; 差异内容：function getLogFile(latestSeconds: number): Array&lt;string&gt;; | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：hilog； API声明：enum OutputType 差异内容：enum OutputType | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：CONSOLE_ONLY = 0 差异内容：CONSOLE_ONLY = 0 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：PRIVATE_SANDBOX_ONLY = 1 差异内容：PRIVATE_SANDBOX_ONLY = 1 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：SHARE_SANDBOX_ONLY = 2 差异内容：SHARE_SANDBOX_ONLY = 2 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：PRIVATE_SANDBOX_WITH_CONSOLE = 3 差异内容：PRIVATE_SANDBOX_WITH_CONSOLE = 3 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：OutputType； API声明：SHARE_SANDBOX_WITH_CONSOLE = 4 差异内容：SHARE_SANDBOX_WITH_CONSOLE = 4 | api/@ohos.hilog.d.ts |
| 新增API | NA | 类名：AppCrashPolicy； API声明：collectMinidump?: boolean; 差异内容：collectMinidump?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：ResourceOverlimitPolicy； API声明：useRefinedLogFileName?: boolean; 差异内容：useRefinedLogFileName?: boolean; | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
