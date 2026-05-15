# ArkTS

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b060

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：TextDecoder； API声明：decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string; 差异内容：NA | 类名：TextDecoder； API声明：decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string; 差异内容：12 | api/@ohos.util.d.ts |
| 错误码变更 | 类名：taskpool； API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>; 差异内容：10200028,10200051,401 | 类名：taskpool； API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>; 差异内容：10200006,10200014,10200028,10200051,401 | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：util； API声明： interface DecodeToStringOptions 差异内容： interface DecodeToStringOptions | api/@ohos.util.d.ts |
| 新增API | NA | 类名：DecodeToStringOptions； API声明：stream?: boolean; 差异内容：stream?: boolean; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：TextDecoder； API声明：decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string; 差异内容：decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：utils； API声明：function isSendable(value: Object \| null \| undefined): boolean; 差异内容：function isSendable(value: Object \| null \| undefined): boolean; | arkts/@arkts.utils.d.ets |
