# Network Boost Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-networkboostkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明： declare namespace netHandover 差异内容： declare namespace netHandover | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明：function on(type: 'handoverChange', callback: Callback&lt;HandoverInfo&gt;): void; 差异内容：function on(type: 'handoverChange', callback: Callback&lt;HandoverInfo&gt;): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明：function off(type: 'handoverChange', callback?: Callback&lt;HandoverInfo&gt;): void; 差异内容：function off(type: 'handoverChange', callback?: Callback&lt;HandoverInfo&gt;): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明：function setHandoverMode(mode: HandoverMode): void; 差异内容：function setHandoverMode(mode: HandoverMode): void; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： interface HandoverInfo 差异内容： interface HandoverInfo | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverInfo； API声明：readonly handoverStart?: HandoverStart; 差异内容：readonly handoverStart?: HandoverStart; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverInfo； API声明：readonly handoverComplete?: HandoverComplete; 差异内容：readonly handoverComplete?: HandoverComplete; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： interface HandoverStart 差异内容： interface HandoverStart | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverStart； API声明：expires: number; 差异内容：expires: number; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverStart； API声明：dataSpeedAction: DataSpeedAction; 差异内容：dataSpeedAction: DataSpeedAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： interface DataSpeedAction 差异内容： interface DataSpeedAction | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：DataSpeedAction； API声明：dataSpeedSimpleAction: netQuality.DataSpeedSimpleAction; 差异内容：dataSpeedSimpleAction: netQuality.DataSpeedSimpleAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：DataSpeedAction； API声明：linkUpBandwidth: netQuality.RateBps; 差异内容：linkUpBandwidth: netQuality.RateBps; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：DataSpeedAction； API声明：linkDownBandwidth: netQuality.RateBps; 差异内容：linkDownBandwidth: netQuality.RateBps; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： interface HandoverComplete 差异内容： interface HandoverComplete | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：result: ErrorResult; 差异内容：result: ErrorResult; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：handoverContinue: boolean; 差异内容：handoverContinue: boolean; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：oldPathLifetime: number; 差异内容：oldPathLifetime: number; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：oldDataSpeedAction: DataSpeedAction; 差异内容：oldDataSpeedAction: DataSpeedAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：pathTypeChanged: boolean; 差异内容：pathTypeChanged: boolean; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：newNetHandle?: connection.NetHandle; 差异内容：newNetHandle?: connection.NetHandle; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：reEstAction: ReEstAction; 差异内容：reEstAction: ReEstAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverComplete； API声明：newDataSpeedAction: DataSpeedAction; 差异内容：newDataSpeedAction: DataSpeedAction; | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： enum HandoverMode 差异内容： enum HandoverMode | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverMode； API声明：DELEGATION = 0 差异内容：DELEGATION = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：HandoverMode； API声明：DISCRETION = 1 差异内容：DISCRETION = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： enum ReEstAction 差异内容： enum ReEstAction | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ReEstAction； API声明：DEFAULT = 0 差异内容：DEFAULT = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ReEstAction； API声明：QUERY_DNS = 1 差异内容：QUERY_DNS = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ReEstAction； API声明：CHANGE_REMOTE_IP = 2 差异内容：CHANGE_REMOTE_IP = 2 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ReEstAction； API声明：CHANGE_IP_VERSION = 3 差异内容：CHANGE_IP_VERSION = 3 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ReEstAction； API声明：NO_EST = 4 差异内容：NO_EST = 4 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：netHandover； API声明： enum ErrorResult 差异内容： enum ErrorResult | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ErrorResult； API声明：ERROR_NONE = 0 差异内容：ERROR_NONE = 0 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ErrorResult； API声明：ERROR_HANDOVER_TIMEOUT = 1 差异内容：ERROR_HANDOVER_TIMEOUT = 1 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ErrorResult； API声明：ERROR_NEW_PATH_ACTIVATION_FAILED = 2 差异内容：ERROR_NEW_PATH_ACTIVATION_FAILED = 2 | api/@hms.networkboost.handover.d.ts |
| 新增API | NA | 类名：ErrorResult； API声明：ERROR_ABORT = 3 差异内容：ERROR_ABORT = 3 | api/@hms.networkboost.handover.d.ts |
