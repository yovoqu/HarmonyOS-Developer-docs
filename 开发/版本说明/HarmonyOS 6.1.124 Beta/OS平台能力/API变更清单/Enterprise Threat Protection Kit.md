# Enterprise Threat Protection Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisethreatprotectionkit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace virusRemediation 差异内容：declare namespace virusRemediation | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：export enum ScanTargetType 差异内容：export enum ScanTargetType | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：ScanTargetType； API声明：BUNDLE = 0 差异内容：BUNDLE = 0 | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：ScanTargetType； API声明：SANDBOX = 1 差异内容：SANDBOX = 1 | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：export interface IsolatedFileInfo 差异内容：export interface IsolatedFileInfo | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：IsolatedFileInfo； API声明：id: string; 差异内容：id: string; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：IsolatedFileInfo； API声明：absolutePath: string; 差异内容：absolutePath: string; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：IsolatedFileInfo； API声明：size: number; 差异内容：size: number; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：IsolatedFileInfo； API声明：isolatedTime: number; 差异内容：isolatedTime: number; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：export interface ScanCallback 差异内容：export interface ScanCallback | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：ScanCallback； API声明：onReceive(paths: string[]): void; 差异内容：onReceive(paths: string[]): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：ScanCallback； API声明：onComplete(): void; 差异内容：onComplete(): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：ScanCallback； API声明：onError(code: number, message: string): void; 差异内容：onError(code: number, message: string): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：export interface QueryCallback 差异内容：export interface QueryCallback | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：QueryCallback； API声明：onQuery(files: IsolatedFileInfo[]): void; 差异内容：onQuery(files: IsolatedFileInfo[]): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：QueryCallback； API声明：onComplete(): void; 差异内容：onComplete(): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：QueryCallback； API声明：onError(code: number, message: string): void; 差异内容：onError(code: number, message: string): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function isolateThreatFile(path: string): Promise<string>; 差异内容：function isolateThreatFile(path: string): Promise<string>; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function restoreIsolatedFile(id: string): Promise<string>; 差异内容：function restoreIsolatedFile(id: string): Promise<string>; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function removeIsolatedFile(id: string): Promise<void>; 差异内容：function removeIsolatedFile(id: string): Promise<void>; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void; 差异内容：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function openFile(path: string): Promise<number>; 差异内容：function openFile(path: string): Promise<number>; | api/@hms.pcService.virusRemediation.d.ts |
| 新增API | NA | 类名：virusRemediation； API声明：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void; 差异内容：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void; | api/@hms.pcService.virusRemediation.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.pcService.virusRemediation.d.ts 差异内容：EnterpriseThreatProtectionKit | api/@hms.pcService.virusRemediation.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：kits@kit.EnterpriseThreatProtectionKit.d.ts 差异内容：EnterpriseThreatProtectionKit | kits/@kit.EnterpriseThreatProtectionKit.d.ts |
