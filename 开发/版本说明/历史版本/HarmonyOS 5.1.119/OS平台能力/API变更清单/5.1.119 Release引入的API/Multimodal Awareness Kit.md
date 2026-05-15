# Multimodal Awareness Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-5112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global； API声明：declare namespace motion 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：global； API声明：declare namespace motion 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion； API声明：export enum OperatingHandStatus 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion； API声明：export enum OperatingHandStatus 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus； API声明：UNKNOWN_STATUS = 0 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus； API声明：UNKNOWN_STATUS = 0 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus； API声明：LEFT_HAND_OPERATED = 1 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus； API声明：LEFT_HAND_OPERATED = 1 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：OperatingHandStatus； API声明：RIGHT_HAND_OPERATED = 2 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：OperatingHandStatus； API声明：RIGHT_HAND_OPERATED = 2 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void; 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void; 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void; 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void; 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
| syscap变更 | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：SystemCapability.MultimodalAwarness.Motion | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：SystemCapability.MultimodalAwareness.Motion | api/@ohos.multimodalAwareness.motion.d.ts |
