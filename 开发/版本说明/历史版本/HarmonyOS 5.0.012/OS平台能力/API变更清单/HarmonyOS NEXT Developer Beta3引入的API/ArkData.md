# ArkData

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：14800014,202,401,801 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>; 差异内容：14800014,202,401,801 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>; 差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：14800014,202,401,801 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 错误码变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>; 差异内容：14800014,202,401,801 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>; 差异内容：14800014,401,801 | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD_DETAILS 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD_DETAILS 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType； API声明：DATA_CHANGE 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：ChangeType； API声明：DATA_CHANGE 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType； API声明：ASSET_CHANGE 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：ChangeType； API声明：ASSET_CHANGE 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType； API声明：DISTRIBUTED_CLOUD 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：DistributedType； API声明：DISTRIBUTED_CLOUD 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>; 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void; 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：RdbStore； API声明：cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>; 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：StoreConfig； API声明：pluginLibs?: Array<string>; 差异内容：pluginLibs?: Array<string>; | api/@ohos.data.relationalStore.d.ts |
