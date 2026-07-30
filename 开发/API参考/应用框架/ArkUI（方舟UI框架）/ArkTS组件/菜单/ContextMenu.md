# ContextMenu

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-menu
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

在页面范围内关闭通过[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12)属性绑定的菜单。
 
> [!NOTE]
> 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### ContextMenu.close(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

static close(): void
 
在页面范围内关闭通过[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu12)绑定的菜单。常用于页面跳转、拖拽开始等需要主动关闭已显示菜单的交互场景。
 
> [!NOTE]
> 从API version 8开始支持。从API version 18开始废弃，建议使用 UIContext 中的 getContextMenuController 获取 ContextMenuController 实例，再通过此实例调用替代方法 close 。 两者功能相同，区别在于：ContextMenu.close()是静态方法，在多窗口场景下可能无法明确指定要关闭哪个窗口的菜单；而通过UIContext获取的ContextMenuController实例调用close()可以关联到具体的UIContext，从而明确指定操作的UI上下文，建议在API version 12及以上版本中使用UIContext方式。

 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该示例演示ContextMenu.close的使用方法，在拖拽开始时关闭通过bindContextMenu绑定的菜单。
 
> [!NOTE]
> 推荐通过使用 UIContext 中的 getContextMenuController 来明确UI的执行上下文。

 
```ArkTS
// xxx.ets
@Entry
@Component
struct Index {
  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('ContextMenu1')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Column() {
        Text('Long press to show ContextMenu')
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
      .onDragStart(() => {
        // 拖拽时关闭菜单
        ContextMenu.close() // 建议使用 this.getUIContext().getContextMenuController().close()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/lsEeeKaBS7OCGtx0QumhVA/zh-cn_image_0000002656008826.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071513Z&HW-CC-Expire=86400&HW-CC-Sign=0E6AB72729773F5A0C7E526D3B1F974C51BE383D1A213CC60D5E221150EB7169)
