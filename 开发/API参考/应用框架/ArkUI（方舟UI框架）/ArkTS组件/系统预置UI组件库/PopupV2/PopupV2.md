# PopupV2

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popupv2
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PopupV2用于显示特定样式的气泡，适用于提示信息、操作确认或信息通知等需要用户关注或响应的场景。

该组件基于[状态管理（V2）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v2)实现，相较于[状态管理（V1）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制显示特定样式的气泡，实现更高效的用户界面刷新。

**起始版本：** 26.0.0


#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { PopupV2, PopupV2Button, PopupV2InitInfo } from '@kit.ArkUI';
```



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无



#### PopupV2

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PopupV2(options: PopupV2InitInfo): void

**起始版本：** 26.0.0

**装饰器类型：** @Builder

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | PopupV2InitInfo | 是 | 定义PopupV2组件的配置参数。 |




#### PopupV2InitInfo

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义PopupV2的具体样式参数。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | ResourceStr | 否 | 是 | 设置PopupV2图标。 说明： 默认值：''，不显示图标。 |
| title | ResourceStr | 否 | 是 | 设置PopupV2标题文本。 说明： 默认值：''，不显示标题文本。 |
| message | ResourceStr | 否 | 否 | 设置PopupV2内容文本。 说明： 默认值：''，不显示内容文本。 |
| titleModifier | TextModifier | 否 | 是 | 设置标题文本属性，如设置标题颜色、字体大小、字重等。 默认值：undefined，使用系统标题文本属性。 |
| iconModifier | ImageModifier | 否 | 是 | 设置图标属性，如图标颜色、大小、边框等。 默认值：undefined，使用系统图标属性。 |
| messageModifier | TextModifier | 否 | 是 | 设置内容文本属性，如设置内容文本颜色、字体大小、字重等。 默认值：undefined，使用系统内容文本属性。 |
| showClose | boolean \| Resource | 否 | 是 | 设置PopupV2关闭按钮。true：显示关闭按钮；false：不显示关闭按钮。Resource类型：显示对应的图标。 默认值：true |
| onClose | Callback&lt;void&gt; | 否 | 是 | 设置PopupV2关闭按钮回调函数。 默认不设置关闭按钮回调函数。 |
| buttons | [PopupV2Button?,PopupV2Button?] | 否 | 是 | 设置PopupV2操作按钮，按钮最多设置两个。默认不显示按钮。 默认值：[{ text: '' }, { text: '' }] |
| direction | Direction | 否 | 是 | 设置PopupV2的布局方向，用于控制文本排列与对齐方式，适用于国际化场景下的RTL（从右到左）布局。具体枚举值含义见Direction。 默认值：Direction.Auto |
| maxWidth | Dimension | 否 | 是 | 设置PopupV2的最大宽度，通过此接口PopupV2可以自定义宽度显示。 默认值：400vp 说明： 1. 在使用引用资源类型时，规定其参数类型要与属性方法本身类型一致。 2. maxWidth为Dimension类型，支持数字、百分比或带单位的字符串（如400、'50%'、'400vp'）。在使用引用资源类型时，资源类型支持float和整型，例如\$r('app.float.maxWidth')、\$r('app.integer.maxWidth')。 3. 当类型为Resource时，如果未设置单位，默认单位为px。 |




#### PopupV2Button

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

PopupV2Button定义按钮的相关属性和事件。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | ResourceStr | 否 | 否 | 设置按钮内容。 |
| action | Callback&lt;void&gt; | 否 | 是 | 设置按钮点击回调。 默认不执行任何操作。 |
| buttonTextModifier | TextModifier | 否 | 是 | 设置按钮文本属性，如设置文本颜色、字体大小等。默认值：undefined，值为undefined时，默认使用系统按钮文本属性。模型约束：此接口仅可在Stage模型下使用。 |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（设置气泡样式）

该示例通过配置[titleModifier](#popupv2initinfo)、[messageModifier](#popupv2initinfo)、[PopupV2Button](#popupv2button)实现气泡样式。

从API版本26.0.0开始，新增titleModifier、messageModifier、PopupV2Button。

```ArkTS
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Row() {
      // PopupV2自定义高级组件
      PopupV2 ({
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width(300)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/W37V2xPyQn6cQbQJml_zVQ/zh-cn_image_0000002685928619.png?HW-CC-KV=V1&HW-CC-Date=20260730T072220Z&HW-CC-Expire=86400&HW-CC-Sign=20A23E234FB8F1E9440D9B2E615B82E41A7BC8B7D2401993DBB4C23955ABA03C)




#### 示例2（设置布局方向）

该示例通过配置[direction](#popupv2initinfo)实现镜像布局效果，适用于国际化场景下的RTL（从右到左）布局需求。

从API版本26.0.0开始，新增direction参数。

```ArkTS
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Column() {
      // PopupV2自定义高级组件
      PopupV2 ({
        direction: Direction.Rtl,
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/I74rHrB9Qx6yvrd8JLFQQg/zh-cn_image_0000002656008940.png?HW-CC-KV=V1&HW-CC-Date=20260730T072220Z&HW-CC-Expire=86400&HW-CC-Sign=4CC235463365E981D24B7F36BD2D2DA5C0BA00952DA179133104B4292B0367AB)




#### 示例3（设置自定义宽度）

该示例通过配置[maxWidth](#popupv2initinfo)实现自定义宽度效果，适用于内容较长的消息通知等需要调整显示宽度的场景。

从API版本26.0.0开始，新增maxWidth参数。

```ArkTS
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Row() {
      // PopupV2自定义高级组件
      PopupV2 ({
        maxWidth: '50%',
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message, This is the message, This is the message, This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width(400)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/av7YoFAVREqB2gucM5PXgw/zh-cn_image_0000002655849020.png?HW-CC-KV=V1&HW-CC-Date=20260730T072220Z&HW-CC-Expire=86400&HW-CC-Sign=E4F84651E5E95986230C1E92711943B54FC953272DF03BCE441BF8BF557CC4E5)
