# Core File Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-7001

## Core File Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：OpenMode； API声明：const UNCACHE = 0o10000000000; 差异内容：const UNCACHE = 0o10000000000; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：declare function listFileExt(path: string, options?: ListFileExtOptions): Promise<string[]>; 差异内容：declare function listFileExt(path: string, options?: ListFileExtOptions): Promise<string[]>; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：declare function listFileExtSync(path: string, options?: ListFileExtOptions): string[]; 差异内容：declare function listFileExtSync(path: string, options?: ListFileExtOptions): string[]; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：export interface FileFilter 差异内容：export interface FileFilter | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileFilter； API声明：filter(name: string): boolean; 差异内容：filter(name: string): boolean; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：export interface ListFileExtOptions 差异内容：export interface ListFileExtOptions | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ListFileExtOptions； API声明：recursion?: boolean; 差异内容：recursion?: boolean; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ListFileExtOptions； API声明：listNum?: number; 差异内容：listNum?: number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：ListFileExtOptions； API声明：fileFilter?: FileFilter; 差异内容：fileFilter?: FileFilter; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：DocumentSelectOptions； API声明：allowsMulFolderSelection?: boolean; 差异内容：allowsMulFolderSelection?: boolean; | api/@ohos.file.picker.d.ts |
