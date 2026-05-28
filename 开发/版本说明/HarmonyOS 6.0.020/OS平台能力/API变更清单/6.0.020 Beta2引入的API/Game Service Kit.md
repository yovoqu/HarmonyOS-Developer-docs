# Game Service Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-gameservicekit-6002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：interface BindParameters 差异内容：interface BindParameters | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：BindParameters； API声明：deviceId: string; 差异内容：deviceId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：BindParameters； API声明：networkId: string; 差异内容：networkId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：interface NearbyGameDevice 差异内容：interface NearbyGameDevice | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice； API声明：deviceName: string; 差异内容：deviceName: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice； API声明：deviceId: string; 差异内容：deviceId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyGameDevice； API声明：networkId: string; 差异内容：networkId: string; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：interface DiscoveryResult 差异内容：interface DiscoveryResult | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：DiscoveryResult； API声明：nearbyGameDevices: Array&lt;NearbyGameDevice&gt;; 差异内容：nearbyGameDevices: Array&lt;NearbyGameDevice&gt;; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：enum Mode 差异内容：enum Mode | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：Mode； API声明：API = 1 差异内容：API = 1 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：Mode； API声明：KNOCK = 2 差异内容：KNOCK = 2 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：NearbyTransferErrorCode； API声明：INVALID_PARAMETER = 1018300008 差异内容：INVALID_PARAMETER = 1018300008 | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：function on(type: 'discovery', callback: Callback&lt;DiscoveryResult&gt;): void; 差异内容：function on(type: 'discovery', callback: Callback&lt;DiscoveryResult&gt;): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：function off(type: 'discovery', callback?: Callback&lt;DiscoveryResult&gt;): void; 差异内容：function off(type: 'discovery', callback?: Callback&lt;DiscoveryResult&gt;): void; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：function discoveryNearbyGame(): Promise&lt;void&gt;; 差异内容：function discoveryNearbyGame(): Promise&lt;void&gt;; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 新增API | NA | 类名：gameNearbyTransfer； API声明：function bindNearbyGame(bindParameters: BindParameters): Promise&lt;void&gt;; 差异内容：function bindNearbyGame(bindParameters: BindParameters): Promise&lt;void&gt;; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：CreateParameters； API声明：mode?: Mode; 差异内容：mode?: Mode; | api/@hms.core.gameservice.gamenearbytransfer.d.ts |
