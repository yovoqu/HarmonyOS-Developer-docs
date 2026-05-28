# ArkData

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：KVManager； API声明：closeKVStore(appId: string, storeId: string): Promise&lt;void&gt;; 差异内容：NA | 类名：KVManager； API声明：closeKVStore(appId: string, storeId: string, kvConfig?: Options): Promise&lt;void&gt;; 差异内容：kvConfig?: Options | api/@ohos.data.distributedKVStore.d.ts |
| 函数变更 | 类名：KVManager； API声明：deleteKVStore(appId: string, storeId: string): Promise&lt;void&gt;; 差异内容：NA | 类名：KVManager； API声明：deleteKVStore(appId: string, storeId: string, kvConfig?: Options): Promise&lt;void&gt;; 差异内容：kvConfig?: Options | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：Options； API声明：rootDir?: string; 差异内容：rootDir?: string; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：distributedKVStore； API声明：interface BackupConfig 差异内容：interface BackupConfig | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：BackupConfig； API声明：fileName: string; 差异内容：fileName: string; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：BackupConfig； API声明：filePath: string; 差异内容：filePath: string; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：SingleKVStore； API声明：backupEx(backupConfig: BackupConfig): Promise&lt;void&gt;; 差异内容：backupEx(backupConfig: BackupConfig): Promise&lt;void&gt;; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：SingleKVStore； API声明：restoreEx(backupConfig: BackupConfig): Promise&lt;void&gt;; 差异内容：restoreEx(backupConfig: BackupConfig): Promise&lt;void&gt;; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：SingleKVStore； API声明：deleteBackupEx(backupConfig: BackupConfig): Promise&lt;void&gt;; 差异内容：deleteBackupEx(backupConfig: BackupConfig): Promise&lt;void&gt;; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明：function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore; 差异内容：function getRdbStoreSync(context: Context, config: StoreConfig): RdbStore; | api/@ohos.data.relationalStore.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemDefinedAppItem； API声明：get appIconId(): string; 差异内容：NA | 类名：SystemDefinedAppItem； API声明：get appIconId(): string; 差异内容：atomicservice | api/@ohos.data.unifiedDataChannel.d.ts |
| API从不支持元服务到支持元服务 | 类名：SystemDefinedAppItem； API声明：get appLabelId(): string; 差异内容：NA | 类名：SystemDefinedAppItem； API声明：get appLabelId(): string; 差异内容：atomicservice | api/@ohos.data.unifiedDataChannel.d.ts |
