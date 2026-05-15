# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：Support； API声明：COMMON_EVENT_ENTER_HIBERNATE = 'usual.event.ENTER_HIBERNATE' 差异内容：COMMON_EVENT_ENTER_HIBERNATE = 'usual.event.ENTER_HIBERNATE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support； API声明：COMMON_EVENT_EXIT_HIBERNATE = 'usual.event.EXIT_HIBERNATE' 差异内容：COMMON_EVENT_EXIT_HIBERNATE = 'usual.event.EXIT_HIBERNATE' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support； API声明：COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED = 'usual.event.MANAGED_BROWSER_POLICY_CHANGED' 差异内容：COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED = 'usual.event.MANAGED_BROWSER_POLICY_CHANGED' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：deviceInfo； API声明：const diskSN: string; 差异内容：const diskSN: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： enum FileConflictOptions 差异内容： enum FileConflictOptions | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：FileConflictOptions； API声明：OVERWRITE 差异内容：OVERWRITE | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：FileConflictOptions； API声明：SKIP 差异内容：SKIP | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： enum ProgressIndicator 差异内容： enum ProgressIndicator | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressIndicator； API声明：NONE 差异内容：NONE | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressIndicator； API声明：DEFAULT 差异内容：DEFAULT | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： interface ProgressInfo 差异内容： interface ProgressInfo | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressInfo； API声明：progress: number; 差异内容：progress: number; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard； API声明：type ProgressListener = (progress: ProgressInfo) => void; 差异内容：type ProgressListener = (progress: ProgressInfo) => void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： export class ProgressSignal 差异内容： export class ProgressSignal | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：ProgressSignal； API声明：cancel(): void; 差异内容：cancel(): void; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： interface GetDataParams 差异内容： interface GetDataParams | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams； API声明：destUri?: string; 差异内容：destUri?: string; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams； API声明：fileConflictOptions?: FileConflictOptions; 差异内容：fileConflictOptions?: FileConflictOptions; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams； API声明：progressIndicator: ProgressIndicator; 差异内容：progressIndicator: ProgressIndicator; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams； API声明：progressListener?: ProgressListener; 差异内容：progressListener?: ProgressListener; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：GetDataParams； API声明：progressSignal?: ProgressSignal; 差异内容：progressSignal?: ProgressSignal; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard； API声明：getDataWithProgress(params: GetDataParams): Promise<PasteData>; 差异内容：getDataWithProgress(params: GetDataParams): Promise<PasteData>; | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Config； API声明：multipart?: boolean; 差异内容：multipart?: boolean; | api/@ohos.request.d.ts |
