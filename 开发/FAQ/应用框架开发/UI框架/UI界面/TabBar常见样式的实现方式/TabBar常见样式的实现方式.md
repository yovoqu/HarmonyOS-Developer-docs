# TabBar常见样式的实现方式

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1101

#### 问题现象

设置TabBar常见样式时可能会遇到如下问题：
 
场景一：使用Tabs组件实现侧边栏时，如何实现自顶到底的效果？
 
场景二：如何在页签被选中时改变字体颜色？
 
场景三：如何实现胶囊页签样式？
 
场景四：如何实现页签栏和内容区重叠，并启用毛玻璃效果？
 
场景五：如何实现悬浮式、两端留空的Tab栏样式？
 
场景六：当页签数量较多时，如何设置TabBar的样式？
 
场景七：如何在页签被选中时，让其上移并超出TabBar区域显示？
 
 

#### 背景知识

- [Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)：进行内容视图切换的容器组件，每个页签对应一个内容视图。
- [TabBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#tabbar)：设置TabBar上显示内容。
- [TabsOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabsoptions15)的barModifier用于设置TabBar的通用属性。
- [barOverlap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#baroverlap10)：设置TabBar是否背后变模糊并叠加在TabContent之上。
- [barBackgroundBlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barbackgroundblurstyle11)：设置TabBar的背景模糊材质。
- [SegmentButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton)：分段按钮组件，适用于页面切换、单选/多选场景。

 
 

#### 解决方案
 
| 实现场景 | 实现方案 |
| --- | --- |
| 场景一：实现自顶到底效果。 | 通过自定义组件实现，导航栏使用List实现。 |
| 场景二：在页签被选中时改变字体颜色。 | 通过自定义TabBar实现。 |
| 场景三：实现胶囊页签样式。 | 方案一：使用SegmentButton与Tabs实现。 |
| 场景三：实现胶囊页签样式。 | 方案二：使用自定义页签实现。 |
| 场景四：实现页签栏和内容区重叠，并启用毛玻璃效果。 | 通过设置Tabs的barOverlap为true，并设置barBackgroundBlurStyle为BlurStyle.Thin。 |
| 场景五：实现悬浮式、两端留空的Tab栏样式。 | 方案一：使用自定义组件实现。 |
| 场景五：实现悬浮式、两端留空的Tab栏样式。 | 方案二：使用HdsTabs实现。 |
| 场景六：处理页签数较多时的TabBar的样式。 | 通过设置barMode为BarMode.Scrollable实现。 |
| 场景七：在页签被选中时使页签超出TabBar区域显示。 | 通过barModifier设置TabBar的clip属性实现。 |
 
 
- **场景一：实现自顶到底效果。**由于Tabs组件无法实现自顶到底的效果，可以通过自定义组件来达到此效果，导航栏可使用List实现。解决方案：参考[Tabs实现自顶到底效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-809)。
- **场景二：在页签被选中时改变字体颜色。**在页签被选中时改变字体颜色，可通过自定义页签实现。解决方案：参考[示例3（自定义页签切换联动）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#示例3自定义页签切换联动)。
- **场景三：实现胶囊页签样式。**
方案一：使用SegmentButton与Tabs实现。将SegmentButton作为页签，将Tabs的属性barHeight设置为0。参考代码如下所示：

  
```text
import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';


@Entry
@Component
struct CapsuleOne {
  tabList: string[] = ['我的内容', '探索内容'];
  @State currentIndex: number = 0;
  @State tabSelectedIndexes: number[] = [];
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '我的' }, { text: '探索' }] as ItemRestriction<SegmentButtonTextItem>,
    textPadding: 6
  });


  build() {
    Column() {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: $tabSelectedIndexes,
       <em> // 点击SegmentButton时Tabs页面切换</em>
        onItemClicked: (index: number) => {
          this.currentIndex = index;
        }
      })
        .width('80%');
      Tabs({ index: this.currentIndex }) {
        ForEach(this.tabList, (item: string) => {
          TabContent() {
            Text(item)
              .fontSize(16);
          };
        });
      }
      .barHeight(0)
      .backgroundColor('#FFFFFF')
      .width('100%')
      .layoutWeight(1)
      .onChange((index: number) => {
        this.currentIndex = index;
      <em>  // 页面滑动时SegmentButton切换选中状态</em>
        this.tabSelectedIndexes = [index];
      });
    }
    .width('100%')
    .margin({ top: 16 })
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Start);
  }
}
```


  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/9t_DQF6UTjiCTuUCuClGGQ/zh-cn_image_0000002658926665.png?HW-CC-KV=V1&HW-CC-Date=20260730T072519Z&HW-CC-Expire=86400&HW-CC-Sign=4D02353F9AF71B375431A34E8773694EEEDCECA50F0246219C1F9E45F09D1CC2)

- 方案二：使用自定义页签实现。设置单个页签的宽度在(页签宽度/页签数-padding值*页签数，页签宽度/页签数)之间。参考代码如下所示：

  
```text
@Entry
@Component
struct CapsuleTwo {
  tabList: string[] = ['备忘', '待办'];
  tabbarWidth: number = 200;
  tabbarPadding: number = 2;
  @State currentIndex: number = 0;


  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .width(this.tabbarWidth / 2 -
          this.tabbarPadding * 2) <em>// 设置宽度在(tabBar宽度/tabBar个数-padding值*tabBar个数，tabBar宽度/tabBar个数)之间</em>
        .height('36vp')
        .textAlign(TextAlign.Center)
        .textVerticalAlign(TextVerticalAlign.CENTER)
        .fontColor(this.currentIndex === index ? '#e6000000' : '#99000000')
        .fontSize(14)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(40)
        .backgroundColor(this.currentIndex === index ? Color.White : '#00000000')
        .borderRadius('50vp');
    }
    .backgroundColor('#0d000000')
    .borderRadius({
      topLeft: index === 0 ? 50 : 0,
      bottomLeft: index === 0 ? 50 : 0,
      topRight: index === this.tabList.length - 1 ? 50 : 0,
      bottomRight: index === this.tabList.length - 1 ? 50 : 0
    })
    .margin({ top: 5 })
    .padding(this.tabbarPadding);
  }


  build() {
    Column() {
      Tabs() {
        ForEach(this.tabList, (item: string, index: number) => {
          TabContent() {
            Text(item)
              .fontSize(16);
          }
          .backgroundColor('#FFFFFF')
          .tabBar(this.tabBuilder(index, item));
        });
      }
      .barWidth(this.tabbarWidth)
      .width('100%')
      .height('100%')
      .onChange((index: number) => {
        this.currentIndex = index;
      });
    };
  }
}
```


  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/NhRyksR5RpK_3N0dT6GMAw/zh-cn_image_0000002658806705.png?HW-CC-KV=V1&HW-CC-Date=20260730T072519Z&HW-CC-Expire=86400&HW-CC-Sign=40FC98759D7F9B7DC7007D42DE1C4193A67477D16A3F178B5790222543EAF816)


 - **场景四：实现页签栏和内容区重叠，并启用毛玻璃效果。**通过设置Tabs的barOverlap为true，并设置barBackgroundBlurStyle为BlurStyle.Thin，实现页签栏和内容区的重叠及毛玻璃效果。设置底部组件的padding值大于TabBar的高度防止遮挡。参考代码如下所示：

  
```text
@Entry
@Component
struct BarOverlapPage {
  tabList: string[] = ['页签1', '页签2'];
  contentList: string[] = ['区域1', '区域2', '区域3', '区域4'];
  listSpace: number = 16;


  @Builder
  tabContentBuilder() {
    List({ space: this.listSpace }) {
      ForEach(this.contentList, (item: string, index: number) => {
        ListItem() {
          Text(item)
            .width('80%')
            .height(500)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .backgroundColor('#26000000');
        }
       <em> // 设置底部组件的padding值大于tabBar的高度</em>
        .padding({ bottom: index === this.contentList.length - 1 ? 56 + this.listSpace : 0 });
      });
    }
    .width('100%')
    .height('100%')
    .lanes(2)
    .alignListItem(ListItemAlign.Center);
  }


  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End }) {
        ForEach(this.tabList, (item: string) => {
          TabContent() {
            this.tabContentBuilder();
          }
          .tabBar(item);
        });
      }
      .barOverlap(true) /<em>/ 开启背景模糊</em>
      .barBackgroundBlurStyle(BlurStyle.Thin);
    }
    .backgroundColor('#fff1f3f5')
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```


  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/yTDbtL9tTByMyM8O6ahh5g/zh-cn_image_0000002628407452.png?HW-CC-KV=V1&HW-CC-Date=20260730T072519Z&HW-CC-Expire=86400&HW-CC-Sign=3424C74E5A8A8EC25480D53D19192C54840A165FFD821DEE64B230CD94F0AA3A)

