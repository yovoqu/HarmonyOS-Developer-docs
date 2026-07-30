# Class (ContextMenuController)

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供控制菜单关闭的能力。开发者可以通过此接口在特定场景下（如定时关闭、点击外部区域关闭等）主动关闭菜单。
 
> [!NOTE]
> 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本Class首批接口从API version 12开始支持。 本模块接口仅可在Stage模型下使用。 以下API需先使用UIContext中的 getContextMenuController() 方法获取ContextMenuController实例，再通过此实例调用对应方法。

  

#### close12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

close(): void
 
关闭当前通过bindContextMenu展示的菜单。若当前无菜单展示，调用本方法无效果。
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**示例：**
 
通过定时器触发，调用ContextMenuController的close方法关闭菜单。
 
```text
import { ContextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  menu: ContextMenuController = this.getUIContext().getContextMenuController();

  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1 Close')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('启动定时器').onClick(() => {
        // 延时10秒后调用close方法关闭菜单
        setTimeout(() => {
          this.menu.close();
        }, 10000);
      })

      Column() {
        Text('Test ContextMenu close')
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      // 绑定自定义菜单，长按触发
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/OtbvURJmTKasL7cDUzXktA/zh-cn_image_0000002655848252.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071444Z&HW-CC-Expire=86400&HW-CC-Sign=721997124CA3728F41CC28F2138A5B0CAC5EC859344FFDE2A05D0E496E9C2151)
