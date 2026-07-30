# Multimodal Awareness Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20] | api/@ohos.multimodalAwareness.motion.d.ts |
