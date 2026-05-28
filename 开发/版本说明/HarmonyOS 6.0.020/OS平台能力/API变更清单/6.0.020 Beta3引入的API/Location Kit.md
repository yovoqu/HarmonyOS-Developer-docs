# Location Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-locationkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：geoLocationManager； API声明：function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise&lt;number&gt;; 差异内容：function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise&lt;number&gt;; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function removeBeaconFence(beaconFence?: BeaconFence): Promise&lt;void&gt;; 差异内容：function removeBeaconFence(beaconFence?: BeaconFence): Promise&lt;void&gt;; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：function isBeaconFenceSupported(): boolean; 差异内容：function isBeaconFenceSupported(): boolean; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export interface BeaconManufactureData 差异内容：export interface BeaconManufactureData | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData； API声明：manufactureId: number; 差异内容：manufactureId: number; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData； API声明：manufactureData: ArrayBuffer; 差异内容：manufactureData: ArrayBuffer; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconManufactureData； API声明：manufactureDataMask: ArrayBuffer; 差异内容：manufactureDataMask: ArrayBuffer; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export interface BeaconFence 差异内容：export interface BeaconFence | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence； API声明：identifier: string; 差异内容：identifier: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence； API声明：beaconFenceInfoType: BeaconFenceInfoType; 差异内容：beaconFenceInfoType: BeaconFenceInfoType; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFence； API声明：manufactureData?: BeaconManufactureData; 差异内容：manufactureData?: BeaconManufactureData; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export interface BeaconFenceRequest 差异内容：export interface BeaconFenceRequest | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest； API声明：beacon: BeaconFence; 差异内容：beacon: BeaconFence; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest； API声明：transitionCallback?: Callback&lt;GeofenceTransition&gt;; 差异内容：transitionCallback?: Callback&lt;GeofenceTransition&gt;; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceRequest； API声明：fenceExtensionAbilityName?: string; 差异内容：fenceExtensionAbilityName?: string; | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：geoLocationManager； API声明：export enum BeaconFenceInfoType 差异内容：export enum BeaconFenceInfoType | api/@ohos.geoLocationManager.d.ts |
| 新增API | NA | 类名：BeaconFenceInfoType； API声明：BEACON_MANUFACTURE_DATA = 1 差异内容：BEACON_MANUFACTURE_DATA = 1 | api/@ohos.geoLocationManager.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：GeofenceTransition； API声明：beaconFence?: BeaconFence; 差异内容：beaconFence?: BeaconFence; | api/@ohos.geoLocationManager.d.ts |
