# Map Kit如何知道地图进行了缩放

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-13

#### 问题现象

应用在用户使用过程中需要知道用户是否进行了地图缩放，是否有地图缩放事件通知？
 
 

#### 背景知识

[Map Kit](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-introduction)：具备丰富地图的细节呈现能力，提供了包括缩放、旋转、移动、倾斜等流畅的交互体验。
 
 

#### 解决方案

通过[on(type: 'cameraChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapeventmanager#section1488710318220)监听地图相机状态变化事件，回调里通过zoom是否变化来判断是否有缩放行为。zoom获取方式为：this.mapController?.getCameraPosition().zoom。
 
```text
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';

<em>/**</em>
<em> *</em>
<em> * 1、监听用户是否进行地图缩放</em>
<em> * 2、监听“我的位置”按钮点击事件，并初始化我的位置</em>
<em> */</em>
@Entry
@Component
struct MapOnChangeZoom {
  private mapOption?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

  aboutToAppear(): void {
  <em>  // 地图初始化参数，设置地图中心点坐标及层级</em>
    this.mapOption = {
      position: {
        target: {
          latitude: 30.246,
          longitude: 120.145
        },
        zoom: 17
      },
      zoomControlsEnabled: false,
      myLocationControlsEnabled: true
    };

   <em> // 地图初始化的回调</em>
    this.callback = async (err, mapController) => {
      if (!err) {
      <em>  // 获取地图的控制器类，用来操作地图</em>
        this.mapController = mapController;
     <em>   // 启用我的位置图层</em>
        this.mapController?.setMyLocationEnabled(true);

        let mapEventManager = mapController.getEventManager();
        let cameraChangeCallback = (position: mapCommon.LatLng) => {
          console.info('cameraChange', `callback position = ${position.longitude}`);
        <em>  // 获取当前地图缩放级别，通过zoom是否变化来判断是否有缩放行为</em>
          let zoom = this.mapController?.getCameraPosition().zoom;
          console.info('cameraChange', `callback zoom = ${zoom}`);
        };
        mapEventManager.on('cameraChange', cameraChangeCallback);

      <em>  // 监听“我的位置”按钮点击事件</em>
        this.mapController.on('myLocationButtonClick', () => {
          console.info('myLocationButtonClick', `myLocationButtonClick`);
          this.getMyLocation();
        });

       <em> // 初始化我的位置</em>
        this.getMyLocation();
      }
    };
  }

  build() {
    Column() {
      MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback }).width('100%').height('100%');
    };
  }

<em>  // 获取当前位置并视图移动过去</em>
  getMyLocation() {
    geoLocationManager.getCurrentLocation().then(async (result) => {
      let position: geoLocationManager.Location = {
        'latitude': result.latitude,
        'longitude': result.longitude,
        'altitude': 0,
        'accuracy': 0,
        'speed': 0,
        'timeStamp': 0,
        'direction': 0,
        'timeSinceBoot': 0
      };

      this.mapController?.setMyLocation(position);
    <em>  // 创建CameraUpdate对象</em>
      let gcj02Position: mapCommon.LatLng = await this.convertCoordinate(result.latitude, result.longitude);
      let latLng: mapCommon.LatLng = {
        latitude: gcj02Position.latitude,
        longitude: gcj02Position.longitude
      };
      let zoom = 17;
      let cameraUpdate = map.newLatLng(latLng, zoom);
   <em>   // 以动画方式移动地图相机</em>
      this.mapController?.animateCamera(cameraUpdate, 1000);
    });
  }

  async convertCoordinate(latitude: number, longitude: number): Promise<mapCommon.LatLng> {
    let wgs84Position: mapCommon.LatLng = {
      latitude: latitude,
      longitude: longitude
    };
    let gcj02Position: mapCommon.LatLng =
      await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);

    return gcj02Position;
  }
}
```
