# Core File Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Environment； API声明：function getUserDownloadDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDownloadDir(): string; 差异内容：201 | api/@ohos.file.environment.d.ts |
| 新增错误码 | 类名：Environment； API声明：function getUserDesktopDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDesktopDir(): string; 差异内容：201 | api/@ohos.file.environment.d.ts |
| 新增错误码 | 类名：Environment； API声明：function getUserDocumentDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDocumentDir(): string; 差异内容：201 | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment； API声明：function getUserDownloadDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDownloadDir(): string; 差异内容：ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment； API声明：function getUserDesktopDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDesktopDir(): string; 差异内容：ohos.permission.READ_WRITE_DESKTOP_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 权限变更 | 类名：Environment； API声明：function getUserDocumentDir(): string; 差异内容：NA | 类名：Environment； API声明：function getUserDocumentDir(): string; 差异内容：ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY [since 11 - 11] | api/@ohos.file.environment.d.ts |
| 新增API | NA | 类名：CloudFileCache； API声明：getCachedTotalSize(): Promise&lt;number&gt;; 差异内容：getCachedTotalSize(): Promise&lt;number&gt;; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：CloudFileCache； API声明：cleanAllFileCache(): Promise&lt;void&gt;; 差异内容：cleanAllFileCache(): Promise&lt;void&gt;; | api/@ohos.file.cloudSync.d.ts |
| 新增API | NA | 类名：global； API声明：declare function mmap(file: number \| File, mode: MappingMode, offset: number, size: number): Promise&lt;FileMapping&gt;; 差异内容：declare function mmap(file: number \| File, mode: MappingMode, offset: number, size: number): Promise&lt;FileMapping&gt;; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：declare function mmapSync(file: number \| File, mode: MappingMode, offset: number, size: number): FileMapping; 差异内容：declare function mmapSync(file: number \| File, mode: MappingMode, offset: number, size: number): FileMapping; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：declare interface FileMapping 差异内容：declare interface FileMapping | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：setPosition(position: number): void; 差异内容：setPosition(position: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：getPosition(): number; 差异内容：getPosition(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：capacity(): number; 差异内容：capacity(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：setLimit(limit: number): void; 差异内容：setLimit(limit: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：getLimit(): number; 差异内容：getLimit(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：flip(): void; 差异内容：flip(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：remaining(): number; 差异内容：remaining(): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：read(buffer: ArrayBuffer, length?: number): number; 差异内容：read(buffer: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：read(position: number, buffer: ArrayBuffer, length?: number): number; 差异内容：read(position: number, buffer: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：write(data: ArrayBuffer, length?: number): number; 差异内容：write(data: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：write(position: number, data: ArrayBuffer, length?: number): number; 差异内容：write(position: number, data: ArrayBuffer, length?: number): number; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：msync(): Promise&lt;void&gt;; 差异内容：msync(): Promise&lt;void&gt;; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：msync(position: number, length: number): Promise&lt;void&gt;; 差异内容：msync(position: number, length: number): Promise&lt;void&gt;; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：msyncSync(): void; 差异内容：msyncSync(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：msyncSync(position: number, length: number): void; 差异内容：msyncSync(position: number, length: number): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：unmap(): Promise&lt;void&gt;; 差异内容：unmap(): Promise&lt;void&gt;; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：FileMapping； API声明：unmapSync(): void; 差异内容：unmapSync(): void; | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：global； API声明：declare enum MappingMode 差异内容：declare enum MappingMode | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode； API声明：READ_ONLY = 0 差异内容：READ_ONLY = 0 | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode； API声明：READ_WRITE = 1 差异内容：READ_WRITE = 1 | api/@ohos.file.fs.d.ts |
| 新增API | NA | 类名：MappingMode； API声明：PRIVATE = 2 差异内容：PRIVATE = 2 | api/@ohos.file.fs.d.ts |
