# 如何处理自定义地图通过JSON指定元素无法显示问题

更新时间：2026-08-12 10:47:00

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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/2qHdJEbfTBykqQ8pwcRABA/zh-cn_image_0000002658793645.png?HW-CC-KV=V1&HW-CC-Date=20260813T095555Z&HW-CC-Expire=86400&HW-CC-Sign=F5EBD6E098715B4F2EFDA8239F6E1F4B8223F55ED65DB0104A846D26F68D46CC)

 
 

#### 背景知识

[显示自定义地图](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style)提供两种方法设置自定义地图样式，其中一种方式设置样式内容：通过传入自定义JSON更改地图样式，JSON的定义参见[样式参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style#样式参考)。
 
 

#### 问题定位

- 查看JSON定义地图样式是否正确。要实现隐藏地图中的交通网，需要定义visibility是否可见属性，true：可见，false：不可见。JSON代码中visibility配置hidden为无效参数。
- 检查自定义样式参数JSON使用是否正确。可以直接放入初始化aboutToAppear()中。也可以通过资源文件传入。

 
 

#### 分析结论

隐藏地图中的交通网Road元素类型需要设置为不可见。visibility为是否可见属性，需设置为false不可见。
 
 

#### 修改建议

前提条件：请优先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#开通地图服务)，如需设置沉浸式请参考[窗口全屏布局方案](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#窗口全屏布局方案)。
 
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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/gjdrvRkcRyqywx1etu6MbA/zh-cn_image_0000002628554280.png?HW-CC-KV=V1&HW-CC-Date=20260813T095555Z&HW-CC-Expire=86400&HW-CC-Sign=F935C723FEF17A2EC84119B858736DF9C3C106A3B054E2D6447A8F5491074BA3)

- 代码示例如下：
```json
// 引入MapKit组件
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
export struct Index {
  // MapKit相关配置
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  mapStyle: string = "";
  uiContext = this.getUIContext();

  aboutToAppear(): void {
    // 获取地图样式json串
    try {
      this.uiContext?.getHostContext()?.resourceManager.getRawFileContent("mapStyle.json").then((value: Uint8Array) => {
        let textDecoder: util.TextDecoder = util.TextDecoder.create(); // 调用util模块的TextDecoder类
        let retStr: string = textDecoder.decodeToString(value); // 对Uint8Array解码
        this.mapStyle = retStr;
      }).catch((error: BusinessError) => {
        console.error(`getRawFileContent promise error is ${error}`);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`promise getRawFileContent failed, error code: ${code}, message: ${message}.`);
    }
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: this.mapStyle
        };
        this.mapController.setCustomMapStyle(param);
      }
    };
  }

  onPageShow(): void {
    // 将地图切换到前台
    if (this.mapController) {
      this.mapController.show();
    }
  }

  onPageHide(): void {
    // 将地图切换到后台
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
