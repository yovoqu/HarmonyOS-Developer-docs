# Location Kit

更新时间：2026-07-28 11:14:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-7002

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; 差异内容：NA | 类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; 差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：NA | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：3301100,3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager； API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array&lt;Location&gt;>): void; 差异内容：NA | 类名：geoLocationManager； API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array&lt;Location&gt;>): void; 差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 新增错误码 | 类名：geoLocationManager； API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array&lt;Location&gt;>): void; 差异内容：NA | 类名：geoLocationManager； API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array&lt;Location&gt;>): void; 差异内容：3301200 | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：401 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：ohos.permission.APPROXIMATELY_LOCATION | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：ohos.permission.APPROXIMATELY_LOCATION [since 9 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager； API声明：function off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void; 差异内容：ohos.permission.APPROXIMATELY_LOCATION | 类名：geoLocationManager； API声明：function off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void; 差异内容：ohos.permission.APPROXIMATELY_LOCATION [since 9 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager； API声明：function removeGnssGeofence(geofenceId: number): Promise&lt;void&gt;; 差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION | 类名：geoLocationManager； API声明：function removeGnssGeofence(geofenceId: number): Promise&lt;void&gt;; 差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION [since 12 - 24] | api/@ohos.geoLocationManager.d.ts |
| 权限变更 | 类名：geoLocationManager； API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise&lt;void&gt;; 差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION | 类名：geoLocationManager； API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise&lt;void&gt;; 差异内容：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION [since 20 - 24] | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function onLocationChange(request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; 差异内容：function onLocationChange(request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function offLocationChange(callback?: Callback&lt;Location&gt;): void; 差异内容：function offLocationChange(callback?: Callback&lt;Location&gt;): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function getCurrentDistrict(params?: DistrictRequestParams): Promise&lt;DistrictInfo&gt;; 差异内容：function getCurrentDistrict(params?: DistrictRequestParams): Promise&lt;DistrictInfo&gt;; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function startBluetoothSearch(request: BluetoothSearchRequestParams, callback: Callback&lt;BluetoothScanResult&gt;): void; 差异内容：function startBluetoothSearch(request: BluetoothSearchRequestParams, callback: Callback&lt;BluetoothScanResult&gt;): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function stopBluetoothSearch(callback?: Callback&lt;BluetoothScanResult&gt;): void; 差异内容：function stopBluetoothSearch(callback?: Callback&lt;BluetoothScanResult&gt;): void; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function getPostProcessingTrack(sportsType: SportsType): Promise<Array&lt;Location&gt;>; 差异内容：function getPostProcessingTrack(sportsType: SportsType): Promise<Array&lt;Location&gt;>; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export interface BluetoothSearchRequestParams 差异内容：export interface BluetoothSearchRequestParams | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothSearchRequestParams； API声明：deviceIdArray: Array&lt;string&gt;; 差异内容：deviceIdArray: Array&lt;string&gt;; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BluetoothSearchRequestParams； API声明：rssiThreshold?: number; 差异内容：rssiThreshold?: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：interface DistrictInfo 差异内容：interface DistrictInfo | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：locale?: string; 差异内容：locale?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：countryCode?: string; 差异内容：countryCode?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：countryName?: string; 差异内容：countryName?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：administrativeArea?: string; 差异内容：administrativeArea?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：subAdministrativeArea?: string; 差异内容：subAdministrativeArea?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：locality?: string; 差异内容：locality?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictInfo； API声明：subLocality?: string; 差异内容：subLocality?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export interface DistrictRequestParams 差异内容：export interface DistrictRequestParams | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictRequestParams； API声明：locale?: string; 差异内容：locale?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：DistrictRequestParams； API声明：timeoutMs?: number; 差异内容：timeoutMs?: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：ContinuousLocationRequest； API声明：sportsType?: SportsType; 差异内容：sportsType?: SportsType; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：Location； API声明：isFromMock?: boolean; 差异内容：isFromMock?: boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType； API声明：SKIING = 4 差异内容：SKIING = 4 | api/@ohos.geoLocationManager.d.ts |
