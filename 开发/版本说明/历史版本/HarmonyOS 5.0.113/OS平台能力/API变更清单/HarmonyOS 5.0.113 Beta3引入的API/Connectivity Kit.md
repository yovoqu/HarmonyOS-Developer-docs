# Connectivity Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-b105

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：wifiManager； API声明：function isWifiActive(): boolean; 差异内容：201,2501000,801 | 类名：wifiManager； API声明：function isWifiActive(): boolean; 差异内容：2501000,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function removeCandidateConfig(networkId: number): Promise&lt;void&gt;; 差异内容：201,2501000,401,801 | 类名：wifiManager； API声明：function removeCandidateConfig(networkId: number): Promise&lt;void&gt;; 差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：201,2501000,401,801 | 类名：wifiManager； API声明：function removeCandidateConfig(networkId: number, callback: AsyncCallback&lt;void&gt;): void; 差异内容：201,2501000,2501001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function isMeteredHotspot(): boolean; 差异内容：201,2501000,801 | 类名：wifiManager； API声明：function isMeteredHotspot(): boolean; 差异内容：201,2501000,2501001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function getP2pLinkedInfo(callback: AsyncCallback&lt;WifiP2pLinkedInfo&gt;): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function getP2pLinkedInfo(callback: AsyncCallback&lt;WifiP2pLinkedInfo&gt;): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function getP2pLocalDevice(callback: AsyncCallback&lt;WifiP2pDevice&gt;): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function getP2pLocalDevice(callback: AsyncCallback&lt;WifiP2pDevice&gt;): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function createGroup(config: WifiP2PConfig): void; 差异内容：201,2801000,401,801 | 类名：wifiManager； API声明：function createGroup(config: WifiP2PConfig): void; 差异内容：201,2801000,2801001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function removeGroup(): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function removeGroup(): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function p2pConnect(config: WifiP2PConfig): void; 差异内容：201,2801000,401,801 | 类名：wifiManager； API声明：function p2pConnect(config: WifiP2PConfig): void; 差异内容：201,2801000,2801001,401,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function p2pCancelConnect(): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function p2pCancelConnect(): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function startDiscoverDevices(): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function startDiscoverDevices(): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 错误码变更 | 类名：wifiManager； API声明：function stopDiscoverDevices(): void; 差异内容：201,2801000,801 | 类名：wifiManager； API声明：function stopDiscoverDevices(): void; 差异内容：201,2801000,2801001,801 | api/@ohos.wifiManager.d.ts |
| 权限变更 | 类名：wifiManager； API声明：function isWifiActive(): boolean; 差异内容：ohos.permission.GET_WIFI_INFO | 类名：wifiManager； API声明：function isWifiActive(): boolean; 差异内容：NA | api/@ohos.wifiManager.d.ts |
| 新增API | NA | 类名：CodecType； API声明：CODEC_TYPE_L2HCST = 3 差异内容：CODEC_TYPE_L2HCST = 3 | api/@ohos.bluetooth.a2dp.d.ts |
| 新增API | NA | 类名：CodecType； API声明：CODEC_TYPE_LDAC = 4 差异内容：CODEC_TYPE_LDAC = 4 | api/@ohos.bluetooth.a2dp.d.ts |
