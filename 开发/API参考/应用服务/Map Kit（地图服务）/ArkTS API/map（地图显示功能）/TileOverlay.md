# Interface (TileOverlay)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-tileoverlay
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { map, mapCommon } from '@kit.MapKit';
```
 
  

#### TileOverlay

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

瓦片图层，继承[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)。瓦片图层是一种基于[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)实现的地图覆盖层，用于展示自定义瓦片。
 
> [!NOTE]
> 由于性能考虑，建议最多添加10个TileOverlay，且提供的图层瓦片分辨率是256*256。

 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**示例：**
 
```text
let params: mapCommon.TileOverlayParams = {
  // 开发者的地图瓦片图层地址，必须使用以http或者https开头的URL地址，且需包含?x={x}&y={y}&z={z}格式的占位符
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```
 
  

#### clearTileCache

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

clearTileCache(): void
 
清除瓦片图层的缓存。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**示例：**
 
```text
tileOverlay.clearTileCache();
```
 
  

#### setFadeIn

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setFadeIn(fadeIn: boolean): void
 
是否开启瓦片图层淡入。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fadeIn | boolean | 是 | 是否开启瓦片图层淡入。 - true：开启瓦片图层淡入。 - false：不开启瓦片图层淡入。 |
 
 
**示例：**
 
```text
tileOverlay.setFadeIn(false);
```
 
  

#### setTransparency

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

setTransparency(transparency: number): void
 
设置瓦片图层的透明度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transparency | number | 是 | 瓦片图层的透明度。取值范围：[0, 1]。0表示不透明，1表示全透明，异常值不处理。 |
 
 
**示例：**
 
```text
tileOverlay.setTransparency(0.5);
```
 
  

#### getFadeIn

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getFadeIn(): boolean
 
返回是否开启瓦片图层淡入。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否开启瓦片图层淡入。 - true：已开启瓦片图层淡入。 - false：未开启瓦片图层淡入。 |
 
 
**示例：**
 
```text
let isFadeIn: boolean = tileOverlay.getFadeIn();
```
 
  

#### getTransparency

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

getTransparency(): number
 
返回瓦片图层的透明度。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.3(15)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| number | 返回瓦片图层的透明度。取值范围：[0, 1]，0表示不透明，1表示全透明。 |
 
 
**示例：**
 
```text
let transparency: number = tileOverlay.getTransparency();
```
 
  

#### clearDiskCache

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

clearDiskCache(): Promise&lt;void&gt;
 
清除磁盘缓存，内存缓存也会被清除。使用Promise异步回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |
 
 
**示例：**
 
```text
tileOverlay.clearDiskCache();
```
