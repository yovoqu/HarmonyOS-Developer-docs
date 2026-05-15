# Performance Analysis Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：hiAppEvent； API声明：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>; 差异内容：NA | 类名：hiAppEvent； API声明：function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>; 差异内容：11100001,11101001,11101002,11101004,11101005 | api/@ohos.hiviewdfx.hiAppEvent.d.ts |
| 新增API | NA | 类名：hidebug； API声明：function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>; 差异内容：function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug； API声明：function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo; 差异内容：function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug； API声明：enum JsRawHeapTrimLevel 差异内容：enum JsRawHeapTrimLevel | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：JsRawHeapTrimLevel； API声明：TRIM_LEVEL_1 = 0 差异内容：TRIM_LEVEL_1 = 0 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：JsRawHeapTrimLevel； API声明：TRIM_LEVEL_2 = 1 差异内容：TRIM_LEVEL_2 = 1 | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug； API声明：function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void; 差异内容：function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：jsLeakWatcher； API声明：function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void; 差异内容：function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
