# WithEnv：环境变量容器

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-env
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WithEnv组件用于为子组件树设置局部环境变量作用域。开发者可以通过该组件为后代组件提供自定义环境变量，或设置系统环境变量。

**起始版本：** 26.0.0

> [!NOTE]
> 此接口仅可在Stage模型下使用。 可通过 customEnv 设置自定义环境变量。 支持通过 env 设置的系统环境变量键，系统环境变量键存于 WritableEnvKey 。 WithEnv嵌套时，同名环境变量按最近作用域生效。



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持单个子组件。



#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

WithEnv()

设置局部环境变量作用域容器。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持以下WithEnv专有属性。



#### env

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

env&lt;T&gt;(key: WritableSystemEnvKey&lt;T&gt;, value: T)

设置作用域内的系统环境变量。当前正式支持的系统环境变量键为WritableEnvKey.FONT_SCALE、WritableEnvKey.DIRECTION。

> [!NOTE]
> WithEnv.env(WritableEnvKey.FONT_SCALE, value)用于为尾随闭包里的作用域内组件提供局部字体缩放比例，value为number类型，表示字体缩放倍数。设置的value小于0时按0处理。 WithEnv尾随闭包里的作用域内组件实际生效的字体缩放值同时受env属性通过键WritableEnvKey.FONT_SCALE设置的值与组件自身的字体缩放限制共同作用。该限制可通过组件的minFontScale和maxFontScale属性设置，也可通过应用配置中的 fontSizeMaxScale 等全局配置生效。最终生效值为WritableEnvKey.FONT_SCALE设置值在各限制范围内的取值。


**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | WritableSystemEnvKey&lt;T&gt; | 是 | 系统环境变量键。当前正式支持WritableEnvKey.FONT_SCALE和WritableEnvKey.DIRECTION。 |
| value | T | 是 | 系统环境变量值。value的类型T对应WritableSystemEnvKey&lt;T&gt;中的类型T。当key为WritableEnvKey.FONT_SCALE时，value类型为number。当key为WritableEnvKey.DIRECTION时，value类型为Direction。 |




#### customEnv

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

customEnv&lt;T&gt;(key: CustomEnvKey&lt;T&gt;, value: T)

设置作用域内可被后代自定义组件读取的自定义环境变量。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | CustomEnvKey&lt;T&gt; | 是 | 自定义环境变量的键。 |
| value | T | 是 | 自定义环境变量的值。value的类型T对应CustomEnvKey&lt;T&gt;的类型T。 |




#### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。



#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



#### 示例1（设置局部字体缩放）

该示例通过env(WritableEnvKey.FONT_SCALE, value)为作用域内组件设置局部字体缩放比例。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.FONT_SCALE。

```ArkTS
// xxx.ets
import { WithEnv } from '@kit.ArkUI';
@Entry
@Component
struct WithEnvExample1 {
  @State fontScale: number = 1.0;

  build() {
    Column({ space: 12 }) {
      Row({ space: 8 }) {
        Button('缩小 0.5x')
          .onClick(() => {
            this.fontScale = 0.5;
          })
        Button('正常 1.0x')
          .onClick(() => {
            this.fontScale = 1.0;
          })
        Button('放大 1.5x')
          .onClick(() => {
            this.fontScale = 1.5;
          })
      }

      WithEnv() {
        Column({ space: 8 }) {
          Text('当前字体缩放作用域内的文本')
            .fontSize(16)
          Text('该文本同样受 WithEnv 字体缩放影响')
            .fontSize(14)
            .fontColor('#99182431')
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .env(WritableEnvKey.FONT_SCALE, this.fontScale) // 设置局部字体缩放比例
    }
    .padding(12)
    .width('100%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QtxJeH_5RfW-ZbG2Kjf_VA/zh-cn_image_0000002685928649.png?HW-CC-KV=V1&HW-CC-Date=20260730T072223Z&HW-CC-Expire=86400&HW-CC-Sign=D67E060795E1F0B845D2D09DEFCB0A7AF0E1DDF423989E55E2FEC96932ADA65C)




#### 示例2（设置局部布局方向）

该示例通过env(WritableEnvKey.DIRECTION, value)为作用域内组件设置局部布局方向。

从API版本26.0.0开始，新增env属性和键值WritableEnvKey.DIRECTION。

```ArkTS
// xxx.ets
import { WithEnv } from '@kit.ArkUI';

@Entry
@Component
struct WithEnvExample2 {
  @State directionValue: Direction = Direction.Ltr;

  build() {
    Column({ space: 12 }) {
      Row({ space: 10 }) {
        Column().backgroundColor('#F0FAFF').width(60).height('100%')
        Column().backgroundColor('#2787D9').width(60).height('100%')
        Column().backgroundColor('#004AAF').width(60).height('100%')

      }.backgroundColor('#D5D5D5').width(200).height(50)

      WithEnv() {
        Row({ space: 10 }) {
          Column().backgroundColor('#F0FAFF').width(60).height('100%')
          Column().backgroundColor('#2787D9').width(60).height('100%')
          Column().backgroundColor('#004AAF').width(60).height('100%')

        }.backgroundColor('#D5D5D5').width(200).height(50)
      }
      .env(WritableEnvKey.DIRECTION, this.directionValue) // 设置局部布局方向

      Button('change direction').onClick(() => {
        if (this.directionValue === Direction.Ltr) {
          this.directionValue = Direction.Rtl;
        } else {
          this.directionValue = Direction.Ltr;
        }
      })
    }
    .width('80%')
    .height('30%')
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Kbgimd3-TeGgRViqoG2AwQ/zh-cn_image_0000002656008970.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072223Z&HW-CC-Expire=86400&HW-CC-Sign=0CE6F7AFCBA616E67B951460324C3008F111ABA94310A1DF7FF61FF4C793AF6A)
