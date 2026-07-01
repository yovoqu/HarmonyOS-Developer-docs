# Scan Kit

更新时间：2026-06-27 01:41:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-scankit-7001

## Scan Kit
 
 
| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：scanCore； API声明：function isDefaultScanSupported(): boolean; 差异内容：function isDefaultScanSupported(): boolean; | api/@hms.core.scan.scanCore.d.ts |
| 新增API | NA | 类名：scanCore； API声明：function isCustomScanSupported(): boolean; 差异内容：function isCustomScanSupported(): boolean; | api/@hms.core.scan.scanCore.d.ts |
| API从不支持元服务到支持元服务 | 类名：global； API声明：declare namespace detectBarcode 差异内容：NA | 类名：global； API声明：declare namespace detectBarcode 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：interface InputImage 差异内容：NA | 类名：detectBarcode； API声明：interface InputImage 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：InputImage； API声明：uri: string; 差异内容：NA | 类名：InputImage； API声明：uri: string; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void; 差异内容：NA | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void; 差异内容：NA | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>; 差异内容：NA | 类名：detectBarcode； API声明：function decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：interface ByteImage 差异内容：NA | 类名：detectBarcode； API声明：interface ByteImage 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ByteImage； API声明：byteBuffer: ArrayBuffer; 差异内容：NA | 类名：ByteImage； API声明：byteBuffer: ArrayBuffer; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ByteImage； API声明：width: number; 差异内容：NA | 类名：ByteImage； API声明：width: number; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ByteImage； API声明：height: number; 差异内容：NA | 类名：ByteImage； API声明：height: number; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ByteImage； API声明：format: ImageFormat; 差异内容：NA | 类名：ByteImage； API声明：format: ImageFormat; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：enum ImageFormat 差异内容：NA | 类名：detectBarcode； API声明：enum ImageFormat 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ImageFormat； API声明：NV21 = 0 差异内容：NA | 类名：ImageFormat； API声明：NV21 = 0 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：interface DetectResult 差异内容：NA | 类名：detectBarcode； API声明：interface DetectResult 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：DetectResult； API声明：scanResults: Array<scanBarcode.ScanResult>; 差异内容：NA | 类名：DetectResult； API声明：scanResults: Array<scanBarcode.ScanResult>; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：DetectResult； API声明：zoomValue: number; 差异内容：NA | 类名：DetectResult； API声明：zoomValue: number; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：detectBarcode； API声明：function decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise&lt;DetectResult&gt;; 差异内容：NA | 类名：detectBarcode； API声明：function decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise&lt;DetectResult&gt;; 差异内容：atomicservice | api/@hms.core.scan.detectBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：scanBarcode； API声明：interface ScanCodeRect 差异内容：NA | 类名：scanBarcode； API声明：interface ScanCodeRect 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanCodeRect； API声明：left: number; 差异内容：NA | 类名：ScanCodeRect； API声明：left: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanCodeRect； API声明：top: number; 差异内容：NA | 类名：ScanCodeRect； API声明：top: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanCodeRect； API声明：right: number; 差异内容：NA | 类名：ScanCodeRect； API声明：right: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanCodeRect； API声明：bottom: number; 差异内容：NA | 类名：ScanCodeRect； API声明：bottom: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：scanBarcode； API声明：interface Point 差异内容：NA | 类名：scanBarcode； API声明：interface Point 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：Point； API声明：x: number; 差异内容：NA | 类名：Point； API声明：x: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：Point； API声明：y: number; 差异内容：NA | 类名：Point； API声明：y: number; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanResult； API声明：scanCodeRect?: ScanCodeRect; 差异内容：NA | 类名：ScanResult； API声明：scanCodeRect?: ScanCodeRect; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
| API从不支持元服务到支持元服务 | 类名：ScanResult； API声明：cornerPoints?: Array&lt;Point&gt;; 差异内容：NA | 类名：ScanResult； API声明：cornerPoints?: Array&lt;Point&gt;; 差异内容：atomicservice | api/@hms.core.scan.scanBarcode.d.ts |
