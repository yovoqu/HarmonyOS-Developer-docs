# 【导航与切换】HdsNavigation滚动模糊场景

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1095

#### 问题现象

场景一：如何实现HdsNavigation内容区延伸到工具栏区域并设置模糊效果？
 
场景二：HdsNavigation嵌套HdsTabs出现滚动模糊效果丢失，问题代码如下所示：
 
```text
import {
  BlurStrategy,
  HdsNavigation,
  HdsNavigationTitleMode,
  HdsTabs,
  ScrollEffectType
} from '@hms.hds.hdsBaseComponent';
import { LengthMetrics } from '@kit.ArkUI';


@Entry
@Component
struct Index {
  pageInfo: NavPathStack = new NavPathStack();
  scroller: Scroller = new Scroller();
  tabList: string[] = ['页签1', '页签2', '页签3'];
  @State currentIndex: number = 0;


  build() {
    HdsNavigation(this.pageInfo) {
      HdsTabs({ barPosition: BarPosition.End }) {
        ForEach(this.tabList, (item: string, index: number) => {
          TabContent() {
            Scroll(this.scroller) {
              Text(`滚动条${index + 1}`)
                .fontSize(20)
                .height(1320) <em>// 使子组件的布局尺寸超过父组件的尺寸，内容可以滚动。</em>
                .backgroundColor('#40000000');
            }
            .scrollBar(BarState.Off)
            .padding({ top: 56 })
            .width('100%')
            .height('100%');
          }
          .tabBar(item);
        });
      }
      .onChange((index: number) => {
        this.currentIndex = index;
      });
    }
    .bindToScrollable([this.scroller])
    .hideBackButton(true)
    .titleBar({
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR, <em>// 设置模糊类型</em>
          blurEffectiveStartOffset: LengthMetrics.vp(0), <em>// 动态样式线性过渡的起始位置</em>
          blurEffectiveEndOffset: LengthMetrics.vp(20) <em>// 动态样式线性过渡的终点位置</em>
        },
        blurStrategy: BlurStrategy.ADAPTIVE,
        originalStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } },
        scrollEffectStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } }
      },
      content: {
        title: {
          mainTitle: '测试标题'
        }
      }
    })
    .hideToolBar(true)
    .titleMode(HdsNavigationTitleMode.MINI);
  }
}
```
 
 
问题效果图如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/1B96VA8bRneFZLRKZXPJrw/zh-cn_image_0000002628567262.png?HW-CC-KV=V1&HW-CC-Date=20260701T041149Z&HW-CC-Expire=86400&HW-CC-Sign=BE2DCA7D47BB3F4E31E36D0B0AE471B6E132DF8992B084AEB9730582B2049860)

 

#### 背景知识

