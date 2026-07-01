# 屏蔽Swiper组件切换效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1426

## 屏蔽Swiper组件切换效果
 


##### 问题现象

如何实现子组件的指定区域不允许滑动切换外部Swiper，但可以滚动内部的Scroll的功能。
 
 

##### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/_LUscq1ZQ9eLqels1dby6A/zh-cn_image_0000002628763646.gif?HW-CC-KV=V1&HW-CC-Date=20260701T025656Z&HW-CC-Expire=86400&HW-CC-Sign=A630FACD258412098DDE1D553D83A42AA5754994F8DC370632E1624B1B5734FB)

 
 

##### 背景知识

[PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)滑动手势事件可实现自定义手势事件。
 
 

##### 解决方案

在需要屏蔽Swiper组件切换效果的组件上使用PanGesture消费掉左右滚动事件。
 
```text
@Entry
@Component
struct TestSwiperPage {
  private swiperController: SwiperController = new SwiperController();
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Swiper(this.swiperController) {
        Text('前')
          .width('90%')
          .height('90%')
          .textAlign(TextAlign.Center)
          .fontSize(15);
        Scroll() {
          Column() {
            Column() {
              Text('此区域不可正常操作').fontColor(Color.Black).fontSize(15);
            }
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center)
            .height(200)
            .width('100%')
            .backgroundColor('#ffcdc9c9')
            .gesture(
              PanGesture(this.panOption)
            );

            Column() {
              Text('此区域可正常操作').fontColor(Color.Black).fontSize(15).margin({ top: 200 });
            }.height(2000)
            .width('100%')
            .backgroundColor('#ff97b6f3');
          };
        }
        .width('90%')
        .height('100%');

        Text('后')
          .width('90%')
          .height('90%')
          .textAlign(TextAlign.Center)
          .fontSize(15);
      }
      .interval(3000)
      .autoPlay(false)
      .height('100%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White);
  }
}
```
