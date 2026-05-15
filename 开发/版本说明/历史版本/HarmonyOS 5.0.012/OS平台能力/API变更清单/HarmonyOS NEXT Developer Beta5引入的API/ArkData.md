# ArkData

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b060

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function insertData(options: Options, data: UnifiedData): Promise<string>; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function insertData(options: Options, data: UnifiedData): Promise<string>; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function updateData(options: Options, data: UnifiedData): Promise<void>; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function updateData(options: Options, data: UnifiedData): Promise<void>; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function queryData(options: Options): Promise<Array<UnifiedData>>; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function queryData(options: Options): Promise<Array<UnifiedData>>; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 错误码变更 | 类名：unifiedDataChannel； API声明：function deleteData(options: Options): Promise<Array<UnifiedData>>; 差异内容：201,401 | 类名：unifiedDataChannel； API声明：function deleteData(options: Options): Promise<Array<UnifiedData>>; 差异内容：401 | api/@ohos.data.unifiedDataChannel.d.ts |
| 权限变更 | 类名：relationalStore； API声明： enum SubscribeType 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：relationalStore； API声明： enum SubscribeType 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_REMOTE = 0 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：SubscribeType； API声明：SUBSCRIBE_TYPE_REMOTE = 0 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：relationalStore； API声明： enum DistributedType 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：relationalStore； API声明： enum DistributedType 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
| 权限变更 | 类名：DistributedType； API声明：DISTRIBUTED_DEVICE 差异内容：ohos.permission.DISTRIBUTED_DATASYNC | 类名：DistributedType； API声明：DISTRIBUTED_DEVICE 差异内容：NA | api/@ohos.data.relationalStore.d.ts |
