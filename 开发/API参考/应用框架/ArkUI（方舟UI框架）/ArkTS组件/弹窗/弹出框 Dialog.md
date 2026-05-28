# 弹出框 (Dialog)

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

弹出框是一种模态窗口，用于临时展示用户需关注的信息或待处理的操作，同时保持当前上下文环境。用户必须完成交互才能退出该模式。

> [!NOTE]
> 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 该组件仅可在Stage模型下使用。 如果Dialog设置 通用属性 和 通用事件 ，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到Dialog本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议Dialog设置通用属性和通用事件。



##### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { TipsDialog, SelectDialog, ConfirmDialog, AlertDialog, LoadingDialog, CustomContentDialog } from '@kit.ArkUI';
```



##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无



##### TipsDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

TipsDialog({controller: CustomDialogController, imageRes: ResourceStr | PixelMap, imageSize?: SizeOptions, title?: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, checkAction?: (isChecked: boolean) => void, onCheckedChange?: Callback&lt;boolean&gt;, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

提示弹出框，即为带图形确认弹出框，必要时可通过图形化方式展现确认弹出框。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | CustomDialogController | 是 | - | 提示弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| imageRes | ResourceStr \| PixelMap | 是 | - | 展示的图片。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| imageSize | SizeOptions | 否 | - | 自定义图片尺寸。 默认值：64*64vp 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| title | ResourceStr | 否 | - | 提示弹出框标题。 默认不设置或设置为undefined，弹出框标题不显示。 说明： 标题超过两行会显示“...”。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| content | ResourceStr | 否 | - | 提示弹出框内容。 默认不设置或设置为undefined，弹出框内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | ResourceStr | 否 | - | checkbox的提示内容。 默认不设置或设置为undefined，提示内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | value为true时，表示checkbox已选中，value为false时，表示未选中。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| checkAction12+ | (isChecked: boolean) => void | 否 | - | checkbox的选中状态改变事件。isChecked为true时，表示checkbox已选中，isChecked为false时，表示checkbox未选中。现推荐使用onCheckedChange12+。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | Callback&lt;boolean&gt; | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | ButtonOptions | 否 | - | 提示弹出框左侧按钮。 默认不设置或设置为undefined，左侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | ButtonOptions | 否 | - | 提示弹出框右侧按钮。 默认不设置或设置为undefined，右侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | Theme \| CustomTheme | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | ThemeColorMode | 否 | - | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### SelectDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

SelectDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, selectedIndex?: number, confirm?: ButtonOptions, radioContent: Array&lt;SheetInfo&gt;, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

选择类弹出框，弹框中以列表或网格的形式提供可选的内容。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | CustomDialogController | 是 | 选择弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| title | ResourceStr | 是 | 选择弹出框标题。 说明： 标题超过两行会显示“...”。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| content | ResourceStr | 否 | 选择弹出框内容。 默认不设置或设置为undefined，弹出框内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| selectedIndex | number | 否 | 选择弹出框的选中项。 取值范围：大于等于-1的整数。 默认值：-1，没有选中项。若设置数值小于-1，按没有选中项处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| confirm | ButtonOptions | 否 | 选择弹出框底部按钮。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| radioContent | Array&lt;SheetInfo&gt; | 是 | 选择弹出框的子项内容列表，每个选择项支持设置文本和选中的回调事件。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | Theme \| CustomTheme | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | ThemeColorMode | 否 | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### ConfirmDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ConfirmDialog({controller: CustomDialogController, title: ResourceStr, content?: ResourceStr, checkTips?: ResourceStr, isChecked?: boolean, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

信息确认类弹出框，操作未正确执行（如网络错误、电池电量过低），或未正确操作时（如指纹录入），反馈的错误或提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | CustomDialogController | 是 | - | 确认弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| title | ResourceStr | 是 | - | 确认弹出框标题。 说明： 标题超过两行会显示“...”。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| content | ResourceStr | 否 | - | 确认弹出框内容。 默认不设置或设置为undefined，确认弹出框内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| checkTips | ResourceStr | 否 | - | checkbox的提示内容。 默认不设置或设置为undefined，checkbox的提示内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| isChecked | boolean | 否 | @Prop | value为true时，表示checkbox已选中，value为false时，表示未选中。 默认值：false 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| onCheckedChange12+ | Callback&lt;boolean&gt; | 否 | - | checkbox的选中状态改变事件回调。回调参数类型为boolean，true表示checkbox已选中，false表示checkbox未选中。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| primaryButton | ButtonOptions | 否 | - | 确认弹出框左侧按钮。 默认不设置或设置为undefined，确认弹出框左侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | ButtonOptions | 否 | - | 确认弹出框右侧按钮。 默认不设置或设置为undefined，确认弹出框右侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | Theme \| CustomTheme | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | ThemeColorMode | 否 | - | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### AlertDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AlertDialog({controller: CustomDialogController, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, content: ResourceStr, primaryButton?: ButtonOptions, secondaryButton?: ButtonOptions, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

操作确认类弹出框，触发一个将产生严重后果的不可逆操作时，如删除、重置、取消编辑、停止等。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | CustomDialogController | 是 | 确认弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| primaryTitle12+ | ResourceStr | 否 | 确认弹出框一级标题。 默认不设置或设置为undefined，确认弹出框一级标题不显示。 说明： 标题超过两行会显示“...”。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| secondaryTitle12+ | ResourceStr | 否 | 确认弹出框二级标题。 默认不设置或设置为undefined，确认弹出框二级标题不显示。 说明： 标题超过两行会显示“...”。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| content | ResourceStr | 是 | 确认弹出框内容。 默认不设置或设置为undefined，确认弹出框内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| primaryButton | ButtonOptions | 否 | 确认弹出框左侧按钮。 默认不设置或设置为undefined，确认弹出框左侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryButton | ButtonOptions | 否 | 确认弹出框右侧按钮。 默认不设置或设置为undefined，确认弹出框右侧按钮不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | Theme \| CustomTheme | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | ThemeColorMode | 否 | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### LoadingDialog

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

LoadingDialog({Controller: CustomDialogController, content?: ResourceStr, theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

进度加载类弹出框，用于显示操作执行中的提示信息。

**装饰器类型：**@CustomDialog

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Controller | CustomDialogController | 是 | 加载弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| content | ResourceStr | 否 | 加载弹出框内容。 默认不设置或设置为undefined，加载弹出框内容不显示。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| theme12+ | Theme \| CustomTheme | 否 | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| themeColorMode12+ | ThemeColorMode | 否 | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |




##### CustomContentDialog12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

CustomContentDialog({controller: CustomDialogController, contentBuilder: () => void, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, contentAreaPadding?: Padding, buttons?: ButtonOptions[], theme?: Theme | CustomTheme, themeColorMode?: ThemeColorMode})

自定义内容区弹出框，同时支持定义操作区按钮样式。

**装饰器类型：**@CustomDialog

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| controller | CustomDialogController | 是 | - | 弹出框控制器。 说明： 未使用@Require装饰，构造时不强制校验参数。 |
| contentBuilder | () => void | 是 | @BuilderParam | 弹出框内容。 |
| primaryTitle | ResourceStr | 否 | - | 弹出框标题。 默认不设置或设置为undefined，弹出框标题不显示。 说明： 标题超过两行会显示“...”。 |
| secondaryTitle | ResourceStr | 否 | - | 弹出框辅助文本。 默认不设置或设置为undefined，弹出框辅助文本不显示。 说明： 辅助文本超过两行会显示“...”。 |
| localizedContentAreaPadding | LocalizedPadding | 否 | - | 弹出框内容区内边距。 |
| contentAreaPadding | Padding | 否 | - | 弹出框内容区内边距。设置了localizedContentAreaPadding属性时该属性不生效。 |
| buttons | ButtonOptions[] | 否 | - | 弹出框操作区按钮，最多支持4个按钮。 |
| theme | Theme \| CustomTheme | 否 | - | 主题信息，可以是CustomTheme或从onWillApplyTheme中获取的Theme实例。 |
| themeColorMode | ThemeColorMode | 否 | - | 自定义弹出框深浅色模式。 默认值：ThemeColorMode.SYSTEM |


> [!NOTE]
> 当弹框高度不足时，触发全局滚动的规格为contentBuilder被压缩，压缩至小于100vp时启动全局滚动。 CustomContentDialog内容区的滚动需由开发者自定义，内容区自定义滚动必须配合属性nestedScroll，nestedScroll({ scrollForward: NestedScrollMode.PARALLEL, scrollBackward: NestedScrollMode.PARALLEL })




##### PopoverDialog14+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PopoverDialog({visible: boolean, popover: PopoverOptions, targetBuilder: Callback&lt;void&gt;})

跟手弹出框，基于目标组件位置弹出，上文中的TipsDialog、SelectDialog、ConfirmDialog、AlertDialog、LoadingDialog、CustomContentDialog都可作为弹出框内容。

**装饰器类型：**@Component

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| visible | boolean | 是 | @Link | 跟手弹出框显示状态。value为true时，表示显示弹出框，value为false时，表示隐藏弹出框。 默认值为false，隐藏弹出框。 |
| popover | PopoverOptions | 是 | @Prop @Require | 配置跟手弹出框的参数。 |
| targetBuilder | Callback&lt;void&gt; | 是 | @Require @BuilderParam | 跟手弹出框基于的目标组件。 |




##### ButtonOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | ResourceStr | 否 | 否 | 按钮的内容。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| action | () => void | 否 | 是 | 按钮的点击事件。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| background | ResourceColor | 否 | 是 | 按钮的背景色。 默认值跟随buttonStyle。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fontColor | ResourceColor | 否 | 是 | 按钮的字体颜色。 默认值跟随buttonStyle。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| buttonStyle12+ | ButtonStyleMode | 否 | 是 | 按钮的样式。 默认值：2in1设备为ButtonStyleMode.NORMAL，其他设备为ButtonStyleMode.TEXTUAL。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| role12+ | ButtonRole | 否 | 是 | 按钮的角色。 默认值：ButtonRole.NORMAL 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| defaultFocus18+ | boolean | 否 | 是 | 按钮是否设置默认焦点。 true：按钮是默认焦点。 false：按钮不是默认焦点。 默认值：false 元服务API： 从API version 18开始，该接口支持在元服务中使用。 |
| textAlign24+ | TextAlign | 否 | 是 | 按钮文本的对齐方式。 默认值：TextAlign.Start 元服务API： 从API version 24开始，该接口支持在元服务中使用。 |


> [!NOTE]
> buttonStyle和role优先级高于fontColor和background。当buttonStyle和role设置的是默认值时，fontColor和background生效。 若同时给多个按钮设置defaultFocus，则默认焦点为设置defaultFocus按钮中显示顺序的第一个按钮。




##### PopoverOptions14+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

跟手弹出框参数，用于设置弹出框内容、位置属性等。

继承自[CustomPopupOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8类型说明)。

> [!NOTE]
> radius默认值为32vp。


**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。



##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



##### 示例1（上图下文弹出框）

上图下文弹出框，包含imageRes、content等内容。

```text
import { TipsDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerImage: CustomDialogController = new CustomDialogController({
    builder: TipsDialog({
      imageRes: $r('sys.media.ohos_ic_public_voice'),
      content: '想要卸载这个APP嘛?',
      primaryButton: {
        value: '取消',
        action: () => {
          console.info('Callback when the first button is clicked')
        },
      },
      secondaryButton: {
        value: '删除',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked')
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked')
      }
    }),
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("上图下文弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerImage.open()
            })
        }.margin({bottom: 300})
      }.align(Alignment.Bottom)
      .width('100%').height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-4.gif)




