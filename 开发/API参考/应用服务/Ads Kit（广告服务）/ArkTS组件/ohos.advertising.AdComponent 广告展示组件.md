# @ohos.advertising.AdComponent (广告展示组件)

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent
**支持设备：** Phone | PC/2in1 | Tablet

本模块提供展示广告的能力，覆盖了原生、贴片、开屏等广告样式。

> [!NOTE]
> 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet

```text
import { AdComponent } from '@kit.AdsKit';
```



#### AdComponent

**支持设备：** Phone | PC/2in1 | Tablet

```text
AdComponent({
  ads: advertising.Advertisement[],
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener,
  @BuilderParam adRenderer?: () => void,
  @Prop rollPlayState?: number
})
```

广告展示组件，提供展示原生、贴片、开屏等广告的能力。

**装饰器类型：**@Component

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ads | advertising.Advertisement[] | 是 | 广告对象数组。 说明：非贴片广告类型，组件只展示数组第一个数据。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| displayOptions | advertising.AdDisplayOptions | 是 | 广告展示参数。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| interactionListener | advertising.AdInteractionListener | 是 | 广告状态变化回调。 元服务API：从API version 12开始，该接口支持在元服务中使用。 |
| adRenderer12+ | () => void | 否 | 应用自渲染广告样式。应用自渲染广告样式为受限使用能力，具体请前往流量变现官网客服支持进行咨询。 元服务API：从API version 20开始，该接口支持在元服务中使用。 装饰器类型：@BuilderParam |
| rollPlayState15+ | number | 否 | 用于对外提供贴片广告播放状态，设置1为播放，2为暂停，默认值为2，其他值为非法值，不改变之前的播放状态。在贴片广告所在页面需要通过@State关联属性，使用方法参考示例代码。 元服务API：从API version 20开始，该接口支持在元服务中使用。 装饰器类型：@Prop |


> [!NOTE]
> 为了保证广告能正确展示，该接口必须和请求广告接口配套使用。效果和使用方法可参考 原生广告 、 贴片广告 、 开屏广告 接入和展示。


**示例：**

```text
import { AdComponent, advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 请求到的广告内容
  private ads: advertising.Advertisement[] = [];
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {};

  build() {
    Column() {
      AdComponent({
        ads: this.ads,
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
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```



#### build

**支持设备：** Phone | PC/2in1 | Tablet

build(): void

用于创建AdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
