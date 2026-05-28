# Distributed Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-distributedservicekit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace linkEnhance 差异内容：declare namespace linkEnhance | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance； API声明：interface ConnectResult 差异内容：interface ConnectResult | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：deviceId: string; 差异内容：deviceId: string; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：success: boolean; 差异内容：success: boolean; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：ConnectResult； API声明：reason: number; 差异内容：reason: number; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance； API声明：interface Server 差异内容：interface Server | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：start(): void; 差异内容：start(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：stop(): void; 差异内容：stop(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：close(): void; 差异内容：close(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：on(type: 'connectionAccepted', callback: Callback&lt;Connection&gt;): void; 差异内容：on(type: 'connectionAccepted', callback: Callback&lt;Connection&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：off(type: 'connectionAccepted', callback?: Callback&lt;Connection&gt;): void; 差异内容：off(type: 'connectionAccepted', callback?: Callback&lt;Connection&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：on(type: 'serverStopped', callback: Callback&lt;number&gt;): void; 差异内容：on(type: 'serverStopped', callback: Callback&lt;number&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Server； API声明：off(type: 'serverStopped', callback?: Callback&lt;number&gt;): void; 差异内容：off(type: 'serverStopped', callback?: Callback&lt;number&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance； API声明：function createServer(name: string): Server; 差异内容：function createServer(name: string): Server; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance； API声明：interface Connection 差异内容：interface Connection | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：connect(): void; 差异内容：connect(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：disconnect(): void; 差异内容：disconnect(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：close(): void; 差异内容：close(): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：getPeerDeviceId(): string; 差异内容：getPeerDeviceId(): string; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：sendData(data: ArrayBuffer): void; 差异内容：sendData(data: ArrayBuffer): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：on(type: 'connectResult', callback: Callback&lt;ConnectResult&gt;): void; 差异内容：on(type: 'connectResult', callback: Callback&lt;ConnectResult&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：off(type: 'connectResult', callback?: Callback&lt;ConnectResult&gt;): void; 差异内容：off(type: 'connectResult', callback?: Callback&lt;ConnectResult&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：on(type: 'disconnected', callback: Callback&lt;number&gt;): void; 差异内容：on(type: 'disconnected', callback: Callback&lt;number&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：off(type: 'disconnected', callback?: Callback&lt;number&gt;): void; 差异内容：off(type: 'disconnected', callback?: Callback&lt;number&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：on(type: 'dataReceived', callback: Callback&lt;ArrayBuffer&gt;): void; 差异内容：on(type: 'dataReceived', callback: Callback&lt;ArrayBuffer&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：Connection； API声明：off(type: 'dataReceived', callback?: Callback&lt;ArrayBuffer&gt;): void; 差异内容：off(type: 'dataReceived', callback?: Callback&lt;ArrayBuffer&gt;): void; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增API | NA | 类名：linkEnhance； API声明：function createConnection(deviceId: string, name: string): Connection; 差异内容：function createConnection(deviceId: string, name: string): Connection; | api/@ohos.distributedsched.linkEnhance.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.distributedsched.linkEnhance.d.ts 差异内容：DistributedServiceKit | api/@ohos.distributedsched.linkEnhance.d.ts |
