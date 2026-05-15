# Share Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare； API声明：function on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; 差异内容：function on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; 差异内容：function off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：enum ShareResultCode 差异内容：enum ShareResultCode | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode； API声明：SHARE_SUCCESS = 0 差异内容：SHARE_SUCCESS = 0 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode； API声明：SEND_FAILED = 1 差异内容：SEND_FAILED = 1 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode； API声明：CANCEL_BY_SENDER = 2 差异内容：CANCEL_BY_SENDER = 2 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode； API声明：CANCEL_BY_RECEIVER = 3 差异内容：CANCEL_BY_RECEIVER = 3 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface TransferBaseResults 差异内容：interface TransferBaseResults | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：TransferBaseResults； API声明：onResult?: Callback<ShareResultCode>; 差异内容：onResult?: Callback<ShareResultCode>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface ReceiveCallback 差异内容：interface ReceiveCallback | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceiveCallback； API声明：onDataReceived: Callback<systemShare.SharedData>; 差异内容：onDataReceived: Callback<systemShare.SharedData>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface BaseCapabilityRegistry 差异内容：interface BaseCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：BaseCapabilityRegistry； API声明：windowId: number; 差异内容：windowId: number; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface RecvCapabilityRegistry 差异内容：interface RecvCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface SendCapabilityRegistry 差异内容：interface SendCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：interface ReceivableTarget 差异内容：interface ReceivableTarget | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceivableTarget； API声明：receive(receiveUri: string, callback: ReceiveCallback): Promise<void>; 差异内容：receive(receiveUri: string, callback: ReceiveCallback): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void; 差异内容：function on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void; 差异内容：function off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
