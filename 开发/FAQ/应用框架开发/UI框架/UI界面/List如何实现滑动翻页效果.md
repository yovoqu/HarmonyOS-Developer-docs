# List如何实现滑动翻页效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1158

## List如何实现滑动翻页效果
 


##### 问题现象

List有无enablePaging类似的方法？Scroll嵌套List后的enablePaging会失效吗？
 
 

##### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)列表包含一系列相同宽度的列表项。
- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
[enablePaging](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#enablepaging11)设置是否支持滑动翻页。如果同时设置了滑动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效。List没有类似方法。

 - [Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)可滚动容器组件的控制器，可以将此组件绑定至容器组件，如Scroll、List等。
[scrollTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollto)滑动到指定位置，可设置滑动的动画效果。
- [currentOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#currentoffset)获取当前的滚动偏移量。

 - [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)组件区域变化时触发该回调，可获取组件的尺寸信息。
- [onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)手指触摸动作触发该回调。包含触摸类型，触摸点坐标等信息。

 
 

##### 解决方案

- **方案一**：在外层使用Scroll包裹List组件，用Scroll的enablePaging方法替代。**内层的List不能设置滚动方向上的组件长度**，否则enablePaging方法会失效。示例代码如下：此时List本身是不可滚动的，外层Scroll可以滚动。
```text
@Entry
@Component
struct ScrollSolution {
  private arr: number[] = new Array(30).fill(0);
  private scroller: Scroller = new Scroller();
  @State centerIndex: number = 0;

  build() {
    Column() {
      Scroll() {
        List({ space: 20, scroller: this.scroller }) {
          ForEach(this.arr, (item: number, index: number) => {
            ListItem() {
              Text(`Item ${index}`)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(this.centerIndex === index ? '#0A59F7' : '#F1F3F5');
            }
            .onClick(() => {
              this.centerIndex = index;
              this.scroller.scrollToIndex(this.centerIndex, true, ScrollAlign.CENTER);
            });
          }, (item: number) => item.toString());
        }
        // 上下滚动，不能设置List的高度，否则Scroll的enablePaging会失效
        .width('100%');
      }
      .enablePaging(true) // 滑动翻页
      .friction(0.8) // 设置摩擦系数
      .width('100%')
      .height('100%');
    }.margin('20vp');
  }
}
```
 效果如下：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/A9WV98ENTuK_FUzNlmC2tA/zh-cn_image_0000002628569770.png?HW-CC-KV=V1&HW-CC-Date=20260701T025706Z&HW-CC-Expire=86400&HW-CC-Sign=787C341BBA6CD1D3DF20E3E61D947289C14DC9286355EC993883CAB833F669F0)

- **方案二**：自定义实现List翻页效果。通过onAreaChange获取List的高度，在onTouch回调中实现滑动翻页逻辑，手指按下时，获取当前List的滚动偏移量，手指抬起时，根据手指滑动方向决定向前或向后滚动一个List高度的距离。示例代码如下：翻页判定条件为手指滑动List的距离超过List高度的三分之一。
```text
@Entry
@Component
struct ListSolution {
  private arr: number[] = new Array(30).fill(0);
  private scroller: Scroller = new Scroller();
  @State centerIndex: number = 0;
  @State listHeight: number = 0;
  @State listWidth: number = 0;
  @State listOffset: number = 0; // List偏移量

  build() {
    Column() {
      List({ space: 20, scroller: this.scroller }) {
        ForEach(this.arr, (item: number, index: number) => {
          ListItem() {
            Text(`Item ${item + index}`)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(this.centerIndex === index ? '#0A59F7' : '#F1F3F5');
          }
          .onClick(() => {
            this.centerIndex = index;
            // 点击某一项，此项移动至屏幕中间
            this.scroller.scrollToIndex(this.centerIndex, true, ScrollAlign.CENTER);
          });
        }, (item: number) => item.toString());
      }
      .edgeEffect(EdgeEffect.None)
      .onAreaChange((oldValue: Area, newValue: Area) => {
        console.info(`${JSON.stringify(oldValue)} ${JSON.stringify(newValue)}`);
        this.listHeight = newValue.height as number;
        this.listWidth = newValue.width as number;
      })
      .onTouch((event: TouchEvent) => {
        if (event.type === TouchType.Down) {
          // 记录手指按下时的偏移量
          this.listOffset = this.scroller.currentOffset().yOffset;
          console.info(`this.currentOffset ${this.listOffset}`);
        }
        if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
          // 滑动距离超过页面三分之一则整页滚动
          let curOffset: number = this.scroller.currentOffset().yOffset - this.listOffset;
          let targetOffset = this.listOffset;
          if (Math.abs(curOffset)  0) {
            targetOffset = this.listOffset + this.listHeight;
          } else if (curOffset