##### 示例2（纯列表弹出框）

纯列表弹出框，包含selectedIndex、radioContent等内容。

```text
import { SelectDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  // 设置默认选中radio的index
  radioIndex: number = 0;
  dialogControllerList: CustomDialogController = new CustomDialogController({
    builder: SelectDialog({
      title: '文本标题',
      selectedIndex: this.radioIndex,
      confirm: {
        value: '取消',
        action: () => {},
      },
      radioContent: [
        {
          title: '文本文本文本文本文本',
          action: () => {
            this.radioIndex = 0
          }
        },
        {
          title: '文本文本文本文本',
          action: () => {
            this.radioIndex = 1
          }
        },
        {
          title: '文本文本文本文本',
          action: () => {
            this.radioIndex = 2
          }
        },
      ]
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("纯列表弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerList.open()
            })
        }.margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-5.png)




##### 示例3（文本与勾选弹出框）

文本与勾选弹出框，包含content、checkTips等内容。

```text
import { ConfirmDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  isChecked: boolean = false;
  dialogControllerCheckBox: CustomDialogController = new CustomDialogController({
    builder: ConfirmDialog({
      title: '文本标题',
      content: '文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本',
      // 勾选框选中状态
      isChecked: this.isChecked,
      // 勾选框说明文本
      checkTips: '禁止后不再提示',
      primaryButton: {
        value: '禁止',
        action: () => {},
      },
      secondaryButton: {
        value: '允许',
        action: () => {
          this.isChecked = false
          console.info('Callback when the second button is clicked')
        }
      },
      onCheckedChange: () => {
        console.info('Callback when the checkbox is clicked')
      },
    }),
    autoCancel: true,
    alignment: DialogAlignment.Bottom
  })

  build() {
    Row() {
      Stack() {
        Column(){
          Button("文本+勾选弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerCheckBox.open()
            })
        }
        .margin({bottom: 300})
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-6.png)




##### 示例4（纯文本弹出框）

纯文本弹出框，包含primaryTitle、secondaryTitle、content等内容。

```text
import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerConfirm: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: '弹框一级标题',
      secondaryTitle: '弹框二级标题',
      content: '文本文本文本文本文本',
      primaryButton: {
        value: '取消',
        action: () => {
        },
      },
      secondaryButton: {
        value: '确认',
        role: ButtonRole.ERROR,
        action: () => {
          console.info('Callback when the second button is clicked')
        }
      },
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("纯文本弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerConfirm.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-7.png)




##### 示例5（进度加载类弹出框）

进度加载类弹出框，包含content等内容。

```text
import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogControllerProgress: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: '文本文本文本文本文本...',
    }),
  })

  build() {
    Row() {
      Stack() {
        Column() {
          Button("进度加载类弹出框")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogControllerProgress.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-8.png)




##### 示例6（自定义主题风格弹出框）

自定义主题风格弹出框，包含content、theme等内容。

```text
import { CustomColors, CustomTheme, LoadingDialog } from '@kit.ArkUI';

class CustomThemeImpl implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}

// 自定义内容文字及loading组件主题颜色
class CustomThemeColors implements CustomColors {
  fontPrimary = '#ffd0a300';
  iconSecondary = '#ffd000cd';
}

@Entry
@Component
struct Index {
  @State customTheme: CustomTheme = new CustomThemeImpl(new CustomThemeColors());
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'text',
      theme: this.customTheme,
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('dialog')
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](assets/弹出框%20Dialog/file-20260514164142653-9.png)




##### 示例7（自定义深浅色模式弹出框）

自定义深浅色模式弹出框，包含content、themeColorMode等内容。

```text
import { LoadingDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialog({
      content: 'Text',
      themeColorMode: ThemeColorMode.DARK, // 设置弹出框深浅色模式为深色模式
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('Dialog')
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open();
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-dHkEEAnTLa0B18TnJ2Cng/zh-cn_image_0000002611756145.png?HW-CC-KV=V1&HW-CC-Date=20260528T024204Z&HW-CC-Expire=86400&HW-CC-Sign=38046DE637BE6719944D02FD9AC856CD04DBC11567A57A58B7935FF684A238A9)




##### 示例8（自定义内容弹出框）

支持自定义内容弹出框，包含contentBuilder、buttons等内容。

```text
import { CustomContentDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: '标题',
      secondaryTitle: '辅助文本',
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: [
        {
          value: '按钮1',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked')
          }
        },
        {
          value: '按钮2',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          role: ButtonRole.ERROR
        }
      ],
    }),
  });

  build() {
    Column() {
      Button("支持自定义内容弹出框")
        .onClick(() => {
          this.dialogController.open()
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
  
  // 自定义弹出框的内容区
  @Builder
  buildContent(): void {
    Column() {
      Text('内容区')
    }
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/sNDnlva0QpOT86dFMW93PQ/zh-cn_image_0000002581436208.png?HW-CC-KV=V1&HW-CC-Date=20260528T024204Z&HW-CC-Expire=86400&HW-CC-Sign=AE2E7FED1136243B3E32BC3FFD4BDF2378470533AF6CD35027F4CEE3A952432B)




##### 示例9（跟手弹出框）

从API version 14开始，该示例展示了设置跟手弹出框（警告弹出框为例），包含visible、popover、targetBuilder等内容。

```text
import { AlertDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State popoverOptions: PopoverOptions = {
    builder: () => {
      this.dialogBuilder();
    },
    width: 320,
  }
  
  // 跟手弹出框内容
  @Builder dialogBuilder() {
    AlertDialog({
      content: '跟手弹出框',
      primaryButton: {
        value: '取消',
        action: () => {
          this.isShow = false;
        },
      },
      secondaryButton: {
        value: '确认',
        action: () => {
          this.isShow = false;
        },
      },
    });
  }
  
  // 跟手弹出框绑定的builder
  @Builder buttonBuilder() {
    Button('跟手弹出框目标组件')
    .onClick(() => {
      this.isShow = true;
    });
  }

  build() {
    Column() {
      PopoverDialog({
        visible: this.isShow,
        popover: this.popoverOptions,
        targetBuilder: () => {
          this.buttonBuilder();
        },
      })
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/t6z0Q40CT2GEqX0CAMZ9yQ/zh-cn_image_0000002611836039.png?HW-CC-KV=V1&HW-CC-Date=20260528T024204Z&HW-CC-Expire=86400&HW-CC-Sign=E147C481DE94434A1FA26FEF474DCC70E9C7803F088AE78EEF886D6F0A3F06F5)




##### 示例10（弹出框按钮设置默认获焦）

从API version 18开始，该示例展示了设置默认获焦按钮弹出框（以AlertDialog为例），包含defaultFocus等内容。

```text
import { AlertDialog } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: AlertDialog({
      primaryTitle: 'AlertDialog',
      secondaryTitle: '副标题',
      content: '第二个按钮设置为默认',
      primaryButton: {
        value: 'DEFAULT',
        action: () => {}
      },
      secondaryButton: {
        value: 'TRUE',
        defaultFocus: true, // 设置该按钮为默认获焦按钮。
        action: () => {}
      },
    })
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button("AlertDialog")
            .width(96)
            .height(40)
            .onClick(() => {
              this.dialogController.open()
            })
        }
        .margin({ bottom: 300 })
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%')
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/wrFh7PX_RNWOQiYDFx7btw/zh-cn_image_0000002581276294.png?HW-CC-KV=V1&HW-CC-Date=20260528T024204Z&HW-CC-Expire=86400&HW-CC-Sign=D2304A3A27A84B10D502D507AA2BE554F4283858BC3451EDEA8A45C561E21326)
