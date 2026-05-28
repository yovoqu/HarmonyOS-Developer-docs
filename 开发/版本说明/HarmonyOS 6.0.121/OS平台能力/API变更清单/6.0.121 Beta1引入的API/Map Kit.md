# Map Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-6011

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：petalMaps； API声明：function openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise&lt;void&gt;; 差异内容：function openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise&lt;void&gt;; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：VehicleType； API声明：TRANSIT = 3 差异内容：TRANSIT = 3 | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：petalMaps； API声明：interface TaxiParams 差异内容：interface TaxiParams | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：originPosition?: mapCommon.LatLng; 差异内容：originPosition?: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：originName?: string; 差异内容：originName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：originPoiId?: string; 差异内容：originPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：destinationPosition: mapCommon.LatLng; 差异内容：destinationPosition: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：destinationName?: string; 差异内容：destinationName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：destinationPoiId?: string; 差异内容：destinationPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 新增API | NA | 类名：TaxiParams； API声明：coordinateType?: mapCommon.CoordinateType; 差异内容：coordinateType?: mapCommon.CoordinateType; | api/@hms.core.map.petalMaps.d.ts |
| 类新增必选属性或非同名方法 | 类名：global； API声明： 差异内容：NA | 类名：MapComponentController； API声明：changeMyLocationLayerOrder(isBelow: boolean): void; 差异内容：changeMyLocationLayerOrder(isBelow: boolean): void; | api/@hms.core.map.map.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PoiDetailParams； API声明：zoom?: number; 差异内容：zoom?: number; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：PoiDetailParams； API声明：coordinateType?: mapCommon.CoordinateType; 差异内容：coordinateType?: mapCommon.CoordinateType; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：RoutePlanParams； API声明：coordinateType?: mapCommon.CoordinateType; 差异内容：coordinateType?: mapCommon.CoordinateType; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：NaviParams； API声明：originPosition?: mapCommon.LatLng; 差异内容：originPosition?: mapCommon.LatLng; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：NaviParams； API声明：originName?: string; 差异内容：originName?: string; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：NaviParams； API声明：originPoiId?: string; 差异内容：originPoiId?: string; | api/@hms.core.map.petalMaps.d.ts |
| 接口新增可选属性 | 类名：global； API声明： 差异内容：NA | 类名：NaviParams； API声明：coordinateType?: mapCommon.CoordinateType; 差异内容：coordinateType?: mapCommon.CoordinateType; | api/@hms.core.map.petalMaps.d.ts |
