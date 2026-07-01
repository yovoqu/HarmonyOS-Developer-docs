# 如何实现Scroll、List单边回弹效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-316

1. [Scroll组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：在onDidScroll里获取currentOffset().yOffset来控制单边回弹效果；
 
2. [List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：在onDidScroll里获取currentOffset().yOffset来控制，还可以通过onScrollIndex实现单边回弹效果。
 
参考代码如下：
 
```text
<em>// Single side rebound effect of Scroll component</em>
@Entry
@Component
struct ScrollSideRebound {
  @State yOffset: number = 0;
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];


  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }
        .width('100%')
      }
      .scrollable(ScrollDirection.Vertical) <em>// Rolling direction vertically</em>
      .scrollBar(BarState.On) <em>// Scroll bar permanent display</em>
      .scrollBarColor(Color.Gray) <em>// Scroll bar color</em>
      .scrollBarWidth(2) <em>// Scroll bar width</em>
      .friction(0.6)
      .edgeEffect(this.yOffset <= 0 ? EdgeEffect.Spring : EdgeEffect.None) <em>// Rebound after rolling to the edge</em>
      .onDidScroll(() => {
        this.yOffset = this.scroller.currentOffset().yOffset;
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```
 
```text
<em>// Single side rebound effect of List component</em>
@Entry
@Component
struct ListSideRebound {
  @State isTop: boolean = true;
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
        }, (item: string) => item)
      }
      .listDirection(Axis.Vertical) <em>// Arrangement direction</em>
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(this.isTop ? EdgeEffect.Spring : EdgeEffect.None)<em> // Enable the flex effect only on the top boundary</em>
      .onScrollIndex((firstIndex: number) => {
        if (this.arr.length === 0 || firstIndex === 0) {
          this.isTop = true;
        } else {
          this.isTop = false;
        }
      })
      .width('90%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```
