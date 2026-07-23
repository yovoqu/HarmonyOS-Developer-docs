# SegmentButton页签与显示的Tabs页不匹配

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1561

#### 问题现象

- 场景一：页面切换时，顶部按钮的突出显示未跟随页面滑动进行切换。问题现象如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/iH_El-S6SNmrJkvXs5EnZQ/zh-cn_image_0000002628769748.png?HW-CC-KV=V1&HW-CC-Date=20260723T012906Z&HW-CC-Expire=86400&HW-CC-Sign=E41B0520EA8CCF026ADC6BD96D08DCBD8815FCA1CD8E7CDCC1C82ED8A3ED6062)

- 场景二：拖动顶部页签按钮进行滑动切换时，Tabs页面未同步切换。问题现象如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/EVAO5lPvRa-_CdZ4OnWJ1A/zh-cn_image_0000002658969069.png?HW-CC-KV=V1&HW-CC-Date=20260723T012906Z&HW-CC-Expire=86400&HW-CC-Sign=E423F6E9716BD020D16C4DC2F9D8401593C939BBEB916E9EAB7ED5E6491FA5AB)


 
 

#### 背景知识

- [onAnimationStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#onanimationstart11)：切换动画开始时触发该回调。当[animationDuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#animationduration)为0时动画关闭且[scrollable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#scrollable)为false时，不触发该回调。
- [SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)：分段按钮组件，包含页签类分段按钮、胶囊类单选分段按钮、胶囊类多选分段按钮。

 
 

#### 问题定位

通过[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)的UIViewer工具查看页面结构。确认顶部页签按钮不是Tabs组件本身的TabBar。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/qvkHIgJ7SaGQR7rLZgKeVA/zh-cn_image_0000002658849113.png?HW-CC-KV=V1&HW-CC-Date=20260723T012906Z&HW-CC-Expire=86400&HW-CC-Sign=188E974BE70495EDDBF3D037776CE5F0EE679FB398698C661F05388617BC6C41)

- 场景一：查看Tabs组件绑定的onChange/onAnimationStart事件。确认页面切换时事件中只改变了currentIndex，但没有更新分段按钮的选中项绑定的segmentIndex变量，导致页面切换时，顶部页签未跟随切换。问题代码如下：
```text
import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem, window } from '@kit.ArkUI';

@Entry
@Component
struct TabPage {
 <em> // SegmentButton配置项</em>
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [
      { text: '测试01' },
      { text: '测试02' },
      { text: '测试03' },
      { text: '测试04' }
    ] as ItemRestriction<SegmentButtonTextItem>,
  });
  controller: TabsController = new TabsController();
  @State segmentIndex: number[] = [0];<em> // 选中项编号列表</em>
  @State currentIndex: number = 0; <em>// 当前Tabs页索引</em>
  tabs: string[] = ['测试01', '测试02', '测试03', '测试04']; <em>// Tabs页列表</em>

  build() {
    Column() {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: this.segmentIndex,
        onItemClicked: (index: number) => {
          this.controller.changeIndex(index); <em>// 点击SegmentButton内的按钮切换Tabs页内容</em>
        }
      });
      Tabs({
        barPosition: BarPosition.End,
        index: $$this.currentIndex, <em>// 双向同步当前Tabs页的索引</em>
        controller: this.controller
      }) {
        ForEach(this.tabs, (item: string, index?: number) => {
          TabContent() {
            Column() {
              Text(item);
            };
          }
          .borderRadius(12)
          .backgroundColor('#f1f3f5') <em>// 灰色占位</em>
          .margin({
            left: index === 0 ? 0 : 6, <em>// 第一页左边距为0，其他页左边距6px</em>
            right: index === this.tabs.length - 1 ? 0 : 6,<em> // 最后一页右边距为0，其他页右边距6px</em>
            top: 8,
            bottom: 30
          }); <em>// 内容避让导航栏</em>
        });
      }
      .barHeight(0) <em>// 隐藏tabBar</em>
      .onChange((newIndex: number) => {
        this.currentIndex = newIndex; <em>// 页面切换，更改Tabs组件的index参数</em>
      });
    }
    .margin({ left: 20 })
    .height('100%')
    .width('90%')
    .padding({ top: 26 }); <em>// 避让状态栏</em>
  }
}
```

