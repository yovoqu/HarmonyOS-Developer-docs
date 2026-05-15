# Ark Data

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkdata-b061

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace sendableRelationalStore 差异内容： declare namespace sendableRelationalStore | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明： interface Asset 差异内容： interface Asset | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：name: string; 差异内容：name: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：uri: string; 差异内容：uri: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：path: string; 差异内容：path: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：createTime: string; 差异内容：createTime: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：modifyTime: string; 差异内容：modifyTime: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：size: string; 差异内容：size: string; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：Asset； API声明：status?: number; 差异内容：status?: number; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：type Assets = collections.Array<Asset>; 差异内容：type Assets = collections.Array<Asset>; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：type ValueType = null \| number \| string \| boolean \| collections.Uint8Array \| Asset \| Assets \| collections.Float32Array \| bigint; 差异内容：type ValueType = null \| number \| string \| boolean \| collections.Uint8Array \| Asset \| Assets \| collections.Float32Array \| bigint; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：type ValuesBucket = collections.Map<string, ValueType>; 差异内容：type ValuesBucket = collections.Map<string, ValueType>; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：type NonSendableBucket = relationalStore.ValuesBucket; 差异内容：type NonSendableBucket = relationalStore.ValuesBucket; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：type NonSendableAsset = relationalStore.Asset; 差异内容：type NonSendableAsset = relationalStore.Asset; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket; 差异内容：function fromSendableValuesBucket(valuesBucket: ValuesBucket): NonSendableBucket; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket; 差异内容：function toSendableValuesBucket(valuesBucket: NonSendableBucket): ValuesBucket; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：function fromSendableAsset(asset: Asset): NonSendableAsset; 差异内容：function fromSendableAsset(asset: Asset): NonSendableAsset; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：sendableRelationalStore； API声明：function toSendableAsset(asset: NonSendableAsset): Asset; 差异内容：function toSendableAsset(asset: NonSendableAsset): Asset; | api/@ohos.data.sendableRelationalStore.d.ets |
| 新增API | NA | 类名：RdbStore； API声明：insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number; 差异内容：insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number; | api/@ohos.data.relationalStore.d.ts |
| 新增API | NA | 类名：ResultSet； API声明：getSendableRow(): sendableRelationalStore.ValuesBucket; 差异内容：getSendableRow(): sendableRelationalStore.ValuesBucket; | api/@ohos.data.relationalStore.d.ts |
