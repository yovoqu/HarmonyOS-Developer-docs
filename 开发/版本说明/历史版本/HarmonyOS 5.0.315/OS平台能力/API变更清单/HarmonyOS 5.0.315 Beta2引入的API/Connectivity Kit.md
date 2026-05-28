# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：ble； API声明：function createBleScanner(): BleScanner; 差异内容：function createBleScanner(): BleScanner; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明： interface BleScanner 差异内容： interface BleScanner | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner； API声明：startScan(filters: Array&lt;ScanFilter&gt;, options?: ScanOptions): Promise&lt;void&gt;; 差异内容：startScan(filters: Array&lt;ScanFilter&gt;, options?: ScanOptions): Promise&lt;void&gt;; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner； API声明：stopScan(): Promise&lt;void&gt;; 差异内容：stopScan(): Promise&lt;void&gt;; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner； API声明：on(type: 'BLEDeviceFind', callback: Callback&lt;ScanReport&gt;): void; 差异内容：on(type: 'BLEDeviceFind', callback: Callback&lt;ScanReport&gt;): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BleScanner； API声明：off(type: 'BLEDeviceFind', callback?: Callback&lt;ScanReport&gt;): void; 差异内容：off(type: 'BLEDeviceFind', callback?: Callback&lt;ScanReport&gt;): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明： interface ScanReport 差异内容： interface ScanReport | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReport； API声明：reportType: ScanReportType; 差异内容：reportType: ScanReportType; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReport； API声明：scanResult: Array&lt;ScanResult&gt;; 差异内容：scanResult: Array&lt;ScanResult&gt;; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanOptions； API声明：reportMode?: ScanReportMode; 差异内容：reportMode?: ScanReportMode; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明： enum ScanReportMode 差异内容： enum ScanReportMode | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportMode； API声明：NORMAL = 1 差异内容：NORMAL = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明： enum ScanReportType 差异内容： enum ScanReportType | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportType； API声明：ON_FOUND = 1 差异内容：ON_FOUND = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanReportType； API声明：ON_LOST = 2 差异内容：ON_LOST = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：connection； API声明：function getLastConnectionTime(deviceId: string): Promise&lt;number&gt;; 差异内容：function getLastConnectionTime(deviceId: string): Promise&lt;number&gt;; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function enableWifi(): void; 差异内容：function enableWifi(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function addDeviceConfig(config: WifiDeviceConfig): Promise&lt;number&gt;; 差异内容：function addDeviceConfig(config: WifiDeviceConfig): Promise&lt;number&gt;; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback&lt;number&gt;): void; 差异内容：function addDeviceConfig(config: WifiDeviceConfig, callback: AsyncCallback&lt;number&gt;): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function connectToNetwork(networkId: number): void; 差异内容：function connectToNetwork(networkId: number): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function disconnect(): void; 差异内容：function disconnect(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function getDeviceMacAddress(): string[]; 差异内容：function getDeviceMacAddress(): string[]; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function getDeviceConfigs(): Array&lt;WifiDeviceConfig&gt;; 差异内容：function getDeviceConfigs(): Array&lt;WifiDeviceConfig&gt;; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function removeDevice(id: number): void; 差异内容：function removeDevice(id: number): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory； API声明：WIFI7 = 4 差异内容：WIFI7 = 4 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiCategory； API声明：WIFI7_PLUS = 5 差异内容：WIFI7_PLUS = 5 | api/@ohos.wifiManager.d.ts |
