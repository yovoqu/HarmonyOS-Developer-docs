# Class (TextMenuController)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

提供控制文本菜单的能力。


## setMenuOptions16+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

setMenuOptions(options: TextMenuOptions): void

设置菜单选项。

**元服务API：** 从API version 16开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextMenuOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuoptions16对象说明) | 是 | 设置菜单选项。 默认值:{showMode: TextMenuShowMode.DEFAULT} |


**示例：**


```ts
// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 设置在对应的UIContext下优先使用独立窗口显示文本选择菜单
    this.getUIContext()
    .getTextMenuController()
    .setMenuOptions(
    {
      showMode: TextMenuShowMode.PREFER_WINDOW
    }
    );
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
        .height(60)
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .caretStyle({ width: '4vp' })

        Text("这是一个Text，长按弹出文本选择菜单")
        .height(60)
        .copyOption(CopyOptions.InApp)
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
      }.width('100%')
    }
    .height('100%')
  }
}
```


## disableSystemServiceMenuItems20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static disableSystemServiceMenuItems(disable: boolean): void

屏蔽文本选择菜单内所有系统服务菜单项。


**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disable | boolean | 是 | 是否禁用系统服务菜单。true表示禁用，false表示不禁用。 默认值: false |


**示例：**


```ts
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 禁用所有系统服务菜单。
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // 页面消失恢复系统服务菜单。
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
        .height(60)
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .caretStyle({ width: '4vp' })
        .editMenuOptions({
          onCreateMenu: (menuItems: Array<TextMenuItem>) => {
            // menuItems不包含被屏蔽的系统菜单项。
            return menuItems
          },
          onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
            return false
          }
        })
      }.width('100%')
    }
    .height('100%')
  }
}
```


## disableMenuItems20+
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

static disableMenuItems(items: Array<TextMenuItemId>): void

屏蔽文本选择菜单内指定的系统服务菜单项。


**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | Array&lt;[TextMenuItemId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#textmenuitemid12)&gt; | 是 | 禁用菜单项的列表。 默认值: [] 默认不禁用任何菜单。 |


**示例：**


```ts
import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 禁用搜索和翻译菜单。
    TextMenuController.disableMenuItems([TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE])
  }

  aboutToDisappear(): void {
    // 恢复系统服务菜单。
    TextMenuController.disableMenuItems([])
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "这是一个TextInput，长按弹出文本选择菜单" })
        .height(60)
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .caretStyle({ width: '4vp' })
        .editMenuOptions({
          onCreateMenu: (menuItems: Array<TextMenuItem>) => {
            // menuItems不包含搜索和翻译。
            return menuItems;
          },
          onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
            return false
          }
        })
      }.width('100%')
    }
    .height('100%')
  }
}
```