- [HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)：路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏。
- [bindToScrollable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#bindtoscrollable)：绑定导航组件和可滚动容器组件，动态显隐标题区域，状态栏及底部自定义区域。
- [titleBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#titlebar)：设置HdsNavigation组件titleBar区域样式以及内容。
- [toolbarConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#toolbarconfiguration)：设置工具栏内容。
- [HdsTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdstabs)：一般作为Page页面的根容器使用。
- [onWillHide](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#onwillhide12)：TabContent即将隐藏时触发此回调。
- [onAnimationStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#onanimationstart11)：切换动画开始时触发该回调。
- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [Scroller](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scroller)：可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。

 
 

#### 解决方案

- **场景一：实现HdsNavigation内容区延伸到工具栏区域并设置模糊效果。**1. titleBar的[TitleBarStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#titlebarstyleoptions)存在scrollEffectOpts属性，可设置标题栏动态模糊效果。

2. 工具栏区域的动态模糊效果，可将toolBar与内容区重叠，可通过设置[toolbarConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation#toolbarconfiguration)的barStyle属性为BarStyle.STACK，并设置toolBar为透明模糊材质。

  参考代码如下所示：

  
```text
import { BlurStrategy, HdsNavigation, HdsNavigationTitleMode, ScrollEffectType } from '@kit.UIDesignKit';
import { LengthMetrics } from '@kit.ArkUI';


@Entry
@Component
struct ExtensionToolBar {
  pageInfo: NavPathStack = new NavPathStack();
  toolBarList: string[] = ['设置', '媒体', '多选'];
  scroller: Scroller = new Scroller();


  @Builder
  toolBarBuilder() {
    Row() {
      ForEach(this.toolBarList, (item: string) => {
        Column() {
          Text(item)
            .fontSize(20)
            .fontWeight(FontWeight.Normal)
            .fontColor('#000000');
        };
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }


  build() {
    HdsNavigation(this.pageInfo) {
      Column() {
        Scroll(this.scroller) {
          Column() {
            Text('滚动条')
              .padding(16)
              .fontSize(24)
              .fontWeight(FontWeight.Medium)
              .fontColor('#ffffff')
              .backgroundColor('#40000000')
              .height('1320'); <em>// 使子组件的布局尺寸超过父组件的尺寸，内容可以滚动。</em>
          }
          .justifyContent(FlexAlign.Center)
          .padding({ top: 56, bottom: 56 });
        }
        .height('100%')
        .width('100%')
        .scrollBar(BarState.Off);
      }
      .height('100%')
      .width('100%');
    }
    .bindToScrollable([this.scroller])<em> // 绑定导航组件和可滚动容器组件</em>
    .height('100%')
    .width('100%')
    .hideBackButton(true)
    .titleBar({
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR, <em>// 设置模糊类型</em>
          blurEffectiveStartOffset: LengthMetrics.vp(0), <em>// 动态样式线性过渡的起始位置</em>
          blurEffectiveEndOffset: LengthMetrics.vp(20) <em>// 动态样式线性过渡的终点位置</em>
        },
        blurStrategy: BlurStrategy.ADAPTIVE,
        originalStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } },
        scrollEffectStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } }
      },
      content: {
        title: {
          mainTitle: '测试标题'
        }
      }
    })
    .titleMode(HdsNavigationTitleMode.MINI)
    .toolbarConfiguration(this.toolBarBuilder, {
      backgroundColor: '#00ffffff',
      backgroundBlurStyle: BlurStyle.Thin,
      backgroundBlurStyleOptions: {
        policy: BlurStyleActivePolicy.FOLLOWS_WINDOW_ACTIVE_STATE, <em>// 模糊激活策略</em>
        inactiveColor: '#00ffffff' <em>// 模糊不生效时使用的背景色</em>
      },
      hideItemValue: false,
      barStyle: BarStyle.STACK <em>// 工具栏的布局样式采用层叠布局</em>
    });
  }
}
```


  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/T2VWkPEcRKKhpxuqa9MwNA/zh-cn_image_0000002658926575.png?HW-CC-KV=V1&HW-CC-Date=20260701T041149Z&HW-CC-Expire=86400&HW-CC-Sign=9D779DD059E92C94319D27B29BDCCE8718B886477F3A1763BA16FDC3AF69688D)

- **场景二：实现HdsNavigation嵌套HdsTabs滚动模糊效果正常显示。**1. 每个Tab单独创建独立的Scroller，互不共用，避免彼此干扰。

2. bindToScrollable仅动态绑定当前Tab的Scroller。

3. 通过onWillHide记录对应Tab的滚动偏移量，通过onAnimationStart恢复对应Tab的滚动位置。

  参考代码如下所示：

  
```text
import {
  BlurStrategy,
  HdsNavigation,
  HdsNavigationTitleMode,
  HdsTabs,
  ScrollEffectType
} from '@hms.hds.hdsBaseComponent';
import { LengthMetrics } from '@kit.ArkUI';


class TabItem {
  id: number;
  name: string;
  scroller: Scroller;
  offsetY: number;


  constructor(id: number, name: string, scroller: Scroller, offsetY: number) {
    this.id = id;
    this.name = name;
    this.scroller = scroller;
    this.offsetY = offsetY;
  }
}


@Entry
@Component
struct Index {
  pageInfo: NavPathStack = new NavPathStack();
  scroller1: Scroller = new Scroller();
  scroller2: Scroller = new Scroller();
  scroller3: Scroller = new Scroller();
  tabList: TabItem[] = [
    new TabItem(0, '页签1', this.scroller1, 0),
    new TabItem(1, '页签2', this.scroller2, 0),
    new TabItem(2, '页签3', this.scroller3, 0)
  ];
  @State currentIndex: number = 0;


  <em>// 只绑定当前显示的scroller</em>
  getCurScroll() {
    return this.tabList[this.currentIndex].scroller;
  }


  build() {
    HdsNavigation(this.pageInfo) {
      HdsTabs({ barPosition: BarPosition.End }) {
        ForEach(this.tabList, (item: TabItem, index: number) => {
          TabContent() {
            Scroll(item.scroller) {
              Text(`滚动条${index + 1}`)
                .padding(16)
                .fontSize(20)
                .height(1320) <em>// 使子组件的布局尺寸超过父组件的尺寸，内容可以滚动。</em>
                .backgroundColor('#40000000');
            }
            .scrollBar(BarState.Off)
            .padding({ top: 56 })
            .width('100%')
            .height('100%');
          }
          .tabBar(item.name)
        <em>  // 保存滚动量</em>
          .onWillHide(() => {
            const offset = item.scroller.currentOffset();
            item.offsetY = offset.yOffset;
          });
        });
      }
    <em>  // 回复滚动量</em>
      .onAnimationStart((index: number, targetIndex: number) => {
        console.info(`Succeeded in getting info.Index:${index},targetIndex:${targetIndex}.`);
        this.currentIndex = targetIndex;
        this.tabList[this.currentIndex].scroller.scrollTo({
          xOffset: 0,
          yOffset: this.tabList[this.currentIndex].offsetY
        });
      });
    }
  <em>  // 只绑定当前页面的scroller，避免互相干扰</em>
    .bindToScrollable([this.getCurScroll()])
    .hideBackButton(true)
    .titleBar({
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR, <em>// 设置模糊类型</em>
          blurEffectiveStartOffset: LengthMetrics.vp(0), <em>/</em><em>/ 动态样式线性过渡的起始位置</em>
          blurEffectiveEndOffset: LengthMetrics.vp(20) <em>// 动态样式线性过渡的终点位置</em>
        },
        blurStrategy: BlurStrategy.ADAPTIVE,
        originalStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } },
        scrollEffectStyle: { backgroundStyle: { backgroundColor: '#00ffffff' } }
      },
      content: {
        title: {
          mainTitle: '测试标题'
        }
      }
    })
    .hideToolBar(true)
    .titleMode(HdsNavigationTitleMode.MINI);
  }
}
```


  效果图如下所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/x7uCOqr0Qq-FmOQKSO_Y5w/zh-cn_image_0000002658806633.png?HW-CC-KV=V1&HW-CC-Date=20260701T041149Z&HW-CC-Expire=86400&HW-CC-Sign=46148B51FDA7BE90C0BD745BBD4DB400316BEB590D66ED118267C97C46528DBA)


 
 

#### 常见FAQ

Q：部分设备设置BlurStrategy.ADAPTIVE无法实现动态模糊，如何处理？
 
A：可通过设置BlurStrategy参数为ENABLE，强制开启模糊效果。
