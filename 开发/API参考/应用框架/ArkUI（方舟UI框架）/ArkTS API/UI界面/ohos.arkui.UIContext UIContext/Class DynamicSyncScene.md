# Class (DynamicSyncScene)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dynamicsyncscene
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供组件自定义场景下相关帧率的配置。


## setFrameRateRange12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setFrameRateRange(range: ExpectedFrameRateRange): void

设置期望帧率范围。

最终结果不一定是设置的帧率，会由系统能力做综合决策，尽量满足开发者的设置帧率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation#expectedframeraterange11) | 是 | 设置期望的帧率范围。 默认值：{min:0, max:120, expected: 120} |


**示例：**


```ts
import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
  private scenes: SwiperDynamicSyncScene[] = [];

  build() {
    Column() {
      Text("动画"+ JSON.stringify(this.ANIMATION))
      Text("跟手"+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(()=>{
          this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
        })
      }

      Button("set frame")
      .onClick(() => {
        this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

          if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
            scenes.setFrameRateRange(this.ANIMATION);
          }

          if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
            scenes.setFrameRateRange(this.GESTURE);
          }
        });
      })
    }
  }
}
```


## getFrameRateRange12+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

getFrameRateRange(): ExpectedFrameRateRange

获取期望帧率范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**


| 类型 | 说明 |
| --- | --- |
| [ExpectedFrameRateRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation#expectedframeraterange11) | 期望帧率范围。 |


**示例：**


```ts
import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30 };
  private scenes: SwiperDynamicSyncScene[] = [];

  build() {
    Column() {
      Text("动画"+ JSON.stringify(this.ANIMATION))
      Text("跟手"+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(() => {
          this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
        })
      }

      Button("set frame")
      .onClick(() => {
        this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

          if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
            scenes.setFrameRateRange(this.ANIMATION);
            scenes.getFrameRateRange();
          }

          if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
            scenes.setFrameRateRange(this.GESTURE);
            scenes.getFrameRateRange();
          }
        });
      })
    }
  }
}
```
