# ArkData

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：cloudData； API声明：enum AutoSyncTriggerMode 差异内容：enum AutoSyncTriggerMode | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode； API声明：ACCOUNT_LOGIN = 0 差异内容：ACCOUNT_LOGIN = 0 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode； API声明：CLOUD_SWITCH_ON = 1 差异内容：CLOUD_SWITCH_ON = 1 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode； API声明：NETWORK_RECOVER = 2 差异内容：NETWORK_RECOVER = 2 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode； API声明：CLOUD_DATA_CHANGE = 3 差异内容：CLOUD_DATA_CHANGE = 3 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerMode； API声明：USER_CHANGE = 4 差异内容：USER_CHANGE = 4 | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData； API声明：interface AutoSyncTriggerInfo 差异内容：interface AutoSyncTriggerInfo | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：AutoSyncTriggerInfo； API声明：mode: AutoSyncTriggerMode; 差异内容：mode: AutoSyncTriggerMode; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData； API声明：function onAutoSyncTrigger(observer: Callback&lt;AutoSyncTriggerInfo&gt;): void; 差异内容：function onAutoSyncTrigger(observer: Callback&lt;AutoSyncTriggerInfo&gt;): void; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：cloudData； API声明：function offAutoSyncTrigger(observer?: Callback&lt;AutoSyncTriggerInfo&gt;): void; 差异内容：function offAutoSyncTrigger(observer?: Callback&lt;AutoSyncTriggerInfo&gt;): void; | api/@ohos.data.cloudData.d.ts |
| 新增API | NA | 类名：dataShare； API声明：enum DataProxyMaxValueLength 差异内容：enum DataProxyMaxValueLength | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyMaxValueLength； API声明：MAX_LENGTH_4K = 4096 差异内容：MAX_LENGTH_4K = 4096 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyMaxValueLength； API声明：MAX_LENGTH_100K = 102400 差异内容：MAX_LENGTH_100K = 102400 | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyConfig； API声明：maxValueLength?: DataProxyMaxValueLength; 差异内容：maxValueLength?: DataProxyMaxValueLength; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle； API声明：deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>; 差异内容：deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：SingleKVStore； API声明：rekey(): Promise&lt;void&gt;; 差异内容：rekey(): Promise&lt;void&gt;; | api/@ohos.data.distributedKVStore.d.ts |
| 新增API | NA | 类名：AssetStatus； API声明：ASSET_TO_DOWNLOAD 差异内容：ASSET_TO_DOWNLOAD | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressCode； API声明：STOP_CLOUD_SYNC = 8 差异内容：STOP_CLOUD_SYNC = 8 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProgressDetails； API声明：message?: string; 差异内容：message?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明：enum AssetConflictPolicy 差异内容：enum AssetConflictPolicy | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy； API声明：CONFLICT_POLICY_DEFAULT = 0 差异内容：CONFLICT_POLICY_DEFAULT = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy； API声明：CONFLICT_POLICY_TIME_FIRST = 1 差异内容：CONFLICT_POLICY_TIME_FIRST = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：AssetConflictPolicy； API声明：CONFLICT_POLICY_TEMP_PATH = 2 差异内容：CONFLICT_POLICY_TEMP_PATH = 2 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig； API声明：assetConflictPolicy?: AssetConflictPolicy; 差异内容：assetConflictPolicy?: AssetConflictPolicy; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig； API声明：assetTempPath?: string; 差异内容：assetTempPath?: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig； API声明：assetDownloadOnDemand?: boolean; 差异内容：assetDownloadOnDemand?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：DistributedConfig； API声明：autoSyncSwitch?: boolean; 差异内容：autoSyncSwitch?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明：interface CloudSyncConfig 差异内容：interface CloudSyncConfig | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig； API声明：mode: SyncMode; 差异内容：mode: SyncMode; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig； API声明：enablePredicate?: boolean; 差异内容：enablePredicate?: boolean; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：CloudSyncConfig； API声明：predicate?: RdbPredicates; 差异内容：predicate?: RdbPredicates; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明：enum SyncResultCode 差异内容：enum SyncResultCode | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：SUCCESS = 0 差异内容：SUCCESS = 0 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：FAIL = 1 差异内容：FAIL = 1 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：OFFLINE = 2 差异内容：OFFLINE = 2 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：INVALID_ARGS = 3 差异内容：INVALID_ARGS = 3 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：DISTRIBUTED_TABLE_NOT_SET = 4 差异内容：DISTRIBUTED_TABLE_NOT_SET = 4 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：TABLE_FIELD_MISMATCH = 5 差异内容：TABLE_FIELD_MISMATCH = 5 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：DISTRIBUTED_SCHEMA_MISMATCH = 6 差异内容：DISTRIBUTED_SCHEMA_MISMATCH = 6 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：BUSY = 7 差异内容：BUSY = 7 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：CORRUPTED = 8 差异内容：CORRUPTED = 8 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：TIMEOUT = 9 差异内容：TIMEOUT = 9 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：SCHEMA_CHANGED = 10 差异内容：SCHEMA_CHANGED = 10 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResultCode； API声明：CONSTRAINT_VIOLATION = 11 差异内容：CONSTRAINT_VIOLATION = 11 | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：relationalStore； API声明：interface SyncResult 差异内容：interface SyncResult | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult； API声明：readonly device: string; 差异内容：readonly device: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult； API声明：readonly code: SyncResultCode; 差异内容：readonly code: SyncResultCode; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：SyncResult； API声明：readonly message: string; 差异内容：readonly message: string; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array&lt;SyncResult&gt;>; 差异内容：syncEx(mode: SyncMode, predicates: RdbPredicates): Promise<Array&lt;SyncResult&gt;>; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：cloudSyncEx(config: CloudSyncConfig, progress: Callback&lt;ProgressDetails&gt;): Promise&lt;void&gt;; 差异内容：cloudSyncEx(config: CloudSyncConfig, progress: Callback&lt;ProgressDetails&gt;): Promise&lt;void&gt;; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：stopCloudSync(): Promise&lt;void&gt;; 差异内容：stopCloudSync(): Promise&lt;void&gt;; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：unifiedDataChannel； API声明：export const enum UriPermission 差异内容：export const enum UriPermission | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission； API声明：NONE = 0 差异内容：NONE = 0 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission； API声明：READ = 1 差异内容：READ = 1 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission； API声明：WRITE = 2 差异内容：WRITE = 2 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UriPermission； API声明：PERSIST = 3 差异内容：PERSIST = 3 | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：UnifiedDataProperties； API声明：uriAuthorizationPolicies?: Array&lt;UriPermission&gt;; 差异内容：uriAuthorizationPolicies?: Array&lt;UriPermission&gt;; | api/@ohos.data.unifiedDataChannel.d.ts |
| 新增API | NA | 类名：HTML； API声明：uriAuthorizationPolicies?: Array&lt;number&gt;; 差异内容：uriAuthorizationPolicies?: Array&lt;number&gt;; | api/@ohos.data.uniformDataStruct.d.ts |
| 新增API | NA | 类名：FileUri； API声明：uriAuthorizationPolicies?: Array&lt;number&gt;; 差异内容：uriAuthorizationPolicies?: Array&lt;number&gt;; | api/@ohos.data.uniformDataStruct.d.ts |
