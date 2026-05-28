# GridContainer

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcontainer
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

纵向排布栅格布局容器，仅在栅格布局场景中使用。
 
> [!NOTE]
> 从API version 9开始，该组件不再维护，推荐使用新组件 GridCol 、 GridRow 。 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

##### 子组件

可以包含子组件。
 
  

##### 接口

  

##### GridContainer(deprecated)

GridContainer(value?: GridContainerOptions)
 
纵向排布栅格布局容器。
 
> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 GridCol 或 GridRow 替代。

 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | GridContainerOptions | 否 | GridContainer参数。 |
 
 
  

##### GridContainerOptions(deprecated)对象说明

> [!TIP]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 GridColOptions 或 GridRowOptions 替代。

 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columns | number \| 'auto' | 否 | 是 | 当前布局总列数。 默认值：'auto' |
| sizeType | SizeType | 否 | 是 | 选用设备宽度类型。 默认值：SizeType.Auto |
| gutter | number \| string | 否 | 是 | 栅格布局列间距，不支持百分比。 |
| margin | number \| string | 否 | 是 | 栅格布局两侧间距，不支持百分比。 |
 
 
  

##### SizeType(deprecated)枚举说明

> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 GridColColumnOption 或 GridRowColumnOption 替代。

 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
  
| 名称 | 说明 |
| --- | --- |
| XS | 最小宽度类型设备。 |
| SM | 小宽度类型设备。 |
| MD | 中等宽度类型设备。 |
| LG | 大宽度类型设备。 |
| Auto | 根据设备类型进行选择。 |
 
 
  

##### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)和Column组件的[属性方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#属性)。
 
  

##### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。
 
  

##### 示例

```ArkTS
// xxx.ets
@Entry
@Component
struct GridContainerExample {
  @State sizeType: SizeType = SizeType.XS

  build() {
    Column({ space: 5 }) {
      GridContainer({ columns: 12, sizeType: this.sizeType, gutter: 10, margin: 20 }) {
        Row() {
          Text('1')
            .useSizeType({
              xs: { span: 6, offset: 0 },
              sm: { span: 2, offset: 0 },
              md: { span: 2, offset: 0 },
              lg: { span: 2, offset: 0 }
            })
            .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
          Text('2')
            .useSizeType({
              xs: { span: 2, offset: 6 },
              sm: { span: 6, offset: 2 },
              md: { span: 2, offset: 2 },
              lg: { span: 2, offset: 2 }
            })
            .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
          Text('3')
            .useSizeType({
              xs: { span: 2, offset: 8 },
              sm: { span: 2, offset: 8 },
              md: { span: 6, offset: 4 },
              lg: { span: 2, offset: 4 }
            })
            .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
          Text('4')
            .useSizeType({
              xs: { span: 2, offset: 10 },
              sm: { span: 2, offset: 10 },
              md: { span: 2, offset: 10 },
              lg: { span: 6, offset: 6 }
            })
            .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
        }
      }.width('90%')

      Text('Click Simulate to change the device width').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row() {
        Button('XS')
          .onClick(() => {
            this.sizeType = SizeType.XS
          }).backgroundColor(0x317aff)
        Button('SM')
          .onClick(() => {
            this.sizeType = SizeType.SM
          }).backgroundColor(0x317aff)
        Button('MD')
          .onClick(() => {
            this.sizeType = SizeType.MD
          }).backgroundColor(0x317aff)
        Button('LG')
          .onClick(() => {
            this.sizeType = SizeType.LG
          }).backgroundColor(0x317aff)
      }
    }.width('100%').margin({ top: 5 })
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Jf5V2unBS3aGpn_5ooHg4Q/zh-cn_image_0000002581436304.gif?HW-CC-KV=V1&HW-CC-Date=20260528T013929Z&HW-CC-Expire=86400&HW-CC-Sign=4A5D1D509FF188B4D0B5C1BEC3DE22B82353B8D6F824920624F0322BDFB66A19)
