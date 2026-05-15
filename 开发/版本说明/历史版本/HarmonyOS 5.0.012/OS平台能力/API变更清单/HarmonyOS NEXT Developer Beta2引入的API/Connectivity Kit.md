# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b031

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：connection； API声明：function setLocalName(name: string): void; 差异内容：NA | 类名：connection； API声明：function setLocalName(name: string): void; 差异内容：12 | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void; 差异内容：function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：connection； API声明：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>; 差异内容：function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>; | api/@ohos.bluetooth.connection.d.ts |
| 新增API | NA | 类名：WifiDeviceConfig； API声明：wapiConfig?: WifiWapiConfig; 差异内容：wapiConfig?: WifiWapiConfig; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明： interface WifiWapiConfig 差异内容： interface WifiWapiConfig | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig； API声明：wapiPskType: WapiPskType; 差异内容：wapiPskType: WapiPskType; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig； API声明：wapiAsCert: string; 差异内容：wapiAsCert: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WifiWapiConfig； API声明：wapiUserCert: string; 差异内容：wapiUserCert: string; | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：wifiManager； API声明： enum WapiPskType 差异内容： enum WapiPskType | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WapiPskType； API声明：WAPI_PSK_ASCII = 0 差异内容：WAPI_PSK_ASCII = 0 | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：WapiPskType； API声明：WAPI_PSK_HEX = 1 差异内容：WAPI_PSK_HEX = 1 | api/@ohos.wifiManager.d.ts |
