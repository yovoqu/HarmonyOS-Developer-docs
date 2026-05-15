# Cloud Foundation Kit

更新时间：2026-04-20 06:33:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-cloudfoundationkit-6101

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode): Promise<PrefetchResult>; 差异内容：NA | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode, params?: PrefetchParams): Promise<PrefetchResult>; 差异内容：params?: PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 函数变更 | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>): void; 差异内容：NA | 类名：cloudResPrefetch； API声明：function getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>, params?: PrefetchParams): void; 差异内容：params?: PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchMode； API声明：LINK_PREFETCH = 3 差异内容：LINK_PREFETCH = 3 | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：cloudResPrefetch； API声明：interface PrefetchParams 差异内容：interface PrefetchParams | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
| 新增API | NA | 类名：PrefetchParams； API声明：link?: string; 差异内容：link?: string; | api/@hms.core.deviceCloudGateway.cloudResPrefetch.d.ts |