- 场景二：排查切换Tabs页相关的代码。确认仅在onItemClicked方法中切换Tabs页，但由于滑动顶部页签按钮进行切换时不会触发onItemClicked方法，导致拖动页签按钮切换时Tabs页未同步切换。问题代码如下：
```text
import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem, window } from '@kit.ArkUI';

@Entry
@Component
struct TabPage {
 <em> // SegmentButton配置项</em>
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [
      { text: '测试01' },
      { text: '测试02' },
      { text: '测试03' },
      { text: '测试04' }
    ] as ItemRestriction<SegmentButtonTextItem>,
  });
  controller: TabsController = new TabsController();
  @State segmentIndex: number[] = [0]; <em>// 选中项编号列表</em>
  @State currentIndex: number = 0; <em>// 当前Tabs页索引</em>
  tabs: string[] = ['测试01', '测试02', '测试03', '测试04']; <em>// Tabs页列表</em>

  build() {
    Column() {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: this.segmentIndex,
        onItemClicked: (index) => {
          this.controller.changeIndex(index);
        }
      });
      Tabs({
        barPosition: BarPosition.End,
        index: $$this.currentIndex,<em> // 双向同步当前Tabs页的索引</em>
        controller: this.controller
      }) {
        ForEach(this.tabs, (item: string, index?: number) => {
          TabContent() {
            Column() {
              Text(item);
            };
          }
          .borderRadius(12)
          .backgroundColor('#f1f3f5')<em> // 灰色占位</em>
          .margin({
            left: index === 0 ? 0 : 6,<em> // 第一页左边距为0，其他页左边距6px</em>
            right: index === this.tabs.length - 1 ? 0 : 6, <em>// 最后一页右边距为0，其他页右边距6px</em>
            top: 8,
            bottom: 30
          }); <em>// 内容避让导航栏</em>
        });
      }
     <em> // 推荐在onAnimationStart事件中更新，onChange事件是Tabs页切换完成后才触发的</em>
      .onAnimationStart((index: number, targetIndex: number) => {
        if (this.currentIndex !== targetIndex) {
         <em> // 添加切换动画</em>
          this.getUIContext().animateTo({
            duration: 300,
            curve: Curve.EaseInOut
          }, () => {
            this.segmentIndex[0] = targetIndex;
          });
        }
      })
      .barHeight(0);<em> // 隐藏tabBar</em>
    }
    .margin({ left: 20 })
    .height('100%')
    .width('90%')
    .padding({ top: 26 }); <em>// 避让状态栏</em>
  }
}
```


 
 
 

#### 分析结论

- 场景一：Tabs组件只改变了自身index的值，但没有改变分段按钮选中项segmentIndex的值，导致页面切换时，顶部页签未跟随切换。
- 场景二：滑动顶部按钮时没有触发onItemClicked，导致Tabs的控制器没有调用changeIndex方法，Tabs的页面不会切换。

 
 

#### 修改建议

- 场景一：当滑动Tab组件切换页面时，同步更改控制按钮显示状态selectedIndexes属性的值。
- 场景二：由于selectedIndexes配置的装饰器类型是@Link，在滑动时会更改selectedIndexes属性的值。可以通过@Watch监听selectedIndexes属性值的变化，在该监听方法中切换Tabs页。

 
完整代码如下：
 
```text
import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';

@Entry
@Component
struct TabPage {
 <em> // SegmentButton配置项</em>
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [
      { text: '测试01' },
      { text: '测试02' },
      { text: '测试03' },
      { text: '测试04' }
    ] as ItemRestriction<SegmentButtonTextItem>,
  });
  @Watch('updateIndex') @State segmentIndex: number[] = [0];<em> // 选中项编号列表</em>
  controller: TabsController = new TabsController();
  @State currentIndex: number = 0; <em>// 当前Tabs页索引</em>
  tabs: string[] = ['测试01', '测试02', '测试03', '测试04']; <em>// Tabs页列表</em>

  updateIndex() {
    if (this.segmentIndex[0] != this.currentIndex) {
      this.controller.changeIndex(this.segmentIndex[0]);
    }
  }

  build() {
    Column() {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: this.segmentIndex
      });

      Tabs({
        barPosition: BarPosition.End,
        index: $$this.currentIndex,<em> // 双向同步当前Tabs页的索引</em>
        controller: this.controller
      }) {
        ForEach(this.tabs, (item: string, index?: number) => {
          TabContent() {
            Column() {
              Text(item);
            };
          }
          .borderRadius(12)
          .backgroundColor('#F1F3F5')<em> // 灰色占位</em>
          .margin({
            left: index === 0 ? 0 : 6,<em> // 第一页左边距为0，其他页左边距6px</em>
            right: index === this.tabs.length - 1 ? 0 : 6, <em>// 最后一页右边距为0，其他页右边距6px</em>
            top: 8,
            bottom: 30
          });<em> // 内容避让导航栏</em>
        });
      }
      .barHeight(0) <em>// 隐藏tabBar</em>
   <em>   // 推荐在onAnimationStart事件中更新，onChange事件是Tabs页切换完成后才触发的</em>
      .onAnimationStart((index: number, targetIndex: number) => {
        if (this.currentIndex !== targetIndex) {
        <em>  // 添加切换动画</em>
          this.getUIContext().animateTo({
            duration: 300,
            curve: Curve.EaseInOut
          }, () => {
            this.segmentIndex[0] = targetIndex;
          });
        }
      })
      .onChange((targetIndex) => {
        this.currentIndex = targetIndex;
      });
    }
    .margin({ left: 20 })
    .height('100%')
    .width('90%')
    .padding({ top: 26 }); <em>// 避让状态栏</em>
  }
}
```
 
运行效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/4Oqk8-LxTTOGzrm_Q6gARw/zh-cn_image_0000002628609854.png?HW-CC-KV=V1&HW-CC-Date=20260723T012906Z&HW-CC-Expire=86400&HW-CC-Sign=76C12EC731ED2EAA02C7064CF4BBD82298A95A0415A73B141CAC953A6CCEC071)
