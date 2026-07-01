# Types

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-types
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

#### MassPointOverlayCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void
 
回调函数，无返回结果。用于监听海量点图层的点击事件。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 6.0.0(20)
 
**参数**：
  
| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| massPointOverlay | MassPointOverlay | 是 | 海量点管理对象。 |
| massPointItem | mapCommon.MassPointItem | 是 | 海量点项。 |
