# newLatLngBounds

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-newlatlngbounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { map, mapCommon } from '@kit.MapKit';
```


## newLatLngBounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding?: number): CameraUpdate

设置地图经纬度范围、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 是 | 地图显示经纬度范围。 |
| padding | number | 否 | 地图区域和边界之间的距离，默认值：0，单位：px，异常值返回401错误码。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate) | 描述地图状态将要发生的变化。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |


**示例：**


```ts
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 33,
    longitude: 118,
  },
  southwest: {
    latitude: 32,
    longitude: 119,
  },
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, 5);
```


## newLatLngBounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, width: number, height: number, padding: number): CameraUpdate

设置地图经纬度范围、经纬度矩形范围的高和宽、地图区域和边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 是 | 地图显示经纬度范围。 |
| width | number | 是 | 经纬度矩形范围的屏幕宽，单位：px，取值范围：大于等于0，异常值返回401错误码。 |
| height | number | 是 | 经纬度矩形范围的屏幕高，单位：px，取值范围：大于等于0，异常值返回401错误码。 |
| padding | number | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate) | 描述地图状态将要发生的变化。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |


**示例：**


```ts
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118,
  },
  southwest: {
    latitude: 30.5,
    longitude: 123,
  },
};
// 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(
  bounds,
  1000,
  1000,
  100,
);
```


## newLatLngBounds
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

newLatLngBounds(bounds: mapCommon.LatLngBounds, padding: mapCommon.Padding): CameraUpdate

设置地图经纬度范围和4个方向与边界之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.1(13)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.1(13)

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bounds | [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 是 | 地图显示经纬度范围，异常值返回401错误码。 |
| padding | [mapCommon.Padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#padding) | 是 | 地图区域和边界之间的距离，单位：px，异常值返回401错误码。 说明： - 地图组件高度减去padding的top值和bottom值，结果需要大于等于100px。 - 地图组件宽度减去padding的left值和right值，结果需要大于等于100px。 |


**返回值：**


| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate) | 描述地图状态将要发生的变化。 |


**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-map)。


| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |


**示例：**


```ts
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118,
  },
  southwest: {
    latitude: 30.5,
    longitude: 123,
  },
};
// 初始化参数，左边距0，底边距50
let padding: mapCommon.Padding = {
  left: 0,
  bottom: 50,
};
let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(bounds, padding);
```
