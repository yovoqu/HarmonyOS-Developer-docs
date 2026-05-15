# Cloud Foundation Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cloudfoundationkit-5031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace cloudResPrefetch 差异内容： declare namespace cloudResPrefetch | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明：function registerPrefetchTask(options: PrefetchOptions): void; 差异内容：function registerPrefetchTask(options: PrefetchOptions): void; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>; 差异内容：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void; 差异内容：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明： interface PrefetchOptions 差异内容： interface PrefetchOptions | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchOptions； API声明：token?: string; 差异内容：token?: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchOptions； API声明：params?: string \| Object; 差异内容：params?: string \| Object; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明： enum PrefetchMode 差异内容： enum PrefetchMode | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode； API声明：INSTALL_PREFETCH = 1 差异内容：INSTALL_PREFETCH = 1 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode； API声明：PERIODIC_PREFETCH = 2 差异内容：PERIODIC_PREFETCH = 2 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明： interface PrefetchResult 差异内容： interface PrefetchResult | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult； API声明：result: string \| Object; 差异内容：result: string \| Object; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult； API声明：timestamp: Date; 差异内容：timestamp: Date; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchResult； API声明：token: string; 差异内容：token: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
