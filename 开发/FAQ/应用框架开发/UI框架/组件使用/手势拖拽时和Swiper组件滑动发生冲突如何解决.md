# 手势拖拽时和Swiper组件滑动发生冲突如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-810

#### 问题现象

当Swiper组件与子组件发生手势冲突，或者Swiper组件的滑动与嵌套了Swiper的外部组件的gesture手势冲突时，如何解决？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VloEHRzcShiQJ2spexrtGg/zh-cn_image_0000002628557800.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041323Z&HW-CC-Expire=86400&HW-CC-Sign=8E0143D39C0D2C986F1E140908C775AB472DE5E3C6A102323FE6757BB2455859)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件是滑块视图容器，提供子组件滑动轮播显示的能力。
- [TapGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture)手势支持单击、双击和多次点击事件的识别。

 
 

#### 解决方案

Swiper嵌套的页面包含[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)时，使Canvas不响应左右滑动事件，不会触发Swiper切换显示。可以通过以下步骤实现：
 1. 通过[priorityGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings#prioritygesture)给画布绑定优先识别手势，使得画布组件Canvas优先于其他组件响应滑动事件。
2. 通过[触摸测试控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)来处理滑动冲突，确保在滑动Swiper时，Canvas组件不会被滑动。
3. 在主组件Index中，创建Swiper组件，同时在Swiper中调用自定义组件CanvasExample，使得画布在Swiper的页面中可见。
 
```text
@Component
struct CanvasExampleOne {
 <em> // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。</em>
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
 <em> // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。</em>
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Text('Canvas');
   <em>   // 在canvas中调用CanvasRenderingContext2D对象。</em>
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffffff')
        .onReady(() => {
     <em>     // 可以在这里绘制内容。</em>
          this.context.strokeRect(50, 50, 200, 150);
        })
        .priorityGesture(GestureGroup(GestureMode.Exclusive,
          SwipeGesture()
            .onAction(() => {
              console.info(`Canvas响应，swiper不响应`);
            })
        ))
        .hitTestBehavior(HitTestMode.Block)
        .width('80%')
        .height('50%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffbfffff');
  }
}

@Entry
@Component
struct GestureDragAndSwiper {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      Text('0')
        .width('100%')
        .height('100%')
        .backgroundColor('#ff96b1ff')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('1')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffdcc6')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('2')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffc9ffd9')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      CanvasExampleOne();
    }.loop(false);
  }
}
```
 
 

#### 常见FAQ

Q：场景二中除了使用优先识别手势priorityGesture，还有其他替代方案吗？
 
A：可以使用自定义手势判定方法[onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)，实现对[手势的自定义判定](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#示例1自定义手势判定)。
