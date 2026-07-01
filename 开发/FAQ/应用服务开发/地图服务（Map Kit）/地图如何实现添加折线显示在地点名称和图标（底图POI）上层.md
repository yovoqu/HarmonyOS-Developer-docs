# 地图如何实现添加折线显示在地点名称和图标（底图POI）上层

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-27

## 地图如何实现添加折线显示在地点名称和图标（底图POI）上层
 


##### 问题现象

地图添加折线后，折线显示在了地点名称和图标（底图POI）的下层，对折线有遮挡，如何让折线显示在上层。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/houvVXnGTdWk_4s8cufwmg/zh-cn_image_0000002658913579.png?HW-CC-KV=V1&HW-CC-Date=20260701T025841Z&HW-CC-Expire=86400&HW-CC-Sign=3F62851EF41EEE519D2ED50023820C7491334ACE78966EB3AB175C11F902A8FF)

 
 

##### 背景知识

- 开发准备：使用地图服务，需要先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。
- [setDisplayOrder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#section10934934202319)：设置地图元素的显示顺序，按照从低到高排列，即后面的覆盖物会压盖前面的覆盖物。从底层到上层，默认顺序为：OVERLAY（覆盖物，包括折线、动态轨迹等）、POI（底图POI）、CUSTOM_POI（点注释、气泡）、MARKER。

 
 

##### 解决方案

调整元素显示顺序，让OVERLAY（包括折线）元素显示在POI的上层。
 
```text
let mapElementTypeArr: ArraymapCommon.MapElementType> = [
  mapCommon.MapElementType.POI,
  mapCommon.MapElementType.OVERLAY,
  mapCommon.MapElementType.CUSTOM_POI,
  mapCommon.MapElementType.MARKER];
this.mapController?.setDisplayOrder(mapElementTypeArr);
```
 
完整代码：
 
```text
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct AddPolylineOrder {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallbackmap.MapComponentController>;

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let mapElementTypeArr: ArraymapCommon.MapElementType> = [
          mapCommon.MapElementType.POI,
          mapCommon.MapElementType.OVERLAY,
          mapCommon.MapElementType.CUSTOM_POI,
          mapCommon.MapElementType.MARKER];
        this.mapController?.setDisplayOrder(mapElementTypeArr);

        let polylineOption: mapCommon.MapPolylineOptions = {
          points: [
            { latitude: 31.984410259206815, longitude: 118.76625379397866 },
            { latitude: 31.979410259206815, longitude: 118.75625379397866 },
          ],
          clickable: true,
          startCap: mapCommon.CapStyle.BUTT,
          endCap: mapCommon.CapStyle.BUTT,
          jointType: mapCommon.JointType.BEVEL,
          color: 0xFF0A59F7,
          width: 20
        };
        let polyline = await this.mapController?.addPolyline(polylineOption);
        console.info(`add polyline success, polyline is ${polyline}`);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
      }.width('100%')
    }.height('100%')
  }
}
```
