# 如何实现ListItem点击后居中显示的效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-576

#### 问题现象

如何利用List实现如下功能：
 1. 横向滚动导航栏支持点击切换。
2. 点击时自动滚动到目标位置。
3. 目标条目在容器中居中显示。
4. 动态高亮当前选中项。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/5QwFVpCoSKGRoj52qygFyw/zh-cn_image_0000002658911373.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072319Z&HW-CC-Expire=86400&HW-CC-Sign=97112C3EE38AFE8B2EABDD1F8110BA0EFB04A070D25FA1402E9A4EBA3963F30F)

 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)是用于展示动态数据集合的核心组件，支持滚动、动态更新等特性。可以利用[listDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#listdirection)设置List组件排列方向。
- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)是一种可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [scrollToIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolltoindex)：滑动到指定Index，支持设置滑动额外偏移量。

 
 

#### 解决方案
1. 定义一个CityList组件，包含一个Scroller和状态focusIndex。
2. 调用scrollToIndex()方法时，第三个参数传入[ScrollAlign.CENTER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollalign10枚举说明)，用来指定滚动对齐方式。
3. 每个标签项点击时会更新focusIndex并滚动到对应位置。
4. 根据focusIndex控制当前选中标签的背景色。
```text
@Entry
@Component
struct CityList {
  private listScroller: Scroller = new Scroller();
  @State focusIndex: number = 0;
  allListString: string[] = ['111', '222', '333', '444', '555', '666', '777', '888', '999'];

  @Builder
  child(tabName: string, tabIndex: number) {
    Column() {
      Text(tabName)
        .fontSize(18)
        .padding(4);
    }
    .borderRadius(3)
    .onClick(() => {
      this.focusIndex = tabIndex;
      this.listScroller.scrollToIndex(tabIndex, true, ScrollAlign.CENTER);
    })
    .margin({ left: tabIndex === 0 ? 20 : 4, right: tabIndex === this.allListString.length - 1 ? 20 : 4 })
    .backgroundColor(tabIndex === this.focusIndex ? '#0088FF' : '#F8F9F7');
  }

  build() {
    List({ scroller: this.listScroller }) {
      ForEach(this.allListString, (item: string, index: number) => {
        ListItem() {
          this.child(item, index);
        };
      }, (item: string) => item);
    }
    .scrollBar(BarState.Off)
    .listDirection(Axis.Horizontal)
    .backgroundColor('#FFF1F3')
    .alignListItem(ListItemAlign.Center)
    .height(60)
    .margin({ top: 100 });
  }
}
```
