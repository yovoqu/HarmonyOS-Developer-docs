# Hyperlink

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

超链接组件，支持文本和图片两种展示形式，在组件宽高范围内点击可实现跳转到指定网页。适用于应用内打开外部网页链接的场景，该组件仅支持与系统浏览器配合使用。

> [!NOTE]
> 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 该组件仅支持与系统浏览器配合使用。



#### 需要权限

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

跳转到目标网页需要使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。



#### 子组件

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

可以包含[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)子组件。



#### 接口

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string \| Resource | 是 | Hyperlink组件跳转的网页地址。 |
| content | string \| Resource | 否 | Hyperlink组件中超链接显示文本。 默认值：''。若不传该参数且组件内无子组件时，默认显示address参数值。 说明： 组件内有子组件时，不显示超链接文本。 |




#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：



#### color

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Color \| number \| string \| Resource | 是 | 超链接文本的颜色。 phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。 |




#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该示例展示了超链接图片和文本跳转的效果。

```text
@Entry
@Component
struct HyperlinkExample {
  build() {
    Column() {
      Column() {
        Hyperlink('https://example.com/') {
          // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.bg'))
            .width(200)
            .height(100)
        }
      }

      Column() {
        Hyperlink('https://example.com/', 'Go to the developer website') {
        }
        .color(Color.Blue)
      }
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/n6yqlyA4S62fqAIK9_Ipvg/zh-cn_image_0000002686088147.png?HW-CC-KV=V1&HW-CC-Date=20260730T071506Z&HW-CC-Expire=86400&HW-CC-Sign=844D07D3402FAE838AEB5C817030121E74DB5FB99FC1B82524DBF51022C2DCED)
