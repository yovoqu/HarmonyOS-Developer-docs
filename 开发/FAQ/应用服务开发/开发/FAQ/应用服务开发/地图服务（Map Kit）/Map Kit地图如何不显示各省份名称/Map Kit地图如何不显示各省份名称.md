# Map Kit地图如何不显示各省份名称

更新时间：2026-07-30 01:03:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-43

#### 问题现象

地图缩放到全国的场景下，如何实现不显示各省份名称？
 
 

#### 背景知识

- 开发准备：使用地图服务，需要先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。
- Map Kit提供两种方法设置自定义地图样式：
设置样式ID：使用[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)管理地图样式，并使用样式ID将它们链接到您的地图上。您可以在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)上创建新样式，或导入现有样式定义。样式一旦发布，使用此样式的应用都会自动应用新样式。
- 设置样式内容：通过传入自定义JSON更改地图样式，JSON的定义参见[样式参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style#样式参考)。

 
 
 

#### 解决方案

配置地图自定义JSON的administrative.province为不显示。
 
代码示例如下：
 
```text
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State mapHeight: number = 0;

  aboutToAppear(): void {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    <em>// 地图初始化参数</em>
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 4
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        <em>// 自定义样式参数</em>
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[
                            {
                                "mapFeature": "administrative.province",
                                "options": "all",
                                "visibility": false
                            }
                        ]`
        };
        <em>// 设置自定义样式</em>
        await this.mapController.setCustomMapStyle(param);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight);
      }.width('100%');
    }.height('100%')
    .ignoreLayoutSafeArea();
  }
}
```
 
实现效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Is19QoMnT5uwEen40-YBGw/zh-cn_image_0000002656002802.png?HW-CC-KV=V1&HW-CC-Date=20260811T005610Z&HW-CC-Expire=86400&HW-CC-Sign=2B60FED6FE50FC76BD273F2FF0155B27E891A94A69EFF50223CA682022530031)
