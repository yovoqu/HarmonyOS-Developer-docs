# IME Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：InputMethodSetting； API声明：getInputMethodState(): Promise<EnabledState>; 差异内容：getInputMethodState(): Promise<EnabledState>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController； API声明：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; 差异内容：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController； API声明：recvMessage(msgHandler?: MessageHandler): void; 差异内容：recvMessage(msgHandler?: MessageHandler): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod； API声明： export enum EnabledState 差异内容： export enum EnabledState | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState； API声明：DISABLED = 0 差异内容：DISABLED = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState； API声明：BASIC_MODE 差异内容：BASIC_MODE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：EnabledState； API声明：FULL_EXPERIENCE_MODE 差异内容：FULL_EXPERIENCE_MODE | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod； API声明： interface MessageHandler 差异内容： interface MessageHandler | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：MessageHandler； API声明：onMessage(msgId: string, msgParam?: ArrayBuffer): void; 差异内容：onMessage(msgId: string, msgParam?: ArrayBuffer): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：MessageHandler； API声明：onTerminated(): void; 差异内容：onTerminated(): void; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputClient； API声明：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; 差异内容：sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputClient； API声明：recvMessage(msgHandler?: MessageHandler): void; 差异内容：recvMessage(msgHandler?: MessageHandler): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel； API声明：startMoving(): void; 差异内容：startMoving(): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel； API声明：getDisplayId(): Promise<number>; 差异内容：getDisplayId(): Promise<number>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel； API声明：getImmersiveMode(): ImmersiveMode; 差异内容：getImmersiveMode(): ImmersiveMode; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：PanelFlag； API声明：FLAG_CANDIDATE 差异内容：FLAG_CANDIDATE | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine； API声明： interface MessageHandler 差异内容： interface MessageHandler | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：MessageHandler； API声明：onMessage(msgId: string, msgParam?: ArrayBuffer): void; 差异内容：onMessage(msgId: string, msgParam?: ArrayBuffer): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：MessageHandler； API声明：onTerminated(): void; 差异内容：onTerminated(): void; | api/@ohos.inputMethodEngine.d.ts |
