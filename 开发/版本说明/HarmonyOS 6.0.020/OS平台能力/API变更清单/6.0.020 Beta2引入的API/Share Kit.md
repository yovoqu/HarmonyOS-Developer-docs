# Share Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare； API声明：interface RecvCapability 差异内容：interface RecvCapability | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：RecvCapability； API声明：utd: string; 差异内容：utd: string; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：RecvCapability； API声明：maxSupportedCount: number; 差异内容：maxSupportedCount: number; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function on(event: 'gesturesShare', callback: Callback&lt;SharableTarget&gt;): void; 差异内容：function on(event: 'gesturesShare', callback: Callback&lt;SharableTarget&gt;): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare； API声明：function off(event: 'gesturesShare', callback?: Callback&lt;SharableTarget&gt;): void; 差异内容：function off(event: 'gesturesShare', callback?: Callback&lt;SharableTarget&gt;): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增必选属性 | 类名：global； API声明： 差异内容：NA | 类名：RecvCapabilityRegistry； API声明：capabilities: RecvCapability[]; 差异内容：capabilities: RecvCapability[]; | api/@hms.collaboration.harmonyShare.d.ts |
