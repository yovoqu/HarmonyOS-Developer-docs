# Web组件内容过长时，底部的内容无法滑动联动如何解决

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-133

#### 问题现象

当Web组件内容过长时，出现了布局问题，底部固定栏文字超出屏幕范围并被截断，该如何解决？
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ol8t07AtRMOEWeuYtJ57LA/zh-cn_image_0000002628899132.png?HW-CC-KV=V1&HW-CC-Date=20260811T005837Z&HW-CC-Expire=86400&HW-CC-Sign=70FB0FDF070668461EF786DEEC472FCC0A5F0E8C73C73DB99E0039FEEABE400A)

 
示例代码：
 
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebScroll {
  controller: webview.WebviewController = new webview.WebviewController();
  private scrollerForScroll: Scroller = new Scroller();

  build() {
    Column() {
      Text('标题');
      Scroll(this.scrollerForScroll) {
        Column() {
          Text('下面是Web组件');
          Web({ src: 'https://developer.huawei.com/consumer/', controller: this.controller })
            .height('100%');
          Text('文字1');
          Text('文字2');
          Text('文字3');
        };
      }
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical);

      Text('底部固定栏');
    };
  }
}
```
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/3gqa3tqzQAqkmrpvo0ctJw/zh-cn_image_0000002659138401.png?HW-CC-KV=V1&HW-CC-Date=20260811T005837Z&HW-CC-Expire=86400&HW-CC-Sign=D34A19119F8E7D3F3DCBFA2601DB946BE4541E25B026038A86C353A8FAC9FDE5)

 
 

#### 背景知识

- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web)：提供具有网页显示能力的Web组件。
- [layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)：设置组件的布局权重，使组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。

 
 

#### 问题定位

针对布局问题，首先分析组件的层级结构：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/WTH7xHS2SlK5-gn738pXzQ/zh-cn_image_0000002629059050.png?HW-CC-KV=V1&HW-CC-Date=20260811T005837Z&HW-CC-Expire=86400&HW-CC-Sign=AC1BFBAC41804ED56F597890F73F268D5E2D283C1CCED96F6F62AE063BBCF775)

 
当未指定高度时，Column、Scroll组件的默认高度、宽度均是100%。
 
 

#### 分析结论

Scroll组件和标题文字已经占据了全部屏幕内容控件，导致底部固定栏文字的位置超过了屏幕内容区域范围，扩展到屏幕底部安全区域。
 
 

#### 修改建议

layoutWeight属性可以实现高度自适应效果，如果父容器尺寸确定时，设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，忽略元素本身尺寸设置，自适应占满剩余空间。将Scroll组件设置layoutWeight(1)即可自适应高度解决此问题。
 
示例代码：
```text
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebScroll {
  controller: WebviewController = new webview.WebviewController();
  private scrollerForScroll: Scroller = new Scroller();

  build() {
    Column() {
      Text('标题');
      Scroll(this.scrollerForScroll) {
        Column() {
          Text('下面是Web组件');
          Web({ src: 'www.example.com', controller: this.controller })
            .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
            .height('100%')
            .fileAccess(false)
            .geolocationAccess(false);
          Text('文字1');
          Text('文字2');
          Text('文字3');
        };
      }
      .scrollBar(BarState.Off)
      .layoutWeight(1)
      .scrollable(ScrollDirection.Vertical);

      Text('底部固定栏');
    };
  }
}
```
