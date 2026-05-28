# Map Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-b035

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 属性变更 | 类名：MapComponent； API声明：@BuilderParam customInfoWindow: (markerDelegate: map.MarkerDelegate) => void; 差异内容：(markerDelegate: map.MarkerDelegate) => void | 类名：MapComponent； API声明：@BuilderParam customInfoWindow: customInfoWindowCallback; 差异内容：customInfoWindowCallback | api/@hms.core.map.MapComponent.d.ets |
| 新增API | NA | 类名：global； API声明：export type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void; 差异内容：export type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void; | api/@hms.core.map.MapComponent.d.ets |
| 新增API | NA | 类名：MapComponentController； API声明：animateCameraWithMarkers(update: CameraUpdate, markers: Array&lt;Marker&gt;, duration: number): Promise&lt;AnimateResult&gt;; 差异内容：animateCameraWithMarkers(update: CameraUpdate, markers: Array&lt;Marker&gt;, duration: number): Promise&lt;AnimateResult&gt;; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController； API声明：setAlwaysShowScaleEnabled(enabled: boolean): void; 差异内容：setAlwaysShowScaleEnabled(enabled: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController； API声明：isAlwaysShowScaleEnabled(): boolean; 差异内容：isAlwaysShowScaleEnabled(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController； API声明：addArc(params: mapCommon.MapArcParams): MapArc; 差异内容：addArc(params: mapCommon.MapArcParams): MapArc; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController； API声明：getEventManager(): MapEventManager; 差异内容：getEventManager(): MapEventManager; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map； API声明：function convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng; 差异内容：function convertCoordinateSync(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): mapCommon.LatLng; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Animation； API声明：on(type: 'animationStart', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'animationStart', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Animation； API声明：off(type: 'animationStart', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'animationStart', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Animation； API声明：on(type: 'animationEnd', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'animationEnd', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Animation； API声明：off(type: 'animationEnd', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'animationEnd', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：ClusterOverlay； API声明：on(type: 'click', callback: Callback<Array<mapCommon.ClusterItem>>): void; 差异内容：on(type: 'click', callback: Callback<Array<mapCommon.ClusterItem>>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：ClusterOverlay； API声明：off(type: 'click', callback?: Callback<Array<mapCommon.ClusterItem>>): void; 差异内容：off(type: 'click', callback?: Callback<Array<mapCommon.ClusterItem>>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map； API声明： interface MapArc 差异内容： interface MapArc | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapArc； API声明：getColor(): number; 差异内容：getColor(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapArc； API声明：getWidth(): number; 差异内容：getWidth(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapArc； API声明：setColor(color: number): void; 差异内容：setColor(color: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapArc； API声明：setWidth(width: number): void; 差异内容：setWidth(width: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：map； API声明： interface MapEventManager 差异内容： interface MapEventManager | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void; 差异内容：on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'cameraChange', callback?: Callback<mapCommon.LatLng>): void; 差异内容：off(type: 'cameraChange', callback?: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'cameraIdle', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'cameraIdle', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'cameraIdle', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'cameraIdle', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'cameraMoveCancel', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'cameraMoveCancel', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'cameraMoveCancel', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'cameraMoveCancel', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'cameraMove', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'cameraMove', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'cameraMove', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'cameraMove', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'cameraMoveStart', callback: Callback&lt;number&gt;): void; 差异内容：on(type: 'cameraMoveStart', callback: Callback&lt;number&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'cameraMoveStart', callback?: Callback&lt;number&gt;): void; 差异内容：off(type: 'cameraMoveStart', callback?: Callback&lt;number&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void; 差异内容：on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'mapClick', callback?: Callback<mapCommon.LatLng>): void; 差异内容：off(type: 'mapClick', callback?: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'mapLoad', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'mapLoad', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'mapLoad', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'mapLoad', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void; 差异内容：on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'mapLongClick', callback?: Callback<mapCommon.LatLng>): void; 差异内容：off(type: 'mapLongClick', callback?: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'myLocationButtonClick', callback: Callback&lt;void&gt;): void; 差异内容：on(type: 'myLocationButtonClick', callback: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'myLocationButtonClick', callback?: Callback&lt;void&gt;): void; 差异内容：off(type: 'myLocationButtonClick', callback?: Callback&lt;void&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void; 差异内容：on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'myLocationClick', callback?: Callback<mapCommon.LatLng>): void; 差异内容：off(type: 'myLocationClick', callback?: Callback<mapCommon.LatLng>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void; 差异内容：on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'poiClick', callback?: Callback<mapCommon.Poi>): void; 差异内容：off(type: 'poiClick', callback?: Callback<mapCommon.Poi>): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'markerClick', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'markerClick', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'markerClick', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'markerClick', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'markerDragStart', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'markerDragStart', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'markerDragStart', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'markerDragStart', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'markerDrag', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'markerDrag', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'markerDrag', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'markerDrag', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'markerDragEnd', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'markerDragEnd', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'markerDragEnd', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'markerDragEnd', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'circleClick', callback: Callback&lt;MapCircle&gt;): void; 差异内容：on(type: 'circleClick', callback: Callback&lt;MapCircle&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'circleClick', callback?: Callback&lt;MapCircle&gt;): void; 差异内容：off(type: 'circleClick', callback?: Callback&lt;MapCircle&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'polylineClick', callback: Callback&lt;MapPolyline&gt;): void; 差异内容：on(type: 'polylineClick', callback: Callback&lt;MapPolyline&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'polylineClick', callback?: Callback&lt;MapPolyline&gt;): void; 差异内容：off(type: 'polylineClick', callback?: Callback&lt;MapPolyline&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'polygonClick', callback: Callback&lt;MapPolygon&gt;): void; 差异内容：on(type: 'polygonClick', callback: Callback&lt;MapPolygon&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'polygonClick', callback?: Callback&lt;MapPolygon&gt;): void; 差异内容：off(type: 'polygonClick', callback?: Callback&lt;MapPolygon&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'infoWindowClick', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'infoWindowClick', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'infoWindowClick', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'infoWindowClick', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'infoWindowClose', callback: Callback&lt;Marker&gt;): void; 差异内容：on(type: 'infoWindowClose', callback: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'infoWindowClose', callback?: Callback&lt;Marker&gt;): void; 差异内容：off(type: 'infoWindowClose', callback?: Callback&lt;Marker&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'pointAnnotationClick', callback: Callback&lt;PointAnnotation&gt;): void; 差异内容：on(type: 'pointAnnotationClick', callback: Callback&lt;PointAnnotation&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'pointAnnotationClick', callback?: Callback&lt;PointAnnotation&gt;): void; 差异内容：off(type: 'pointAnnotationClick', callback?: Callback&lt;PointAnnotation&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'bubbleClick', callback: Callback&lt;Bubble&gt;): void; 差异内容：on(type: 'bubbleClick', callback: Callback&lt;Bubble&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'bubbleClick', callback?: Callback&lt;Bubble&gt;): void; 差异内容：off(type: 'bubbleClick', callback?: Callback&lt;Bubble&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'imageOverlayClick', callback: Callback&lt;ImageOverlay&gt;): void; 差异内容：on(type: 'imageOverlayClick', callback: Callback&lt;ImageOverlay&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'imageOverlayClick', callback?: Callback&lt;ImageOverlay&gt;): void; 差异内容：off(type: 'imageOverlayClick', callback?: Callback&lt;ImageOverlay&gt;): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：on(type: 'error', callback: ErrorCallback): void; 差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapEventManager； API声明：off(type: 'error', callback?: ErrorCallback): void; 差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapOptions； API声明：alwaysShowScaleEnabled?: boolean; 差异内容：alwaysShowScaleEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：mapCommon； API声明： interface MapArcParams 差异内容： interface MapArcParams | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapArcParams； API声明：startPoint: LatLng; 差异内容：startPoint: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapArcParams； API声明：centerPoint: LatLng; 差异内容：centerPoint: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapArcParams； API声明：endPoint: LatLng; 差异内容：endPoint: LatLng; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapArcParams； API声明：color?: number; 差异内容：color?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MapArcParams； API声明：width?: number; 差异内容：width?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：DistrictSelectOptions； API声明：address?: string; 差异内容：address?: string; | api/@hms.core.map.sceneMap.d.ts |
| 新增API | NA | 类名：DistrictSelectResult； API声明：addressDescription?: string; 差异内容：addressDescription?: string; | api/@hms.core.map.sceneMap.d.ts |
