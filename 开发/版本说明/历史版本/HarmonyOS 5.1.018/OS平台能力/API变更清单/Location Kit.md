# Location Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global； API声明：export default class FenceExtensionAbility 差异内容：NA | 类名：global； API声明：export default class FenceExtensionAbility 差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility； API声明：context: FenceExtensionContext; 差异内容：NA | 类名：FenceExtensionAbility； API声明：context: FenceExtensionContext; 差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility； API声明：onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void; 差异内容：NA | 类名：FenceExtensionAbility； API声明：onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void; 差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：FenceExtensionAbility； API声明：onDestroy(): void; 差异内容：NA | 类名：FenceExtensionAbility； API声明：onDestroy(): void; 差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionAbility.d.ts |
| API模型切换 | 类名：global； API声明：export default class FenceExtensionContext 差异内容：NA | 类名：global； API声明：export default class FenceExtensionContext 差异内容：stagemodelonly | api/@ohos.app.ability.FenceExtensionContext.d.ts |
| 删除错误码 | 类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; 差异内容：3301200 | 类名：geoLocationManager； API声明：function on(type: 'locationChange', request: LocationRequest \| ContinuousLocationRequest, callback: Callback&lt;Location&gt;): void; 差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：3301100,3301200 | 类名：geoLocationManager； API声明：function off(type: 'locationChange', callback?: Callback&lt;Location&gt;): void; 差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager； API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array&lt;Location&gt;>): void; 差异内容：3301200 | 类名：geoLocationManager； API声明：function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array&lt;Location&gt;>): void; 差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 删除错误码 | 类名：geoLocationManager； API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array&lt;Location&gt;>): void; 差异内容：3301200 | 类名：geoLocationManager； API声明：function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array&lt;Location&gt;>): void; 差异内容：NA | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export enum SportsType 差异内容：export enum SportsType | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType； API声明：RUNNING = 1 差异内容：RUNNING = 1 | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType； API声明：WALKING 差异内容：WALKING | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：SportsType； API声明：CYCLING 差异内容：CYCLING | api/@ohos.geoLocationManager.d.ts |
