# ComposeTitleBarV2

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composetitlebarv2
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ComposeTitleBarV2组件是一种标题栏，支持设置标题、头像（可选）和副标题（可选），可用于一级页面、二级及其以上界面配置返回键。

该组件基于[状态管理（V2）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v2)实现，相较于[状态管理（V1）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制普通标题栏的数据和状态，实现更高效的用户界面刷新。

> [!NOTE]
> 该组件仅可在Stage模型下使用。 如果ComposeTitleBarV2设置 通用属性 和 通用事件 ，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ComposeTitleBarV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ComposeTitleBarV2设置通用属性和通用事件。


**起始版本：** 26.0.0


#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { ComposeTitleBarV2, ComposeTitleBarV2MenuItem } from '@kit.ArkUI';
```



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无



#### ComposeTitleBarV2

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ComposeTitleBarV2({item?: ComposeTitleBarV2MenuItem, title: ResourceStr, subtitle?: ResourceStr, menuItems?: Array&lt;ComposeTitleBarV2MenuItem&gt;})

ComposeTitleBarV2组件是一种标题栏，支持设置标题、头像（可选）和副标题（可选），可用于一级页面、二级及其以上界面配置返回键。

> [!NOTE]
> 入参不可为undefined，即ComposeTitleBarV2(undefined)。


**起始版本：** 26.0.0

**装饰器类型：** @ComponentV2

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet、TV）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Wearable）。因硬件能力限制，该接口在Wearable设备中调用将运行异常，异常信息中提示接口未定义。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| item | ComposeTitleBarV2MenuItem | 否 | @Param | 用于左侧头像的单个菜单项。 |
| title | ResourceStr | 是 | @Param | 标题。 |
| subtitle | ResourceStr | 否 | @Param | 副标题。 |
| menuItems | Array&lt;ComposeTitleBarV2MenuItem&gt; | 否 | @Param | 右侧菜单项列表。 |




#### ComposeTitleBarV2MenuItem

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

菜单项类，用于定义标题栏左侧头像或右侧菜单项。

**装饰器类型：** @ObservedV2



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet、TV）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Wearable）。因硬件能力限制，该接口在Wearable设备中调用将运行异常，异常信息中提示接口未定义。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 图标资源。 装饰器类型： @Trace |
| symbolStyle | SymbolGlyphModifier | 否 | 是 | Symbol图标资源，优先级大于value，item左侧头像不支持设置该属性。 装饰器类型： @Trace |
| label | ResourceStr | 否 | 是 | 图标标签描述。 装饰器类型： @Trace |
| isEnabled | boolean | 否 | 是 | 是否启用，默认启用。 isEnabled为true时，表示启用。 isEnabled为false时，表示禁用。 item属性不支持触发isEnabled属性。 默认值：true。 装饰器类型： @Trace |
| action | OnActionCallback | 否 | 是 | 触发时的动作闭包，item属性不支持触发action事件。 装饰器类型： @Trace |
| accessibilityLevel | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会根据情况转换成'yes'或'no'。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"。 装饰器类型： @Trace |
| accessibilityText | ResourceStr | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为" "。 装饰器类型： @Trace |
| accessibilityDescription | ResourceStr | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值："单指双击即可执行"。 装饰器类型： @Trace |




#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(params?: ComposeTitleBarV2MenuItemParams)

ComposeTitleBarV2MenuItem的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet、TV）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Wearable）。因硬件能力限制，该接口在Wearable设备中调用将运行异常，异常信息中提示接口未定义。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | ComposeTitleBarV2MenuItemParams | 否 | 菜单项参数对象。 |




#### ComposeTitleBarV2MenuItemParams

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

菜单项参数接口，用于创建ComposeTitleBarV2MenuItem实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet、TV）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Wearable）。因硬件能力限制，该接口在Wearable设备中调用将运行异常，异常信息中提示接口未定义。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 图标资源。 |
| symbolStyle | SymbolGlyphModifier | 否 | 是 | Symbol图标资源，优先级大于value，item左侧头像不支持设置该属性。 |
| label | ResourceStr | 否 | 是 | 图标标签描述。 |
| isEnabled | boolean | 否 | 是 | 是否启用，默认启用。 isEnabled为true时，表示启用。 isEnabled为false时，表示禁用。 item属性不支持触发isEnabled属性。 默认值：true。 |
| action | OnActionCallback | 否 | 是 | 触发时的动作闭包，item属性不支持触发action事件。 |
| accessibilityLevel | string | 否 | 是 | 标题栏右侧自定义按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。 支持的值为： "auto"：当前组件会根据情况转换成'yes'或'no'。 "yes"：当前组件可被无障碍辅助服务所识别。 "no"：当前组件不可被无障碍辅助服务所识别。 "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。 默认值："auto"。 |
| accessibilityText | ResourceStr | 否 | 是 | 标题栏右侧自定义按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。 默认值：有label默认值为当前项label属性内容，没有设置label时，默认值为" "。 |
| accessibilityDescription | ResourceStr | 否 | 是 | 标题栏右侧自定义按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。 默认值："单指双击即可执行"。 |




#### OnActionCallback

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type OnActionCallback = () => void

点击菜单项时触发的回调函数类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet、TV）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、TV、Wearable）。因硬件能力限制，该接口在Wearable设备中调用将运行异常，异常信息中提示接口未定义。



#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。



#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（简单的标题栏）

从API版本26.0.0开始，可以使用ComposeTitleBarV2接口实现简单的标题栏，该示例展示了ComposeTitleBarV2的基本用法。

```text
import { ComposeTitleBarV2, ComposeTitleBarV2MenuItem, Prompt } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  // 定义右侧菜单项目列表
  @Local menuItems: Array<ComposeTitleBarV2MenuItem> = [
    new ComposeTitleBarV2MenuItem({
      // 菜单图片资源
      value: $r('sys.media.ohos_save_button_filled'),
      // 启用图标
      isEnabled: true,
      // 点击菜单时触发事件
      action: () => Prompt.showToast({ message: 'icon 1' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_copy'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 2' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_edit'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 3' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_remove'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 4' }),
    }),
  ]

  build(): void {
    Row() {
      Column() {
        // 分割线
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 1),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 2),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems,
        })
        Divider().height(2).color(0xCCCCCC)
        // 定义带头像的标题栏
        ComposeTitleBarV2({
          menuItems: [
            new ComposeTitleBarV2MenuItem({
              isEnabled: true,
              value: $r('sys.media.ohos_save_button_filled'),
              action: () => Prompt.showToast({ message: 'icon' }),
            })
          ],
          title: '标题',
          subtitle: '副标题',
          item: new ComposeTitleBarV2MenuItem({
            isEnabled: true,
            value: $r('sys.media.ohos_app_icon')
          })
        })
        Divider().height(2).color(0xCCCCCC)
      }
    }.height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/vz0Nxx44QA2oG141n-OpJA/zh-cn_image_0000002698223107.png?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=69834A9AD94694DA775C9FE30ED730534D4648EE6A25EE1DE5A98AE9E17F70A5)




