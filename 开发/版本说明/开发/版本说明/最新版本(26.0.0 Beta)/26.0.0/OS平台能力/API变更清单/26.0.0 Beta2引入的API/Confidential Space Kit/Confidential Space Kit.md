# Confidential Space Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-confidentialspacekit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace confidentialSpace 差异内容：declare namespace confidentialSpace | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace； API声明：interface DataAppErrorInfo 差异内容：interface DataAppErrorInfo | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppErrorInfo； API声明：readonly dataAppErrorCode: number; 差异内容：readonly dataAppErrorCode: number; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace； API声明：class DataAppHandle 差异内容：class DataAppHandle | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public stop(): void; 差异内容：public stop(): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public sendData(data: Uint8Array): Promise&lt;void&gt;; 差异内容：public sendData(data: Uint8Array): Promise&lt;void&gt;; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public onReceiveData(callback: Callback&lt;Uint8Array&gt;): void; 差异内容：public onReceiveData(callback: Callback&lt;Uint8Array&gt;): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public offReceiveData(callback?: Callback&lt;Uint8Array&gt;): void; 差异内容：public offReceiveData(callback?: Callback&lt;Uint8Array&gt;): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public onReceiveDataError(callback: ErrorCallback<BusinessError&lt;DataAppErrorInfo&gt;>): void; 差异内容：public onReceiveDataError(callback: ErrorCallback<BusinessError&lt;DataAppErrorInfo&gt;>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle； API声明：public offReceiveDataError(callback?: ErrorCallback<BusinessError&lt;DataAppErrorInfo&gt;>): void; 差异内容：public offReceiveDataError(callback?: ErrorCallback<BusinessError&lt;DataAppErrorInfo&gt;>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace； API声明：function runApp(appPath: string, argv: string[]): Promise&lt;DataAppHandle&gt;; 差异内容：function runApp(appPath: string, argv: string[]): Promise&lt;DataAppHandle&gt;; | api/@hms.security.confidentialSpace.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.security.confidentialSpace.d.ts 差异内容：ConfidentialSpaceKit | api/@hms.security.confidentialSpace.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：kits@kit.ConfidentialSpaceKit.d.ts 差异内容：ConfidentialSpaceKit | kits/@kit.ConfidentialSpaceKit.d.ts |
