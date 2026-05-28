# Divider

更新时间：2026-04-02 08:41:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供分割线组件，分割不同内容块/内容元素。
 
> [!NOTE]
> 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。 如果出现分割线粗细不一或者消失的问题，请参考 组件级像素取整常见问题 。

  

##### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

无
 
  

##### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Divider()
 
创建分割线组件。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

##### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：
 
  

##### vertical

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

vertical(value: boolean)
 
设置分割线的方向，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 使用水平分割线还是垂直分割线。 false：水平分割线；true：垂直分割线。 默认值：false 非法值：按默认值处理。 |
 
 
  

##### color

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

color(value: ResourceColor)
 
设置分割线的颜色，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 分割线颜色。 默认值：'#33182431' 非法值：按默认值处理。 支持通过WithTheme设置通用分割线颜色。 |
 
 
  

##### strokeWidth

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

strokeWidth(value: number | string)
 
设置分割线的宽度，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。
 
> [!NOTE]
> 分割线的宽度不支持百分比设置。 使用水平分割线时，strokeWidth控制高度，优先级低于通用属性 height ；使用垂直分割线时，strokeWidth控制宽度，优先级低于通用属性 width 。 超过通用属性设置大小时，按照通用属性进行裁切。 如果设备硬件存在1像素取整后分割线不显示问题，建议使用2像素。

 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string | 是 | 分割线宽度。 默认值：1px 非法值：按默认值处理。 单位：vp |
 
 
  

##### lineCap

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

lineCap(value: LineCapStyle)
 
设置分割线的端点样式，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。
 
**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。
 
**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LineCapStyle | 是 | 分割线的端点样式。 默认值：LineCapStyle.Butt 非法值：按默认值处理。 |
 
 
  

##### 事件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。
 
  

##### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 示例1（定义Divider方向、颜色及宽度）

该示例定义了Divider的样式，如方向、颜色及宽度。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct DividerExample {
  build() {
    Column() {
      // 使用横向分割线场景
      Text('Horizontal divider').fontSize(9).fontColor(0xCCCCCC)
      List() {
        ForEach([1, 2, 3], (item: number) => {
          ListItem() {
            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)
          }.width(244).height(48)
        }, (item: number) => item.toString())
      }.padding({ left: 24, bottom: 8 })

      Divider().strokeWidth(8).color('#F1F3F5')
      List() {
        ForEach([4, 5], (item: number) => {
          ListItem() {
            Text('list' + item).width('100%').fontSize(14).fontColor('#182431').textAlign(TextAlign.Start)
          }.width(244).height(48)
        }, (item: number) => item.toString())
      }.padding({ left: 24, top: 8 })

      // 使用纵向分割线场景
      Text('Vertical divider').fontSize(9).fontColor(0xCCCCCC)
      Column() {
        Column() {
          Row().width(288).height(64).backgroundColor('#30C9F0').opacity(0.3)
          Row() {
            Button('Button')
              .width(136)
              .height(22)
              .fontSize(16)
              .fontColor('#007DFF')
              .fontWeight(500)
              .backgroundColor(Color.Transparent)
            Divider()
              .vertical(true)
              .height(22)
              .color('#182431')
              .opacity(0.6)
              .margin({ left: 8, right: 8 })
            Button('Button')
              .width(136)
              .height(22)
              .fontSize(16)
              .fontColor('#007DFF')
              .fontWeight(500)
              .backgroundColor(Color.Transparent)
          }.margin({ top: 17 })
        }
        .width(336)
        .height(152)
        .backgroundColor('#FFFFFF')
        .borderRadius(24)
        .padding(24)
      }
      .width('100%')
      .height(168)
      .backgroundColor('#F1F3F5')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 8 })
    }.width('100%').padding({ top: 24 })
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/eyB0Y9MES-CcC3IjlMhB-Q/zh-cn_image_0000002581436058.png?HW-CC-KV=V1&HW-CC-Date=20260528T024230Z&HW-CC-Expire=86400&HW-CC-Sign=5320B05D4AE55912BFB5AE07C34B079AA16D1218E1D808D01A50E09FA46B48F4)

 
  

##### 示例2（定义Divider的lineCap样式）

该示例定义了Divider的lineCap样式。
 
```ArkTS
// xxx.ets
@Entry
@Component
struct DividerExample {
  build() {
    Column({space:30}) {
      Text("LineCap:Butt")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Butt)

      Text("LineCap:Round")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Round)

      Text("LineCap:Square")
      Divider()
        .strokeWidth(20)
        .width("90%")
        .color('#F1F3F5')
        .lineCap(LineCapStyle.Square)

    }.width('100%').padding({ top: 24 })
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/lh0rD0PgTh-ASUDKv_SlLg/zh-cn_image_0000002611835889.png?HW-CC-KV=V1&HW-CC-Date=20260528T024230Z&HW-CC-Expire=86400&HW-CC-Sign=1187043E1FFC5B044B1D0A6F4DC05D88D7E238D3970B176A11B87EEA6E911340)
