# Enterprise Data Guard Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-5111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SecurityLevel； API声明：DEFAULT = -1 差异内容：DEFAULT = -1 | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：openFileWrite(path: string): Promise&lt;number&gt;; 差异内容：openFileWrite(path: string): Promise&lt;number&gt;; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：openFileWrite(path: string, callback: AsyncCallback&lt;number&gt;): void; 差异内容：openFileWrite(path: string, callback: AsyncCallback&lt;number&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：setFileCustomTag(path: string, tagList: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; 差异内容：setFileCustomTag(path: string, tagList: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：setFileCustomTag(path: string, tagList: Array&lt;string&gt;): Promise&lt;void&gt;; 差异内容：setFileCustomTag(path: string, tagList: Array&lt;string&gt;): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：unsetFileCustomTag(path: string, tagList: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; 差异内容：unsetFileCustomTag(path: string, tagList: Array&lt;string&gt;, callback: AsyncCallback&lt;void&gt;): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：FileGuard； API声明：unsetFileCustomTag(path: string, tagList: Array&lt;string&gt;): Promise&lt;void&gt;; 差异内容：unsetFileCustomTag(path: string, tagList: Array&lt;string&gt;): Promise&lt;void&gt;; | api/@hms.pcService.fileGuard.d.ts |
