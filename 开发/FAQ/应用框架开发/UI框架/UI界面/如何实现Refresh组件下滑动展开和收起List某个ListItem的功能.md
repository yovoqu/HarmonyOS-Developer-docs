# 如何实现Refresh组件下滑动展开和收起List某个ListItem的功能

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1380

#### 问题现象

如何实现在Refresh组件下，通过滑动操作展开和收起List组件的第一个ListItem，实现下拉刷新的效果。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bBdO_zFhSf6RMuiBqXVSZA/zh-cn_image_0000002628762558.png?HW-CC-KV=V1&HW-CC-Date=20260701T041159Z&HW-CC-Expire=86400&HW-CC-Sign=969EE49BB852A11EDC7BC49EAC66834F8DF1EA1214587BFA81DFCF4C7ED07859)

 
 

#### 背景知识

[Refresh组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh)可以通过下拉一定距离，实现页面的刷新，下拉的响应灵敏度可以通过[pullDownRatio属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh#pulldownratio12)调整；而滑动[List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)，会在组件滚动前触发[onWillScroll事件回调](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common#onwillscroll12)，执行回调操作。
 
 

#### 解决方案

在onWillScroll事件回调中判断当前List组件滚动的偏移量和移动状态，当满足预定条件时，修改第一个ListItem的高度，实现ListItem的展开和收起；同时为了避免手势冲突，当此ListItem未展开时，设置Refresh的pullDownRatio属性参数为0，即不跟随手势下拉。
 
示例代码如下：
 
```text
@Entry
@Component
struct ScalingComponent {
  @State isRefreshing: boolean = false;
  @State itemList: string[] = [];
  @State isExpand: boolean = false;
  private minHeight = 30;
  private maxHeight = 200;
  private scroller: ListScroller = new ListScroller();
  aboutToAppear(): void {
    for (let i = 1; i < 11; i++) {
      this.itemList.push(`Item Text ${i}`);
    };
  };

  build() {
    Refresh({ refreshing: $$this.isRefreshing }) {
      List({ space: 5, scroller: this.scroller }) {
        <em>// 可展开收起的ListItem</em>
        ListItem() {
          Text('Scaling component');
        }
        .height(this.isExpand ? this.maxHeight : this.minHeight) <em>// 通过状态变量的变化改变组件高度</em>
        .width('100%')
        .align(Alignment.Top);

        ForEach(this.itemList, (item: string) => {
          ListItem() {
            Text(item)
              .fontColor('#000');
          }
          .height(100)
          .width('100%')
          .borderRadius(16)
          .backgroundColor('#f1f3f5');
        });
      } .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])

      .padding({left:16,right:16})
      .height('100%')
      .width('100%')
      .onWillScroll((offset, state, source) => {
       <em> // 当List处于开始边缘时，手势向下拉，回调结果为偏移量offset=0，滚动状态state=1，此时展开ListItem；其他情况收起ListItem</em>
        console.info(`source: ${source}`);
        if (offset === 0 && state === 1) {
          this.isExpand = true;
        } else {
          this.isExpand = false;
        };
      });
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    .height('100%')
    .width('100%')

    <em>// 当ListItem未展开时，Refresh组件不随手势下拉</em>
    .pullDownRatio(this.isExpand ? undefined : 0)
    .onRefreshing(() => {
      setTimeout(() => {
        this.isRefreshing = false;
      }, 2000);
    });
  };
};
```
