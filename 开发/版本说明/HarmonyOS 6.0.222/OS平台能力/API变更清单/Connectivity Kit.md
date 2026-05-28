# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6021

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：2900011 | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | api/@ohos.bluetooth.ble.d.ts |
| 删除错误码 | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：2900011 | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：NA | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer； API声明：getService(serviceUuid: string): GattService; 差异内容：getService(serviceUuid: string): GattService; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer； API声明：getServices(): GattService[]; 差异内容：getServices(): GattService[]; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer； API声明：getConnectedState(deviceId: string): ProfileConnectionState; 差异内容：getConnectedState(deviceId: string): ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice； API声明：getConnectedState(): ProfileConnectionState; 差异内容：getConnectedState(): ProfileConnectionState; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice； API声明：updateConnectionParam(param: ConnectionParam): Promise&lt;void&gt;; 差异内容：updateConnectionParam(param: ConnectionParam): Promise&lt;void&gt;; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice； API声明：on(type: 'serviceChange', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'serviceChange', callback: Callback&lt;void&gt;): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice； API声明：off(type: 'serviceChange', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'serviceChange', callback?: Callback&lt;void&gt;): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：advertiseFlags?: number; 差异内容：advertiseFlags?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：manufacturerDataMap?: Map<number, Uint8Array>; 差异内容：manufacturerDataMap?: Map<number, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：serviceDataMap?: Map<string, Uint8Array>; 差异内容：serviceDataMap?: Map<string, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：serviceUuids?: string[]; 差异内容：serviceUuids?: string[]; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：txPowerLevel?: number; 差异内容：txPowerLevel?: number; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ScanResult； API声明：advertisingDataMap?: Map<number, Uint8Array>; 差异内容：advertisingDataMap?: Map<number, Uint8Array>; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明：enum ConnectionParam 差异内容：enum ConnectionParam | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam； API声明：LOW_POWER = 1 差异内容：LOW_POWER = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam； API声明：BALANCED = 2 差异内容：BALANCED = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ConnectionParam； API声明：HIGH = 3 差异内容：HIGH = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：access； API声明：function convertUuid(uuid: string): string; 差异内容：function convertUuid(uuid: string): string; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：socket； API声明：function getMaxReceiveDataSize(clientSocket: number): number; 差异内容：function getMaxReceiveDataSize(clientSocket: number): number; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function getMaxTransmitDataSize(clientSocket: number): number; 差异内容：function getMaxTransmitDataSize(clientSocket: number): number; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：socket； API声明：function isConnected(clientSocket: number): boolean; 差异内容：function isConnected(clientSocket: number): boolean; | api/@ohos.bluetooth.socket.d.ts |
