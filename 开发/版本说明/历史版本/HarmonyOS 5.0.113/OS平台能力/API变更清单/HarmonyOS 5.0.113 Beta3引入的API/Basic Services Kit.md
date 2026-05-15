# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：settings； API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>; 差异内容：201 | 类名：settings； API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>; 差异内容：NA | api/@ohos.settings.d.ts |
| 错误码变更 | 类名：settings； API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean; 差异内容：201 | 类名：settings； API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean; 差异内容：NA | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：deviceInfo； API声明：const distributionOSApiName: string; 差异内容：const distributionOSApiName: string; | api/@ohos.deviceInfo.d.ts |
| 新增API | NA | 类名：pasteboard； API声明： enum Pattern 差异内容： enum Pattern | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern； API声明：URL = 0 差异内容：URL = 0 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern； API声明：NUMBER = 1 差异内容：NUMBER = 1 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：Pattern； API声明：EMAIL_ADDRESS = 2 差异内容：EMAIL_ADDRESS = 2 | api/@ohos.pasteboard.d.ts |
| 新增API | NA | 类名：SystemPasteboard； API声明：detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>; 差异内容：detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>; | api/@ohos.pasteboard.d.ts |
