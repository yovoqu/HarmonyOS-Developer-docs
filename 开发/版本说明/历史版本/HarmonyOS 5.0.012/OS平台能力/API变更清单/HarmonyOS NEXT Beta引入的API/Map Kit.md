# Map Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MapComponentController； API声明：setDisplayOrder(types: Array<mapCommon.MapElementType>): void; 差异内容：setDisplayOrder(types: Array<mapCommon.MapElementType>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map； API声明：function rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>; 差异内容：function rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：mapCommon； API声明： interface CoordinateLatLng 差异内容： interface CoordinateLatLng | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：CoordinateLatLng； API声明：coordinateType: CoordinateType; 差异内容：coordinateType: CoordinateType; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：CoordinateLatLng； API声明：location: LatLng; 差异内容：location: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon； API声明： enum MapElementType 差异内容： enum MapElementType | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapElementType； API声明：OVERLAY = 1 差异内容：OVERLAY = 1 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapElementType； API声明：POI = 2 差异内容：POI = 2 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapElementType； API声明：CUSTOM_POI = 3 差异内容：CUSTOM_POI = 3 | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapElementType； API声明：MARKER = 4 差异内容：MARKER = 4 | api/@hms.core.map.mapCommon.d.ts |
