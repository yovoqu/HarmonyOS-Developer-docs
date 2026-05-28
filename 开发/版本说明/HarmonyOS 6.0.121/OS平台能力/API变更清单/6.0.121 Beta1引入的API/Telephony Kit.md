# Telephony Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-telephonykit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：call； API声明：export enum TelCallState 差异内容：export enum TelCallState | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_UNKNOWN = -1 差异内容：TEL_CALL_STATE_UNKNOWN = -1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_IDLE = 0 差异内容：TEL_CALL_STATE_IDLE = 0 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_RINGING = 1 差异内容：TEL_CALL_STATE_RINGING = 1 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_OFFHOOK = 2 差异内容：TEL_CALL_STATE_OFFHOOK = 2 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_ANSWERED = 3 差异内容：TEL_CALL_STATE_ANSWERED = 3 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：TelCallState； API声明：TEL_CALL_STATE_CONNECTED = 4 差异内容：TEL_CALL_STATE_CONNECTED = 4 | api/@ohos.telephony.call.d.ts |
| 新增API | NA | 类名：observer； API声明：type TelCallState = call.TelCallState; 差异内容：type TelCallState = call.TelCallState; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer； API声明：function on(type: 'callStateChangeEx', callback: Callback&lt;TelCallState&gt;, options?: ObserverOptions): void; 差异内容：function on(type: 'callStateChangeEx', callback: Callback&lt;TelCallState&gt;, options?: ObserverOptions): void; | api/@ohos.telephony.observer.d.ts |
| 新增API | NA | 类名：observer； API声明：function off(type: 'callStateChangeEx', callback?: Callback&lt;TelCallState&gt;): void; 差异内容：function off(type: 'callStateChangeEx', callback?: Callback&lt;TelCallState&gt;): void; | api/@ohos.telephony.observer.d.ts |
