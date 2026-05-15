# Push Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pushService； API声明：function on(type: 'distributedMessageReceive', callee: Callee, callback: DistributedMessageCallback): void; 差异内容：function on(type: 'distributedMessageReceive', callee: Callee, callback: DistributedMessageCallback): void; | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService； API声明：function off(type: 'distributedMessageReceive', callback?: DistributedMessageCallback): void; 差异内容：function off(type: 'distributedMessageReceive', callback?: DistributedMessageCallback): void; | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService； API声明：type DistributedMessageCallback = (PushPayload: pushCommon.PushPayload) => Promise<DistributedMessageResult>; 差异内容：type DistributedMessageCallback = (PushPayload: pushCommon.PushPayload) => Promise<DistributedMessageResult>; | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService； API声明：interface DistributedMessageResult 差异内容：interface DistributedMessageResult | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：DistributedMessageResult； API声明：resultCode: ResultCode; 差异内容：resultCode: ResultCode; | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService； API声明：enum ResultCode 差异内容：enum ResultCode | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：ResultCode； API声明：SUCCESS = 0 差异内容：SUCCESS = 0 | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：ResultCode； API声明：FAILED = 1 差异内容：FAILED = 1 | api/@hms.core.push.pushService.d.ts |
