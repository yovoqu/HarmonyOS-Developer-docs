# Core File Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-6001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：OperationMode； API声明：CREATE_MODE = 0b100 差异内容：CREATE_MODE = 0b100 | api/@ohos.fileshare.d.ts |
| 新增API | NA | 类名：OperationMode； API声明：DELETE_MODE = 0b1000 差异内容：DELETE_MODE = 0b1000 | api/@ohos.fileshare.d.ts |
| 新增API | NA | 类名：OperationMode； API声明：RENAME_MODE = 0b10000 差异内容：RENAME_MODE = 0b10000 | api/@ohos.fileshare.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function createStream(path: string, mode: string): Promise<Stream>; 差异内容：NA | 类名：global； API声明：declare function createStream(path: string, mode: string): Promise<Stream>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void; 差异内容：NA | 类名：global； API声明：declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function createStreamSync(path: string, mode: string): Stream; 差异内容：NA | 类名：global； API声明：declare function createStreamSync(path: string, mode: string): Stream; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function fdopenStream(fd: number, mode: string): Promise<Stream>; 差异内容：NA | 类名：global； API声明：declare function fdopenStream(fd: number, mode: string): Promise<Stream>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void; 差异内容：NA | 类名：global； API声明：declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare function fdopenStreamSync(fd: number, mode: string): Stream; 差异内容：NA | 类名：global； API声明：declare function fdopenStreamSync(fd: number, mode: string): Stream; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare interface Stream 差异内容：NA | 类名：global； API声明：declare interface Stream 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：close(): Promise<void>; 差异内容：NA | 类名：Stream； API声明：close(): Promise<void>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：close(callback: AsyncCallback<void>): void; 差异内容：NA | 类名：Stream； API声明：close(callback: AsyncCallback<void>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：closeSync(): void; 差异内容：NA | 类名：Stream； API声明：closeSync(): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：flush(): Promise<void>; 差异内容：NA | 类名：Stream； API声明：flush(): Promise<void>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：flush(callback: AsyncCallback<void>): void; 差异内容：NA | 类名：Stream； API声明：flush(callback: AsyncCallback<void>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：flushSync(): void; 差异内容：NA | 类名：Stream； API声明：flushSync(): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, options?: WriteOptions): Promise<number>; 差异内容：NA | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, options?: WriteOptions): Promise<number>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, callback: AsyncCallback<number>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, options: WriteOptions, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：Stream； API声明：write(buffer: ArrayBuffer \| string, options: WriteOptions, callback: AsyncCallback<number>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：writeSync(buffer: ArrayBuffer \| string, options?: WriteOptions): number; 差异内容：NA | 类名：Stream； API声明：writeSync(buffer: ArrayBuffer \| string, options?: WriteOptions): number; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>; 差异内容：NA | 类名：Stream； API声明：read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：Stream； API声明：read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void; 差异内容：NA | 类名：Stream； API声明：read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
| API从不支持元服务到支持元服务 | 类名：Stream； API声明：readSync(buffer: ArrayBuffer, options?: ReadOptions): number; 差异内容：NA | 类名：Stream； API声明：readSync(buffer: ArrayBuffer, options?: ReadOptions): number; 差异内容：atomicservice | api/@ohos.file.fs.d.ts |
