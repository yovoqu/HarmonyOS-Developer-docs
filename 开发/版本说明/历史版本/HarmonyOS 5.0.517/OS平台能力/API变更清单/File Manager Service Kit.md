# File Manager Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-filemanagerservicekit-5051

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace fileManagerService 差异内容：declare namespace fileManagerService | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService； API声明：function deleteToTrash(uri: string): Promise&lt;string&gt;; 差异内容：function deleteToTrash(uri: string): Promise&lt;string&gt;; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService； API声明：function getFileIconSync(fileType: string): string \| Resource; 差异内容：function getFileIconSync(fileType: string): string \| Resource; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增API | NA | 类名：fileManagerService； API声明：function getFileIcon(fileType: string): Promise<string \| Resource>; 差异内容：function getFileIcon(fileType: string): Promise<string \| Resource>; | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.filemanagement.fileManagerService.d.ts 差异内容：FileManagerServiceKit | api/@hms.filemanagement.fileManagerService.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：kits@kit.FileManagerServiceKit.d.ts 差异内容：FileManagerServiceKit | kits/@kit.FileManagerServiceKit.d.ts |
