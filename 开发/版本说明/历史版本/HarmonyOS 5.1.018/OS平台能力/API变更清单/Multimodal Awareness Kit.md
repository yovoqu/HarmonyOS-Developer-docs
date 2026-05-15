# Multimodal Awareness Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-multimodalawarenesskit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace deviceStatus 差异内容：declare namespace deviceStatus | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：deviceStatus； API声明：export enum SteadyStandingStatus 差异内容：export enum SteadyStandingStatus | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：SteadyStandingStatus； API声明：STATUS_EXIT = 0 差异内容：STATUS_EXIT = 0 | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：SteadyStandingStatus； API声明：STATUS_ENTER = 1 差异内容：STATUS_ENTER = 1 | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：deviceStatus； API声明：function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void; 差异内容：function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void; | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：deviceStatus； API声明：function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void; 差异内容：function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void; | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace metadataBinding 差异内容：declare namespace metadataBinding | api/@ohos.multimodalAwareness.metadataBinding.d.ts |
| 新增API | NA | 类名：metadataBinding； API声明：function submitMetadata(metadata: string): void; 差异内容：function submitMetadata(metadata: string): void; | api/@ohos.multimodalAwareness.metadataBinding.d.ts |
| 新增API | NA | 类名：metadataBinding； API声明：function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void; 差异内容：function on(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void; | api/@ohos.multimodalAwareness.metadataBinding.d.ts |
| 新增API | NA | 类名：metadataBinding； API声明：function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void; 差异内容：function off(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void; | api/@ohos.multimodalAwareness.metadataBinding.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.multimodalAwareness.deviceStatus.d.ts 差异内容：MultimodalAwarenessKit | api/@ohos.multimodalAwareness.deviceStatus.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.multimodalAwareness.metadataBinding.d.ts 差异内容：MultimodalAwarenessKit | api/@ohos.multimodalAwareness.metadataBinding.d.ts |
