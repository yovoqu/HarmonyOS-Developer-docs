# Scan Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scankit-b123sp18

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：customScan； API声明：function init(options?: scanBarcode.ScanOptions): void; 差异内容：1000500001,401 | 类名：customScan； API声明：function init(options?: scanBarcode.ScanOptions): void; 差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
| 错误码变更 | 类名：customScan； API声明：function start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback&lt;ScanFrame&gt;): void; 差异内容：1000500001,401 | 类名：customScan； API声明：function start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback&lt;ScanFrame&gt;): void; 差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
| 错误码变更 | 类名：customScan； API声明：function start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>; 差异内容：1000500001,401 | 类名：customScan； API声明：function start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>; 差异内容：1000500001,201,401 | api/@hms.core.scan.customScan.d.ts |