#### 示例2（右侧自定义按钮播报）

从API版本26.0.0开始，通过设置标题栏右侧自定义按钮的以下属性接口accessibilityText、accessibilityDescription、accessibilityLevel，实现自定义屏幕朗读播报文本。

```text
import { ComposeTitleBarV2, ComposeTitleBarV2MenuItem, Prompt } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  // 定义右侧菜单项目列表
  @Local menuItems: Array<ComposeTitleBarV2MenuItem> = [
    new ComposeTitleBarV2MenuItem({
      // 菜单图片资源
      value: $r('sys.media.ohos_save_button_filled'),
      // 启用图标
      isEnabled: true,
      // 点击菜单时触发事件
      action: () => Prompt.showToast({ message: 'icon 1' }),
      // 屏幕朗读播报文本，优先级比label高
      accessibilityText: '保存',
      // 屏幕朗读是否可以聚焦到
      accessibilityLevel: 'yes',
      // 屏幕朗读最后播报的描述文本
      accessibilityDescription: '点击操作保存图标',
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_copy'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 2' }),
      accessibilityText: '复制',
      // 此处为no，屏幕朗读不聚焦
      accessibilityLevel: 'no',
      accessibilityDescription: '点击操作复制图标',
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_edit'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 3' }),
      accessibilityText: '编辑',
      accessibilityLevel: 'yes',
      accessibilityDescription: '点击操作编辑图标',
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.media.ohos_ic_public_remove'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'icon 4' }),
      accessibilityText: '移除',
      accessibilityLevel: 'yes',
      accessibilityDescription: '点击操作移除图标',
    }),
  ]

  build(): void {
    Row() {
      Column() {
        // 分割线
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 1),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 2),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems,
        })
        Divider().height(2).color(0xCCCCCC)
        // 定义带头像的标题栏
        ComposeTitleBarV2({
          menuItems: [
            new ComposeTitleBarV2MenuItem({
              isEnabled: true,
              value: $r('sys.media.ohos_save_button_filled'),
              action: () => Prompt.showToast({ message: 'icon' }),
            })
          ],
          title: '标题',
          subtitle: '副标题',
          item: new ComposeTitleBarV2MenuItem({
            isEnabled: true,
            value: $r('sys.media.ohos_app_icon'),
          }),
        })
        Divider().height(2).color(0xCCCCCC)
      }
    }.height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/oqI1FIOWR_SM9BwAoMpYzA/zh-cn_image_0000002698143015.png?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=6DFC76DA1465D81F1508220B8629EF7D68D5BEC3530EBDD6AF0D76ACC63D1FCB)




#### 示例3（设置Symbol类型图标）

从API版本26.0.0开始，通过设置ComposeTitleBarV2MenuItem的属性接口symbolStyle，实现Symbol类型图标的配置。

```text
import { ComposeTitleBarV2, ComposeTitleBarV2MenuItem, Prompt, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  // 定义右侧菜单项目列表
  @Local menuItems: Array<ComposeTitleBarV2MenuItem> = [
    new ComposeTitleBarV2MenuItem({
      // 菜单图片资源
      value: $r('sys.symbol.house'),
      // 菜单symbol图标，优先级大于value
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]),
      // 启用图标
      isEnabled: true,
      // 点击菜单时触发事件
      action: () => Prompt.showToast({ message: 'symbol icon 1' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.symbol.house'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'symbol icon 2' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.symbol.car'),
      symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor([Color.Pink]),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'symbol icon 3' }),
    }),
    new ComposeTitleBarV2MenuItem({
      value: $r('sys.symbol.car'),
      isEnabled: true,
      action: () => Prompt.showToast({ message: 'symbol icon 4' }),
    }),
  ]

  build(): void {
    Row() {
      Column() {
        // 分割线
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 1),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems.slice(0, 2),
        })
        Divider().height(2).color(0xCCCCCC)
        ComposeTitleBarV2({
          title: '标题',
          subtitle: '副标题',
          menuItems: this.menuItems,
        })
        Divider().height(2).color(0xCCCCCC)
        // 定义带头像的标题栏
        ComposeTitleBarV2({
          menuItems: [
            new ComposeTitleBarV2MenuItem({
              isEnabled: true,
              value: $r('sys.symbol.heart'),
              action: () => Prompt.showToast({ message: 'symbol icon 1' }),
            })
          ],
          title: '标题',
          subtitle: '副标题',
          item: new ComposeTitleBarV2MenuItem({
            isEnabled: true,
            value: $r('sys.media.ohos_app_icon'),
          }),
        })
        Divider().height(2).color(0xCCCCCC)
      }
    }.height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/UAUZLF_zRYGjrT_lpJSF4A/zh-cn_image_0000002668303350.png?HW-CC-KV=V1&HW-CC-Date=20260811T005506Z&HW-CC-Expire=86400&HW-CC-Sign=687803E5AD1DA0DC0DD3C237454A28393EDBD1E4EC9807EAC474B3D8CDDE42A6)
