# Media Library Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-5031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：MediaAssetManager； API声明：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler&lt;boolean&gt;): Promise&lt;string&gt;; 差异内容：14000011,201,401 | 类名：MediaAssetManager； API声明：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler&lt;boolean&gt;): Promise&lt;string&gt;; 差异内容：14000011,201,401,801 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明： enum CompatibleMode 差异内容： enum CompatibleMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompatibleMode； API声明：ORIGINAL_FORMAT_MODE = 0 差异内容：ORIGINAL_FORMAT_MODE = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompatibleMode； API声明：COMPATIBLE_FORMAT_MODE = 1 差异内容：COMPATIBLE_FORMAT_MODE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper； API声明： interface MediaAssetProgressHandler 差异内容： interface MediaAssetProgressHandler | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetProgressHandler； API声明：onProgress(progress: number): void; 差异内容：onProgress(progress: number): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RequestOptions； API声明：compatibleMode?: CompatibleMode; 差异内容：compatibleMode?: CompatibleMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RequestOptions； API声明：mediaAssetProgressHandler?: MediaAssetProgressHandler; 差异内容：mediaAssetProgressHandler?: MediaAssetProgressHandler; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest； API声明：setOrientation(orientation: number): void; 差异内容：setOrientation(orientation: number): void; | api/@ohos.file.photoAccessHelper.d.ts |
