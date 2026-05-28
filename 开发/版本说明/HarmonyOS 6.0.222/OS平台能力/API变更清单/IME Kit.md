# IME Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：export type CustomValueType = number \| string \| boolean; 差异内容：export type CustomValueType = number \| string \| boolean; | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：global； API声明：export interface InputMethodExtraConfig 差异内容：export interface InputMethodExtraConfig | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：InputMethodExtraConfig； API声明：customSettings: Record<string, CustomValueType>; 差异内容：customSettings: Record<string, CustomValueType>; | api/@ohos.inputMethod.ExtraConfig.d.ts |
| 新增API | NA | 类名：inputMethod； API声明：function onAttachmentDidFail(callback: Callback&lt;AttachFailureReason&gt;): void; 差异内容：function onAttachmentDidFail(callback: Callback&lt;AttachFailureReason&gt;): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod； API声明：function offAttachmentDidFail(callback?: Callback&lt;AttachFailureReason&gt;): void; 差异内容：function offAttachmentDidFail(callback?: Callback&lt;AttachFailureReason&gt;): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod； API声明：export enum AttachFailureReason 差异内容：export enum AttachFailureReason | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason； API声明：CALLER_NOT_FOCUSED = 0 差异内容：CALLER_NOT_FOCUSED = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason； API声明：IME_ABNORMAL 差异内容：IME_ABNORMAL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachFailureReason； API声明：SERVICE_ABNORMAL 差异内容：SERVICE_ABNORMAL | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Panel； API声明：setSystemPanelButtonColor(fillColor: string \| undefined, backgroundColor: string \| undefined): Promise&lt;void&gt;; 差异内容：setSystemPanelButtonColor(fillColor: string \| undefined, backgroundColor: string \| undefined): Promise&lt;void&gt;; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EditorAttribute； API声明：readonly extraConfig?: InputMethodExtraConfig; 差异内容：readonly extraConfig?: InputMethodExtraConfig; | api/@ohos.inputMethodEngine.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.inputMethod.ExtraConfig.d.ts 差异内容：IMEKit | api/@ohos.inputMethod.ExtraConfig.d.ts |
