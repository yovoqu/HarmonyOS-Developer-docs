# ArcSwiper如何适配表冠

更新时间：2026-06-15 08:43:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-439

可以滑动的组件需要适配旋转表冠，默认支持的组件在获焦时即可响应表冠事件。
 1. 默认支持表冠事件的组件: Slider、DatePicker、TextPicker、 TimePicker、Scroll、List、Grid、WaterFlow、ArcList、Refresh和ArcSwiper。默认支持组件只需要添加.focusable(true)、 .focusOnTouch(true)、.defaultFocus(true)属性获焦即可响应。
2. 通过onDigitalCrown监听表冠事件。示例代码如下：

  
```text
import {
  ArcSwiper,
  ArcSwiperAttribute,
  ArcDotIndicator,
  ArcDirection,
  ArcSwiperController
} from '@kit.ArkUI';

@Entry
@Component
struct ArcSwiperDemo {
  @State currentIndex: number = 0;
  private swiperController: ArcSwiperController = new ArcSwiperController();

  build() {
    ArcSwiper(this.swiperController) {
      Text('page 1')
        .width('100%').height('100%').backgroundColor(Color.Red)
      Text('page 2')
        .width('100%').height('100%').backgroundColor(Color.Green)
      Text('page 3')
        .width('100%').height('100%').backgroundColor(Color.Blue)
    }
    .focusable(true)
    .focusOnTouch(true)
    .defaultFocus(true)
    .onDigitalCrown((event: CrownEvent) => {
      if (event.degree > 0) {
        this.swiperController.showNext();
      } else if (event.degree < 0) {
        this.swiperController.showPrevious();
      }
    })
  }
}
```

 
**参考链接**
 
[表冠事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown)
 
[焦点控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus)
 
[ArcSwiper示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#示例)
