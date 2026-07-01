# Tabs如何实现TabBar中TabItem不均匀分布

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-958

#### 问题现象

如何实现Tabs的页签不均匀分布，两个靠左，两个靠右，中间留下一个按钮的区域。
 
 

#### 背景知识

- [position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#position)(value:[Position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#position)|[Edges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edges12)|[LocalizedEdges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizededges12))确定子组件相对父组件内容区的位置。其中Edges类型基于父组件内容区四边确定位置，top/left/right/bottom分别为组件各边距离父组件内容区相应边的边距，通过边距来确定组件相对于父组件内容区的位置。
- [Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

 
 

#### 解决方案

方案一：利用组件的position属性自定义每一个TabItem的位置。
 1. 使用@Builder装饰器自定义以Column为主体的TabItem组件，为Column设置position属性，以不同TabItem的Index为条件，为每一个TabItem设置不同的边距值，达到自定义每一个TabItem的位置。
```text
@Builder
TabItem(tabName: string, tabIndex: number) {
<em>  // 标签页项的布局</em>
  Column({ space: 10 }) {
    Column() {
      Image($r('app.media.startIcon'))
        .width(32).height(32)
        .margin({ top: 5 });
      Text(tabName).fontSize(14)
        .margin({ top: 5 });
    }
    .width('100%')
    .height('10%')
    .justifyContent(FlexAlign.Center);
  }
  .justifyContent(FlexAlign.Center)
  .onClick(() => {
    this.controller.changeIndex(tabIndex);
    this.focusIndex = tabIndex;
  })
  .width('12%')
  .padding({ bottom: 10 })
  .backgroundColor(Color.White)
  .position( <em>// 设置TabItem的相对位置</em>
    tabIndex === 1 ? { left: 80 } :
      tabIndex === 2 ? { right: 90 } :
        tabIndex === 3 ? { right: 0 } : {});
}
```

2. 最后用Row组件和ForEach方法依序为TabItem赋Index值。则可实现TabItem在TabBar中不均匀分布的效果。
```text
<em>// 用Row组件实现TabBar效果</em>
Row() {
  ForEach(this.tabArray, (item: number, index: number) => {
    this.TabItem('页签 ' + item, index);
  });
}
.justifyContent(FlexAlign.SpaceBetween)
.alignItems(VerticalAlign.Bottom)
.width('100%')
.backgroundColor(Color.White);
```

 
完整示例参考如下：
 
```text
@Entry
@Component
export struct CusTab2 {
  @State tabArray: Array<number> = [0, 1, 2, 3];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  TabItem(tabName: string, tabIndex: number) {
   <em> // 标签页项的布局</em>
    Column({ space: 10 }) {
      Column() {
        Image($r('app.media.startIcon'))
          .width(32).height(32)
          .margin({ top: 5 });
        Text(tabName).fontSize(14)
          .margin({ top: 5 });
      }
      .width('100%')
      .height('10%')
      .justifyContent(FlexAlign.Center);
    }
    .justifyContent(FlexAlign.Center)
    .onClick(() => {
      this.controller.changeIndex(tabIndex);
      this.focusIndex = tabIndex;
    })
    .width('12%')
    .padding({ bottom: 10 })
    .backgroundColor(Color.White)
    .position( <em>// 设置TabItem的相对位置</em>
      tabIndex === 1 ? { left: 80 } :
        tabIndex === 2 ? { right: 90 } :
          tabIndex === 3 ? { right: 0 } : {});
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.BottomStart }) {
       <em> // Tabs</em>
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text('我是页面 ' + item + ' 的内容')
                .height(10)
                .width('100%')
                .fontSize(30)
                .textAlign(TextAlign.Center);
            }
            .backgroundColor(Color.White);
          });
        }
        .barHeight(0)
        .animationDuration(100)
        .onChange((index: number) => {
          console.info('foo change');
          this.focusIndex = index;
        });

       <em> // 用Row组件实现TabBar效果</em>
        Row() {
          ForEach(this.tabArray, (item: number, index: number) => {
            this.TabItem('页签 ' + item, index);
          });
        }
        .justifyContent(FlexAlign.SpaceBetween)
        .alignItems(VerticalAlign.Bottom)
        .width('100%')
        .backgroundColor(Color.White);

      }
      .width('100%');
    }
    .height('100%');
  }
}
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/z9KWFqpDQcq-Ph41r6OVRg/zh-cn_image_0000002658800929.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041145Z&HW-CC-Expire=86400&HW-CC-Sign=01017F0BADAD37A87AE75A26C6285B3D9B00DB77275F7CADEAB9465ADB20BBB1)

 
方案二：设置异形TabBar达到不均匀分布的效果。1. 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%。
```text
@Builder
Tab(tabName: string, tabIndex: number) {
  Column({ space: 10 }) {
    Stack() {
      Column() {
        Image($r('app.media.startIcon'))
          .width(32).height(32);
        Text(tabName).fontSize(14)
          .margin({ top: 5 });
      }
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
    .margin({ bottom: tabIndex === 2 ? 40 : 0 });
  }
  .justifyContent(FlexAlign.Center)
  .onClick(() => {
    this.controller.changeIndex(tabIndex);
    this.focusIndex = tabIndex;
  })
  .width(tabIndex === 2 ? '28%' : '18%')
 <em> // 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%</em>
  .padding({ top: 10, bottom: 10 })
  .backgroundColor(Color.White)
  .borderRadius(tabIndex === 2 ? { topLeft: '50%', topRight: '50%' } : {});
}
```

 
 
完整示例参考如下：
 
```text
@Entry
@Component
export struct CusTab2 {
  @State tabArray: Array<number> = [0, 1, 2, 3, 4];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  Tab(tabName: string, tabIndex: number) {
    Column({ space: 10 }) {
      Stack() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(32).height(32);
          Text(tabName).fontSize(14)
            .margin({ top: 5 });
        }
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .margin({ bottom: tabIndex === 2 ? 40 : 0 });
    }
    .justifyContent(FlexAlign.Center)
    .onClick(() => {
      this.controller.changeIndex(tabIndex);
      this.focusIndex = tabIndex;
    })
    .width(tabIndex === 2 ? '28%' : '18%')
   <em> // 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%</em>
    .padding({ top: 10, bottom: 10 })
    .backgroundColor(Color.White)
    .borderRadius(tabIndex === 2 ? { topLeft: '50%', topRight: '50%' } : {});
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.BottomStart }) {
       <em> // tabs</em>
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text('我是页面 ' + item + ' 的内容')
                .height(10)
                .width('100%')
                .fontSize(30)
                .textAlign(TextAlign.Center);
            }
            .backgroundColor('#F1F3F5');
          });
        }
        .barHeight(0)
        .animationDuration(100)
        .onChange((index: number) => {
          console.info('foo change');
          this.focusIndex = index;
        }); <em>// 页签</em>

        Row() {
          ForEach(this.tabArray, (item: number, index: number) => {
            this.Tab('页签 ' + item, index);
          });
        }
        .justifyContent(FlexAlign.SpaceBetween)
        .alignItems(VerticalAlign.Bottom)
        .width('100%');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/_WPSkHNCThKcLtEYmzDtJg/zh-cn_image_0000002628401672.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041145Z&HW-CC-Expire=86400&HW-CC-Sign=CBE823A2EFB5D4D0F561D81091FA4A8E7C9BBEE6746A81B332F577155596CB6F)

 
 

#### 总结

使用@Builder装饰器自定义以Column为主体的TabItem组件，为Column设置position属性，以不同TabItem的Index为条件，为每一个TabItem设置不同的边距值，达到自定义每一个TabItem的位置。
