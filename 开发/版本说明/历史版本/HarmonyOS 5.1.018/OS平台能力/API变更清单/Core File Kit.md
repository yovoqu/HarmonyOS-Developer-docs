# Core File Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corefilekit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：PhotoViewMIMETypes； API声明：IMAGE_TYPE = 'image/*' 差异内容：NA | 类名：PhotoViewMIMETypes； API声明：IMAGE_TYPE = 'image/*' 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewMIMETypes； API声明：VIDEO_TYPE = 'video/*' 差异内容：NA | 类名：PhotoViewMIMETypes； API声明：VIDEO_TYPE = 'video/*' 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoViewMIMETypes； API声明：IMAGE_VIDEO_TYPE = '/' 差异内容：NA | 类名：PhotoViewMIMETypes； API声明：IMAGE_VIDEO_TYPE = '/' 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectOptions； API声明：MIMEType?: PhotoViewMIMETypes; 差异内容：NA | 类名：PhotoSelectOptions； API声明：MIMEType?: PhotoViewMIMETypes; 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectOptions； API声明：maxSelectNumber?: number; 差异内容：NA | 类名：PhotoSelectOptions； API声明：maxSelectNumber?: number; 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectResult； API声明：photoUris: Array&lt;string&gt;; 差异内容：NA | 类名：PhotoSelectResult； API声明：photoUris: Array&lt;string&gt;; 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSelectResult； API声明：isOriginalPhoto: boolean; 差异内容：NA | 类名：PhotoSelectResult； API声明：isOriginalPhoto: boolean; 差异内容：18 | api/@ohos.file.picker.d.ts |
| API废弃版本变更 | 类名：PhotoSaveOptions； API声明：newFileNames?: Array&lt;string&gt;; 差异内容：NA | 类名：PhotoSaveOptions； API声明：newFileNames?: Array&lt;string&gt;; 差异内容：18 | api/@ohos.file.picker.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getTotalSize(callback: AsyncCallback&lt;number&gt;): void; 差异内容：9 | 类名：storageStatistics； API声明：function getTotalSize(callback: AsyncCallback&lt;number&gt;): void; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getTotalSize(): Promise&lt;number&gt;; 差异内容：9 | 类名：storageStatistics； API声明：function getTotalSize(): Promise&lt;number&gt;; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getTotalSizeSync(): number; 差异内容：10 | 类名：storageStatistics； API声明：function getTotalSizeSync(): number; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getFreeSize(callback: AsyncCallback&lt;number&gt;): void; 差异内容：9 | 类名：storageStatistics； API声明：function getFreeSize(callback: AsyncCallback&lt;number&gt;): void; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getFreeSize(): Promise&lt;number&gt;; 差异内容：9 | 类名：storageStatistics； API声明：function getFreeSize(): Promise&lt;number&gt;; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
| 起始版本有变化 | 类名：storageStatistics； API声明：function getFreeSizeSync(): number; 差异内容：10 | 类名：storageStatistics； API声明：function getFreeSizeSync(): number; 差异内容：15 | api/@ohos.file.storageStatistics.d.ts |
