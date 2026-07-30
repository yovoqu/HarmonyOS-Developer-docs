# Swiper如何实现惯性滚动效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1512

#### 问题现象

Swiper组件在滑动时只能一次滚动一页，在需要一次滑动多个页面的场景下效率较低，Swiper组件如何实现惯性滚动效果，提高滑动效率？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/FirrMhCdSSKQurRC15Xcaw/zh-cn_image_0000002658845805.png?HW-CC-KV=V1&HW-CC-Date=20260730T072406Z&HW-CC-Expire=86400&HW-CC-Sign=CC7D2135F2DA343C3CF4E44FE33229B61721DE82C6DEDE3B935C99900CE831B2)

 
 

#### 背景知识

- [parallelGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding#parallelgesture并行手势绑定方法)：parallelGesture是并行的手势绑定方法，在父子组件上绑定可以同时响应的相同手势。
- [changeIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#changeindex15)：Swiper翻页至指定页面。

 
 

#### 解决方案

方案逻辑：向后翻动几页；如果抬手时速度小于设置的值，则保持原来每次翻一页的效果。通过以上逻辑实现快速滑动Swiper时，可以惯性向后翻几页。
 
```text
.parallelGesture( <em>// 同步手势</em>
  PanGesture()
    .onActionEnd(e => {
   <em>   // 手势结束，获取当前的速度</em>
      let velocityX = e.velocityX || 0;
      if (velocityX > 2000) {
        this.swiperController.changeIndex(this.currentIndex - 2, SwiperAnimationMode.FAST_ANIMATION);
      } else if (velocityX < -2000) {
        this.swiperController.changeIndex(this.currentIndex + 2, SwiperAnimationMode.FAST_ANIMATION);
      }
    })
)
```
 
完整示例参考如下：
 
```text
@Entry
@Component
struct Swiper1 {
  private swiperController: SwiperController = new SwiperController();
  private data: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
  private currentIndex: number = 0;

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        ForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor(0xf1f3f5)
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(12)
        }, (index: number) => index.toString())
      }
      .cachedCount(2)
      .index($$this.currentIndex)
      .loop(false)
      .indicator(false)
      .duration(500)
      .itemSpace(5)
      .curve(Curve.Friction)
      .prevMargin(35, true)
      .nextMargin(35, true)
      .parallelGesture( <em>// </em><em>同步手势</em>
        PanGesture()
          .onActionEnd(e => {
          <em>  // 手势结束，获取当前的速度</em>
            let velocityX = e.velocityX || 0;
            if (velocityX > 2000) {
              this.swiperController.changeIndex(this.currentIndex - 2, SwiperAnimationMode.FAST_ANIMATION);
            } else if (velocityX < -2000) {
              this.swiperController.changeIndex(this.currentIndex + 2, SwiperAnimationMode.FAST_ANIMATION);
            }
          })
      )
    }.width('100%')
    .margin({ top: 5 })
  }
}
```
 
 

#### 常见FAQ

Q：如何实现自定义组件滑动时的惯性效果？
 
A：与解决方案同理，使用PanGesture手势即可实现惯性滑动效果，具体可以参考示例[如何通过PanGesture手势或者SwipeGesture手势实现自定义组件的惯性滚动效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-33)。
