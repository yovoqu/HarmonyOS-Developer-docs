# @ohos.advertising.AutoAdComponent (轮播广告展示组件)

更新时间：2026-04-24 08:10:21

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent
**支持设备：** Phone | PC/2in1 | Tablet

本模块提供展示轮播广告的能力。
 
> [!NOTE]
> 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### 导入模块

```text
import { AutoAdComponent } from '@kit.AdsKit';
```
 
  

##### AutoAdComponent

```text
AutoAdComponent({
  adParam: advertising.AdRequestParams,
  adOptions: advertising.AdOptions,
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener
})
```
 
用于展示轮播广告的组件。
 
**装饰器类型：**@Component
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Advertising.Ads
 
**参数：**
  
| 参数名 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| adParam | advertising.AdRequestParams | 是 | - | 广告请求参数。 |
| adOptions | advertising.AdOptions | 是 | - | 广告配置参数。 |
| displayOptions | advertising.AdDisplayOptions | 是 | - | 广告展示参数。 |
| interactionListener | advertising.AdInteractionListener | 是 | - | 广告状态变化回调。 |
 
 
**示例：**
 
```text
import { advertising, AutoAdComponent } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 广告请求参数
  private adRequestParams: advertising.AdRequestParams = {
    // 广告位ID
    adId: 'h5xkz3mbr2',
    // 广告类型
    adType: 8,
    // 广告位宽，单位vp
    adWidth: 360,
    // 广告位高，单位vp
    adHeight: 57
  };
  // 广告配置参数
  private adOptions: advertising.AdOptions = {};
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {
    // 广告轮播的时间间隔，单位ms，取值范围[30000, 120000]
    refreshTime: 30000
  };
  private ratio: number = -1;

  aboutToAppear() {
    if (this.adRequestParams.adWidth && this.adRequestParams.adHeight) {
      this.ratio = this.adRequestParams.adWidth / this.adRequestParams.adHeight;
    }
  }
  
  build() {
    Column() {
      AutoAdComponent({
        adParam: this.adRequestParams,
        adOptions: this.adOptions,
        displayOptions: this.adDisplayOptions,
        interactionListener: {
          onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
            switch (status) {
              case 'onAdOpen':
                hilog.info(0x0000, 'testTag', 'onAdOpen');
                break;
              case 'onAdClick':
                hilog.info(0x0000, 'testTag', 'onAdClick');
                break;
              case 'onAdClose':
                hilog.info(0x0000, 'testTag', 'onAdClose');
                break;
            }
          }
        }
      })
        .width('100%')
        .aspectRatio(this.ratio)
    }
    .width('100%')
    .height('100%')
  }
}
```
 
**效果图：**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Ebt__649QsOfg026N9IOYw/zh-cn_image_0000002581274942.png?HW-CC-KV=V1&HW-CC-Date=20260528T013445Z&HW-CC-Expire=86400&HW-CC-Sign=C1E3F66D39E1EBBC0F5019E73DB5E2C921E38FFF2622BCB4E850C9AA01F27E67)

 
  

##### build

build(): void
 
用于创建AutoAdComponent对象的构造函数。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Advertising.Ads
