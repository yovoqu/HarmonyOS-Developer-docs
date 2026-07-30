# WithTheme

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色。当全局主题无法满足局部区域独立风格需求时，可使用该组件在不影响其他区域的前提下实现局部换肤或独立主题风格的定制。

> [!NOTE]
> 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 本模块接口仅可在Stage模型下使用。 WithTheme支持的系统组件如下： TextInput 、 Search 、 Button 、 Badge 、 Swiper 、 Text 、 Select 、 Menu 、 TimePicker 、 DatePicker 、 TextPicker 、 Checkbox 、 CheckboxGroup 、 Radio 、 Slider 、 Progress 、 QRCode 、 Toggle 、 TextClock 、 PatternLock 、 Divider 。从API版本26.0.0开始，新增 CalendarPicker 、 UIPickerComponent 、 TextArea 、 属性字符串 、 Gauge 、 DataPanel 、 RichEditor 、 MenuItem 、 MenuItemGroup 、 Image 、 ImageAnimator 、 Counter 、 bindSheet 、 LoadingProgress 。 WithTheme相关使用指导请参考 设置应用内主题换肤 。



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持单个子组件。



#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WithTheme(options: WithThemeOptions)

设置应用局部页面自定义主题风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | WithThemeOptions | 是 | 用于配置WithTheme作用域内组件的主题配色和深浅色模式，支持范围见上方说明中的组件列表。 |




#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。



#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。



#### WithThemeOptions

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

用于设置WithTheme作用域内组件主题配色及深浅色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| theme | CustomTheme | 否 | 是 | 用于设置WithTheme作用域内组件的自定义主题配色。 默认值：undefined，默认配色跟随系统token默认样式。 |
| colorMode | ThemeColorMode | 否 | 是 | 用于指定WithTheme作用域内组件配色的深浅色模式。取值原则：ThemeColorMode.SYSTEM跟随系统深浅色设置，ThemeColorMode.DARK强制使用深色模式，ThemeColorMode.LIGHT强制使用浅色模式。设置深浅色模式时需要添加dark.json资源文件才能生效。 默认值：ThemeColorMode.SYSTEM |




#### CustomTheme

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

type CustomTheme = import('../api/@ohos.arkui.theme').CustomTheme

用于自定义WithTheme作用域内组件的配色方案，具体配色项通过CustomColors接口配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.theme').CustomTheme | 自定义WithTheme作用域内组件默认主题配色。 |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

设置局部深浅色模式时，需要添加dark.json资源文件，深浅色模式才会生效。


![](assets/WithTheme/file-20260514164145232-1.png)


dark.json数据示例：

```json
{
    "color": [
      {
        "name": "start_window_background",
        "value": "#000000"
      }
    ]
  }
```



#### 示例1（指定局部深浅色模式）

```text
// 指定局部深浅色模式
@Entry
@Component
struct Index {
  build() {
    Column() {
    // 系统默认
      Column() {
        Text('无WithTheme')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('33%')
      .backgroundColor($r('app.color.start_window_background'))
      // 设置组件为深色模式
      WithTheme({ colorMode: ThemeColorMode.DARK }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('DARK')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }
      // 设置组件为浅色模式
      WithTheme({ colorMode: ThemeColorMode.LIGHT }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('LIGHT')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }
    }
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START])
  }
}
```


![](assets/WithTheme/file-20260514164145232-2.gif)




#### 示例2（自定义WithTheme作用域内组件默认配色）

```text
// 自定义WithTheme作用域内组件缺省配色
import { CustomTheme, CustomColors } from '@kit.ArkUI';

class GreenColors implements CustomColors {
  fontPrimary = '#ff049404';
  fontEmphasize = '#FF00541F';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#1111FF11';
  backgroundEmphasize = '#FF00541F';
  compEmphasizeSecondary = '#3322FF22';
}

class RedColors implements CustomColors {
  fontPrimary = '#fff32b3c';
  fontEmphasize = '#FFD53032';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#44FF2222';
  backgroundEmphasize = '#FFD00000';
  compEmphasizeSecondary = '#33FF1111';
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors;

  constructor(colors: CustomColors) {
    this.colors = colors;
  }
}

@Entry
@Component
struct IndexPage {
  static readonly themeCount = 3;
  themeNames: string[] = ['System', 'Custom (green)', 'Custom (red)'];
  themeArray: (CustomTheme | undefined)[] = [
    undefined, // System
    new PageCustomTheme(new GreenColors()),
    new PageCustomTheme(new RedColors())
  ];
  @State themeIndex: number = 0;

  build() {
    Column() {
      Column({ space: '8vp' }) {
        Text('未使用WithTheme')
        // 点击按钮切换局部换肤
        Button(`切换theme配色：${this.themeNames[this.themeIndex]}`)
          .onClick(() => {
            this.themeIndex = (this.themeIndex + 1) % IndexPage.themeCount;
          })

        // 系统默认按钮配色
        Button('Button.style(NORMAL) with System Theme')
          .buttonStyle(ButtonStyleMode.NORMAL)
        Button('Button.style(EMP..ED) with System Theme')
          .buttonStyle(ButtonStyleMode.EMPHASIZED)
        Button('Button.style(TEXTUAL) with System Theme')
          .buttonStyle(ButtonStyleMode.TEXTUAL)
      }
      .margin({
        top: '50vp'
      })

      WithTheme({ theme: this.themeArray[this.themeIndex] }) {
        // WithTheme作用域
        Column({ space: '8vp' }) {
          Text('使用WithTheme')
          Button('Button.style(NORMAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.NORMAL)
          Button('Button.style(EMP..ED) with Custom Theme')
            .buttonStyle(ButtonStyleMode.EMPHASIZED)
          Button('Button.style(TEXTUAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.TEXTUAL)
        }
        .width('100%')
      }
    }
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/mCrIxIUfRiKG4HKlfDvqaQ/zh-cn_image_0000002655848964.gif?HW-CC-KV=V1&HW-CC-Date=20260730T071516Z&HW-CC-Expire=86400&HW-CC-Sign=05B39FCEE20D16968EDC30AD38C4A2B442E713F39B2FF038CF1E1C0B6496CC9E)
