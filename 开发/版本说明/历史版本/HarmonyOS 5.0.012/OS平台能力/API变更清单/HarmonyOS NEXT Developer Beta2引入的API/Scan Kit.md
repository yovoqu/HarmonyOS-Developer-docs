# Scan Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scankit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, callback: AsyncCallback&lt;ScanResult&gt;): void; 差异内容：1000500001,401 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, callback: AsyncCallback&lt;ScanResult&gt;): void; 差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 错误码变更 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback&lt;ScanResult&gt;): void; 差异内容：1000500001,401 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback&lt;ScanResult&gt;): void; 差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 错误码变更 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, options?: ScanOptions): Promise&lt;ScanResult&gt;; 差异内容：1000500001,401 | 类名：scanBarcode； API声明：function startScanForResult(context: common.Context, options?: ScanOptions): Promise&lt;ScanResult&gt;; 差异内容：1000500001,1000500002,401 | api/@hms.core.scan.scanBarcode.d.ts |
| 新增API | NA | 类名：generateBarcode； API声明：function createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>; 差异内容：function createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>; | api/@hms.core.scan.generateBarcode.d.ts |
| 新增API | NA | 类名：customScan； API声明：function rescan(): void; 差异内容：function rescan(): void; | api/@hms.core.scan.customScan.d.ts |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_SERVICE_CANCELED = 1000500002 差异内容：SCAN_SERVICE_CANCELED = 1000500002 | api/@hms.core.scan.scanCore.d.ts |
