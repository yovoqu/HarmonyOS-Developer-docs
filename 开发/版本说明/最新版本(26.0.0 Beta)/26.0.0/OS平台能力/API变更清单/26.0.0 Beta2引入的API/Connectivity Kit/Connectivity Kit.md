# Connectivity Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：wifiManager； API声明：enum WifiCapability 差异内容：SystemCapability.Communication.WiFi.Core | 类名：wifiManager； API声明：enum WifiCapability 差异内容：SystemCapability.Communication.WiFi.STA | api/@ohos.wifiManager.d.ts |
| syscap变更 | 类名：WifiCapability； API声明：WIFI_AUTO_ENABLE = 0 差异内容：SystemCapability.Communication.WiFi.Core | 类名：WifiCapability； API声明：WIFI_AUTO_ENABLE = 0 差异内容：SystemCapability.Communication.WiFi.STA | api/@ohos.wifiManager.d.ts |
| 新增错误码 | 类名：access； API声明：function getState(): BluetoothState; 差异内容：NA | 类名：access； API声明：function getState(): BluetoothState; 差异内容：201 | api/@ohos.bluetooth.access.d.ts |
| 新增错误码 | 类名：access； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：NA | 类名：access； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：201 | api/@ohos.bluetooth.access.d.ts |
| 新增错误码 | 类名：access； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：NA | 类名：access； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：201 | api/@ohos.bluetooth.access.d.ts |
| 新增错误码 | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：NA | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：2900011 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：NA | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：2900011 | api/@ohos.bluetooth.ble.d.ts |
| 新增错误码 | 类名：connection； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：NA | 类名：connection； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：201 | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：access； API声明：function getState(): BluetoothState; 差异内容：NA | 类名：access； API声明：function getState(): BluetoothState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10 - 12] | api/@ohos.bluetooth.access.d.ts |
| 权限变更 | 类名：access； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：NA | 类名：access； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10 - 17] | api/@ohos.bluetooth.access.d.ts |
| 权限变更 | 类名：access； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：NA | 类名：access； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10 - 17] | api/@ohos.bluetooth.access.d.ts |
| 权限变更 | 类名：connection； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：NA | 类名：connection； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10 - 17] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：BaseProfile； API声明：getConnectedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BaseProfile； API声明：getConnectedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.baseProfile.d.ts |
| 权限变更 | 类名：BaseProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BaseProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.baseProfile.d.ts |
| 权限变更 | 类名：ble； API声明：function getConnectedBLEDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：ble； API声明：function getConnectedBLEDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble； API声明：function getConnectedBLEDevices(profile: BleProfile): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：ble； API声明：function getConnectedBLEDevices(profile: BleProfile): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble； API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) | 类名：ble； API声明：function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) [since 23] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble； API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) | 类名：ble； API声明：function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) [since 23] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble； API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise&lt;number&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) | 类名：ble； API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise&lt;number&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME) [since 23] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：ble； API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：ble； API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'characteristicRead', callback: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'characteristicRead', callback: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'characteristicWrite', callback: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'characteristicWrite', callback: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'descriptorRead', callback: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'descriptorRead', callback: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'descriptorWrite', callback: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'descriptorWrite', callback: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'connectionStateChange', callback: Callback&lt;BLEConnectionChangeState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'connectionStateChange', callback: Callback&lt;BLEConnectionChangeState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：BleScanner； API声明：on(type: 'BLEDeviceFind', callback: Callback&lt;ScanReport&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BleScanner； API声明：on(type: 'BLEDeviceFind', callback: Callback&lt;ScanReport&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.ble.d.ts |
| 权限变更 | 类名：connection； API声明：function getPairedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：connection； API声明：function getPairedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：connection； API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function on(type: 'discoveryResult', callback: Callback<Array&lt;DiscoveryResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：connection； API声明：function on(type: 'discoveryResult', callback: Callback<Array&lt;DiscoveryResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function on(type: 'bondStateChange', callback: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：connection； API声明：function on(type: 'bondStateChange', callback: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：connection； API声明：function on(type: 'pinRequired', callback: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：connection； API声明：function on(type: 'pinRequired', callback: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0] | api/@ohos.bluetooth.connection.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getState(): BluetoothState; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getState(): BluetoothState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getBtConnectionState(): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getBtConnectionState(): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function pairDevice(deviceId: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function pairDevice(deviceId: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getRemoteDeviceName(deviceId: string): string; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getRemoteDeviceName(deviceId: string): string; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getRemoteDeviceClass(deviceId: string): DeviceClass; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function enableBluetooth(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function enableBluetooth(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function disableBluetooth(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function disableBluetooth(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getLocalName(): string; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getLocalName(): string; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getPairedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getPairedDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getProfileConnectionState(profileId: ProfileId): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH | 类名：bluetoothManager； API声明：function setDevicePairingConfirmation(device: string, accept: boolean): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function setLocalName(name: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function setLocalName(name: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function setBluetoothScanMode(mode: ScanMode, duration: number): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function getBluetoothScanMode(): ScanMode; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function getBluetoothScanMode(): ScanMode; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function startBluetoothDiscovery(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function startBluetoothDiscovery(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function stopBluetoothDiscovery(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function stopBluetoothDiscovery(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function on(type: 'bluetoothDeviceFind', callback: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function off(type: 'bluetoothDeviceFind', callback?: Callback<Array&lt;string&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function on(type: 'bondStateChange', callback: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function on(type: 'bondStateChange', callback: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function off(type: 'bondStateChange', callback?: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function off(type: 'bondStateChange', callback?: Callback&lt;BondStateParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function on(type: 'pinRequired', callback: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function on(type: 'pinRequired', callback: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function off(type: 'pinRequired', callback?: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function off(type: 'pinRequired', callback?: Callback&lt;PinRequiredParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function on(type: 'stateChange', callback: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function off(type: 'stateChange', callback?: Callback&lt;BluetoothState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function sppListen(name: string, option: SppOption, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：bluetoothManager； API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：bluetoothManager； API声明：function sppConnect(device: string, option: SppOption, callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BaseProfile； API声明：getConnectionDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BaseProfile； API声明：getConnectionDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BaseProfile； API声明：getDeviceState(device: string): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BaseProfile； API声明：getDeviceState(device: string): ProfileConnectionState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile； API声明：connect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：A2dpSourceProfile； API声明：connect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile； API声明：disconnect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：A2dpSourceProfile； API声明：disconnect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：A2dpSourceProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：A2dpSourceProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：A2dpSourceProfile； API声明：getPlayingState(device: string): PlayingState; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：A2dpSourceProfile； API声明：getPlayingState(device: string): PlayingState; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile； API声明：connect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile； API声明：connect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile； API声明：disconnect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile； API声明：disconnect(device: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HandsFreeAudioGatewayProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HandsFreeAudioGatewayProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HidHostProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HidHostProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：HidHostProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：HidHostProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：PanProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：PanProfile； API声明：on(type: 'connectionStateChange', callback: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：PanProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：PanProfile； API声明：off(type: 'connectionStateChange', callback?: Callback&lt;StateChangeParam&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE； API声明：function getConnectedBLEDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BLE； API声明：function getConnectedBLEDevices(): Array&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE； API声明：function startBLEScan(filters: Array&lt;ScanFilter&gt;, options?: ScanOptions): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BLE； API声明：function startBLEScan(filters: Array&lt;ScanFilter&gt;, options?: ScanOptions): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE； API声明：function stopBLEScan(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BLE； API声明：function stopBLEScan(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE； API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BLE； API声明：function on(type: 'BLEDeviceFind', callback: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：BLE； API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：BLE； API声明：function off(type: 'BLEDeviceFind', callback?: Callback<Array&lt;ScanResult&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：stopAdvertising(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：stopAdvertising(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：addService(service: GattService): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：addService(service: GattService): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：removeService(serviceUuid: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：removeService(serviceUuid: string): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：close(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：close(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：sendResponse(serverResponse: ServerResponse): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：sendResponse(serverResponse: ServerResponse): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'characteristicRead', callback: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'characteristicRead', callback: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：off(type: 'characteristicRead', callback?: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：off(type: 'characteristicRead', callback?: Callback&lt;CharacteristicReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'characteristicWrite', callback: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'characteristicWrite', callback: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：off(type: 'characteristicWrite', callback?: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：off(type: 'characteristicWrite', callback?: Callback&lt;CharacteristicWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'descriptorRead', callback: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'descriptorRead', callback: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：off(type: 'descriptorRead', callback?: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：off(type: 'descriptorRead', callback?: Callback&lt;DescriptorReadRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'descriptorWrite', callback: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'descriptorWrite', callback: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：off(type: 'descriptorWrite', callback?: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：off(type: 'descriptorWrite', callback?: Callback&lt;DescriptorWriteRequest&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：on(type: 'connectStateChange', callback: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：on(type: 'connectStateChange', callback: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattServer； API声明：off(type: 'connectStateChange', callback?: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattServer； API声明：off(type: 'connectStateChange', callback?: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：connect(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：connect(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：disconnect(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：disconnect(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：close(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：close(): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getDeviceName(callback: AsyncCallback&lt;string&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getDeviceName(callback: AsyncCallback&lt;string&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getDeviceName(): Promise&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getDeviceName(): Promise&lt;string&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getServices(callback: AsyncCallback<Array&lt;GattService&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getServices(callback: AsyncCallback<Array&lt;GattService&gt;>): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getServices(): Promise<Array&lt;GattService&gt;>; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getServices(): Promise<Array&lt;GattService&gt;>; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise&lt;BLECharacteristic&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：readCharacteristicValue(characteristic: BLECharacteristic): Promise&lt;BLECharacteristic&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback&lt;BLEDescriptor&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback&lt;BLEDescriptor&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise&lt;BLEDescriptor&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：readDescriptorValue(descriptor: BLEDescriptor): Promise&lt;BLEDescriptor&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：writeCharacteristicValue(characteristic: BLECharacteristic): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：writeDescriptorValue(descriptor: BLEDescriptor): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：writeDescriptorValue(descriptor: BLEDescriptor): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getRssiValue(callback: AsyncCallback&lt;number&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：getRssiValue(): Promise&lt;number&gt;; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：setBLEMtuSize(mtu: number): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：setBLEMtuSize(mtu: number): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：on(type: 'BLECharacteristicChange', callback: Callback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：on(type: 'BLECharacteristicChange', callback: Callback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：off(type: 'BLECharacteristicChange', callback?: Callback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：off(type: 'BLECharacteristicChange', callback?: Callback&lt;BLECharacteristic&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：on(type: 'BLEConnectionStateChange', callback: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：on(type: 'BLEConnectionStateChange', callback: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 权限变更 | 类名：GattClientDevice； API声明：off(type: 'BLEConnectionStateChange', callback?: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH | 类名：GattClientDevice； API声明：off(type: 'BLEConnectionStateChange', callback?: Callback&lt;BLEConnectChangedState&gt;): void; 差异内容：ohos.permission.ACCESS_BLUETOOTH [since 10] | api/@ohos.bluetoothManager.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace ranging 差异内容：declare namespace ranging | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function isRangingSupported(): boolean; 差异内容：function isRangingSupported(): boolean; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function getRangingCapability(): Promise&lt;RangingCapabilitySupported&gt;; 差异内容：function getRangingCapability(): Promise&lt;RangingCapabilitySupported&gt;; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function startRanging(params: RangingParams, callback: Callback&lt;RangingResult&gt;): void; 差异内容：function startRanging(params: RangingParams, callback: Callback&lt;RangingResult&gt;): void; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function stopRanging(callback: Callback&lt;RangingResult&gt;, params?: RangingParams): void; 差异内容：function stopRanging(callback: Callback&lt;RangingResult&gt;, params?: RangingParams): void; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function startPassiveRanging(capabilityType: RangingTypes): Promise&lt;number&gt;; 差异内容：function startPassiveRanging(capabilityType: RangingTypes): Promise&lt;number&gt;; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function stopPassiveRanging(handle: number, capabilityType: RangingTypes): void; 差异内容：function stopPassiveRanging(handle: number, capabilityType: RangingTypes): void; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function onRangingStateChange(callback: Callback&lt;RangingStateChangeInfo&gt;): void; 差异内容：function onRangingStateChange(callback: Callback&lt;RangingStateChangeInfo&gt;): void; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：function offRangingStateChange(callback?: Callback&lt;RangingStateChangeInfo&gt;): void; 差异内容：function offRangingStateChange(callback?: Callback&lt;RangingStateChangeInfo&gt;): void; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：interface RangingParams 差异内容：interface RangingParams | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingParams； API声明：deviceId: string; 差异内容：deviceId: string; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingParams； API声明：capabilityType: RangingTypes; 差异内容：capabilityType: RangingTypes; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：interface RangingStateChangeInfo 差异内容：interface RangingStateChangeInfo | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStateChangeInfo； API声明：state: RangingState; 差异内容：state: RangingState; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStateChangeInfo； API声明：cause: RangingStoppedCause; 差异内容：cause: RangingStoppedCause; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStateChangeInfo； API声明：deviceId?: string; 差异内容：deviceId?: string; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStateChangeInfo； API声明：handle?: number; 差异内容：handle?: number; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：interface RangingResult 差异内容：interface RangingResult | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingResult； API声明：deviceId: string; 差异内容：deviceId: string; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingResult； API声明：distance: RangingMeasurement; 差异内容：distance: RangingMeasurement; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingResult； API声明：angle: RangingMeasurement; 差异内容：angle: RangingMeasurement; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingResult； API声明：rssi: number; 差异内容：rssi: number; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：interface RangingCapabilitySupported 差异内容：interface RangingCapabilitySupported | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingCapabilitySupported； API声明：nearlinkHadm: boolean; 差异内容：nearlinkHadm: boolean; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：interface RangingMeasurement 差异内容：interface RangingMeasurement | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingMeasurement； API声明：value: number; 差异内容：value: number; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingMeasurement； API声明：confidence: RangingConfidence; 差异内容：confidence: RangingConfidence; | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：enum RangingTypes 差异内容：enum RangingTypes | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingTypes； API声明：NEARLINK_HADM = 1 差异内容：NEARLINK_HADM = 1 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：enum RangingState 差异内容：enum RangingState | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingState； API声明：RANGING_STOPPED = 0 差异内容：RANGING_STOPPED = 0 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingState； API声明：RANGING_STARTED = 1 差异内容：RANGING_STARTED = 1 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：enum RangingStoppedCause 差异内容：enum RangingStoppedCause | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStoppedCause； API声明：NO_ERROR = 0 差异内容：NO_ERROR = 0 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStoppedCause； API声明：INTERNAL_ERROR = 1 差异内容：INTERNAL_ERROR = 1 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStoppedCause； API声明：BUSINESS_CONFLICT = 2 差异内容：BUSINESS_CONFLICT = 2 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingStoppedCause； API声明：BACKGROUND_PAUSED = 3 差异内容：BACKGROUND_PAUSED = 3 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：ranging； API声明：enum RangingConfidence 差异内容：enum RangingConfidence | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingConfidence； API声明：HIGH = 0 差异内容：HIGH = 0 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingConfidence； API声明：MEDIUM = 1 差异内容：MEDIUM = 1 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：RangingConfidence； API声明：LOW = 2 差异内容：LOW = 2 | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace advertising 差异内容：declare namespace advertising | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：function startAdvertising(advertisingParams: AdvertisingParams): Promise&lt;number&gt;; 差异内容：function startAdvertising(advertisingParams: AdvertisingParams): Promise&lt;number&gt;; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：function stopAdvertising(advertisingId: number): Promise&lt;void&gt;; 差异内容：function stopAdvertising(advertisingId: number): Promise&lt;void&gt;; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：function onAdvertisingStateChange(callback: Callback&lt;AdvertisingStateChangeInfo&gt;): void; 差异内容：function onAdvertisingStateChange(callback: Callback&lt;AdvertisingStateChangeInfo&gt;): void; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：function offAdvertisingStateChange(callback?: Callback&lt;AdvertisingStateChangeInfo&gt;): void; 差异内容：function offAdvertisingStateChange(callback?: Callback&lt;AdvertisingStateChangeInfo&gt;): void; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface AdvertisingParams 差异内容：interface AdvertisingParams | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingParams； API声明：advertisingSettings: AdvertisingSettings; 差异内容：advertisingSettings: AdvertisingSettings; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingParams； API声明：advertisingData: AdvertisingData; 差异内容：advertisingData: AdvertisingData; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface AdvertisingSettings 差异内容：interface AdvertisingSettings | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings； API声明：interval?: number; 差异内容：interval?: number; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings； API声明：power?: TxPowerMode; 差异内容：power?: TxPowerMode; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingSettings； API声明：isConnectable?: boolean; 差异内容：isConnectable?: boolean; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface AdvertisingData 差异内容：interface AdvertisingData | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData； API声明：serviceUuids?: string[]; 差异内容：serviceUuids?: string[]; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData； API声明：manufacturerData?: ManufacturerData[]; 差异内容：manufacturerData?: ManufacturerData[]; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData； API声明：serviceData?: ServiceData[]; 差异内容：serviceData?: ServiceData[]; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingData； API声明：includeDeviceName?: boolean; 差异内容：includeDeviceName?: boolean; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface ManufacturerData 差异内容：interface ManufacturerData | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ManufacturerData； API声明：manufacturerId: number; 差异内容：manufacturerId: number; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ManufacturerData； API声明：manufacturerData: ArrayBuffer; 差异内容：manufacturerData: ArrayBuffer; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface ServiceData 差异内容：interface ServiceData | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ServiceData； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：ServiceData； API声明：serviceData: ArrayBuffer; 差异内容：serviceData: ArrayBuffer; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：enum TxPowerMode 差异内容：enum TxPowerMode | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode； API声明：ADV_TX_POWER_LOW = 1 差异内容：ADV_TX_POWER_LOW = 1 | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode； API声明：ADV_TX_POWER_MEDIUM = 2 差异内容：ADV_TX_POWER_MEDIUM = 2 | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：TxPowerMode； API声明：ADV_TX_POWER_HIGH = 3 差异内容：ADV_TX_POWER_HIGH = 3 | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：interface AdvertisingStateChangeInfo 差异内容：interface AdvertisingStateChangeInfo | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo； API声明：advertisingId: number; 差异内容：advertisingId: number; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingStateChangeInfo； API声明：state: AdvertisingState; 差异内容：state: AdvertisingState; | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：advertising； API声明：enum AdvertisingState 差异内容：enum AdvertisingState | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingState； API声明：STARTED = 1 差异内容：STARTED = 1 | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：AdvertisingState； API声明：STOPPED = 2 差异内容：STOPPED = 2 | api/@ohos.nearlink.advertising.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace cdsm 差异内容：declare namespace cdsm | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm； API声明：function createCdsmClient(address: string): CdsmClient; 差异内容：function createCdsmClient(address: string): CdsmClient; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm； API声明：interface CdsmClient 差异内容：interface CdsmClient | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient； API声明：getCdsmInfo(): CdsmInfo; 差异内容：getCdsmInfo(): CdsmInfo; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient； API声明：onCdsmInfoChange(callback: Callback&lt;CdsmInfo&gt;): void; 差异内容：onCdsmInfoChange(callback: Callback&lt;CdsmInfo&gt;): void; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmClient； API声明：offCdsmInfoChange(callback?: Callback&lt;CdsmInfo&gt;): void; 差异内容：offCdsmInfoChange(callback?: Callback&lt;CdsmInfo&gt;): void; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm； API声明：interface CdsmInfo 差异内容：interface CdsmInfo | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmInfo； API声明：members: CdsmMemberInfo[]; 差异内容：members: CdsmMemberInfo[]; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm； API声明：interface CdsmMemberInfo 差异内容：interface CdsmMemberInfo | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmMemberInfo； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmMemberInfo； API声明：state: CdsmConnectionState; 差异内容：state: CdsmConnectionState; | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：cdsm； API声明：enum CdsmConnectionState 差异内容：enum CdsmConnectionState | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmConnectionState； API声明：DISCONNECTED = 0 差异内容：DISCONNECTED = 0 | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：CdsmConnectionState； API声明：CONNECTED = 1 差异内容：CONNECTED = 1 | api/@ohos.nearlink.cdsm.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace nearlinkConstant 差异内容：declare namespace nearlinkConstant | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：nearlinkConstant； API声明：export enum PairingState 差异内容：export enum PairingState | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState； API声明：PAIRING_STATE_NONE = 1 差异内容：PAIRING_STATE_NONE = 1 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState； API声明：PAIRING_STATE_PAIRING = 2 差异内容：PAIRING_STATE_PAIRING = 2 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：PairingState； API声明：PAIRING_STATE_PAIRED = 3 差异内容：PAIRING_STATE_PAIRED = 3 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：nearlinkConstant； API声明：export enum ConnectionState 差异内容：export enum ConnectionState | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState； API声明：STATE_CONNECTING = 0 差异内容：STATE_CONNECTING = 0 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState； API声明：STATE_CONNECTED = 1 差异内容：STATE_CONNECTED = 1 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState； API声明：STATE_DISCONNECTING = 2 差异内容：STATE_DISCONNECTING = 2 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：ConnectionState； API声明：STATE_DISCONNECTED = 3 差异内容：STATE_DISCONNECTED = 3 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：nearlinkConstant； API声明：export enum DeviceClass 差异内容：export enum DeviceClass | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_INVALID_CLASS = -1 差异内容：DEVICE_INVALID_CLASS = -1 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_UNCATEGORIZED = 0x000100 差异内容：DEVICE_UNCATEGORIZED = 0x000100 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_PHONE = 0x000200 差异内容：DEVICE_PHONE = 0x000200 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMARTPHONE = 0x000201 差异内容：DEVICE_SMARTPHONE = 0x000201 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_COMPUTER = 0x000300 差异内容：DEVICE_COMPUTER = 0x000300 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_LAPTOP = 0x000301 差异内容：DEVICE_LAPTOP = 0x000301 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_TABLET = 0x000302 差异内容：DEVICE_TABLET = 0x000302 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ALL_IN_ONE_COMPUTER = 0x000303 差异内容：DEVICE_ALL_IN_ONE_COMPUTER = 0x000303 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_MINI_PC = 0x000304 差异内容：DEVICE_MINI_PC = 0x000304 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_WATCH = 0x000400 差异内容：DEVICE_WATCH = 0x000400 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_WATCH = 0x000401 差异内容：DEVICE_SMART_WATCH = 0x000401 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_HUMAN_INTERFACE = 0x000500 差异内容：DEVICE_HUMAN_INTERFACE = 0x000500 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_KEYBOARD = 0x000501 差异内容：DEVICE_KEYBOARD = 0x000501 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_MOUSE = 0x000502 差异内容：DEVICE_MOUSE = 0x000502 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_HANDLE = 0x000503 差异内容：DEVICE_HANDLE = 0x000503 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_STYLUS = 0x000504 差异内容：DEVICE_STYLUS = 0x000504 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_TOUCHPAD = 0x000505 差异内容：DEVICE_TOUCHPAD = 0x000505 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_AUDIO_PLAYBACK = 0x000600 差异内容：DEVICE_AUDIO_PLAYBACK = 0x000600 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_SPEAKER = 0x000601 差异内容：DEVICE_SMART_SPEAKER = 0x000601 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ECHO_WALL = 0x000602 差异内容：DEVICE_ECHO_WALL = 0x000602 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_AUDIO_CAPTURE = 0x000700 差异内容：DEVICE_AUDIO_CAPTURE = 0x000700 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_KARAOKE_MICROPHONE = 0x000701 差异内容：DEVICE_KARAOKE_MICROPHONE = 0x000701 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_LAPEL_MICROPHONE = 0x000702 差异内容：DEVICE_LAPEL_MICROPHONE = 0x000702 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_WEARABLE_AUDIO = 0x000800 差异内容：DEVICE_WEARABLE_AUDIO = 0x000800 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_IN_EAR_EARPHONE = 0x000801 差异内容：DEVICE_IN_EAR_EARPHONE = 0x000801 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_HEADSET = 0x000802 差异内容：DEVICE_HEADSET = 0x000802 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_OVER_EAR_HEADPHONE = 0x000803 差异内容：DEVICE_OVER_EAR_HEADPHONE = 0x000803 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_NECKBAND_EARPHONE = 0x000804 差异内容：DEVICE_NECKBAND_EARPHONE = 0x000804 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_PERSONAL_CARE = 0x000900 差异内容：DEVICE_PERSONAL_CARE = 0x000900 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_INTELLIGENT_TOOTHBRUSH = 0x000901 差异内容：DEVICE_INTELLIGENT_TOOTHBRUSH = 0x000901 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_CUP = 0x000902 差异内容：DEVICE_SMART_CUP = 0x000902 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_INTELLIGENT_SHAVER = 0x000903 差异内容：DEVICE_INTELLIGENT_SHAVER = 0x000903 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_HVAC = 0x000A00 差异内容：DEVICE_HVAC = 0x000A00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_AIR_PURIFIER = 0x000A01 差异内容：DEVICE_AIR_PURIFIER = 0x000A01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_HUMIDIFIER = 0x000A02 差异内容：DEVICE_HUMIDIFIER = 0x000A02 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_AIR_CIRCULATION_FAN = 0x000A03 差异内容：DEVICE_AIR_CIRCULATION_FAN = 0x000A03 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ELECTRIC_RIDE = 0x000B00 差异内容：DEVICE_ELECTRIC_RIDE = 0x000B00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ELECTRIC_SCOOTER = 0x000B01 差异内容：DEVICE_ELECTRIC_SCOOTER = 0x000B01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ELECTRIC_BICYCLE = 0x000B02 差异内容：DEVICE_ELECTRIC_BICYCLE = 0x000B02 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_LIGHT_FITTING = 0x000C00 差异内容：DEVICE_LIGHT_FITTING = 0x000C00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_TABLE_LAMP = 0x000C01 差异内容：DEVICE_SMART_TABLE_LAMP = 0x000C01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_REMOTE_CONTROL = 0x000D00 差异内容：DEVICE_REMOTE_CONTROL = 0x000D00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_TV_REMOTE_CONTROL = 0x000D01 差异内容：DEVICE_TV_REMOTE_CONTROL = 0x000D01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_IMAGING = 0x000E00 差异内容：DEVICE_IMAGING = 0x000E00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_TV = 0x000E01 差异内容：DEVICE_SMART_TV = 0x000E01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_IP_CAMERA = 0x000E02 差异内容：DEVICE_IP_CAMERA = 0x000E02 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SCREEN_CASTER = 0x000E03 差异内容：DEVICE_SCREEN_CASTER = 0x000E03 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_NETWORKING = 0x000F00 差异内容：DEVICE_NETWORKING = 0x000F00 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_IOT_GATEWAY = 0x000F01 差异内容：DEVICE_IOT_GATEWAY = 0x000F01 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_ACCESS_CONTROL = 0x001000 差异内容：DEVICE_ACCESS_CONTROL = 0x001000 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_INTELLIGENT_LOCK = 0x001001 差异内容：DEVICE_INTELLIGENT_LOCK = 0x001001 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_SMART_KEY = 0x001002 差异内容：DEVICE_SMART_KEY = 0x001002 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_VEHICLE_KEY = 0x001003 差异内容：DEVICE_VEHICLE_KEY = 0x001003 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：DeviceClass； API声明：DEVICE_VEHICLE_LOCK = 0x001004 差异内容：DEVICE_VEHICLE_LOCK = 0x001004 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：nearlinkConstant； API声明：export enum AcbState 差异内容：export enum AcbState | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState； API声明：DISCONNECTED = 0 差异内容：DISCONNECTED = 0 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState； API声明：CONNECTED = 1 差异内容：CONNECTED = 1 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：AcbState； API声明：ENCRYPTED = 2 差异内容：ENCRYPTED = 2 | api/@ohos.nearlink.constant.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace dataTransfer 差异内容：declare namespace dataTransfer | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：type ConnectionState = nearlinkConstant.ConnectionState; 差异内容：type ConnectionState = nearlinkConstant.ConnectionState; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function createPort(uuid: string): void; 差异内容：function createPort(uuid: string): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function destroyPort(uuid: string): void; 差异内容：function destroyPort(uuid: string): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function connect(params: ConnectionParams): Promise&lt;void&gt;; 差异内容：function connect(params: ConnectionParams): Promise&lt;void&gt;; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function disconnect(params: ConnectionParams): Promise&lt;void&gt;; 差异内容：function disconnect(params: ConnectionParams): Promise&lt;void&gt;; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function onConnectionStateChanged(callback: Callback&lt;ConnectionResult&gt;): void; 差异内容：function onConnectionStateChanged(callback: Callback&lt;ConnectionResult&gt;): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function offConnectionStateChanged(callback?: Callback&lt;ConnectionResult&gt;): void; 差异内容：function offConnectionStateChanged(callback?: Callback&lt;ConnectionResult&gt;): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function writeData(params: DataParams): Promise&lt;void&gt;; 差异内容：function writeData(params: DataParams): Promise&lt;void&gt;; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function onReadData(callback: Callback&lt;DataParams&gt;): void; 差异内容：function onReadData(callback: Callback&lt;DataParams&gt;): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function offReadData(callback?: Callback&lt;DataParams&gt;): void; 差异内容：function offReadData(callback?: Callback&lt;DataParams&gt;): void; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：function getConnectionState(params: ConnectionStateParams): ConnectionState; 差异内容：function getConnectionState(params: ConnectionStateParams): ConnectionState; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：interface ConnectionParams 差异内容：interface ConnectionParams | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams； API声明：uuid: string; 差异内容：uuid: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionParams； API声明：transferMode?: TransferMode; 差异内容：transferMode?: TransferMode; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：interface DataParams 差异内容：interface DataParams | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams； API声明：uuid: string; 差异内容：uuid: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：DataParams； API声明：data: ArrayBuffer; 差异内容：data: ArrayBuffer; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：interface ConnectionResult 差异内容：interface ConnectionResult | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult； API声明：uuid: string; 差异内容：uuid: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult； API声明：mtu: number; 差异内容：mtu: number; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionResult； API声明：state: ConnectionState; 差异内容：state: ConnectionState; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：interface ConnectionStateParams 差异内容：interface ConnectionStateParams | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionStateParams； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：ConnectionStateParams； API声明：uuid: string; 差异内容：uuid: string; | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：dataTransfer； API声明：enum TransferMode 差异内容：enum TransferMode | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：TransferMode； API声明：BASIC = 0 差异内容：BASIC = 0 | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：TransferMode； API声明：RELIABLE = 1 差异内容：RELIABLE = 1 | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace manager 差异内容：declare namespace manager | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function isNearLinkSupported(): boolean; 差异内容：function isNearLinkSupported(): boolean; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function getState(): NearlinkState; 差异内容：function getState(): NearlinkState; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function getLocalName(): string; 差异内容：function getLocalName(): string; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function getPairedDevices(): string[]; 差异内容：function getPairedDevices(): string[]; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function onStateChange(callback: Callback&lt;NearlinkState&gt;): void; 差异内容：function onStateChange(callback: Callback&lt;NearlinkState&gt;): void; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：function offStateChange(callback?: Callback&lt;NearlinkState&gt;): void; 差异内容：function offStateChange(callback?: Callback&lt;NearlinkState&gt;): void; | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：manager； API声明：enum NearlinkState 差异内容：enum NearlinkState | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState； API声明：STATE_TURNING_ON = 0 差异内容：STATE_TURNING_ON = 0 | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState； API声明：STATE_ON = 1 差异内容：STATE_ON = 1 | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState； API声明：STATE_TURNING_OFF = 2 差异内容：STATE_TURNING_OFF = 2 | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：NearlinkState； API声明：STATE_OFF = 3 差异内容：STATE_OFF = 3 | api/@ohos.nearlink.manager.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace remoteDevice 差异内容：declare namespace remoteDevice | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：type PairingState = nearlinkConstant.PairingState; 差异内容：type PairingState = nearlinkConstant.PairingState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：type ConnectionState = nearlinkConstant.ConnectionState; 差异内容：type ConnectionState = nearlinkConstant.ConnectionState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：type DeviceClass = nearlinkConstant.DeviceClass; 差异内容：type DeviceClass = nearlinkConstant.DeviceClass; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：type AcbState = nearlinkConstant.AcbState; 差异内容：type AcbState = nearlinkConstant.AcbState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function createRemoteDevice(address: string): RemoteDevice; 差异内容：function createRemoteDevice(address: string): RemoteDevice; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function onPairingStateChange(callback: Callback&lt;PairingStateParam&gt;): void; 差异内容：function onPairingStateChange(callback: Callback&lt;PairingStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function offPairingStateChange(callback?: Callback&lt;PairingStateParam&gt;): void; 差异内容：function offPairingStateChange(callback?: Callback&lt;PairingStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function onConnectionStateChange(callback: Callback&lt;ConnectionStateParam&gt;): void; 差异内容：function onConnectionStateChange(callback: Callback&lt;ConnectionStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function offConnectionStateChange(callback?: Callback&lt;ConnectionStateParam&gt;): void; 差异内容：function offConnectionStateChange(callback?: Callback&lt;ConnectionStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function onAcbStateChange(callback: Callback&lt;AcbStateParam&gt;): void; 差异内容：function onAcbStateChange(callback: Callback&lt;AcbStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：function offAcbStateChange(callback?: Callback&lt;AcbStateParam&gt;): void; 差异内容：function offAcbStateChange(callback?: Callback&lt;AcbStateParam&gt;): void; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface RemoteDevice 差异内容：interface RemoteDevice | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：startPairing(): Promise&lt;void&gt;; 差异内容：startPairing(): Promise&lt;void&gt;; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getPairingState(): PairingState; 差异内容：getPairingState(): PairingState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getDeviceName(): string; 差异内容：getDeviceName(): string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getDeviceClass(): DeviceClass; 差异内容：getDeviceClass(): DeviceClass; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getConnectionState(): ConnectionState; 差异内容：getConnectionState(): ConnectionState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getAcbState(): AcbState; 差异内容：getAcbState(): AcbState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：RemoteDevice； API声明：getDeviceInformation(): DeviceInformation; 差异内容：getDeviceInformation(): DeviceInformation; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface PairingStateParam 差异内容：interface PairingStateParam | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingStateParam； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingStateParam； API声明：preState: PairingState; 差异内容：preState: PairingState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingStateParam； API声明：state: PairingState; 差异内容：state: PairingState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingStateParam； API声明：reason: PairingReason; 差异内容：reason: PairingReason; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingStateParam； API声明：reasonMsg?: string; 差异内容：reasonMsg?: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：enum PairingReason 差异内容：enum PairingReason | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_SUCCESS = 0 差异内容：PAIRING_REASON_SUCCESS = 0 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_FAILURE = 1 差异内容：PAIRING_REASON_FAILURE = 1 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_ACB_CONNECTION_FAIL = 2 差异内容：PAIRING_REASON_ACB_CONNECTION_FAIL = 2 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_EXCEED_ACB_MAX = 3 差异内容：PAIRING_REASON_EXCEED_ACB_MAX = 3 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_REMOTE_CANCELED = 4 差异内容：PAIRING_REASON_REMOTE_CANCELED = 4 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_LOCAL_CANCELED = 5 差异内容：PAIRING_REASON_LOCAL_CANCELED = 5 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingReason； API声明：PAIRING_REASON_AUTH_FAIL = 6 差异内容：PAIRING_REASON_AUTH_FAIL = 6 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface PairingRequestParam 差异内容：interface PairingRequestParam | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingRequestParam； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingRequestParam； API声明：passkey: string; 差异内容：passkey: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingRequestParam； API声明：pairingType: PairingType; 差异内容：pairingType: PairingType; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：enum PairingType 差异内容：enum PairingType | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingType； API声明：NO_PASSKEY_CONFIRMATION = 0 差异内容：NO_PASSKEY_CONFIRMATION = 0 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingType； API声明：PAIRING_TYPE_PASSCODE = 1 差异内容：PAIRING_TYPE_PASSCODE = 1 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：PairingType； API声明：PAIRING_TYPE_NUMBER_COMPARE = 2 差异内容：PAIRING_TYPE_NUMBER_COMPARE = 2 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface ConnectionStateParam 差异内容：interface ConnectionStateParam | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionStateParam； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionStateParam； API声明：preState: ConnectionState; 差异内容：preState: ConnectionState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionStateParam； API声明：state: ConnectionState; 差异内容：state: ConnectionState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionStateParam； API声明：connectionReason: ConnectionReason; 差异内容：connectionReason: ConnectionReason; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionStateParam； API声明：reasonMsg?: string; 差异内容：reasonMsg?: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：enum ConnectionReason 差异内容：enum ConnectionReason | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_SUCCESS = 0 差异内容：CONNECTION_SUCCESS = 0 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_FAILURE = 1 差异内容：CONNECTION_FAILURE = 1 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_LOCAL_DISCONNECT = 2 差异内容：CONNECTION_LOCAL_DISCONNECT = 2 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_REMOTE_DISCONNECT = 3 差异内容：CONNECTION_REMOTE_DISCONNECT = 3 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_FAIL_ACB_CONNECTION = 4 差异内容：CONNECTION_FAIL_ACB_CONNECTION = 4 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_FAIL_SERVICE_DISCOVERY = 5 差异内容：CONNECTION_FAIL_SERVICE_DISCOVERY = 5 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_FAIL_NO_AVAILABLE_SERVICE = 6 差异内容：CONNECTION_FAIL_NO_AVAILABLE_SERVICE = 6 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：ConnectionReason； API声明：CONNECTION_FAIL_CONNECTION_NUM_LIMITED = 7 差异内容：CONNECTION_FAIL_CONNECTION_NUM_LIMITED = 7 | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface AcbStateParam 差异内容：interface AcbStateParam | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：AcbStateParam； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：AcbStateParam； API声明：state: AcbState; 差异内容：state: AcbState; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：remoteDevice； API声明：interface DeviceInformation 差异内容：interface DeviceInformation | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：DeviceInformation； API声明：manufacturerData: string; 差异内容：manufacturerData: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：DeviceInformation； API声明：modelData: string; 差异内容：modelData: string; | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace scan 差异内容：declare namespace scan | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：function startScan(filters: ScanFilters[] \| null, options?: ScanOptions): Promise&lt;void&gt;; 差异内容：function startScan(filters: ScanFilters[] \| null, options?: ScanOptions): Promise&lt;void&gt;; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：function stopScan(): Promise&lt;void&gt;; 差异内容：function stopScan(): Promise&lt;void&gt;; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：function onDeviceFound(callback: Callback<ScanResults[]>): void; 差异内容：function onDeviceFound(callback: Callback<ScanResults[]>): void; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：function offDeviceFound(callback?: Callback<ScanResults[]>): void; 差异内容：function offDeviceFound(callback?: Callback<ScanResults[]>): void; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：interface ScanResults 差异内容：interface ScanResults | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：rssi: number; 差异内容：rssi: number; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：data: ArrayBuffer; 差异内容：data: ArrayBuffer; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：deviceName: string; 差异内容：deviceName: string; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：isConnectable: boolean; 差异内容：isConnectable: boolean; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanResults； API声明：deviceClass?: nearlinkConstant.DeviceClass; 差异内容：deviceClass?: nearlinkConstant.DeviceClass; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：interface ScanFilters 差异内容：interface ScanFilters | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：address?: string; 差异内容：address?: string; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：deviceName?: string; 差异内容：deviceName?: string; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：manufacturerId?: number; 差异内容：manufacturerId?: number; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：manufacturerData?: ArrayBuffer; 差异内容：manufacturerData?: ArrayBuffer; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：manufacturerDataMask?: ArrayBuffer; 差异内容：manufacturerDataMask?: ArrayBuffer; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanFilters； API声明：rssi?: number; 差异内容：rssi?: number; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：interface ScanOptions 差异内容：interface ScanOptions | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanOptions； API声明：scanMode?: ScanMode; 差异内容：scanMode?: ScanMode; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanOptions； API声明：duration?: number; 差异内容：duration?: number; | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：scan； API声明：enum ScanMode 差异内容：enum ScanMode | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanMode； API声明：SCAN_MODE_LOW_POWER = 0 差异内容：SCAN_MODE_LOW_POWER = 0 | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：ScanMode； API声明：SCAN_MODE_BALANCED = 1 差异内容：SCAN_MODE_BALANCED = 1 | api/@ohos.nearlink.scan.d.ts |
| 新增API | NA | 类名：global； API声明：declare namespace ssap 差异内容：declare namespace ssap | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：type ConnectionState = nearlinkConstant.ConnectionState; 差异内容：type ConnectionState = nearlinkConstant.ConnectionState; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：function createClient(address: string): Client; 差异内容：function createClient(address: string): Client; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：function createServer(): Server; 差异内容：function createServer(): Server; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface Client 差异内容：interface Client | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：connect(): Promise&lt;void&gt;; 差异内容：connect(): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：disconnect(): Promise&lt;void&gt;; 差异内容：disconnect(): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：close(): void; 差异内容：close(): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：getServices(): Promise<Service[]>; 差异内容：getServices(): Promise<Service[]>; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：readProperty(property: Property): Promise&lt;Property&gt;; 差异内容：readProperty(property: Property): Promise&lt;Property&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：writeProperty(property: Property, writeType: PropertyWriteType): Promise&lt;void&gt;; 差异内容：writeProperty(property: Property, writeType: PropertyWriteType): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：setPropertyNotification(property: Property, enable: boolean): Promise&lt;void&gt;; 差异内容：setPropertyNotification(property: Property, enable: boolean): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：requestMtuSize(mtu: number): Promise&lt;void&gt;; 差异内容：requestMtuSize(mtu: number): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：onPropertyChange(callback: Callback&lt;Property&gt;): void; 差异内容：onPropertyChange(callback: Callback&lt;Property&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：offPropertyChange(callback?: Callback&lt;Property&gt;): void; 差异内容：offPropertyChange(callback?: Callback&lt;Property&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：onConnectionStateChange(callback: Callback&lt;ConnectionChangeState&gt;): void; 差异内容：onConnectionStateChange(callback: Callback&lt;ConnectionChangeState&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：offConnectionStateChange(callback?: Callback&lt;ConnectionChangeState&gt;): void; 差异内容：offConnectionStateChange(callback?: Callback&lt;ConnectionChangeState&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：onMtuChange(callback: Callback&lt;number&gt;): void; 差异内容：onMtuChange(callback: Callback&lt;number&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Client； API声明：offMtuChange(callback?: Callback&lt;number&gt;): void; 差异内容：offMtuChange(callback?: Callback&lt;number&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface Server 差异内容：interface Server | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：addService(service: Service): void; 差异内容：addService(service: Service): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：removeService(serviceUuid: string): void; 差异内容：removeService(serviceUuid: string): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：close(): void; 差异内容：close(): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：notifyPropertyChanged(address: string, property: Property): Promise&lt;void&gt;; 差异内容：notifyPropertyChanged(address: string, property: Property): Promise&lt;void&gt;; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：sendResponse(response: ServerResponse): void; 差异内容：sendResponse(response: ServerResponse): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：onConnectionStateChange(callback: Callback&lt;ConnectionChangeState&gt;): void; 差异内容：onConnectionStateChange(callback: Callback&lt;ConnectionChangeState&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：offConnectionStateChange(callback?: Callback&lt;ConnectionChangeState&gt;): void; 差异内容：offConnectionStateChange(callback?: Callback&lt;ConnectionChangeState&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：onPropertyRead(callback: Callback&lt;PropertyReadRequest&gt;): void; 差异内容：onPropertyRead(callback: Callback&lt;PropertyReadRequest&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：offPropertyRead(callback?: Callback&lt;PropertyReadRequest&gt;): void; 差异内容：offPropertyRead(callback?: Callback&lt;PropertyReadRequest&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：onPropertyWrite(callback: Callback&lt;PropertyWriteRequest&gt;): void; 差异内容：onPropertyWrite(callback: Callback&lt;PropertyWriteRequest&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：offPropertyWrite(callback?: Callback&lt;PropertyWriteRequest&gt;): void; 差异内容：offPropertyWrite(callback?: Callback&lt;PropertyWriteRequest&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：onMtuChange(callback: Callback&lt;number&gt;): void; 差异内容：onMtuChange(callback: Callback&lt;number&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Server； API声明：offMtuChange(callback?: Callback&lt;number&gt;): void; 差异内容：offMtuChange(callback?: Callback&lt;number&gt;): void; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface Service 差异内容：interface Service | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Service； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Service； API声明：properties: Property[]; 差异内容：properties: Property[]; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface Property 差异内容：interface Property | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property； API声明：propertyUuid: string; 差异内容：propertyUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property； API声明：value: ArrayBuffer; 差异内容：value: ArrayBuffer; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property； API声明：descriptors?: PropertyDescriptor[]; 差异内容：descriptors?: PropertyDescriptor[]; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Property； API声明：operation?: number; 差异内容：operation?: number; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface PropertyDescriptor 差异内容：interface PropertyDescriptor | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor； API声明：propertyUuid: string; 差异内容：propertyUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor； API声明：value: ArrayBuffer; 差异内容：value: ArrayBuffer; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor； API声明：descriptorType: PropertyDescriptorType; 差异内容：descriptorType: PropertyDescriptorType; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptor； API声明：isWriteable?: boolean; 差异内容：isWriteable?: boolean; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface PropertyReadRequest 差异内容：interface PropertyReadRequest | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest； API声明：propertyUuid: string; 差异内容：propertyUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyReadRequest； API声明：requestId: number; 差异内容：requestId: number; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface PropertyWriteRequest 差异内容：interface PropertyWriteRequest | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：serviceUuid: string; 差异内容：serviceUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：propertyUuid: string; 差异内容：propertyUuid: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：value: ArrayBuffer; 差异内容：value: ArrayBuffer; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：requestId: number; 差异内容：requestId: number; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteRequest； API声明：writeType: PropertyWriteType; 差异内容：writeType: PropertyWriteType; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface ServerResponse 差异内容：interface ServerResponse | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse； API声明：requestId: number; 差异内容：requestId: number; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ServerResponse； API声明：value: ArrayBuffer; 差异内容：value: ArrayBuffer; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：interface ConnectionChangeState 差异内容：interface ConnectionChangeState | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ConnectionChangeState； API声明：address: string; 差异内容：address: string; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ConnectionChangeState； API声明：state: ConnectionState; 差异内容：state: ConnectionState; | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：enum PropertyDescriptorType 差异内容：enum PropertyDescriptorType | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType； API声明：PROPERTY = 1 差异内容：PROPERTY = 1 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType； API声明：CLIENT_PROPERTY_CONFIG = 2 差异内容：CLIENT_PROPERTY_CONFIG = 2 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType； API声明：SERVER_PROPERTY_CONFIG = 3 差异内容：SERVER_PROPERTY_CONFIG = 3 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType； API声明：PROPERTY_FORMAT = 4 差异内容：PROPERTY_FORMAT = 4 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyDescriptorType； API声明：TYPE_VENDOR = 255 差异内容：TYPE_VENDOR = 255 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：enum Operation 差异内容：enum Operation | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation； API声明：READABLE = 0x01 差异内容：READABLE = 0x01 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation； API声明：WRITE_NO_RESPONSE = 0x02 差异内容：WRITE_NO_RESPONSE = 0x02 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation； API声明：WRITE_WITH_RESPONSE = 0x04 差异内容：WRITE_WITH_RESPONSE = 0x04 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：Operation； API声明：NOTIFY = 0x08 差异内容：NOTIFY = 0x08 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：ssap； API声明：enum PropertyWriteType 差异内容：enum PropertyWriteType | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteType； API声明：WRITE = 1 差异内容：WRITE = 1 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：PropertyWriteType； API声明：WRITE_NO_RESPONSE = 2 差异内容：WRITE_NO_RESPONSE = 2 | api/@ohos.nearlink.ssap.d.ts |
| 新增API | NA | 类名：StateChangeParam； API声明：role?: PanRole; 差异内容：role?: PanRole; | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：baseProfile； API声明：enum PanRole 差异内容：enum PanRole | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：PanRole； API声明：ROLE_PANNAP = 0 差异内容：ROLE_PANNAP = 0 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：PanRole； API声明：ROLE_PANU = 1 差异内容：ROLE_PANU = 1 | api/@ohos.bluetooth.baseProfile.d.ts |
| 新增API | NA | 类名：ble； API声明：type BluetoothTransport = connection.BluetoothTransport; 差异内容：type BluetoothTransport = connection.BluetoothTransport; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer； API声明：connect(deviceId: string, autoConnect?: boolean): void; 差异内容：connect(deviceId: string, autoConnect?: boolean): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattServer； API声明：disconnect(deviceId: string): void; 差异内容：disconnect(deviceId: string): void; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattClientDevice； API声明：setBLEMtu(mtu: number): Promise&lt;number&gt;; 差异内容：setBLEMtu(mtu: number): Promise&lt;number&gt;; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BLEConnectionChangeState； API声明：reasonMessage?: string; 差异内容：reasonMessage?: string; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：ble； API声明：interface GattSetting 差异内容：interface GattSetting | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattSetting； API声明：autoConnect?: boolean; 差异内容：autoConnect?: boolean; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：GattSetting； API声明：transport?: BluetoothTransport; 差异内容：transport?: BluetoothTransport; | api/@ohos.bluetooth.ble.d.ts |
| 新增API | NA | 类名：BondStateParam； API声明：causeMessage?: string; 差异内容：causeMessage?: string; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：PanProfile； API声明：isTetheringOn(): boolean; 差异内容：isTetheringOn(): boolean; | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：PanProfile； API声明：isPanSupported(): boolean; 差异内容：isPanSupported(): boolean; | api/@ohos.bluetooth.pan.d.ts |
| 新增API | NA | 类名：wifiManager； API声明：function isWlanSupported(): boolean; 差异内容：function isWlanSupported(): boolean; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：hfp； API声明：function createHfpHfProfile(): HandsFreeHfProfile; 差异内容：function createHfpHfProfile(): HandsFreeHfProfile; | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：hfp； API声明：interface HandsFreeHfProfile 差异内容：interface HandsFreeHfProfile | api/@ohos.bluetooth.hfp.d.ts |
| 新增API | NA | 类名：nfcController； API声明：function isNfcSupported(): boolean; 差异内容：function isNfcSupported(): boolean; | api/@ohos.nfc.controller.d.ts |
| 新增API | NA | 类名：tag； API声明：const SKIP_NDEF = 11; 差异内容：const SKIP_NDEF = 11; | api/@ohos.nfc.tag.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.FusionConnectivity.ranging.d.ts 差异内容：ConnectivityKit | api/@ohos.FusionConnectivity.ranging.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.advertising.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.advertising.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.cdsm.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.cdsm.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.constant.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.constant.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.dataTransfer.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.dataTransfer.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.manager.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.manager.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.remoteDevice.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.remoteDevice.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.scan.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.scan.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@ohos.nearlink.ssap.d.ts 差异内容：ConnectivityKit | api/@ohos.nearlink.ssap.d.ts |
