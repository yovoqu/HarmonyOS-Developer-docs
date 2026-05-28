# MapComponent（地图组件）

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-mapcomponent
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

本模块提供Map组件，您需要提供mapOptions和回调，通过回调获取MapComponentController对象。
 
**起始版本：** 4.1.0(11)
  

##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
import { MapComponent } from '@kit.MapKit';
```
 
  

##### MapComponent

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

MapComponent提供map组件，通过回调获取MapComponentController对象。
 
**装饰器类型：** @Component
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
**参数**：
  
| 名称 | 类型 | 只读 | 可选 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- | --- |
| mapOptions | mapCommon.MapOptions | 否 | 否 | NA | 地图初始化参数。 |
| mapCallback | AsyncCallback<map.MapComponentController> | 否 | 否 | NA | 回调函数，当地图初始化成功，err为undefined，data为获取到的map.MapComponentController；否则为错误对象。 |
| customInfoWindow | customInfoWindowCallback | 否 | 是 | @BuilderParam | 自定义信息窗，显示一个自定义样式的信息窗，可用于展示标记相关的详细信息。 |
 
 
**示例：**
 
```text
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { customInfoWindowCallback } from '@hms.core.map.MapComponent';

@Entry
@Component
struct MarkerDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private mapCallback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.120750,
          longitude: 118.788765
        },
        zoom: 15
      }
    }

    this.mapCallback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.120750,
            longitude: 118.788765
          },
          clickable: true,
          // 设置信息窗标题
          title: "自定义信息窗"
        };
        await this.mapController?.addMarker(markerOptions);
      }
    }
  }

  build() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.mapCallback,
          // 自定义信息窗
          customInfoWindow: this.customInfoWindow
        })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }

  // 自定义信息窗BuilderParam
  @BuilderParam customInfoWindow: customInfoWindowCallback = this.customInfoWindowBuilder;

  // 自定义信息窗Builder
  @Builder
  customInfoWindowBuilder($$: map.MarkerDelegate) {
    if ($$.marker) {
      Text($$.marker.getTitle())
        .width("50%")
        .height(50)
        .backgroundColor(Color.Green)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .font({ size: 25, weight: 10, style: FontStyle.Italic })
        .border({
          width: 3,
          color: Color.Black,
          radius: 25,
          style: BorderStyle.Dashed
        })
    }
  }
}
```
 
  

##### build

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

build(): void
 
struct的默认构造函数，无法直接调用此方法。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 4.1.0(11)
 
  

##### customInfoWindowCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void
 
自定义信息窗回调。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Map.Core
 
**起始版本：** 5.0.0(12)
 
**参数**：
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| markerDelegate | map.MarkerDelegate | 是 | 用于表示代理对象的标记。 |
