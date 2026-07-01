# 如何实现List滑动时数据更新不渲染到组件上

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1469

## 如何实现List滑动时数据更新不渲染到组件上
 


##### 问题现象

List和Repeat搭配实现了一个列表组件，如何让List在滑动的时候，数据更新但不渲染到组件上，停止滑动时把最后一次更新的值渲染到组件上。
 
 

##### 背景知识

- [@Monitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor#概述)：@Monitor装饰器用于监听状态变量修改，使得状态变量具有深度监听的能力。
- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
- [Repeat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat)：Repeat基于数组类型数据来进行循环渲染，一般与容器组件配合使用。

 
 

##### 解决方案

设置一个中间变量用来接收更新的值，在[onDidScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common#ondidscroll12)回调中判断当前List滑动状态，如果是滑动时，数据只更新到中间变量，不刷新到List数据源，滑动停止时把中间变量的数据刷新到数据源上。非滑动时，更新到中间变量后，立即更新进List数据源，从而实现在List滑动期间仅更新数据而不触发组件渲染。
 
```text
@Entry
@ComponentV2
struct ListScrollDemo {
  @Local dataArr: Array = [];
  @Local num: number = 0;
  @Local temp: string = '';
  @Local isScroll: boolean = false;

  @Monitor('temp')
  onStrChange() {
    // 非滚动状态，把状态变量更新到数据源
    if (!this.isScroll) {
      this.dataArr[5] = this.temp;
    }
  }

  aboutToAppear(): void {
    for (let i = 0; i  {
      // 模拟数据刷新
      this.temp = JSON.stringify(this.num);
      this.num++;
    }, 1000);
  }

  build() {
    List() {
      Repeat(this.dataArr)
        .each((ri: RepeatItem) => {
          ListItem() {
            Text(ri.item)
              .width('100%')
              .height(60)
              .fontSize(20)
              .textAlign(TextAlign.Center)
              .backgroundColor(0xFFFFFF)
          }
        })
    }
    .height('100%')
    .width('100%')
    .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
      console.info(`scrollOffset: ${scrollOffset}`);
      if (scrollState === 0) {
        this.isScroll = false;
      } else {
        this.isScroll = true;
      }
    })
    .onScrollStop(() => {
      // 滚动停止时，将最新中间变量的值更新到数据源
      this.dataArr[5] = this.temp;
    })
  }
}
```
