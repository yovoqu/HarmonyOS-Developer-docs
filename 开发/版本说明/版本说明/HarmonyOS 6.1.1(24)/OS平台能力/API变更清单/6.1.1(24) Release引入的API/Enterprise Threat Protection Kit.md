# Enterprise Threat Protection Kit

更新时间：2026-05-26 06:42:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisethreatprotectionkit-6112

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：virusRemediation； API声明：function isolateThreatFile(path: string): Promise&lt;string&gt;; 差异内容：NA | 类名：virusRemediation； API声明：function isolateThreatFile(path: string): Promise&lt;string&gt;; 差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation； API声明：function restoreIsolatedFile(id: string): Promise&lt;string&gt;; 差异内容：NA | 类名：virusRemediation； API声明：function restoreIsolatedFile(id: string): Promise&lt;string&gt;; 差异内容：1023801001,1023802003,1023803001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation； API声明：function removeIsolatedFile(id: string): Promise&lt;void&gt;; 差异内容：NA | 类名：virusRemediation； API声明：function removeIsolatedFile(id: string): Promise&lt;void&gt;; 差异内容：1023801001,1023803001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation； API声明：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void; 差异内容：NA | 类名：virusRemediation； API声明：function queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void; 差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation； API声明：function openFile(path: string): Promise&lt;number&gt;; 差异内容：NA | 类名：virusRemediation； API声明：function openFile(path: string): Promise&lt;number&gt;; 差异内容：1023801001,1023803001,1023804001 | api/@hms.pcService.virusRemediation.d.ts |
| 新增错误码 | 类名：virusRemediation； API声明：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void; 差异内容：NA | 类名：virusRemediation； API声明：function scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void; 差异内容：1023801001 | api/@hms.pcService.virusRemediation.d.ts |
