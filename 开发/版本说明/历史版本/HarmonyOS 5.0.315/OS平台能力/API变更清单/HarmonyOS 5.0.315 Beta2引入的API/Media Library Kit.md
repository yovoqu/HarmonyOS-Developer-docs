# Media Library Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PickerController； API声明：replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback&lt;void&gt;): void; 差异内容：replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback&lt;void&gt;): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController； API声明：saveTrustedPhotoAssets(trustedUris: Array&lt;string&gt;, callback: AsyncCallback<Array&lt;string&gt;>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void; 差异内容：saveTrustedPhotoAssets(trustedUris: Array&lt;string&gt;, callback: AsyncCallback<Array&lt;string&gt;>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global； API声明： export declare enum SaveMode 差异内容： export declare enum SaveMode | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SaveMode； API声明：SAVE_AS = 0 差异内容：SAVE_AS = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SaveMode； API声明：OVERWRITE = 1 差异内容：OVERWRITE = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
