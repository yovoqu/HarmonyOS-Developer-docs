# Swiper组件禁止手动滑动

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-690

#### 问题现象

如何能禁止如下图Swiper组件的手动滑动？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/zwsz1Lx5TNCGPS-gwRYw0g/zh-cn_image_0000002628394854.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=D046186059ABC92CC5D0F9FF7664AA02F5E8E3111FCBA803A964666894CC17BC)

 
 

#### 背景知识

- [disableSwipe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#disableswipe8)：设置禁用组件滑动切换功能。
- [enabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable#enabled)：设置组件是否可交互。当未设置enabled时，组件默认可交互。
- [showNext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#shownext)：翻至下一页。
- [showPrevious](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#showprevious)：翻至上一页。

 
 

#### 解决方案

- 方案一：禁止手动滑动，但保留导航点功能。通过设置Swiper组件的disableSwipe属性为true实现禁止手动滑动功能。

  代码示例如下：
```text
@Entry
@Component
struct DisableSwiperOne {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      ForEach(['1', '2', '3'], (item: string) => {
        Text(`Item${item}`)
          .width('100%')
          .height(250)
          .backgroundColor('#F1F3F5')
          .textAlign(TextAlign.Center)
          .fontSize(30)
      })
    }
    .indicator(true)
    .disableSwipe(true) <em>// 设置禁止手势滑动，点击导航点依旧可以滑动</em>
    .displayCount(1)
    .padding(16)
  }
}
```


  效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/FlsQiHzkRRCC9Bi7H--3Wg/zh-cn_image_0000002658914073.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=7B6C30ECCBBF7EFBBDF81050BA95DA638C8163C560A89AEA1D258609771B5D93)

- 方案二：禁止手动滑动和导航点切换。通过设置enabled属性为false，使Swiper组件不可交互，不响应事件。此时Swiper组件可以通过[SwiperController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#swipercontroller)的showNext和showPrevious方法进行翻页。

  代码示例如下：

  
```text
@Entry
@Component
struct DisableSwiperTwo {
  private swiperController: SwiperController = new SwiperController();
  @State canSwiper: boolean = true;<em> // 设置组件是否可交互</em>

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(['1', '2', '3'], (item: string) => {
          Text(`Item${item}`)
            .width('100%')
            .height(250)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
        })
      }
      .indicator(true)
      .enabled(this.canSwiper)
      .displayCount(1)
      .padding(16)

      Column({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          })
        Button('canSwiper')
          .onClick(() => {
            this.canSwiper = !this.canSwiper;
          })
      }.margin(5)
    }
  }
}
```
 效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/GzoOxk12RBqyrjCrtaDkYg/zh-cn_image_0000002658794121.png?HW-CC-KV=V1&HW-CC-Date=20260730T072325Z&HW-CC-Expire=86400&HW-CC-Sign=924B59861A7E4667197474AF330388F9DBBAB709133443817AFEF132BBB031EC)
