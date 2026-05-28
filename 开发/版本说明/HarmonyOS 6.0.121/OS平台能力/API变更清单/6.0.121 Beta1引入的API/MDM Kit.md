# MDM Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mdmkit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：applicationManager； API声明：function addDisallowedRunningBundlesSync(admin: Want, appIds: Array&lt;string&gt;, accountId?: number): void; 差异内容：NA | 类名：applicationManager； API声明：function addDisallowedRunningBundlesSync(admin: Want, appIds: Array&lt;string&gt;, accountId?: number): void; 差异内容：9200010 | api/@ohos.enterprise.applicationManager.d.ts |
| 新增错误码 | 类名：restrictions； API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void; 差异内容：NA | 类名：restrictions； API声明：function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void; 差异内容：9200013 | api/@ohos.enterprise.restrictions.d.ts |
| 函数变更 | 类名：restrictions； API声明：function getDisallowedPolicy(admin: Want, feature: string): boolean; 差异内容：admin: Want | 类名：restrictions； API声明：function getDisallowedPolicy(admin: Want \| null, feature: string): boolean; 差异内容：admin: Want \| null | api/@ohos.enterprise.restrictions.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function addAllowedRunningBundles(admin: Want, appIdentifiers: Array&lt;string&gt;, accountId: number): void; 差异内容：function addAllowedRunningBundles(admin: Want, appIdentifiers: Array&lt;string&gt;, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array&lt;string&gt;, accountId: number): void; 差异内容：function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array&lt;string&gt;, accountId: number): void; | api/@ohos.enterprise.applicationManager.d.ts |
| 新增API | NA | 类名：applicationManager； API声明：function getAllowedRunningBundles(admin: Want, accountId: number): Array&lt;string&gt;; 差异内容：function getAllowedRunningBundles(admin: Want, accountId: number): Array&lt;string&gt;; | api/@ohos.enterprise.applicationManager.d.ts |
