# Share Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare； API声明：function on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; 差异内容：function on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; 差异内容：function off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface UpdatedData 差异内容：interface UpdatedData | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：UpdatedData； API声明：thumbnailUri?: string; 差异内容：thumbnailUri?: string; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：enum ReceivableErrorCode 差异内容：enum ReceivableErrorCode | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceivableErrorCode； API声明：NO_RECEIVABLE_ERROR = 1 差异内容：NO_RECEIVABLE_ERROR = 1 | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：SharableTarget； API声明：updateShareData(data: UpdatedData): Promise<void>; 差异内容：updateShareData(data: UpdatedData): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选或必选方法 | 类名：global； API声明： 差异内容：NA | 类名：ReceivableTarget； API声明：reject(error: ReceivableErrorCode): Promise<void>; 差异内容：reject(error: ReceivableErrorCode): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：SendCapabilityRegistry； API声明：sendOnly?: boolean; 差异内容：sendOnly?: boolean; | api/@hms.collaboration.harmonyShare.d.ts |
