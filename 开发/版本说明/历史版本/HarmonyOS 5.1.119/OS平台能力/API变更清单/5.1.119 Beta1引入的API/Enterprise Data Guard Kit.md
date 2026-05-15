# Enterprise Data Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SecurityLevel； API声明：DEFAULT = -1 差异内容：DEFAULT = -1 | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：openFileWrite(path: string): Promise<number>; 差异内容：openFileWrite(path: string): Promise<number>; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void; 差异内容：openFileWrite(path: string, callback: AsyncCallback<number>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; 差异内容：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>; 差异内容：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; 差异内容：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>; 差异内容：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
