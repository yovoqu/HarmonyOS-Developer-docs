# SymbolSpan

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

作为Text组件的子组件，用于显示图标小符号的组件。
 
> [!NOTE]
> 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 该组件支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的全部属性。 SymbolSpan拖拽不会置灰显示。

  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持子组件。
 
  

##### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

SymbolSpan(value: Resource)
 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Resource | 是 | SymbolSpan组件的资源名，如 \$r('sys.symbol.ohos_wifi')。 |
 
 
> [!NOTE]
> \$r('sys.symbol.ohos_wifi')中引用的资源为系统预置，SymbolSpan仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，支持以下属性：
 
  

##### fontColor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fontColor(value: Array&lt;ResourceColor&gt;)
 
设置SymbolSpan组件颜色。
 
> [!NOTE]
> 从API version 12开始，该接口支持在 attributeModifier 中调用。

 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;ResourceColor&gt; | 是 | SymbolSpan组件颜色。 默认值：不同渲染策略下默认值不同。 |
 
 
  

##### fontSize

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fontSize(value: number | string | Resource)
 
设置SymbolSpan组件大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。
 
> [!NOTE]
> 从API version 12开始，该接口支持在 attributeModifier 中调用。

 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string \| Resource | 是 | SymbolSpan组件大小。 默认值：16fp 单位：fp |
 
 
  

##### fontWeight

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

fontWeight(value: number | FontWeight | string)
 
设置SymbolSpan组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。
 
sys.symbol.ohos_lungs图标不支持设置fontWeight。
 
> [!NOTE]
> 从API version 12开始，该接口支持在 attributeModifier 中调用。

 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| FontWeight \| string | 是 | SymbolSpan组件粗细。 默认值：FontWeight.Normal |
 
 
  

##### renderingStrategy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

renderingStrategy(value: SymbolRenderingStrategy)
 
设置SymbolSpan渲染策略。
 
> [!NOTE]
> 从API version 12开始，该接口支持在 attributeModifier 中调用。

 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SymbolRenderingStrategy | 是 | SymbolSpan渲染策略。 默认值：SymbolRenderingStrategy.SINGLE |
 
 
不同渲染策略效果可参考以下示意图。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/F9NJLGxfQRqL2nf3_UTRZg/zh-cn_image_0000002581276032.png?HW-CC-KV=V1&HW-CC-Date=20260528T024227Z&HW-CC-Expire=86400&HW-CC-Sign=5D19974CE19504927F17F8F6F4BEBD0EE8D7C04EACC410DA51F1FE90088162F2)

 
  

##### effectStrategy

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

effectStrategy(value: SymbolEffectStrategy)
 
设置SymbolSpan动效策略。
 
> [!NOTE]
> 从API version 12开始，该接口支持在 attributeModifier 中调用。

 
**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SymbolEffectStrategy | 是 | SymbolSpan动效策略。 默认值：SymbolEffectStrategy.NONE |
 
 
  

##### attributeModifier12+

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

attributeModifier(modifier: AttributeModifier&lt;SymbolSpanAttribute&gt;)
 
设置组件的动态属性。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | AttributeModifier&lt;SymbolSpanAttribute&gt; | 是 | 动态设置组件的属性。 |
 
 
  

##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 示例1（设置渲染和动效策略）

从API version 11开始，该示例通过[renderingStrategy](#renderingstrategy)、[effectStrategy](#effectstrategy)属性展示了不同的渲染和动效策略。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Column() {
          Text("Light")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Lighter)
              .fontSize(96)
          }
        }

        Column() {
          Text("Normal")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Normal)
              .fontSize(96)
          }
        }

        Column() {
          Text("Bold")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Bold)
              .fontSize(96)
          }
        }
      }

      Row() {
        Column() {
          Text("单色")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.SINGLE)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }

        Column() {
          Text("多色")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }

        Column() {
          Text("分层")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }
      }

      Row() {
        Column() {
          Text("无动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.NONE)
          }
        }

        Column() {
          Text("整体缩放动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.SCALE)
          }
        }

        Column() {
          Text("层级动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
          }
        }
      }
    }
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Njdt9fxBTBCyEuUhvjARhw/zh-cn_image_0000002611755887.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024227Z&HW-CC-Expire=86400&HW-CC-Sign=0D2053C7AD36FE3C1BB0E7E5960DCFDA0D78762C92A8935B5ABEA766D851E8F2)

 
  

##### 示例2（设置动态属性）

从API version 12开始，该示例通过[attributeModifier](#attributemodifier12)属性创建指定样式图标。
 
```text
import { SymbolSpanModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State modifier: SymbolSpanModifier =
    new SymbolSpanModifier($r("sys.symbol.ohos_wifi")).fontColor([Color.Blue]).fontSize(100);

  build() {
    Row() {
      Column() {
        Text() {
          SymbolSpan(undefined).attributeModifier(this.modifier)
        }

        Button('更改SymbolSpanModifier')
          .onClick(() => {
            this.modifier = new SymbolSpanModifier($r("sys.symbol.ohos_trash")).fontColor([Color.Red]).fontSize(100);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/IINveTJFQNO1ac7gYa_YUA/zh-cn_image_0000002581435950.gif?HW-CC-KV=V1&HW-CC-Date=20260528T024227Z&HW-CC-Expire=86400&HW-CC-Sign=B9829D60D8BDC84D0CE32C3AF19A90CC5C17B0642FC0B5CD159B8AB0C8DE3391)
