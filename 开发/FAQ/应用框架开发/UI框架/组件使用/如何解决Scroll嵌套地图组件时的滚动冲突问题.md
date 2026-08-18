# 如何解决Scroll嵌套地图组件时的滚动冲突问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1555

#### 问题现象

将地图组件，内嵌到了Scroll里面，会出现上下滑动时同时滚动的问题，如何控制滑动地图时Scroll不响应？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/1Dq-a9xlRX2FvIoH_lKm9g/zh-cn_image_0000002658848495.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041314Z&HW-CC-Expire=86400&HW-CC-Sign=167E33F2CF0EF92BA81C89C6239C2C98D234C7D82272035978C3A163BF1F4099)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/aZKz9j7gSoivpJpqb2xN3w/zh-cn_image_0000002628609232.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041314Z&HW-CC-Expire=86400&HW-CC-Sign=E9C73F92989F03E6EBE5E20C96112D104590ADAC92DB0E55EC63071B7095BA24)

 
 

#### 背景知识

- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，若子组件尺寸不超过父组件则Scroll不提供滚动能力。
- [滚动组件通用接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common)滚动组件通用属性和事件目前只支持List、Grid、Scroll和WaterFlow组件。提供了诸如滚动条、摩擦系数、滚动到组件最后触发的回调注册等。
- 在使用地图服务之前，需要先通过DevEco Studio或AppGallery Connect网站开通地图服务，详情可见官网指南[开发准备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc)。

 
 

#### 解决方案

Scroll中嵌套地图组件的情况，可以在MapComponent的onTouch事件中确认父组件Scroll的滑动状态，若点击到地图则Scroll不响应滑动，松开时恢复。
 
在onTouch回调函数中，使用switch语句根据触摸事件的类型来更新地图组件的滚动方向：
 
- 当触摸事件类型为TouchType.Down时，表示开始触摸，此时设置this.scrollable为ScrollDirection.None，表示停止滚动。
- 当触摸事件类型为TouchType.Up或TouchType.Cancel时，表示停止触摸或取消操作，此时设置this.scrollable为ScrollDirection.Vertical，表示允许垂直滚动。

 
> [!NOTE]
> 地图组件在 开通地图服务 后才可以正常加载地图信息。

 
在EntryAbility中配置沉浸式，示例代码如下：
 
```json
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
    });

    windowStage.loadContent('pages/MapDemo', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```
 
完整示例参考如下：
 
```text
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapDemo {
  @State scrollable: ScrollDirection = ScrollDirection.Vertical;
  private mapEventManager?: map.MapEventManager;
  private TAG = 'HuaweiMapDemo';
  private mapOption?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOption = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      }
    };
    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, `on-mapLoad`);
        };
        this.mapEventManager.on('mapLoad', callback);
      }
    };
  }

  build() {
    Stack() {
      Scroll() {
        Column() {
          // 调用MapComponent组件初始化地图
          MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
            .width('100%')
            .height('60%')
            .onTouch((event) => {
              switch (event.type) {
                case TouchType.Down:
                  this.scrollable = ScrollDirection.None;
                  break;
                case TouchType.Up:
                  this.scrollable = ScrollDirection.Vertical;
                  break;
                case TouchType.Cancel:
                  this.scrollable = ScrollDirection.Vertical;
                  break;
              }
            });
          // 用于观测是否跟随滑动
          Text('测试是否可以滑动').width('100%').height('50%').textAlign(TextAlign.Center);
        }
        .width('100%');
      }
      .scrollable(this.scrollable)
      .scrollBar(BarState.Off)
      .width('100%')
      .height('100%');
    }.height('100%');
  }
}
```
