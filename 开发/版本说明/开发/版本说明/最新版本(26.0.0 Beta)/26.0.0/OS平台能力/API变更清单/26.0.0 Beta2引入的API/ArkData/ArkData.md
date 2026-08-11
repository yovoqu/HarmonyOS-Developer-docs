# ArkData

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：DataObject； API声明：setSessionId(callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：DataObject； API声明：setSessionId(callback: AsyncCallback&lt;void&gt;): void; 差异内容：201 | api/@ohos.data.distributedDataObject.d.ts |
| 删除错误码 | 类名：RdbStore； API声明：stopCloudSync(): Promise&lt;void&gt;; 差异内容：14800000 | 类名：RdbStore； API声明：stopCloudSync(): Promise&lt;void&gt;; 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DataObject； API声明：setSessionId(callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | 类名：DataObject； API声明：setSessionId(callback: AsyncCallback&lt;void&gt;): void; 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 9 - 19] | api/@ohos.data.distributedDataObject.d.ts |
| 权限变更 | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD = 1 差异内容：NA | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD = 1 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD_DETAILS = 2 差异内容：NA | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_CLOUD_DETAILS = 2 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType； API声明：DATA_CHANGE = 0 差异内容：NA | 类名：ChangeType； API声明：DATA_CHANGE = 0 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：ChangeType； API声明：ASSET_CHANGE = 1 差异内容：NA | 类名：ChangeType； API声明：ASSET_CHANGE = 1 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType； API声明：DISTRIBUTED_CLOUD = 1 差异内容：NA | 类名：DistributedType； API声明：DISTRIBUTED_CLOUD = 1 差异内容：ohos.permission.DISTRIBUTED_DATASYNC [since 10 - 11] | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：queryByStep(sql: string, bindArgs?: Array&lt;ValueType&gt;): Promise&lt;ResultSet&gt;; 差异内容：queryByStep(sql: string, bindArgs?: Array&lt;ValueType&gt;): Promise&lt;ResultSet&gt;; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：RdbStore； API声明：queryByStep(predicates: RdbPredicates, columns?: Array&lt;string&gt;): Promise&lt;ResultSet&gt;; 差异内容：queryByStep(predicates: RdbPredicates, columns?: Array&lt;string&gt;): Promise&lt;ResultSet&gt;; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ProxyData； API声明：isMultiValues?: boolean; 差异内容：isMultiValues?: boolean; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData； API声明：values?: Record<number, ValueType>; 差异内容：values?: Record<number, ValueType>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：ProxyData； API声明：trustProviders?: string[]; 差异内容：trustProviders?: string[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyChangeInfo； API声明：values?: ValueType[]; 差异内容：values?: ValueType[]; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle； API声明：putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise&lt;void&gt;; 差异内容：putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise&lt;void&gt;; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle； API声明：removeValue(uri: string, key: number, config: DataProxyConfig): Promise&lt;void&gt;; 差异内容：removeValue(uri: string, key: number, config: DataProxyConfig): Promise&lt;void&gt;; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：DataProxyHandle； API声明：getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>; 差异内容：getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>; | api/@ohos.data.dataShare.d.ts |
| 新增API | NA | 类名：intelligence； API声明：interface CloudModelInfo 差异内容：interface CloudModelInfo | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：CloudModelInfo； API声明：modelType: string; 差异内容：modelType: string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：CloudModelInfo； API声明：modelVersionCode?: string; 差异内容：modelVersionCode?: string; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence； API声明：enum NetworkPolicy 差异内容：enum NetworkPolicy | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：NetworkPolicy； API声明：WIFI_ONLY = 0 差异内容：WIFI_ONLY = 0 | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：NetworkPolicy； API声明：WIFI_AND_CELLULAR = 1 差异内容：WIFI_AND_CELLULAR = 1 | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig； API声明：modelInfo?: CloudModelInfo; 差异内容：modelInfo?: CloudModelInfo; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：ModelConfig； API声明：networkPolicy?: NetworkPolicy; 差异内容：networkPolicy?: NetworkPolicy; | api/@ohos.data.intelligence.d.ts |
| 新增API | NA | 类名：intelligence； API声明：function getSupportedCloudModel(): Promise<Array&lt;CloudModelInfo&gt;>; 差异内容：function getSupportedCloudModel(): Promise<Array&lt;CloudModelInfo&gt;>; | api/@ohos.data.intelligence.d.ts |
