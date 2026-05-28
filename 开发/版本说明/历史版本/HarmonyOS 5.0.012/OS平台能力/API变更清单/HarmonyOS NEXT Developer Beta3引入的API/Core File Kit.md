# Core File Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：BackupExtensionAbility； API声明：onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string \| Promise&lt;string&gt;; 差异内容：onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string \| Promise&lt;string&gt;; | api/@ohos.application.BackupExtensionAbility.d.ts |
| API废弃版本变更 | 类名：picker； API声明： export enum PhotoViewMIMETypes 差异内容：NA | 类名：picker； API声明： export enum PhotoViewMIMETypes 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSelectOptions 差异内容：NA | 类名：picker； API声明： class PhotoSelectOptions 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSelectResult 差异内容：NA | 类名：picker； API声明： class PhotoSelectResult 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoSaveOptions 差异内容：NA | 类名：picker； API声明： class PhotoSaveOptions 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：picker； API声明： class PhotoViewPicker 差异内容：NA | 类名：picker； API声明： class PhotoViewPicker 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(option?: PhotoSelectOptions): Promise&lt;PhotoSelectResult&gt;; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(option?: PhotoSelectOptions): Promise&lt;PhotoSelectResult&gt;; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：select(callback: AsyncCallback&lt;PhotoSelectResult&gt;): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：select(callback: AsyncCallback&lt;PhotoSelectResult&gt;): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(option?: PhotoSaveOptions): Promise<Array&lt;string&gt;>; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(option?: PhotoSaveOptions): Promise<Array&lt;string&gt;>; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(option: PhotoSaveOptions, callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(option: PhotoSaveOptions, callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewPicker； API声明：save(callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：NA | 类名：PhotoViewPicker； API声明：save(callback: AsyncCallback<Array&lt;string&gt;>): void; 差异内容：12 | api/@ohos.file.picker.d.ts |
