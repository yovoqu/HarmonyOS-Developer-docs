# Interface (MapPolygon)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mappolygon

支持设备：Phone | PC/2in1 | Tablet | Wearable

#### 导入模块

```ts
import { map, mapCommon } from '@kit.MapKit';
```

#### MapPolygon
多边形，继承[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)。多边形可以是凸面或凹面，它可以跨越180子午线并且可以具有未填充的孔。在调用map.[MapComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller)类的[addPolygon](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#addpolygon)方法时会返回该类型的实例。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```ts
let polygonOptions: mapCommon.MapPolygonOptions = {
  points: [
    { latitude: 31.9844102, longitude: 118.7662 },
    { latitude: 31.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 123.7662 },
    { latitude: 36.9844102, longitude: 118.7662 }
  ],
  fillColor: 0xffff4500
};
let mapPolygon = await this.mapController.addPolygon(polygonOptions);
```

#### getFillColor
getFillColor(): number
获取ARGB格式的多边形的填充色值。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | ARGB格式的颜色值。 |

**示例：**

```ts
let fillColor: number = mapPolygon.getFillColor();
```

#### getHoles
getHoles(): Array<Array&lt;mapCommon.LatLng&gt;>
获取多边形的空心洞。

> [!NOTE] 说明
> 多边形的空心洞：多边形可能包含一个或多个内部空洞，形成“空心”效果。这些区域不被填充，使得多边形的内部结构更加复杂和多样化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Array<[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)>> | 多边形的空心洞数组，其中空心洞是[LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)数组。 |

**示例：**

```ts
let holes: Array<Array<mapCommon.LatLng>> = mapPolygon.getHoles();
```

#### getPoints
getPoints(): Array&lt;mapCommon.LatLng&gt;
获取多边形的顶点坐标。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)> | 多边形的顶点坐标。 |

**示例：**

```ts
let points: Array<mapCommon.LatLng> = mapPolygon.getPoints();
```

#### getStrokeColor
getStrokeColor(): number
获取多边形的边框颜色。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | ARGB格式颜色值。 |

**示例：**

```ts
let strokeColor: number = mapPolygon.getStrokeColor();
```

#### getJointType
getJointType(): mapCommon.JointType
获取多边形的顶点样式。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [mapCommon.JointType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#jointtype) | 多边形的顶点样式。 |

**示例：**

```ts
let jointType: mapCommon.JointType = mapPolygon.getJointType();
```

#### getPatterns
getPatterns(): Array&lt;mapCommon.PatternItem&gt;
获取多边形的边框样式。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[mapCommon.PatternItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#patternitem)> | 多边形的边框样式。 |

**示例：**

```ts
let patterns: Array<mapCommon.PatternItem> = mapPolygon.getPatterns();
```

#### getStrokeWidth
getStrokeWidth(): number
获取多边形的边框宽度。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 多边形的边框宽度，单位：px。 |

**示例：**

```ts
let strokeWidth: number = mapPolygon.getStrokeWidth();
```

#### isClickable
isClickable(): boolean
获取多边形的可点击性。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 多边形的可点击性。 - true：可点击 - false：不可点击 |

**示例：**

```ts
let clickable: boolean = mapPolygon.isClickable();
```

#### isGeodesic
isGeodesic(): boolean
获取多边形的每个线段是否为大地线。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 多边形的每个线段是否为大地线。 - true：大地线 - false：非大地线 |

**示例：**

```ts
let geodesic: boolean = mapPolygon.isGeodesic();
```

#### setClickable
setClickable(clickable: boolean): void
设置多边形的可点击性。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| clickable | boolean | 是 | 多边形的可点击性，异常值不处理。 - true：可点击 - false：不可点击 |

**示例：**

```ts
mapPolygon.setClickable(true);
```

#### setFillColor
setFillColor(color: number): void
设置多边形的填充色。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 多边形的填充色，ARGB格式颜色值，异常值不处理。 |

**示例：**

```ts
mapPolygon.setFillColor(0xff000FFF);
```

#### setGeodesic
setGeodesic(geodesic: boolean): void
设置是否将多边形的每个线段绘制为大地线。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| geodesic | boolean | 是 | 将多边形的每个线段绘制为大地线，异常值不处理。 - true：每段绘制为大地线 - false：不是大地线 |

**示例：**

```ts
mapPolygon.setGeodesic(true);
```

#### setHoles
setHoles(holes: Array<Array&lt;mapCommon.LatLng&gt;>): void
设置多边形的空心洞。

> [!NOTE] 说明
> 多边形的空心洞：多边形可能包含一个或多个内部空洞，形成“空心”效果。这些区域不被填充，使得多边形的内部结构更加复杂和多样化。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| holes | Array<Array<[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)>> | 是 | 空心洞数组，其中空心洞是[LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)数组。异常值不处理。 |

**示例：**

```ts
let holes: Array<Array<mapCommon.LatLng>> = [
  [
    {
      latitude: 32.98,
      longitude: 121.76
    },
    {
      latitude: 32.98,
      longitude: 119.76
    },
    {
      latitude: 35.98,
      longitude: 119.76
    },
    {
      latitude: 35.98,
      longitude: 121.76
    }
  ]
];
mapPolygon.setHoles(holes);
```


> [!NOTE] 说明
> 当空心洞的坐标贴合多边形边缘时，会导致渲染出现异常，渲染多余的空心区域。

#### setPoints
setPoints(points: Array&lt;mapCommon.LatLng&gt;): void
重新设置多边形的顶点坐标。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| points | Array<[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)> | 是 | 顶点坐标数组。异常值不处理。 |

**示例：**

```ts
let points: Array<mapCommon.LatLng> = [
  {
    latitude: 31.98,
    longitude: 115.76
  },
  {
    latitude: 31.98,
    longitude: 118.76
  },
  {
    latitude: 35.98,
    longitude: 118.76
  },
  {
    latitude: 35.98,
    longitude: 118.76
  }
];
mapPolygon.setPoints(points);
```

#### setStrokeColor
setStrokeColor(color: number): void
设置多边形的边框颜色。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| color | number | 是 | 多边形的边框颜色，ARGB格式颜色值，异常值不处理。 |

**示例：**

```ts
mapPolygon.setStrokeColor(0xff00DB93);
```

#### setJointType
setJointType(jointType: mapCommon.JointType): void
设置多边形的顶点样式。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| jointType | [mapCommon.JointType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#jointtype) | 是 | 顶点样式，异常值不处理。 |

**示例：**

```ts
mapPolygon.setJointType(mapCommon.JointType.ROUND);
```

#### setPatterns
setPatterns(patterns: Array&lt;mapCommon.PatternItem&gt;): void
设置多边形的边框样式。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| patterns | Array<[mapCommon.PatternItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#patternitem)> | 是 | [PatternItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#patternitem)对象的数组，异常值不处理。 |

**示例：**

```ts
let linePatterns: Array<mapCommon.PatternItem> = [
  {
    type: mapCommon.PatternItemType.DASH,
    length: 100
  },
  {
    type: mapCommon.PatternItemType.DOT,
    length: 100
  },
  {
    type: mapCommon.PatternItemType.GAP,
    length: 100
  }
];
mapPolygon.setPatterns(linePatterns);
```

#### setStrokeWidth
setStrokeWidth(width: number): void
设置多边形的边框宽度。
**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| width | number | 是 | 边框的宽度，单位：px，取值范围：大于等于0，异常值不处理。 |

**示例：**

```ts
mapPolygon.setStrokeWidth(30);
```
