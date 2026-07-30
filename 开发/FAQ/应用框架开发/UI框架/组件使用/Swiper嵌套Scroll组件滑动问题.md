# Swiper嵌套Scroll组件滑动问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1270

#### 问题现象

Swiper嵌套Scroll组件，Swiper不同索引内容高度不一样的情况下，如何实现Scroll组件可以滚动并且内容顶部对齐的效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/KS0Ie8_hQV-0MfudAFev8A/zh-cn_image_0000002628756012.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041249Z&HW-CC-Expire=86400&HW-CC-Sign=85B8674F39D494FB68743CF7AD688A2912C2C83D3885F58ADECC4E6DDB1939BD)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)：滑块视图容器，提供子组件滑动轮播显示的能力。
- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [align](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#align)：设置容器元素绘制区域内的子元素的对齐方式。

 
 

#### 解决方案

Scroll组件不能滚动的原因是将Scroll包裹的Column组件的高度值设置为100%，将高度去掉之后可以实现滚动效果但内容会居中显示，这时将Scroll组件的align属性值设置为Alignment.Top即可实现内容顶部对齐效果。
 
```json
@Entry
@Component
export struct ScrollPage {
  controller: SwiperController = new SwiperController();
  @State dataList: string[] = ['1', '2', '3', '4'];
  private swiperCurrentIndex: number = 0;

  build() {
    Column() {
      Text('标题');

      Swiper(this.controller) {
        ForEach(this.dataList, (data: string, index: number) => {
          Scroll() {
            Column() {
              if (index === 1) {
                Column() {
                  Row().width('100%').height(300).backgroundColor('#0A59F7');
                  Row().width('100%').height(300).backgroundColor('#ff0af7c0');
                  Row().width('100%').height(300).backgroundColor('#ffeff70a');
                };
              } else if (index === 2) {
                Column() {
                  Row().width('100%').height(300).backgroundColor('#fff7790a');
                  Row().width('100%').height(300).backgroundColor('#ff0af7e3');
                  Row().width('100%').height(300).backgroundColor('#ee0a88f7');
                  Row().width('100%').height(300).backgroundColor('#ddf7eb0a');
                  Row().width('100%').height(300).backgroundColor('#dd0af7f7');
                };
              } else {
                Text(data + '内容顶部对齐').alignSelf(ItemAlign.Start);
              }
            }
     <em>       // .height("100%") 这里将高度去掉</em>
            .alignItems(HorizontalAlign.Start).justifyContent(FlexAlign.Start);
          }
     <em>     // 设置Alignment.Top</em>
          .align(Alignment.Top)
          .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST });

        }, (item: string) => JSON.stringify(item));
      }
      .layoutWeight(1)
      .cachedCount(1)
      .backgroundColor(Color.Transparent)
      .index(this.swiperCurrentIndex)
      .width('100%')
      .loop(false)
      .autoPlay(false)
      .indicator(false);

      Blank();
      Text('底部组件');
    };
  }
}
```
