# Multimodal Awareness Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION | 类名：motion； API声明：function on(type: 'operatingHandChanged', callback: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION | 类名：motion； API声明：function off(type: 'operatingHandChanged', callback?: Callback&lt;OperatingHandStatus&gt;): void; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 权限变更 | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：ohos.permission.ACTIVITY_MOTION | 类名：motion； API声明：function getRecentOperatingHandStatus(): OperatingHandStatus; 差异内容：ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace userStatus 差异内容：declare namespace userStatus | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus； API声明：export interface UserClassification 差异内容：export interface UserClassification | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserClassification； API声明：ageGroup?: UserAgeGroup; 差异内容：ageGroup?: UserAgeGroup; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserClassification； API声明：confidence?: float; 差异内容：confidence?: float; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus； API声明：export enum UserAgeGroup 差异内容：export enum UserAgeGroup | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserAgeGroup； API声明：OTHERS = 0 差异内容：OTHERS = 0 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：UserAgeGroup； API声明：CHILD = 1 差异内容：CHILD = 1 | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus； API声明：function on(type: 'userAgeGroupDetected', callback: Callback&lt;UserClassification&gt;): void; 差异内容：function on(type: 'userAgeGroupDetected', callback: Callback&lt;UserClassification&gt;): void; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：userStatus； API声明：function off(type: 'userAgeGroupDetected', callback?: Callback&lt;UserClassification&gt;): void; 差异内容：function off(type: 'userAgeGroupDetected', callback?: Callback&lt;UserClassification&gt;): void; | api/@ohos.multimodalAwareness.userStatus.d.ts |
| 新增API | NA | 类名：motion； API声明：export enum HoldingHandStatus 差异内容：export enum HoldingHandStatus | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus； API声明：NOT_HELD = 0 差异内容：NOT_HELD = 0 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus； API声明：LEFT_HAND_HELD = 1 差异内容：LEFT_HAND_HELD = 1 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus； API声明：RIGHT_HAND_HELD = 2 差异内容：RIGHT_HAND_HELD = 2 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus； API声明：BOTH_HANDS_HELD = 3 差异内容：BOTH_HANDS_HELD = 3 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：HoldingHandStatus； API声明：UNKNOWN_STATUS = 16 差异内容：UNKNOWN_STATUS = 16 | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion； API声明：function on(type: 'holdingHandChanged', callback: Callback&lt;HoldingHandStatus&gt;): void; 差异内容：function on(type: 'holdingHandChanged', callback: Callback&lt;HoldingHandStatus&gt;): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增API | NA | 类名：motion； API声明：function off(type: 'holdingHandChanged', callback?: Callback&lt;HoldingHandStatus&gt;): void; 差异内容：function off(type: 'holdingHandChanged', callback?: Callback&lt;HoldingHandStatus&gt;): void; | api/@ohos.multimodalAwareness.motion.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.multimodalAwareness.userStatus.d.ts 差异内容：MultimodalAwarenessKit | api/@ohos.multimodalAwareness.userStatus.d.ts |
