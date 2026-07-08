# Asset Store Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-assetstorekit-7001

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：asset； API声明：function batchAdd(attributesArray: Array&lt;AssetMap&gt;): Promise&lt;BatchResult&gt;; 差异内容：function batchAdd(attributesArray: Array&lt;AssetMap&gt;): Promise&lt;BatchResult&gt;; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset； API声明：function batchRemove(assetsToBeRemoved: Array&lt;AssetMap&gt;): Promise&lt;void&gt;; 差异内容：function batchRemove(assetsToBeRemoved: Array&lt;AssetMap&gt;): Promise&lt;void&gt;; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset； API声明：function batchUpdate(sourceAttributes: Array&lt;AssetMap&gt;, destAttributes: Array&lt;AssetMap&gt;): Promise&lt;BatchResult&gt;; 差异内容：function batchUpdate(sourceAttributes: Array&lt;AssetMap&gt;, destAttributes: Array&lt;AssetMap&gt;): Promise&lt;BatchResult&gt;; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset； API声明：interface BatchErrInfo 差异内容：interface BatchErrInfo | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo； API声明：index: number; 差异内容：index: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo； API声明：errCode: number; 差异内容：errCode: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchErrInfo； API声明：message: string; 差异内容：message: string; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：asset； API声明：interface BatchResult 差异内容：interface BatchResult | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchResult； API声明：failedCount: number; 差异内容：failedCount: number; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：BatchResult； API声明：failedErrorInfos: Array&lt;BatchErrInfo&gt;; 差异内容：failedErrorInfos: Array&lt;BatchErrInfo&gt;; | api/@ohos.security.asset.d.ts |
| 新增API | NA | 类名：ErrorCode； API声明：INCONSISTENT_ATTRIBUTE = 24000019 差异内容：INCONSISTENT_ATTRIBUTE = 24000019 | api/@ohos.security.asset.d.ts |
