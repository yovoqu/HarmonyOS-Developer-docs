# CameraUpdate

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { map, mapCommon } from '@kit.MapKit';
```


## CameraUpdate
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

CameraUpdate定义了相机移动参数。CameraUpdate的创建方法参见[newCameraPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-newcameraposition)等function。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**


```ts
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4,
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10,
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 移动相机
this.mapController.moveCamera(cameraUpdate);
```
