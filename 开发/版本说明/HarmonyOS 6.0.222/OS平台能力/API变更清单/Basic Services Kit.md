# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：settings； API声明：function setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean; 差异内容：ohos.permission.MANAGE_SECURE_SETTINGS | 类名：settings； API声明：function setValueSync(dataAbilityHelper: DataAbilityHelper, name: string, value: string): boolean; 差异内容：ohos.permission.MANAGE_SETTINGS | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：emitter； API声明：export class Emitter 差异内容：export class Emitter | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：on(eventId: string, callback: Callback&lt;EventData&gt;): void; 差异内容：on(eventId: string, callback: Callback&lt;EventData&gt;): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：on&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; 差异内容：on&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：once(eventId: string, callback: Callback&lt;EventData&gt;): void; 差异内容：once(eventId: string, callback: Callback&lt;EventData&gt;): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：once&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; 差异内容：once&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：off(eventId: string): void; 差异内容：off(eventId: string): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：off(eventId: string, callback: Callback&lt;EventData&gt;): void; 差异内容：off(eventId: string, callback: Callback&lt;EventData&gt;): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：off&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; 差异内容：off&lt;T&gt;(eventId: string, callback: Callback<GenericEventData&lt;T&gt;>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：emit(eventId: string, data?: EventData): void; 差异内容：emit(eventId: string, data?: EventData): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：emit&lt;T&gt;(eventId: string, data?: GenericEventData&lt;T&gt;): void; 差异内容：emit&lt;T&gt;(eventId: string, data?: GenericEventData&lt;T&gt;): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：emit(eventId: string, options: Options, data?: EventData): void; 差异内容：emit(eventId: string, options: Options, data?: EventData): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：emit&lt;T&gt;(eventId: string, options: Options, data?: GenericEventData&lt;T&gt;): void; 差异内容：emit&lt;T&gt;(eventId: string, options: Options, data?: GenericEventData&lt;T&gt;): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：Emitter； API声明：getListenerCount(eventId: string): number; 差异内容：getListenerCount(eventId: string): number; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：pasteboard； API声明：type UpdateCallback = () => void; 差异内容：type UpdateCallback = () => void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard； API声明：onRemoteUpdate(callback: UpdateCallback): void; 差异内容：onRemoteUpdate(callback: UpdateCallback): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard； API声明：offRemoteUpdate(callback?: UpdateCallback): void; 差异内容：offRemoteUpdate(callback?: UpdateCallback): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Notification； API声明：wantAgent?: WantAgent; 差异内容：wantAgent?: WantAgent; | api/@ohos.request.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.annotation.d.ets 差异内容：BasicServicesKit | api/@ohos.annotation.d.ets |
