# @ohos.arkui.theme(主题换肤)

更新时间：2026-04-29 07:35:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持自定义主题风格，实现App组件风格跟随Theme切换。

> [!NOTE]
> 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { Theme, ThemeControl, CustomColors, Colors, CustomTheme, CustomDarkColors } from '@kit.ArkUI';
```



#### Theme

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

当前生效的主题风格对象，可从[onWillApplyTheme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#onwillapplytheme12)中获取。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | Colors | 否 | 否 | 主题颜色资源。 |




#### Colors

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

主题颜色资源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

> [!NOTE]
> 颜色对应的组件可参考 文本色与图标色 。


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| brand | ResourceColor | 否 | 否 | 品牌色。 影响组件： TextInput、Search |
| warning | ResourceColor | 否 | 否 | 一级警示色。 影响组件： TipsDialog、AlertDialog、CustomContentDialog、 Badge、Button |
| alert | ResourceColor | 否 | 否 | 二级提示色。 影响组件： 暂无组件使用。 |
| confirm | ResourceColor | 否 | 否 | 确认色。 影响组件： 暂无组件使用。 |
| fontPrimary | ResourceColor | 否 | 否 | 一级文本字体颜色。 影响组件： EditableTitleBar、LoadingDialog、TipsDialog、 ConfirmDialog、AlertDialog、SelectDialog、 CustomContentDialog、Swiper、Text、 SubHeader、ProgressButton、AlphabetIndexer、 Popup、Select、Chip、 ToolBar、Menu、TextInput、 Search、Counter、TimePicker、DatePicker、 TextPicker、ComposeListItem、TreeView |
| fontSecondary | ResourceColor | 否 | 否 | 二级文本字体颜色。 影响组件： EditableTitleBar、AlertDialog、CustomContentDialog、 SubHeader、AlphabetIndexer、Popup、 TextInput、Search、ComposeListItem、 TreeView、TextClock。 |
| fontTertiary | ResourceColor | 否 | 否 | 三级文本字体颜色。 影响组件： ComposeListItem |
| fontFourth | ResourceColor | 否 | 否 | 四级文本字体颜色。 影响组件： 暂无组件使用。 |
| fontEmphasize | ResourceColor | 否 | 否 | 高亮字体颜色。 影响组件： TipsDialog、ConfirmDialog、AlertDialog、 SelectDialog、CustomContentDialog、SubHeader、 AlphabetIndexer、Popup、Button、 Select、ToolBar、Search、 TimePicker、DatePicker、TextPicker |
| fontOnPrimary | ResourceColor | 否 | 否 | 一级文本反转颜色，用于彩色背景。 影响组件： Badge、Button、Chip |
| fontOnSecondary | ResourceColor | 否 | 否 | 二级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| fontOnTertiary | ResourceColor | 否 | 否 | 三级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| fontOnFourth | ResourceColor | 否 | 否 | 四级文本反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| iconPrimary | ResourceColor | 否 | 否 | 一级图标颜色。 影响组件： EditableTitleBar、Swiper、ToolBar、 TreeView |
| iconSecondary | ResourceColor | 否 | 否 | 二级图标颜色。 影响组件： LoadingDialog、SubHeader、LoadingProgress、 Popup、Chip、Search、 TreeView |
| iconTertiary | ResourceColor | 否 | 否 | 三级图标颜色。 影响组件： SubHeader |
| iconFourth | ResourceColor | 否 | 否 | 四级图标颜色。 影响组件： Checkbox、CheckboxGroup、Radio |
| iconEmphasize | ResourceColor | 否 | 否 | 高亮图标颜色。 影响组件： ToolBar |
| iconSubEmphasize | ResourceColor | 否 | 否 | 高亮辅助图标颜色。 影响组件： 暂无组件使用。 |
| iconOnPrimary | ResourceColor | 否 | 否 | 一级图标反转颜色，用于彩色背景。 影响组件： Checkbox、CheckboxGroup、Radio |
| iconOnSecondary | ResourceColor | 否 | 否 | 二级图标反转颜色，用于彩色背景。 影响组件： Chip |
| iconOnTertiary | ResourceColor | 否 | 否 | 三级图标反转颜色，用于彩色背景。 影响组件： 暂无组件使用。 |
| iconOnFourth | ResourceColor | 否 | 否 | 四级图标反转颜色，用于彩色背景。 影响组件： ProgressButton |
| backgroundPrimary | ResourceColor | 否 | 否 | 一级背景颜色（实色，不透明）。 影响组件： TextInput、QRCode |
| backgroundSecondary | ResourceColor | 否 | 否 | 二级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundTertiary | ResourceColor | 否 | 否 | 三级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundFourth | ResourceColor | 否 | 否 | 四级背景颜色（实色，不透明）。 影响组件： 暂无组件使用。 |
| backgroundEmphasize | ResourceColor | 否 | 否 | 高亮背景颜色（实色，不透明）。 影响组件： Progress、Button、Slider |
| compForegroundPrimary | ResourceColor | 否 | 否 | 前背景。 影响组件： QRCode |
| compBackgroundPrimary | ResourceColor | 否 | 否 | 白色背景。 影响组件： 暂无组件使用。 |
| compBackgroundPrimaryTran | ResourceColor | 否 | 否 | 白色透明背景。 影响组件： 暂无组件使用。 |
| compBackgroundPrimaryContrary | ResourceColor | 否 | 否 | 常亮背景。 影响组件： Toggle、Slider |
| compBackgroundGray | ResourceColor | 否 | 否 | 灰色背景。 影响组件： 暂无组件使用。 |
| compBackgroundSecondary | ResourceColor | 否 | 否 | 二级背景。 影响组件： Swiper、Slider |
| compBackgroundTertiary | ResourceColor | 否 | 否 | 三级背景。 影响组件： EditableTitleBar、Progress、AlphabetIndexer、 Button、Select、Toggle、 Chip、TextInput、Search |
| compBackgroundEmphasize | ResourceColor | 否 | 否 | 高亮背景。 影响组件： Swiper、Toggle、Chip、 Checkbox、CheckboxGroup、Radio |
| compBackgroundNeutral | ResourceColor | 否 | 否 | 黑色中性高亮背景颜色。 影响组件： PatternLock |
| compEmphasizeSecondary | ResourceColor | 否 | 否 | 20%高亮背景颜色。 影响组件： Progress、ProgressButton、AlphabetIndexer、 Select、Toggle |
| compEmphasizeTertiary | ResourceColor | 否 | 否 | 10%高亮背景颜色。 影响组件： 暂无组件使用。 |
| compDivider | ResourceColor | 否 | 否 | 通用分割线颜色。 影响组件： SelectDialog、PatternLock、Divider |
| compCommonContrary | ResourceColor | 否 | 否 | 通用反转颜色。 影响组件： 暂无组件使用。 |
| compBackgroundFocus | ResourceColor | 否 | 否 | 获焦态背景颜色。 影响组件： 暂无组件使用。 |
| compFocusedPrimary | ResourceColor | 否 | 否 | 获焦态一级反转颜色。 影响组件： 暂无组件使用。 |
| compFocusedSecondary | ResourceColor | 否 | 否 | 获焦态二级反转颜色。 影响组件： 暂无组件使用。 |
| compFocusedTertiary | ResourceColor | 否 | 否 | 获焦态三级反转颜色。 影响组件： Scroll |
| interactiveHover | ResourceColor | 否 | 否 | 通用悬停交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactivePressed | ResourceColor | 否 | 否 | 通用按压交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactiveFocus | ResourceColor | 否 | 否 | 通用获焦交互式颜色。 影响组件： EditableTitleBar、Chip、TreeView |
| interactiveActive | ResourceColor | 否 | 否 | 通用激活交互式颜色。 影响组件： TreeView |
| interactiveSelect | ResourceColor | 否 | 否 | 通用选择交互式颜色。 影响组件： TreeView |
| interactiveClick | ResourceColor | 否 | 否 | 通用点击交互式颜色。 影响组件： 暂无组件使用。 |




#### CustomTheme

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

自定义主题风格对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | CustomColors | 否 | 是 | 自定义浅色主题颜色资源。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| darkColors20+ | CustomDarkColors | 否 | 是 | 自定义深色主题颜色资源。 说明：如果未设置darkColors，颜色值将与浅色模式下的colors配置相同，并且不会随着颜色模式的变化而变化，除非该颜色是通过dark目录下的资源进行设置的。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |




#### CustomColors

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type CustomColors = Partial&lt;Colors&gt;

自定义主题颜色资源类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial&lt;Colors&gt; | 自定义主题颜色资源类型。 |




#### CustomDarkColors20+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type CustomDarkColors = Partial&lt;Colors&gt;

自定义深色主题颜色资源类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| Partial&lt;Colors&gt; | 自定义深色主题颜色资源类型。 |




#### ThemeControl

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ThemeControl将自定义Theme应用于App组件内，实现App组件风格跟随Theme切换。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full



#### setDefaultTheme

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

setDefaultTheme(theme: [CustomTheme](#customtheme)): void

将用户自定义Theme设置应用级默认主题，以实现应用风格跟随Theme切换。若在页面中使用此接口设置应用级默认主题，需确保该接口在页面build前执行。若在UIAbility中使用此接口设置应用级默认主题，需确保该接口在onWindowStageCreate阶段里windowStage.[loadContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage#loadcontent9)接口调用完成的回调函数中执行。详细代码可参考[设置应用内组件自定义主题色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning#设置应用内组件自定义主题色)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | CustomTheme | 是 | 表示设置的自定义主题风格。 |


**示例**

```text
import { CustomTheme, CustomColors, ThemeControl } from '@kit.ArkUI';
// 自定义主题颜色
class BlueColors implements CustomColors {
  fontPrimary = "#FF707070";
  backgroundPrimary = "#FF2787D9";
  brand = "#FFEEAAFF"; // 品牌色
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}
// 创建实例
const BlueColorsTheme = new PageCustomTheme(new BlueColors());
// 在页面build之前执行ThemeControl.setDefaultTheme，设置App默认样式风格为BlueColorsTheme。
ThemeControl.setDefaultTheme(BlueColorsTheme);

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        // 文本颜色应用fontPrimary
        Text('这是一段文本')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin('5%')
        // 二维码背景色应用backgroundPrimary
        QRCode('Hello')
          .width(100)
          .height(100)
        // 输入框光标颜色应用brand
        TextInput({placeholder: 'input your word...'})
          .width('80%')
          .height(40)
          .margin(20)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/NgBmT124SkS9UeYrdOdqdg/zh-cn_image_0000002611755469.png?HW-CC-KV=V1&HW-CC-Date=20260528T025450Z&HW-CC-Expire=86400&HW-CC-Sign=8DFAED64B1EBDCC847A3AB2812B1248D230EE5179F646BCFE444A1A49D51C492)



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/JxqKQO0fSCWR3HvXV5a7hg/zh-cn_image_0000002581435532.png?HW-CC-KV=V1&HW-CC-Date=20260528T025450Z&HW-CC-Expire=86400&HW-CC-Sign=271B886C98B22115F64B8F0715B4348CBA3E5B2901595650401AB941EC56EE87)
