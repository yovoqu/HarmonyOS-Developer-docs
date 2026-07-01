# 如何控制Swiper组件只能向一个方向滑动

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-503

#### 问题现象

在使用Swiper组件时，需要控制Swiper组件只往一个方向滑动，例如：
 
期望只能向右滑动，实际在使用onGestureRecognizerJudgeBegin拦截滑动手势时，先向右滑动不松手，再快速向左滑动Swiper组件会向左滑动并翻页与预期不符。具体现象如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/wpneRZIqSGCcLfRD4HTklQ/zh-cn_image_0000002628388618.png?HW-CC-KV=V1&HW-CC-Date=20260701T041310Z&HW-CC-Expire=86400&HW-CC-Sign=5DBD84A47CF9CD12811EC21FAC43F27C4590024AAF849DB2DAD61439A9003C24)

 
问题代码如下：
 
```text
@Entry
@Component
struct Index {
  @State list: string[] = ['1', '2', '3'];
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string, index: number) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(8);
        }, (item: string) => item);
      }
      .loop(true)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
        recognizers: Array<GestureRecognizer>) => {
      <em>  // 判断手势识别器的类型</em>
        if (current.getType() === GestureControl.GestureType.PAN_GESTURE) {
          let pan: PanGestureEvent = event as PanGestureEvent;
        <em>  // 获取手势事件偏移量X</em>
          if (pan.offsetX < 0) {
            current.setEnabled(true);
            return GestureJudgeResult.CONTINUE;
          } else {
            current.setEnabled(false);
          <em>  // 判定手势结果为失败</em>
            return GestureJudgeResult.REJECT;
          }
        }
        return GestureJudgeResult.CONTINUE;
      })
      .prevMargin(100)
      .height(400);
    }
    .width('100%')
    .height('100%');
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ntikjJMnSK-9LfXQkKF3lw/zh-cn_image_0000002628548518.png?HW-CC-KV=V1&HW-CC-Date=20260701T041310Z&HW-CC-Expire=86400&HW-CC-Sign=6650EF719A01995789DE85010243D15D368A1DCC0FC90C18A9A83C51A8F9A7DD)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)：滑块视图容器，提供子组件滑动轮播显示的能力；
- [onGestureRecognizerJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement#ongesturerecognizerjudgebegin13)：自定义手势识别器判定回调，可以获取Swiper组件进行手势滑动时的offsetX从而判断是向右滑动还是向左滑动，再通过返回[GestureJudgeResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common#gesturejudgeresult11)手势判定结果，实现控制Swiper组件单一方向滑动的需求。

 
 

#### 解决方案

使用onGestureRecognizerJudgeBegin回调时，按住Swiper组件先向一个方向滑动，不松手再快速向另一个方向滑动时，Swiper组件会向另一个方向滑动并翻页，排查后发现在不松手滑动时Swiper组件不会逐帧触发onGestureRecognizerJudgeBegin回调，因此无法逐帧拦截滑动手势。
 
可以将[disableSwipe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#disableswipe8)设置为true，禁止组件滑动切换功能，并且通过PanGesture手势获取滑动的速度，从而判断是调用showNext()还是showPrevious()方法，从而控制Swiper组件只能往一个方向滑动。代码示例如下：
 
```text
@Entry
@Component
struct SwiperLimitTest {
  @State list: string[] = ['1', '2', '3'];
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.list, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(160)
            .backgroundColor('#F1F3F5')
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .borderRadius(8)
            .parallelGesture(
              PanGesture().onActionEnd(e => {
              <em>  // 手势结束，获取当前的速度</em>
                let velocityX = e.velocityX || 0;
                if (velocityX < 0) {
                 <em> // x轴方向速度小于0时，向左移动</em>
                  this.swiperController.showNext();
                }
              })
            )
        }, (item: string) => item);
      }
      .disableSwipe(true)
      .loop(true)
      .itemSpace(5)
      .prevMargin(35)
      .nextMargin(35)
      .prevMargin(100)
      .height(400);
    }
    .width('100%')
    .height('100%');
  }
}
```
