# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：wifiManager； API声明：function on(type: 'hotspotStateChange', callback: Callback&lt;number&gt;): void; 差异内容：202 | 类名：wifiManager； API声明：function on(type: 'hotspotStateChange', callback: Callback&lt;number&gt;): void; 差异内容：NA | api/@ohos.wifiManager.d.ts |
| 删除错误码 | 类名：wifiManager； API声明：function off(type: 'hotspotStateChange', callback?: Callback&lt;number&gt;): void; 差异内容：202 | 类名：wifiManager； API声明：function off(type: 'hotspotStateChange', callback?: Callback&lt;number&gt;): void; 差异内容：NA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function disableWifi(): void; 差异内容：function disableWifi(): void; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：access； API声明：function enableBluetoothAsync(): Promise&lt;void&gt;; 差异内容：function enableBluetoothAsync(): Promise&lt;void&gt;; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：access； API声明：function disableBluetoothAsync(): Promise&lt;void&gt;; 差异内容：function disableBluetoothAsync(): Promise&lt;void&gt;; | api/@ohos.bluetooth.access.d.ts |
| 新增API | NA | 类名：ble； API声明：enum GattDisconnectReason 差异内容：enum GattDisconnectReason | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason； API声明：CONN_TIMEOUT = 1 差异内容：CONN_TIMEOUT = 1 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason； API声明：CONN_TERMINATE_PEER_USER = 2 差异内容：CONN_TERMINATE_PEER_USER = 2 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason； API声明：CONN_TERMINATE_LOCAL_HOST = 3 差异内容：CONN_TERMINATE_LOCAL_HOST = 3 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattDisconnectReason； API声明：CONN_UNKNOWN = 4 差异内容：CONN_UNKNOWN = 4 | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：connection； API声明：function getRemoteDeviceTransport(deviceId: string): BluetoothTransport; 差异内容：function getRemoteDeviceTransport(deviceId: string): BluetoothTransport; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport； API声明：TRANSPORT_DUAL = 2 差异内容：TRANSPORT_DUAL = 2 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：BluetoothTransport； API声明：TRANSPORT_UNKNOWN = 3 差异内容：TRANSPORT_UNKNOWN = 3 | api/@ohos.bluetooth.connection.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：BLEConnectionChangeState； API声明：reason?: GattDisconnectReason; 差异内容：reason?: GattDisconnectReason; | api/@ohos.bluetooth.ble.d.ts |
