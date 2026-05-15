# rectifyCoordinate

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-rectifycoordinate
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { map, mapCommon } from '@kit.MapKit';
```


## rectifyCoordinate
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

rectifyCoordinate(context: common.Context, locations: Array<mapCommon.CoordinateLatLng>): Promise<Array<mapCommon.CoordinateLatLng>>

根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。如果需要修正，则返回修正后的坐标系和坐标。使用Promise异步回调。


**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | Context上下文。 |
| locations | Array&lt;[mapCommon.CoordinateLatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#coordinatelatlng)&gt; | 是 | 输入坐标系和坐标。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[mapCommon.CoordinateLatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#coordinatelatlng)&gt;&gt; | Promise对象，返回修正后的坐标系和坐标。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600013 | The current routing location is unknown. Try again later. |


**示例：**


```ts
let locations: Array<mapCommon.CoordinateLatLng> = [
  {
    // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
    coordinateType: mapCommon.CoordinateType.WGS84,
    location: { latitude: 22.280556, longitude: 114.984 },
  },
];
// 包含await的外层方法需要添加async关键字
let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(
  this.getUIContext().getHostContext(),
  locations,
);
```
