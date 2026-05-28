# Call Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-callkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：voipCall； API声明：function reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise&lt;void&gt;; 差异内容：function reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise&lt;void&gt;; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallAttribute； API声明：isConferenceCall?: boolean; 差异内容：isConferenceCall?: boolean; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallAttribute； API声明：isVoiceAnswerSupported?: boolean; 差异内容：isVoiceAnswerSupported?: boolean; | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallState； API声明：VOIP_CALL_STATE_ANSWERED = 6 差异内容：VOIP_CALL_STATE_ANSWERED = 6 | api/@hms.telephony.voipCall.d.ts |
| 新增API | NA | 类名：VoipCallState； API声明：VOIP_CALL_STATE_DISCONNECTING = 7 差异内容：VOIP_CALL_STATE_DISCONNECTING = 7 | api/@hms.telephony.voipCall.d.ts |