- **场景五：实现悬浮式、两端留空的Tab栏样式。**
方案一：使用自定义组件实现。通过自定义组件实现，使用Stack容器将Tabs与自定义页签堆叠，实现悬浮式、两端留空的Tab栏样式，参考代码如下所示：

  
```text
interface tabInterface {
  text: string;
  icon: Resource;
}


@Entry
@Component
struct SuspensionPage {
<em>  // 图片资源开发者可根据自身需求替换成所需资源</em>
  tabList: tabInterface[] = [
    { text: '内容1', icon: $r('app.media.heart') },
    { text: '内容2', icon: $r('app.media.clock') },
    { text: '内容3', icon: $r('app.media.rectangle_on_rectangle') },
    { text: '内容4', icon: $r('app.media.person_2') }
  ];
  private controller: TabsController = new TabsController();
  @State currentIndex: number = 0;


  @Builder
  myTabBar() {
    Row() {
      Row() {
        ForEach(this.tabList, (item: tabInterface, index: number) => {
          Column() {
            Image(item.icon)
              .width(50)
              .aspectRatio(1)
              .padding(8)
              .backgroundColor(this.currentIndex === index ? '#26000000' : '#f1f3f5')
              .borderRadius(12);
          }
          .onClick(() => {
            this.controller.changeIndex(index);
            this.currentIndex = index;
          })
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center)
          .width(50)
          .height(50);
        });
      }
      .height(70)
      .width('90%')
      .justifyContent(FlexAlign.SpaceAround)
      .backgroundColor('#f1f3f5')
      .borderRadius(18);
    }
    .justifyContent(FlexAlign.Center)
    .height('50')
    .width('100%')
    .margin({ bottom: 20 });
  }


  build() {
    Column() {
      Stack({ alignContent: Alignment.BottomStart }) {
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabList, (item: tabInterface) => {
            TabContent() {
              Column() {
                Text(item.text)
                  .fontSize(20);
              }
              .justifyContent(FlexAlign.Center)
              .height('100%')
              .width('100%');
            }
            .backgroundColor('#ffffff');
          });
        }
        .barHeight(0)
        .animationDuration(200)
        .onChange((index: number) => {
          this.currentIndex = index;
        });
    <em>    // 页签</em>
        this.myTabBar();
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

- 方案二：使用HdsTabs实现。从API23开始，HdsTabs新增支持设置页签栏的悬浮样式。解决方案：参考[页签栏的悬浮样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating)。

  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/STgUMaMZQTiCi1YcR6LcbQ/zh-cn_image_0000002628567350.png?HW-CC-KV=V1&HW-CC-Date=20260730T072519Z&HW-CC-Expire=86400&HW-CC-Sign=761BD66887DD99AFB643356F5796E1067672A89EAC6FF70813B4746BEAD71C17)


 - **场景六：处理页签数较多时的TabBar的样式。**通过设置barMode为BarMode.Scrollable，当标签数量较多或内容超出屏幕宽度时，用户可以通过滑动来切换标签。解决方案：参考[示例2（设置Scrollable模式下的TabBar的布局样式）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#示例2设置scrollable模式下的tabbar的布局样式)。
- **场景七：在页签被选中时使页签超出TabBar区域显示。**通过barModifier设置TabBar的clip属性，实现页签被选中时超出TabBar区域显示的效果。解决方案：参考[示例15（页签超出TabBar区域显示）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#示例15页签超出tabbar区域显示)。

 
 

#### 常见FAQ

Q：如何在标签页中嵌入一个动图图标？
 
A：通过自定义TabBar实现，在CustomBuilder中提供支持动图的gif。
 
Q：TabBar高度的默认值是多少？
 
A：CustomBuilder设置自定义样式的TabBar且vertical属性为false时，默认值为56vp。开发者可参考[barHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barheight20)。
