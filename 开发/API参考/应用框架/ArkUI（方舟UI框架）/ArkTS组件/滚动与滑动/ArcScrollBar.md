# ArcScrollBar

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

弧形滚动条组件ArcScrollBar，用于配合可滚动组件使用，如[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)、[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Grid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid)、[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)、[WaterFlow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)。
 
> [!NOTE]
> 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 ArcScrollBar不设置宽高时，采用父组件 LayoutConstraint 中的maxSize作为宽高。如果ArcScrollBar的父组件存在可滚动组件，如 ArcList 、 List 、 Grid 、 Scroll 、 WaterFlow ，建议设置ArcScrollBar宽高，否则ArcScrollBar的宽高可能为无穷大。 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

  

#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不包含子组件。
 
  

#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcScrollBar(options: ArcScrollBarOptions)
 
ArcScrollBar的构造函数。
 
**元服务API：** 从API version 18开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Circle
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ArcScrollBarOptions | 是 | 滚动条组件参数。 |
 
 
  

#### ArcScrollBarOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ArcScrollBar的构造函数参数。
 
**元服务API：** 从API version 18开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Circle
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scroller | Scroller | 否 | 否 | 可滚动组件的控制器，用于与可滚动组件进行绑定。 |
| state | BarState | 否 | 是 | 滚动条状态。 默认值：BarState.Auto |
 
 
> [!NOTE]
> ArcScrollBar与可滚动组件需通过scroller进行绑定后方能实现联动，且ArcScrollBar与可滚动组件仅限于一对一的绑定方式。

 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该示例通过ArcScrollBar与[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件联动，设置了弧形外置滚动条。
 
```text
import { ArcScrollBar } from '@kit.ArkUI';

@Entry
@Component
struct ArcScrollBarExample {
  private scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              Text(item.toString())
                .width('80%')
                .height(60)
                .backgroundColor('#3366CC')
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 5 })
            }
          }, (item: number) => item.toString())
        }.margin({ right: 15 })
      }
      .width('90%')
      .scrollBar(BarState.Off)

      ArcScrollBar({ scroller: this.scroller, state: BarState.Auto })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/GH8pVXxGTHi6cpVe6bTj1A/zh-cn_image_0000002628862394.png?HW-CC-KV=V1&HW-CC-Date=20260701T014335Z&HW-CC-Expire=86400&HW-CC-Sign=992915F72CF63B453D7316FC1F2E81F4B2E9F90225D32D123308E45AAA4AB2BD)
