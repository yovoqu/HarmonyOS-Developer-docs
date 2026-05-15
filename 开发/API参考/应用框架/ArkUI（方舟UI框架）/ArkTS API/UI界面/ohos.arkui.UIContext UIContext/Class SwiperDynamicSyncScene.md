# Class (SwiperDynamicSyncScene)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-swiperdynamicsyncscene
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供Swiper组件相关帧率的配置。


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type12+ | [SwiperDynamicSyncSceneType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#swiperdynamicsyncscenetype12) | 是 | 否 | Swiper的动态帧率场景。 |


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
          let scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
          if (scenes) {
            this.scenes = scenes;
          }
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
