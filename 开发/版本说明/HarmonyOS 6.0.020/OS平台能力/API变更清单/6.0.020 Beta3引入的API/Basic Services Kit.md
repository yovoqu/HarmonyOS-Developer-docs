# Basic Services Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API跨平台权限变更 | 类名：UploadConfig； API声明：index?: number; 差异内容：NA | 类名：UploadConfig； API声明：index?: number; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：UploadConfig； API声明：begins?: number; 差异内容：NA | 类名：UploadConfig； API声明：begins?: number; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：UploadConfig； API声明：ends?: number; 差异内容：NA | 类名：UploadConfig； API声明：ends?: number; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Config； API声明：proxy?: string; 差异内容：NA | 类名：Config； API声明：proxy?: string; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：agent； API声明：interface HttpResponse 差异内容：NA | 类名：agent； API声明：interface HttpResponse 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：HttpResponse； API声明：readonly version: string; 差异内容：NA | 类名：HttpResponse； API声明：readonly version: string; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：HttpResponse； API声明：readonly statusCode: number; 差异内容：NA | 类名：HttpResponse； API声明：readonly statusCode: number; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：HttpResponse； API声明：readonly reason: string; 差异内容：NA | 类名：HttpResponse； API声明：readonly reason: string; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：HttpResponse； API声明：readonly headers: Map<string, Array<string>>; 差异内容：NA | 类名：HttpResponse； API声明：readonly headers: Map<string, Array<string>>; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：on(event: 'pause', callback: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：on(event: 'pause', callback: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：off(event: 'pause', callback?: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：off(event: 'pause', callback?: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：on(event: 'resume', callback: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：on(event: 'resume', callback: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：off(event: 'resume', callback?: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：off(event: 'resume', callback?: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：on(event: 'remove', callback: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：on(event: 'remove', callback: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：off(event: 'remove', callback?: (progress: Progress) => void): void; 差异内容：NA | 类名：Task； API声明：off(event: 'remove', callback?: (progress: Progress) => void): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：on(event: 'response', callback: Callback<HttpResponse>): void; 差异内容：NA | 类名：Task； API声明：on(event: 'response', callback: Callback<HttpResponse>): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：off(event: 'response', callback?: Callback<HttpResponse>): void; 差异内容：NA | 类名：Task； API声明：off(event: 'response', callback?: Callback<HttpResponse>): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：pause(callback: AsyncCallback<void>): void; 差异内容：NA | 类名：Task； API声明：pause(callback: AsyncCallback<void>): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：pause(): Promise<void>; 差异内容：NA | 类名：Task； API声明：pause(): Promise<void>; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：resume(callback: AsyncCallback<void>): void; 差异内容：NA | 类名：Task； API声明：resume(callback: AsyncCallback<void>): void; 差异内容：crossplatform | api/@ohos.request.d.ts |
| API跨平台权限变更 | 类名：Task； API声明：resume(): Promise<void>; 差异内容：NA | 类名：Task； API声明：resume(): Promise<void>; 差异内容：crossplatform | api/@ohos.request.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace scan 差异内容：declare namespace scan | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum ScanErrorCode 差异内容：enum ScanErrorCode | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_NO_PERMISSION = 201 差异内容：SCAN_ERROR_NO_PERMISSION = 201 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_NOT_SYSTEM_APPLICATION = 202 差异内容：SCAN_ERROR_NOT_SYSTEM_APPLICATION = 202 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_INVALID_PARAMETER = 401 差异内容：SCAN_ERROR_INVALID_PARAMETER = 401 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_GENERIC_FAILURE = 13100001 差异内容：SCAN_ERROR_GENERIC_FAILURE = 13100001 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_RPC_FAILURE = 13100002 差异内容：SCAN_ERROR_RPC_FAILURE = 13100002 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_SERVER_FAILURE = 13100003 差异内容：SCAN_ERROR_SERVER_FAILURE = 13100003 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_UNSUPPORTED = 13100004 差异内容：SCAN_ERROR_UNSUPPORTED = 13100004 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_CANCELED = 13100005 差异内容：SCAN_ERROR_CANCELED = 13100005 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_DEVICE_BUSY = 13100006 差异内容：SCAN_ERROR_DEVICE_BUSY = 13100006 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_INVALID = 13100007 差异内容：SCAN_ERROR_INVALID = 13100007 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_JAMMED = 13100008 差异内容：SCAN_ERROR_JAMMED = 13100008 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_NO_DOCS = 13100009 差异内容：SCAN_ERROR_NO_DOCS = 13100009 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_COVER_OPEN = 13100010 差异内容：SCAN_ERROR_COVER_OPEN = 13100010 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_IO_ERROR = 13100011 差异内容：SCAN_ERROR_IO_ERROR = 13100011 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScanErrorCode； API声明：SCAN_ERROR_NO_MEMORY = 13100012 差异内容：SCAN_ERROR_NO_MEMORY = 13100012 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum ConstraintType 差异内容：enum ConstraintType | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ConstraintType； API声明：SCAN_CONSTRAINT_NONE = 0 差异内容：SCAN_CONSTRAINT_NONE = 0 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ConstraintType； API声明：SCAN_CONSTRAINT_RANGE = 1 差异内容：SCAN_CONSTRAINT_RANGE = 1 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ConstraintType； API声明：SCAN_CONSTRAINT_WORD_LIST = 2 差异内容：SCAN_CONSTRAINT_WORD_LIST = 2 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ConstraintType； API声明：SCAN_CONSTRAINT_STRING_LIST = 3 差异内容：SCAN_CONSTRAINT_STRING_LIST = 3 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum PhysicalUnit 差异内容：enum PhysicalUnit | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_NONE = 0 差异内容：SCAN_UNIT_NONE = 0 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_PIXEL = 1 差异内容：SCAN_UNIT_PIXEL = 1 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_BIT = 2 差异内容：SCAN_UNIT_BIT = 2 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_MM = 3 差异内容：SCAN_UNIT_MM = 3 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_DPI = 4 差异内容：SCAN_UNIT_DPI = 4 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_PERCENT = 5 差异内容：SCAN_UNIT_PERCENT = 5 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PhysicalUnit； API声明：SCAN_UNIT_MICROSECOND = 6 差异内容：SCAN_UNIT_MICROSECOND = 6 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum OptionValueType 差异内容：enum OptionValueType | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：OptionValueType； API声明：SCAN_TYPE_BOOL = 0 差异内容：SCAN_TYPE_BOOL = 0 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：OptionValueType； API声明：SCAN_TYPE_INT = 1 差异内容：SCAN_TYPE_INT = 1 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：OptionValueType； API声明：SCAN_TYPE_FIXED = 2 差异内容：SCAN_TYPE_FIXED = 2 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：OptionValueType； API声明：SCAN_TYPE_STRING = 3 差异内容：SCAN_TYPE_STRING = 3 | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum ScannerSyncMode 差异内容：enum ScannerSyncMode | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncMode； API声明：UPDATE_STR = 'update' 差异内容：UPDATE_STR = 'update' | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncMode； API声明：DELETE_STR = 'delete' 差异内容：DELETE_STR = 'delete' | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：enum ScannerDiscoveryMode 差异内容：enum ScannerDiscoveryMode | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDiscoveryMode； API声明：TCP_STR = 'TCP' 差异内容：TCP_STR = 'TCP' | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDiscoveryMode； API声明：USB_STR = 'USB' 差异内容：USB_STR = 'USB' | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface Range 差异内容：interface Range | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：Range； API声明：minValue: number; 差异内容：minValue: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：Range； API声明：maxValue: number; 差异内容：maxValue: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：Range； API声明：quantValue: number; 差异内容：quantValue: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface ScannerParameter 差异内容：interface ScannerParameter | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionName: string; 差异内容：optionName: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionIndex: number; 差异内容：optionIndex: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionTitle: string; 差异内容：optionTitle: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionDesc: string; 差异内容：optionDesc: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionType: OptionValueType; 差异内容：optionType: OptionValueType; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionUnit: PhysicalUnit; 差异内容：optionUnit: PhysicalUnit; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionConstraintType: ConstraintType; 差异内容：optionConstraintType: ConstraintType; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionConstraintString?: string[]; 差异内容：optionConstraintString?: string[]; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionConstraintInt?: number[]; 差异内容：optionConstraintInt?: number[]; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerParameter； API声明：optionConstraintRange?: Range; 差异内容：optionConstraintRange?: Range; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface ScannerOptionValue 差异内容：interface ScannerOptionValue | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerOptionValue； API声明：valueType: OptionValueType; 差异内容：valueType: OptionValueType; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerOptionValue； API声明：numValue?: number; 差异内容：numValue?: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerOptionValue； API声明：strValue?: string; 差异内容：strValue?: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerOptionValue； API声明：boolValue?: boolean; 差异内容：boolValue?: boolean; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface PictureScanProgress 差异内容：interface PictureScanProgress | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PictureScanProgress； API声明：progress: number; 差异内容：progress: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PictureScanProgress； API声明：pictureFd: number; 差异内容：pictureFd: number; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：PictureScanProgress； API声明：isFinal: boolean; 差异内容：isFinal: boolean; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface ScannerDevice 差异内容：interface ScannerDevice | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：scannerId: string; 差异内容：scannerId: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：discoveryMode: ScannerDiscoveryMode; 差异内容：discoveryMode: ScannerDiscoveryMode; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：uniqueId: string; 差异内容：uniqueId: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：manufacturer: string; 差异内容：manufacturer: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：model: string; 差异内容：model: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerDevice； API声明：deviceName: string; 差异内容：deviceName: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：interface ScannerSyncDevice 差异内容：interface ScannerSyncDevice | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncDevice； API声明：scannerId: string; 差异内容：scannerId: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncDevice； API声明：discoveryMode: ScannerDiscoveryMode; 差异内容：discoveryMode: ScannerDiscoveryMode; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncDevice； API声明：uniqueId: string; 差异内容：uniqueId: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncDevice； API声明：syncMode: ScannerSyncMode; 差异内容：syncMode: ScannerSyncMode; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：ScannerSyncDevice； API声明：oldScannerId?: string; 差异内容：oldScannerId?: string; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function init(): Promise<void>; 差异内容：function init(): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function exit(): Promise<void>; 差异内容：function exit(): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function startScannerDiscovery(): Promise<void>; 差异内容：function startScannerDiscovery(): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function openScanner(scannerId: string): Promise<void>; 差异内容：function openScanner(scannerId: string): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function closeScanner(scannerId: string): Promise<void>; 差异内容：function closeScanner(scannerId: string): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>; 差异内容：function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function setScannerParameter(scannerId: string, optionIndex: number, value: ScannerOptionValue): Promise<void>; 差异内容：function setScannerParameter(scannerId: string, optionIndex: number, value: ScannerOptionValue): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function setScanAutoOption(scannerId: string, optionIndex: number): Promise<void>; 差异内容：function setScanAutoOption(scannerId: string, optionIndex: number): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>; 差异内容：function getScannerCurrentSetting(scannerId: string, optionIndex: number): Promise<ScannerOptionValue>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function startScan(scannerId: string, batchMode: boolean): Promise<void>; 差异内容：function startScan(scannerId: string, batchMode: boolean): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function cancelScan(scannerId: string): Promise<void>; 差异内容：function cancelScan(scannerId: string): Promise<void>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>; 差异内容：function getPictureScanProgress(scannerId: string): Promise<PictureScanProgress>; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void; 差异内容：function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void; 差异内容：function off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void; 差异内容：function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：scan； API声明：function off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void; 差异内容：function off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void; | api/@ohos.scan.d.ets |
| 新增API | NA | 类名：DevicePowerMode； API声明：MODE_CUSTOM_POWER_SAVE = 650 差异内容：MODE_CUSTOM_POWER_SAVE = 650 | api/@ohos.power.d.ts |
| 新增API | NA | 类名：PrintJobSubState； API声明：PRINT_JOB_BLOCK_DRIVER_EXCEPTION = 17 差异内容：PRINT_JOB_BLOCK_DRIVER_EXCEPTION = 17 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState； API声明：PRINT_JOB_BLOCK_DRIVER_MISSING = 34 差异内容：PRINT_JOB_BLOCK_DRIVER_MISSING = 34 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState； API声明：PRINT_JOB_BLOCK_INTERRUPT = 35 差异内容：PRINT_JOB_BLOCK_INTERRUPT = 35 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：PrintJobSubState； API声明：PRINT_JOB_BLOCK_PRINTER_UNAVAILABLE = 98 差异内容：PRINT_JOB_BLOCK_PRINTER_UNAVAILABLE = 98 | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void; 差异内容：function startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function startDiscoverPrinter(extensionList: Array<string>): Promise<void>; 差异内容：function startDiscoverPrinter(extensionList: Array<string>): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function stopDiscoverPrinter(callback: AsyncCallback<void>): void; 差异内容：function stopDiscoverPrinter(callback: AsyncCallback<void>): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function stopDiscoverPrinter(): Promise<void>; 差异内容：function stopDiscoverPrinter(): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function connectPrinter(printerId: string, callback: AsyncCallback<void>): void; 差异内容：function connectPrinter(printerId: string, callback: AsyncCallback<void>): void; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：print； API声明：function connectPrinter(printerId: string): Promise<void>; 差异内容：function connectPrinter(printerId: string): Promise<void>; | api/@ohos.print.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：interface ResourceInfo 差异内容：interface ResourceInfo | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：ResourceInfo； API声明：readonly size: number; 差异内容：readonly size: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：interface NetworkInfo 差异内容：interface NetworkInfo | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：NetworkInfo； API声明：readonly dnsServers: string[]; 差异内容：readonly dnsServers: string[]; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：interface PerformanceInfo 差异内容：interface PerformanceInfo | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly dnsTime: number; 差异内容：readonly dnsTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly connectTime: number; 差异内容：readonly connectTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly tlsTime: number; 差异内容：readonly tlsTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly firstSendTime: number; 差异内容：readonly firstSendTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly firstReceiveTime: number; 差异内容：readonly firstReceiveTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly totalTime: number; 差异内容：readonly totalTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：PerformanceInfo； API声明：readonly redirectTime: number; 差异内容：readonly redirectTime: number; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：interface DownloadInfo 差异内容：interface DownloadInfo | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：DownloadInfo； API声明：readonly resource: ResourceInfo; 差异内容：readonly resource: ResourceInfo; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：DownloadInfo； API声明：readonly network: NetworkInfo; 差异内容：readonly network: NetworkInfo; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：DownloadInfo； API声明：readonly performance: PerformanceInfo; 差异内容：readonly performance: PerformanceInfo; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：function getDownloadInfo(url: string): DownloadInfo \| undefined; 差异内容：function getDownloadInfo(url: string): DownloadInfo \| undefined; | api/@ohos.request.cacheDownload.d.ts |
| 新增API | NA | 类名：cacheDownload； API声明：function setDownloadInfoListSize(size: number): void; 差异内容：function setDownloadInfoListSize(size: number): void; | api/@ohos.request.cacheDownload.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.scan.d.ets 差异内容：BasicServicesKit | api/@ohos.scan.d.ets |
