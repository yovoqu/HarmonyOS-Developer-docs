# 动态SymbolGlyphModifier属性设置

更新时间：2026-06-03 01:38:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-symbolglyphmodifier
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

SymbolGlyphModifier用于动态设置SymbolGlyph组件的属性和样式，支持使用if/else语句进行设置。[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)是一个用于展示图标符号的组件。
 
> [!NOTE]
> 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

  

#### SymbolGlyphModifier

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义SymbolGlyphModifier。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
  

#### constructor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

constructor(src?: Resource)
 
SymbolGlyphModifier的构造函数。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Resource | 否 | 资源信息。 |
 
 
  

#### applyNormalAttribute

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

applyNormalAttribute?(instance: SymbolGlyphAttribute): void
 
组件普通状态时的样式。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.ArkUI.ArkUI.Full
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | SymbolGlyphAttribute | 是 | 动态设置SymbolGlyph组件的属性。 |
 
 
  

#### 示例

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

该示例通过[SymbolGlyphModifier](#symbolglyphmodifier)和TextInput组件的[cancelButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。
 
```ArkTS
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // 从API version 18开始支持symbol类型
        })
    }.margin(10)
  }
}
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/IibAudzzTFqYJIYq_lZr8w/zh-cn_image_0000002587270052.png?HW-CC-KV=V1&HW-CC-Date=20260604T012955Z&HW-CC-Expire=86400&HW-CC-Sign=3D6E4DFAD606905B917B8A788EF0D4C94A958A2F11811F374A7EFFF4B8CAFC69)
