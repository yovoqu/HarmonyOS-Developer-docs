# Core File Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：BackupExtensionAbility； API声明：onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string \| Promise<string>; 差异内容：onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string \| Promise<string>; | api/@ohos.application.BackupExtensionAbility.d.ts |
| API废弃版本变更 | 类名：picker； API声明： export enum PhotoViewMIMETypes 差异内容：NA | 类名：picker； API声明： export enum PhotoViewMIMETypes 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSelectOptions 差异内容：NA | 类名：picker； API声明： class PhotoSelectOptions 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSelectResult 差异内容：NA | 类名：picker； API声明： class PhotoSelectResult 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSaveOptions 差异内容：NA | 类名：picker； API声明： class PhotoSaveOptions 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoViewPicker 差异内容：NA | 类名：picker； API声明： class PhotoViewPicker 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(callback: AsyncCallback<PhotoSelectResult>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(callback: AsyncCallback<PhotoSelectResult>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(option?: PhotoSaveOptions): Promise<Array<string>>; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(option?: PhotoSaveOptions): Promise<Array<string>>; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(callback: AsyncCallback<Array<string>>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(callback: AsyncCallback<Array<string>>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
