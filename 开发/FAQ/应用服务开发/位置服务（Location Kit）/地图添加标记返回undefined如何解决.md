# 地图添加标记返回undefined如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-20

## 地图添加标记返回undefined如何解决
 


##### 问题现象

在地图的指定位置添加标记，但地图没有显示标记，添加标记返回undefined，如何解决？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/xV01HIRNR3e9AjMLY6Xf-A/zh-cn_image_0000002658913755.png?HW-CC-KV=V1&HW-CC-Date=20260701T025853Z&HW-CC-Expire=86400&HW-CC-Sign=C4F5755EA828319E153C7957AFE421BF5ACBABA6A11D0D127AA1BD5FD4B3DBDC)

 
 
问题代码示例如下：
 
```text
@Entry
@Component
struct MarkerPage {

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 10
      },
      myLocationControlsEnabled: true
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        mapController.setMyLocationEnabled(true);
        mapController.setMyLocationControlsEnabled(true)
        let callback = () => {
        }
        this.mapEventManager.on("mapLoad", callback);
      }
    };
  }

  build() {
    NavDestination() {
      Stack() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
      }
    }
    .onReady(async (context) => {
      if (context) {
        this.pathStack = context.pathStack
        let position: mapCommon.LatLng = {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        };
        let markerOptions: mapCommon.MarkerOptions = {
          position: position
        };
        this.marker = await this.mapController?.addMarker(markerOptions)
      }
    })
  }
}
```
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7lWGEMfKTAOyWuKrDPYK5A/zh-cn_image_0000002658793809.png?HW-CC-KV=V1&HW-CC-Date=20260701T025853Z&HW-CC-Expire=86400&HW-CC-Sign=ACD3BAC4EDF126557B0BC93E371B9CEFB91735FA7EC39BBBE07CDEB6C1E899A7)

 
 

##### 背景知识

点标记用来在地图上标记任何位置，例如用户位置、车辆位置、店铺位置等一切带有位置属性的事物，具体实现可参考：[开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-marker#section1564972414506)。
 
 

##### 问题定位

- 从代码中看出，添加marker的代码是在NavDestination组件的onReady()方法中实现。
- NavDestination组件即将构建完时会触发onReady()方法，而这时并不能保证Mapkit的callback回调方法已经执行完了，如果执行onReady()方法之前，Mapkit的callback回调方法还没有被触发，那么在onReady()方法中调用mapController对象就会是undefined。

 
 

##### 分析结论

在调用this.mapController对象之前要保证callback回调方法已经执行完成，另外callback回调方法是地图组件MapComponent加载完成之后才会触发。
 
 

##### 修改建议

将this.marker = await this.mapController?.addMarker(markerOptions)相关的代码挪到Mapkit的callback方法里执行，代码示例如下：
 
```text
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MarkerPage {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallbackmap.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;
  pathStack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 10
      },
      myLocationControlsEnabled: true
    };
    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        mapController.setMyLocationEnabled(true);
        mapController.setMyLocationControlsEnabled(true);
        let callback = () => {
        };
        this.mapEventManager.on('mapLoad', callback);

        let position: mapCommon.LatLng = {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        };
        let markerOptions: mapCommon.MarkerOptions = {
          position: position
        };
        try {
          await this.mapController?.addMarker(markerOptions);
        } catch (error) {
          console.error('addMarker error');
        }
      }
    };
  }

  build() {
    NavDestination() {
      Stack() {
        // 调用MapComponent组件初始化地图
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .width('100%')
          .height('75%');
      }
      .height('100%');
    }
    .hideTitleBar(true)
    .onReady(async (context) => {
      if (context) {
        this.pathStack = context.pathStack;
      }
    })
    .onShown(() => {
      if (this.mapController) {
        this.mapController.show();
      }
    })
    .onHidden(() => {
      if (this.mapController) {
        this.mapController.hide();
      }
    });
  }
}
```
