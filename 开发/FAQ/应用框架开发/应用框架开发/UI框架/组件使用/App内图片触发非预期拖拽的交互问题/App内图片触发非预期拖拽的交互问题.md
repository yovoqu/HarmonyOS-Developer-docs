# App内图片触发非预期拖拽的交互问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1503

#### 问题现象

某些场景下的图片，如PC自由多窗模式下，左侧导航页签图标可以拖动，与使用习惯不符合。异常效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/mtp43iQtREuhcnJWGvs_vQ/zh-cn_image_0000002658965761.png?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=F758B37131211E51F963109E9BCAB2B6F2F7232B70E00963DA236F4A255D8795)

 
 

#### 背景知识

- [Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
- [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)：图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式，不支持apng和svga格式。
- [draggable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#draggable9)：设置组件默认拖拽效果。默认值为true，组件可拖拽，绑定的长按手势不生效。若需要设置自定义手势，则需要将draggable设置为false。设置为false之后，拖拽类事件不再触发。
- [拖拽实现原理](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-unified-drag-and-drop)：拖拽流程可以分为三部分：发起拖拽、拖拽中和释放拖拽。其中，拖出方通过draggable()和onDragStart()等接口处理拖出数据，拖入方通过allowDrop()和onDrop()等接口处理拖入数据。

 
 

#### 问题定位
1. 使用DevEco Testing-实用工具-UIViewer查看页面布局，发现菜单栏Tabs组件下使用了Image组件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ELLWFYk_Ruiup1aXsweyjw/zh-cn_image_0000002628606550.png?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=CCB55ADB92E7CF8BB36B8C960339B833CE0DB5E084C5CCBDA36622D9C22A253C)

2. 排查代码Image组件中draggable属性值是否为可拖拽状态。Image的draggable设置为true或者未设置，图片都是可拖动。示例代码如下：
```text
Image($r('sys.media.ohos_ic_public_albums')) <em>// 本地资源，需自行替换</em>
  .width(24)
  .height(24)
  .objectFit(ImageFit.Fill)
  .margin({ bottom: 8 })
```

 
 

#### 分析结论

Image组件中未设置draggable属性，该属性默认为true，组件可拖拽。
 
 

#### 修改建议

给Image组件设置draggable属性为false，使拖拽类事件不再触发。示例代码如下：
 
```text
@Entry
@Component
struct TabImageExample {
  private currentIndex: number = 0;
  @State selectedIndex: number = 0;
  private controller: TabsController = new TabsController();
  private data: number[] = [];


  aboutToAppear(): void {
    for (let i = 0; i < 4; i++) {
      this.data.push(i);
    }
  }


  @Builder
  tabBuilder(index: number) {
    Column() {
      Image($r('sys.media.ohos_ic_public_albums')) <em>// 本地资源，需自行替换</em>
        .width(24)
        .height(24)
        .objectFit(ImageFit.Fill)
        .margin({ bottom: 8 })
        .draggable(false);


      Text(`页签${index}`)
        .fontWeight(this.selectedIndex === index ? FontWeight.Bold : FontWeight.Normal)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400);
    }
    .width('100%');
  }


  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        ForEach(this.data, (item: number) => {
          TabContent() {
            Column() {
              Text(`页签${item}`)
                .fontSize(20);
            }
            .width('100%')
            .height('100%')
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#E5E5EA');
          }.tabBar(this.tabBuilder(item));
        });
      }
      .vertical(true)
      .barMode(BarMode.Fixed)
      .barWidth(100)
      .barHeight('100%')
      .animationDuration(400)
      .onAnimationStart((targetIndex: number) => {
        this.selectedIndex = targetIndex;
      })
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5');
    }
    .width('100%');
  }
}
```
 
效果图如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/X_OiIAcrTseMaQNGFg_NxQ/zh-cn_image_0000002658845799.png?HW-CC-KV=V1&HW-CC-Date=20260811T005742Z&HW-CC-Expire=86400&HW-CC-Sign=5C149C70A9FD38C68B5800CEF5EC9B327EB2AF9BF4F24EF0F04E923550FE0F04)
