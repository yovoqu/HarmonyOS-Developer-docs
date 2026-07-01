# Data Protection Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-dataprotectionkit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：DlpConnPlugin； API声明：connectServer(requestId: string, requestData: string, callback: Callback&lt;string&gt;): void; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE | 类名：DlpConnPlugin； API声明：connectServer(requestId: string, requestData: string, callback: Callback&lt;string&gt;): void; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager； API声明：static registerPlugin(plugin: DlpConnPlugin): number; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE | 类名：DlpConnManager； API声明：static registerPlugin(plugin: DlpConnPlugin): number; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 权限变更 | 类名：DlpConnManager； API声明：static unregisterPlugin(): void; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE | 类名：DlpConnManager； API声明：static unregisterPlugin(): void; 差异内容：ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE[since 26.0.0] | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：CustomProperty； API声明：options?: DlpFileQueryOptions; 差异内容：options?: DlpFileQueryOptions; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function queryOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<Array&lt;string&gt;>; 差异内容：function queryOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise<Array&lt;string&gt;>; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise&lt;void&gt;; 差异内容：function closeOpenedEnterpriseDlpFiles(options?: DlpFileQueryOptions): Promise&lt;void&gt;; | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：dlpPermission； API声明：export interface DlpFileQueryOptions 差异内容：export interface DlpFileQueryOptions | api/@ohos.dlpPermission.d.ts |
| 新增API | NA | 类名：DlpFileQueryOptions； API声明：classificationLabel?: string; 差异内容：classificationLabel?: string; | api/@ohos.dlpPermission.d.ts |
