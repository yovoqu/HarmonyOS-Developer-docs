# Swiper如何设置数字指示器的背景色

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-812

#### 问题现象

当Swiper修改指示器为数字指示器，如何修改指示器的背景颜色？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/BHDZ-RslSDG_wldOKD9R1Q/zh-cn_image_0000002658797167.png?HW-CC-KV=V1&HW-CC-Date=20260701T041249Z&HW-CC-Expire=86400&HW-CC-Sign=153B54F882C645FE1B1F088BD9B1E4977359F4B85D52BC37FC1B0B6524C3B5B3)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)用于实现滑动切换功能的核心组件，常用于轮播图、图片展示、多页面切换等场景，指示器是用于显示当前滑动的位置。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)是一个用于实现层叠布局的核心组件，它允许将多个子组件按照指定的顺序进行层叠排列，常用于实现弹窗、提示框、覆盖层等需要层级交互的UI场景。

 
 

#### 解决方案

Swiper的[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicator15)属性提供了设置导航点指示器样式的能力，其中DigitIndicator为数字指示器样式，但并未暴露出可修改背景色样式的能力。可通过使用Stack提供的层叠能力结合Swiper组件的onChange事件，监听当前所处页数来自定义指示器实现。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct SwiperIndicator {
  private swiperData: number[] = [1, 2, 3, 4, 5];
  @State curIndex: number = 1;

  build() {
    Stack() {
      Swiper() {
        ForEach(this.swiperData, (item: number) => {
          Column() {
            Text(item.toString())
              .fontColor(Color.White);
          }
          .width('100%')
          .backgroundColor(Color.Gray)
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center);
        });
      }
      .onChange((index: number) => {
        // 修改计数器
        this.curIndex = index + 1;
      })
      .padding(10)
      .indicator(false)
      .width('100%')
      .height(300);

      Row() {
        Text(this.curIndex.toString())
          .fontColor(Color.Black);
        Text('/')
          .fontColor(Color.Black);
        Text(this.swiperData.length.toString())
          .fontColor(Color.Black);
      }
      .padding({
        left: 6,
        right: 6,
        top: 4,
        bottom: 4
      })
      .backgroundColor('#ffd0cece')
      .offset({ left: 150, top: 120 });
    };
  }
}
```
