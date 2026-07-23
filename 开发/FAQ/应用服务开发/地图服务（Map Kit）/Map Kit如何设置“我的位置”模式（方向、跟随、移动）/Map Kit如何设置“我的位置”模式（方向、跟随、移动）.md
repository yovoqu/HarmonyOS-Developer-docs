# Map Kit如何设置“我的位置”模式（方向、跟随、移动）

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-49

#### 问题现象

Map Kit地图服务提供自带的“我的位置”图标显示，但应用有时需根据业务自定义“我的位置”的显示策略，如“我的位置”图标是否显示设备方向、图标是否跟随设备位置移动、相机是否跟随位置移动到屏幕中心等。
 
 

#### 背景知识

- [setMyLocationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#section126791641317)：设置用户的位置样式。
- [MyLocationStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section3713124215275)：自定义“我的位置”样式。
- [MyLocationDisplayType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#section78428244375)：定位图标的展示模式。可以设置是否连续定位、是否跟随设备移动、是否跟随设备方向旋转、相机是否跟随移动到“我的位置”为屏幕中心。默认为连续定位，相机不移动到“我的位置”，定位蓝点跟踪设备移动。
- 前提条件：
使用地图服务，需要先[开通地图服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc#section16133115441516)。
- 使用“我的位置”能力需声明和向用户授权ohos.permission.LOCATION、ohos.permission.APPROXIMATELY_LOCATION权限。

 
 
 

#### 解决方案

- **场景一：显示或隐藏“我的位置”图标。**设置[setMyLocationEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#section201759451313)为true表示显示“我的位置”图标，设置为false表示隐藏“我的位置”图标。
- **场景二：“我的位置”图标跟随设备移动，跟随设备旋转，相机不跟随移动到“我的位置”为屏幕中心。**从版本6.0.0(20)开始MyLocationDisplayType支持TRACK_ROTATE模式，满足此场景需求。

  
```text
let style: mapCommon.MyLocationStyle = {
  anchorU: 0.5,
  anchorV: 0.5,
  radiusFillColor: 0x00000000,
  displayType: mapCommon.MyLocationDisplayType.TRACK_ROTATE
};
this.mapController?.setMyLocationStyle(style);
```
 实现效果：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/v2q9i0eJQsq-gExjZvjk4A/zh-cn_image_0000002658913611.png?HW-CC-KV=V1&HW-CC-Date=20260723T013729Z&HW-CC-Expire=86400&HW-CC-Sign=91E61F3D0897EEDA3F06A3ABDA147C3AE4D8A365D02E8296B0C9901536B5D531)


  完整代码：

  
```text
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { map, MapComponent, mapCommon } from '@kit.MapKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct HuaweiMyLocationDemo {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  @State mapHeight: number = 0;

  async checkPermission(): Promise<void> {
    let applyResult: boolean = false;
    const permissions: Array<Permissions> =
      ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
    for (let permission of permissions) {
      let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
      if (grantStatus == abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        applyResult = true;
      } else {
        applyResult = false;
      }
    }

    if (!applyResult) {
      this.requestPermissions();
    } else {
      <em>// 启用我的位置图层，mapController为地图操作类对象，获取方式详见地图呈现章节</em>
      this.mapController?.setMyLocationEnabled(true);
      <em>// 启用我的位置按钮</em>
      this.mapController?.setMyLocationControlsEnabled(true);
      let style: mapCommon.MyLocationStyle = {
        anchorU: 0.5,
        anchorV: 0.5,
        radiusFillColor: 0x00000000,
        displayType: mapCommon.MyLocationDisplayType.TRACK_ROTATE
      };
      this.mapController?.setMyLocationStyle(style);
    }
  }

  <em>// 向用户申请授权</em>
  requestPermissions(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
      ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'])
      .then(() => {
        <em>// 启用我的位置图层</em>
        this.mapController?.setMyLocationEnabled(true);
        <em>// 启用我的位置按钮</em>
        this.mapController?.setMyLocationControlsEnabled(true);
        let style: mapCommon.MyLocationStyle = {
          anchorU: 0.5,
          anchorV: 0.5,
          radiusFillColor: 0x00000000,
          displayType: mapCommon.MyLocationDisplayType.TRACK_ROTATE
        };
        this.mapController?.setMyLocationStyle(style);
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
      });
  }

  <em>// 获取相应的权限</em>
  async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus:
      abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;
    <em>// 获取应用程序的accessTokenID</em>
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to get bundle info for self. Code is ${err.code},message is ${err.message}`);
    }
    <em>// 校验应用是否被授予权限</em>
    try {
      grantStatus = await atManager.checkAccessToken(tokenId, permission);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to check access token. Code is ${err.code}, message is ${err.message}`);
    }
    return grantStatus;
  }

  aboutToAppear(): void {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    <em>// 地图初始化参数，设置地图中心坐标以及层级</em>
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
      myLocationControlsEnabled: true,
      scaleControlsEnabled: true,
    };
    <em>// 地图初始化的回调</em>
    this.callback = async (err, mapController) => {
      if (!err) {
        <em>// 获取地图的控制器类，用来操作地图</em>
        this.mapController = mapController;
        this.checkPermission();
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight);
      }.width('100%');
    }
    .ignoreLayoutSafeArea();
  }
}
```

- **场景三：“我的位置”图标跟随设备移动，跟随设备旋转，相机跟随移动到“我的位置”为屏幕中心。**将MyLocationDisplayType配置为FOLLOW_ROTATE模式。
- **场景四：“我的位置”图标跟随设备移动，不跟随设备旋转，相机跟随移动到“我的位置”为屏幕中心。**将MyLocationDisplayType配置为FOLLOW模式。
- **场景五：“我的位置”图标跟随设备移动，不跟随设备旋转，相机不跟随移动到“我的位置”为屏幕中心。**将MyLocationDisplayType配置为DEFAULT模式。
- **场景六：“我的位置”图标跟随设备移动，不跟随设备旋转，但显示为设备移动方向，相机跟随移动到“我的位置”为屏幕中心。**默认的“我的位置”显示是设备方向，无法显示设备移动方向，需要创建Marker后，通过[geoLocationManager.on('locationChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanageronlocationchange)动态获取设备移动方向后，设置Marker的角度。请参见[Map Kit地图服务如何设置我的位置图标实时指向当前设备移动方向](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-20)。
- **场景七：单次查看当前设备所在的位置，并移动相机当前位置。**将MyLocationDisplayType配置为LOCATE模式。
