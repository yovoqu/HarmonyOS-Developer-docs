# Map Kit

更新时间：2026-04-30 02:39:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-6111

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MapEventManager； API声明：onMarkerLongClick(callback: Callback<Marker>): void; 差异内容：onMarkerLongClick(callback: Callback<Marker>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：offMarkerLongClick(callback?: Callback<Marker>): void; 差异内容：offMarkerLongClick(callback?: Callback<Marker>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：onPoiLongClick(callback: Callback<mapCommon.Poi>): void; 差异内容：onPoiLongClick(callback: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：offPoiLongClick(callback?: Callback<mapCommon.Poi>): void; 差异内容：offPoiLongClick(callback?: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MarkerOptions； API声明：annotationBackgroundColor?: number; 差异内容：annotationBackgroundColor?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：TileOverlayOptions； API声明：tileDataReuse?: number[]; 差异内容：tileDataReuse?: number[]; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：petalMaps； API声明：function openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>; 差异内容：function openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：PoiDetailParams； API声明：destinationAddress?: string; 差异内容：destinationAddress?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps； API声明：interface OfflineDataParams 差异内容：interface OfflineDataParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：OfflineDataParams； API声明：scenarios: string; 差异内容：scenarios: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：OfflineDataParams； API声明：recommendedRegionIds?: string[]; 差异内容：recommendedRegionIds?: string[]; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions； API声明：maxAdminLevel?: number; 差异内容：maxAdminLevel?: number; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：Site； API声明：reliability?: number; 差异内容：reliability?: number; | api/@hms.core.map.site.d.ts |
