# Interface (IndoorMapInfo)

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-indoormapinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { map } from '@kit.MapKit';
```
 
  

#### IndoorMapInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

室内图信息。使用[on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager#onindoormapenter)(type: 'indoorMapEnter', callback: Callback<[IndoorMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-indoormapinfo)>)方法会在进入室内图时触发回调，并返回[IndoorMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-indoormapinfo)类型的实例。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.1.1(19)
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buildingId | string | 否 | 否 | 表示建筑物的id。 |
| floorNames | string[] | 否 | 否 | 建筑物楼层名称数组。 |
| floorOrders | number[] | 否 | 否 | 建筑楼层顺序数组。 |
| currentFloorName | string | 否 | 否 | 当前展示楼层的名称。 |
 
 
**示例：**
 
```text
mapEventManager.on('indoorMapEnter', (indoorMapInfo: map.IndoorMapInfo)=>{
  console.info('indoorMapinfo: ' , indoorMapInfo);
})
```
