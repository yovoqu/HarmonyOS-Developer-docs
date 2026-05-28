# Map Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-510

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：petalMaps； API声明：function openMapHomePage(context: common.Context): Promise&lt;void&gt;; 差异内容：NA | 类名：petalMaps； API声明：function openMapHomePage(context: common.Context): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps； API声明：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise&lt;void&gt;; 差异内容：NA | 类名：petalMaps； API声明：function openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps； API声明：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise&lt;void&gt;; 差异内容：NA | 类名：petalMaps； API声明：function openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps； API声明：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise&lt;void&gt;; 差异内容：NA | 类名：petalMaps； API声明：function openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：petalMaps； API声明：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise&lt;void&gt;; 差异内容：NA | 类名：petalMaps； API声明：function openMapNavi(context: common.Context, naviParams: NaviParams): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.petalMaps.d.ts |
| 新增错误码 | 类名：sceneMap； API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise&lt;void&gt;; 差异内容：NA | 类名：sceneMap； API声明：function queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise&lt;void&gt;; 差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 新增错误码 | 类名：sceneMap； API声明：function chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise&lt;LocationChoosingResult&gt;; 差异内容：NA | 类名：sceneMap； API声明：function chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise&lt;LocationChoosingResult&gt;; 差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 新增错误码 | 类名：sceneMap； API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise&lt;DistrictSelectResult&gt;; 差异内容：NA | 类名：sceneMap； API声明：function selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise&lt;DistrictSelectResult&gt;; 差异内容：801 | api/@hms.core.map.sceneMap.d.ts |
| 属性变更 | 类名：MarkerOptions； API声明：annotations?: Array&lt;Text&gt;; 差异内容：Array&lt;Text&gt; | 类名：MarkerOptions； API声明：annotations?: Text[]; 差异内容：Text[] | api/@hms.core.map.mapCommon.d.ts |
