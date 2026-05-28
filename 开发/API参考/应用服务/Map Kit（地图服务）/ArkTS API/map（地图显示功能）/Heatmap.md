# Interface (Heatmap)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-heatmap
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { map, mapCommon } from '@kit.MapKit';
```
 
  

##### Heatmap

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

热力图管理对象。在调用map.[MapComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller)类的[addHeatmap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#addheatmap)方法时会返回该类型的实例。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**示例：**
 
```text
let data: mapCommon.WeightedLatLng[] = [];
for (let i = 0; i < 500; i++) {
  data.push({
    point: {
      longitude: 118.000000 + Math.random() * 1 - 0.25,
      latitude: 31.000000 + Math.random() * 1 - 0.25,
    },
    intensity: 1
  });
}
let heatMapOptions: mapCommon.HeatmapParams = {
  id: 'heatmap0001',
  data: data,
  radius: 20,
  intensity: {
    2: 1,
    5: 5,
    8: 10
  },
}
let heatMap = await this.mapController.addHeatmap(heatMapOptions)
```
 
  

##### setData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setData(data: mapCommon.WeightedLatLng[]): void
 
更新热力图数据。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | mapCommon.WeightedLatLng[] | 是 | 热力图数据（建议数据量小于10000条，数据量过大可能导致卡顿），异常值不处理。 |
 
 
**示例：**
 
```text
let data: mapCommon.WeightedLatLng[] = [
  {
    point: {
      longitude: -151.5129,
      latitude: 63.1016
    },
    intensity: 2.3
  }
];
heatMap.setData(data);
```
 
  

##### getData

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getData(): mapCommon.WeightedLatLng[]
 
获取热力图数据。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| mapCommon.WeightedLatLng[] | 热力图数据。 |
 
 
**示例：**
 
```text
let data: mapCommon.WeightedLatLng[] = heatMap.getData();
```
 
  

##### setColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setColor(color: Record<number, number>): void
 
更新热力图颜色。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Record<number, number> | 是 | 热力图颜色。 - key：数据密度，取值范围[0, 1]。 - value：颜色渐变值，ARGB格式。 异常值不处理。 |
 
 
**示例：**
 
```text
let record: Record<number, number> = {
  0: 0x26C3999,    // 深蓝色
  0.15: 0xFF4D4DFF, // 蓝紫色
  0.3: 0xFF9999FF,  // 浅蓝紫色
  0.45: 0xFFE6E6FF, // 非常浅的蓝紫色
  0.6: 0xFFFFCCFF,  // 浅紫色
  0.75: 0xFFFF99FF, // 紫色
  0.9: 0xFFFF66FF,  // 深紫色
  1: 0xFFFF00FF    // 非常深的紫色
};
heatMap.setColor(record);
```
 
  

##### getColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getColor(): Record<number, number>
 
获取热力图颜色。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Record<number, number> | 热力图颜色。 - key：数据密度，取值范围[0, 1]。 - value：颜色渐变值，ARGB格式。 |
 
 
**示例：**
 
```text
let record: Record<number, number> = heatMap.getColor();
```
 
  

##### setIntensity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setIntensity(intensity: number | Record<number, number>): void
 
更新热力图强度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intensity | number \| Record<number, number> | 是 | 热力图强度，如果是number类型，所有层级使用同一个强度。 - key：层级，取值范围[2, 20]。 - value：热力图强度，取值范围大于0。 异常值不处理。 |
 
 
**示例：**
 
```text
let intensity: Record<number, number> | number = {
  2:0.1,
  3:0.1,
  4:0.1
};
heatMap.setIntensity(intensity);
```
 
  

##### getIntensity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getIntensity(): number | Record<number, number>
 
获取热力图强度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number \| Record<number, number> | 热力图强度，如果是number类型，所有层级使用同一个强度。 - key：层级，取值范围[2, 20]。 - value：热力图强度，取值范围大于0。 |
 
 
**示例：**
 
```text
let intensity: Record<number, number> | number = heatMap.getIntensity();
```
 
  

##### setOpacity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setOpacity(opacity: number | Record<number, number>): void
 
更新热力图透明度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opacity | number \| Record<number, number> | 是 | 热力图透明度，如果是number类型，所有层级使用同一个透明度。 - key：层级，取值范围[2, 20]。 - value：热力图透明度，取值范围[0, 1]，0表示完全不透明，1表示完全透明。 异常值不处理。 |
 
 
**示例：**
 
```text
let opacity: Record<number, number> | number = {
  2:0.1,
  3:0.1,
  4:0.1
}
heatMap.setOpacity(opacity);
```
 
  

##### getOpacity

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getOpacity(): number | Record<number, number>
 
获取热力图透明度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number \| Record<number, number> | 热力图透明度，如果是number类型，所有层级使用同一个透明度。 - key：热力图颜色渐变层级，取值范围[2, 20]。 - value：热力图透明度，取值范围[0, 1]，0表示完全不透明，1表示完全透明。 |
 
 
**示例：**
 
```text
let opacity: Record<number, number> | number = heatMap.getOpacity();
```
 
  

##### setRadius

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setRadius(radius: number | Record<number, number>): void
 
更新热力图半径。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number \| Record<number, number> | 是 | 热力图半径，如果是number类型，所有层级使用同一个半径。 - key：层级，取值范围[2, 20]。 - value：热力图半径，取值范围：[1, +∞)。 异常值不处理。 |
 
 
**示例：**
 
```text
heatMap.setRadius(3000);
```
 
  

##### getRadius

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getRadius(): number | Record<number, number>
 
获取热力图半径。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number \| Record<number, number> | 热力图半径，如果是number类型，所有层级使用同一个半径。 - key：层级，取值范围[2, 20]。 - value：热力图半径，取值范围：[1, +∞)。 |
 
 
**示例：**
 
```text
let radius: number | Record<number, number> = heatMap.getRadius();
```
 
  

##### setRadiusUnit

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setRadiusUnit(radiusUnit: mapCommon.RadiusUnit): void
 
更新热力图半径的单位。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radiusUnit | mapCommon.RadiusUnit | 是 | 热力图半径单位。异常值不处理。 |
 
 
**示例：**
 
```text
heatMap.setRadiusUnit(mapCommon.RadiusUnit.PIXEL_UNIT);
```
 
  

##### getRadiusUnit

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getRadiusUnit(): mapCommon.RadiusUnit
 
获取热力图半径单位。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| mapCommon.RadiusUnit | 热力图半径单位。 |
 
 
**示例：**
 
```text
let radiusUnit: mapCommon.RadiusUnit = heatMap.getRadiusUnit();
```
 
  

##### setVisible

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setVisible(visible: boolean): void
 
更新热力图是否可见。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 热力图是否可见。 - true：可见。 - false：不可见。 异常值不处理。 |
 
 
**示例：**
 
```text
heatMap.setVisible(false);
```
 
  

##### isVisible

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

isVisible(): boolean
 
获取热力图是否可见。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 热力图是否可见。 - true：可见。 - false：不可见。 |
 
 
**示例：**
 
```text
let isVisible: boolean = heatMap.isVisible();
```
 
  

##### remove

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

remove(): void
 
删除热力图。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**示例：**
 
```text
heatMap.remove();
```
