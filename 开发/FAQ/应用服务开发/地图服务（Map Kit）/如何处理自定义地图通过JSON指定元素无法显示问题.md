# 如何处理自定义地图通过JSON指定元素无法显示问题

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-38

#### 问题现象

自定义地图指定的样式JSON如下，无法隐藏地图中的交通网。
 
```json
[
  {
    "mapFeature": "road.city-arterial",
    "visibility": "hidden"
  },
  {
    "mapFeature": "road.highway",
    "visibility": "hidden"
  },
  {
    "mapFeature": "road.minor-road",
    "visibility": "hidden"
  },
  {
    "mapFeature": "road.national",
    "visibility": "hidden"
  },
  {
    "mapFeature": "road.province",
    "visibility": "hidden"
  },
  {
    "mapFeature": "road.sidewalk",
    "visibility": "hidden"
  }
]
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/TxpwT5SASoa7ziZCfZX7-Q/zh-cn_image_0000002658793645.png?HW-CC-KV=V1&HW-CC-Date=20260701T041109Z&HW-CC-Expire=86400&HW-CC-Sign=9519D48FF87A386EF282715AF480E08AC86B071EA9659109C5466DA239CFE022)

 
 

#### 背景知识

[显示自定义地图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style)提供两种方法设置自定义地图样式，其中一种方式设置样式内容：通过传入自定义JSON更改地图样式，JSON的定义参见[样式参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style#section156991344101012)。
 
 

#### 问题定位

- 查看JSON定义地图样式是否正确。要实现隐藏地图中的交通网，需要定义visibility是否可见属性，true：可见，false：不可见。JSON代码中visibility配置hidden为无效参数。
- 检查自定义样式参数JSON使用是否正确。可以直接放入初始化aboutToAppear()中。也可以通过资源文件传入。

 
 

#### 分析结论

隐藏地图中的交通网Road元素类型需要设置为不可见。visibility为是否可见属性，需设置为false不可见。
 
 

#### 修改建议

前提条件：请优先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)，如需设置沉浸式请参考[窗口全屏布局方案](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#section15671730447)。
 
- JSON文件如mapStyle.json中将visibility可见属性应该从hidden改为false。
```json
[
  {
    "mapFeature": "road.city-arterial",
    "visibility": false
  },
  {
    "mapFeature": "road.highway",
    "visibility": false
  },
  {
    "mapFeature": "road.minor-road",
    "visibility": false
  },
  {
    "mapFeature": "road.national",
    "visibility": false
  },
  {
    "mapFeature": "road.province",
    "visibility": false
  },
  {
    "mapFeature": "road.sidewalk",
    "visibility": false
  }
]
```

- JSON文件放入..\entry\src\main\resources\rawfile下。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Mr2O083_QEeYpTyDlqHopw/zh-cn_image_0000002628554280.png?HW-CC-KV=V1&HW-CC-Date=20260701T041109Z&HW-CC-Expire=86400&HW-CC-Sign=216D3A478313AE7806DE9B4BAF1CF0E0044593653B9F477CE9E6B95D1C8F1BBC)

- 代码示例如下：
```json
<em>// 引入MapKit组件</em>
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
export struct Index {
 <em> // MapKit相关配置</em>
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  mapStyle: string = "";
  uiContext = this.getUIContext();

  aboutToAppear(): void {
   <em> // 获取地图样式json串</em>
    try {
      this.uiContext?.getHostContext()?.resourceManager.getRawFileContent("mapStyle.json").then((value: Uint8Array) => {
        let textDecoder: util.TextDecoder = util.TextDecoder.create(); <em>// 调用util模块的TextDecoder类</em>
        let retStr: string = textDecoder.decodeToString(value); <em>// 对Uint8Array解码</em>
        this.mapStyle = retStr;
      }).catch((error: BusinessError) => {
        console.error(`getRawFileContent promise error is ${error}`);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`promise getRawFileContent failed, error code: ${code}, message: ${message}.`);
    }
   <em> // 地图初始化参数，设置地图中心点坐标及层级</em>
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
    };

  <em>  // 地图初始化的回调</em>
    this.callback = async (err, mapController) => {
      if (!err) {
     <em>   // 获取地图的控制器类，用来操作地图</em>
        this.mapController = mapController;
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: this.mapStyle
        };
        this.mapController.setCustomMapStyle(param);
      }
    };
  }

  onPageShow(): void {
   <em> // 将地图切换到前台</em>
    if (this.mapController) {
      this.mapController.show();
    }
  }

  onPageHide(): void {
  <em>  // 将地图切换到后台</em>
    if (this.mapController) {
      this.mapController.hide();
    }
  }

  build() {
    Stack() {
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```
