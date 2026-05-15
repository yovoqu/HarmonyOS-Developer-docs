# zoomOut

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-zoomout
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```ts
import { map } from '@kit.MapKit';
```


## zoomOut
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

zoomOut(): CameraUpdate

缩小地图缩放级别，在当前地图显示的级别基础上减1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [CameraUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate) | 描述地图状态将要发生的变化。 |


**示例：**


```ts
let cameraUpdate: map.CameraUpdate = map.zoomOut();
```
