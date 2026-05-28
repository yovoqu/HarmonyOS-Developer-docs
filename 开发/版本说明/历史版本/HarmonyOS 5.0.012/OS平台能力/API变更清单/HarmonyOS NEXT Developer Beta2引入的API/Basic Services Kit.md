# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：RunningLock； API声明：hold(timeout: number): void; 差异内容：401,4900101 | 类名：RunningLock； API声明：hold(timeout: number): void; 差异内容：201,401,4900101 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：RunningLock； API声明：unhold(): void; 差异内容：4900101 | 类名：RunningLock； API声明：unhold(): void; 差异内容：201,4900101 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：runningLock； API声明：function create(name: string, type: RunningLockType, callback: AsyncCallback&lt;RunningLock&gt;): void; 差异内容：401 | 类名：runningLock； API声明：function create(name: string, type: RunningLockType, callback: AsyncCallback&lt;RunningLock&gt;): void; 差异内容：201,401 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：runningLock； API声明：function create(name: string, type: RunningLockType): Promise&lt;RunningLock&gt;; 差异内容：401 | 类名：runningLock； API声明：function create(name: string, type: RunningLockType): Promise&lt;RunningLock&gt;; 差异内容：201,401 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：SystemPasteboard； API声明：clear(callback: AsyncCallback&lt;void&gt;): void; 差异内容：401 | 类名：SystemPasteboard； API声明：clear(callback: AsyncCallback&lt;void&gt;): void; 差异内容：NA | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard； API声明：getPasteData(callback: AsyncCallback&lt;PasteData&gt;): void; 差异内容：401 | 类名：SystemPasteboard； API声明：getPasteData(callback: AsyncCallback&lt;PasteData&gt;): void; 差异内容：NA | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：settings； API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise&lt;boolean&gt;; 差异内容：201 | 类名：settings； API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise&lt;boolean&gt;; 差异内容：NA | api/@ohos.settings.d.ts |
| 错误码变更 | 类名：settings； API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean; 差异内容：201 | 类名：settings； API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean; 差异内容：NA | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：global； API声明： declare namespace customConfig 差异内容： declare namespace customConfig | api/@ohos.customization.customConfig.d.ts |
| 新增API | NA | 类名：customConfig； API声明：function getChannelId(): string; 差异内容：function getChannelId(): string; | api/@ohos.customization.customConfig.d.ts |
| 新增API | NA | 类名：batteryInfo； API声明：const nowCurrent: number; 差异内容：const nowCurrent: number; | api/@ohos.batteryInfo.d.ts |
| 新增API | NA | 类名：Support； API声明：COMMON_EVENT_DATA_SHARE_READY = 'usual.event.DATA_SHARE_READY' 差异内容：COMMON_EVENT_DATA_SHARE_READY = 'usual.event.DATA_SHARE_READY' | api/@ohos.commonEventManager.d.ts |
