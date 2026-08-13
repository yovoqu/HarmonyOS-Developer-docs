# 长列表使用scrollToIndex卡顿问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-632

#### 问题现象

使用List和Scroller嵌套实现的长列表使用scrollToIndex()方法跳转跨越过多项时性能低下，如何优化？
 
```text
@Entry
@ComponentV2
export struct ListTest {
  private readonly list: string[] = Array
    .from({ length: 2000 }, (_: number, i: number) => i + 1)
    .map((i: number) => `index: ${i}`);
  private readonly scroller: Scroller = new Scroller();

  build() {
    Column() {
      Row({ space: 10 }) {
        Button('scroll to top').onClick(() => this.scroller.scrollToIndex(0, true)).fontSize(13);
        Button('scroll to bottom').onClick(() => this.scroller.scrollToIndex(this.list.length - 1, true)).fontSize(13);
        Button('jump 1000').onClick(() => this.scroller.scrollToIndex(1000, false)).fontSize(13);
      }
      .width('100%')
      .margin({ left: 25 });

      List({
        scroller: this.scroller,
      }) {
        Repeat(this.list)
          .key((item: string) => item)
          .virtualScroll({ totalCount: this.list.length })
          .templateId(() => '1')
          .template('1', (repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(50)
                .padding(5)
                .textAlign(TextAlign.Center);
            };
          })
          .each((repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(50)
                .padding(5);
            };
          });
      }
      .width('100%')
      .layoutWeight(1);
    }
    .backgroundColor(Color.White);
  }
}
```
 
 

#### 背景知识

- 使用工具Profiler查看性能参数可以参考[使用Profiler进行性能调优](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-introduction)。
- [currentOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#currentoffset)可以用来获取当前的滚动偏移量。
- [scrollToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolltoindex)开启smooth动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题，导致整个列表卡顿。

 
 

#### 解决方案

- 可以采用先调用scrollToIndex关闭动画跳转到目标附近位置，再调用scrollToIndex开启动画滚动到目标位置的间接跳转的方式，优化性能。以纵向滚动的5000个元素的长列表，调用scroller反复滚动到列表顶部和底部为例。

  
```text
@Entry
@ComponentV2
export struct virtrulScroll {
  private itemHeight: number = 50;
  private readonly list: string[] = Array
    .from({ length: 5000 }, (_: number, i: number) => i + 1)
    .map((i: number) => `index: ${i}`);
  private readonly scroller: Scroller = new Scroller();

  build() {
    Column() {
      Row({ space: 10 }) {
        Button('scroll to top')
          .fontSize(13)
          .onClick(() => {
            <em>// 用currentOffset().yOffset获取当前滑动偏移量除以单项高度获得index做判断，离目标位置超过200项则以关闭动效先滚动到目标位置附近</em>
            if (this.scroller.currentOffset().yOffset / this.itemHeight >= 200) {
              this.scroller.scrollToIndex(200, false);
            }
            this.scroller.scrollToIndex(0, true);
          });
        Button('scroll to bottom')
          .fontSize(13)
          .onClick(() => {
            if (this.scroller.currentOffset().yOffset / this.itemHeight <= this.list.length - 200) {
              this.scroller.scrollToIndex(this.list.length - 200, false);
            }
            this.scroller.scrollToIndex(this.list.length - 1, true);
          });
        Button('jump 1000')
          .fontSize(13)
          .onClick(() => {
            console.info('currentoffset: ', this.scroller.currentOffset().yOffset);
            this.scroller.scrollToIndex(1000, false);
          });
      };

      List({
        scroller: this.scroller,
      }) {
        Repeat(this.list)
          .key((item: string) => item)
          .virtualScroll({ totalCount: this.list.length })
          .templateId(() => '1')
          .template('1', (repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(this.itemHeight)
                .padding(5)
                .textAlign(TextAlign.Center);
            };
          })
          .each((repeatItem: RepeatItem<string>) => {
            ListItem() {
              Text(repeatItem.item)
                .width('100%')
                .height(this.itemHeight)
                .padding(5);
            };
          });
      }
      .width('100%')
      .height(200)
      .layoutWeight(1);
    }.backgroundColor(Color.White);
  }
}
```

- 开动效直接跳到目标位置和先关动效跳到附近位置再开启动效跳转到目标位置对比，通过DevEco Studio的Profiler抓取launch数据可以得到如下，可以明显看出实现了性能优化。
直接跳转：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/J0aIbq9_TEOoibgXElbJJQ/zh-cn_image_0000002658793543.png?HW-CC-KV=V1&HW-CC-Date=20260701T041332Z&HW-CC-Expire=86400&HW-CC-Sign=20A4FCE049A5DCEE00DA021B4C450B0CB1F5D1C35E8790EA57DEF82179550BAE)

- 间接跳转：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/jCVw54aURUei9X6qRWkoug/zh-cn_image_0000002628554176.png?HW-CC-KV=V1&HW-CC-Date=20260701T041332Z&HW-CC-Expire=86400&HW-CC-Sign=79C8CB2B48CB1362A08AAEB702B1EC9BA8AAC4BE25CD0018EEEFFF8DC5770D82)

- 数据对比：

| 对比数据 | 直接跳转 | 间接跳转 |
| --- | --- | --- |
| 布局任务数量LayoutTasks/个 | 4968 | 185 |
| 布局时间/ms | 518.811 | 16.480 |
- 实际运行效果比较：

| 优化前 | 优化后 |
| --- | --- |
|  |  |
