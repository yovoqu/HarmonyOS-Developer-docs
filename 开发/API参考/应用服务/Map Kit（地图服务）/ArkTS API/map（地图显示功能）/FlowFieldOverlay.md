# Interface (FlowFieldOverlay)

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-flowfieldoverlay
**支持设备：** Phone | PC/2in1 | Tablet

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { map, mapCommon } from '@kit.MapKit';
```
 
  

#### FlowFieldOverlay

**支持设备：** Phone | PC/2in1 | Tablet

流场图层管理对象。在调用map.[MapComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller)类的[addFlowFieldOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#addflowfieldoverlay)方法时会返回该类型的实例，继承[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core.EnhancedOverlay
 
**起始版本：** 6.0.0(20)
 
**示例：**
 
```json
let params: mapCommon.FlowFieldOverlayParams = {
  // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式参考
  data: 'xxx'
};
let fieldOverlay = await mapController.addFlowFieldOverlay(params);
```
 
  

#### setStyle

**支持设备：** Phone | PC/2in1 | Tablet

setStyle(style: mapCommon.ParticleStyle): void
 
设置粒子样式。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core.EnhancedOverlay
 
**起始版本：** 6.0.0(20)
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | mapCommon.ParticleStyle | 是 | 粒子样式。 |
 
 
**示例：**
 
```text
let style: mapCommon.ParticleStyle = {
  count: 200,
  color: 0xff009575,
  maxSpeed: 60,
  speedFactor: 0.3
};
fieldOverlay.setStyle(style);
```
 
  

#### getStyle

**支持设备：** Phone | PC/2in1 | Tablet

getStyle(): mapCommon.ParticleStyle
 
获取粒子样式。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core.EnhancedOverlay
 
**起始版本：** 6.0.0(20)
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| mapCommon.ParticleStyle | 粒子样式。 |
 
 
**示例：**
 
```text
let style: mapCommon.ParticleStyle = fieldOverlay.getStyle();
```
