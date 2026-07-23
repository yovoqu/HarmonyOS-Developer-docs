# 如何解决RichText设置backgroundColor无效的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1133

#### 问题现象

在深色模式下，RichText组件通过backgroundColor属性设置背景颜色不生效。
 
 

#### 背景知识

- RichText组件适用于加载与显示一段HTML字符串，且不需要对显示效果进行较多自定义的应用场景。RichText组件仅支持有限的通用[属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext)和事件。
- 当前系统存在深浅色两种显示模式，为了给用户更好的使用体验，应用应适配[深浅色模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation)。

 
 

#### 解决方案

RichText组件不支持设置backgroundColor属性，所以当系统切换到深色模式后未生效，如果有较多的自定义HTML显示效果的场景，推荐使用Web组件。
 
但是对于一些简单场景如通过加载与显示一段HTML字符串，可以通过设置支持的style标签来定义RichText组件内要显示的内容样式，如：
 
```text
import { ConfigurationConstant } from '@kit.AbilityKit';

@Entry
@Component
struct ToggleExample {
  @State isOn: boolean = false;
  <em>// 背景颜色，通过内容中添加style样式，内容添加背景颜色或者其他样式信息</em>
  richBgContent: string =
    '<style>*{ background-color: blue;width:100%;padding:0;font-size:50px}</style>';
  <em>// 文字内容</em>
  richContent: string =
    '<p style="background-color: blue"><span></span><span style="white-space: pre-wrap;">温馨提示：<br/>' +
      '这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字这是一段文字，仅供参考。</span></p>';

  build() {
    Column() {
      RichText(this.richBgContent + this.richContent)
        .margin({ top: 28 })
        .padding(0)
        .width('100%')
        .height(150);

      Row() {
        Toggle({ type: ToggleType.Switch, isOn: this.isOn })
          .onChange(() => {
            this.isOn = !this.isOn;
            <em>// 切换深浅色主题</em>
            let context = this.getUIContext().getHostContext()?.getApplicationContext();
            if (context) {
              context.setColorMode(this.isOn ? ConfigurationConstant.ColorMode.COLOR_MODE_DARK :
                ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
            }
          });
      };
    };
  }
}
```
 
浅色模式效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/dEwUsuBfT9C4-EdMT8UHmg/zh-cn_image_0000002628569428.png?HW-CC-KV=V1&HW-CC-Date=20260723T013010Z&HW-CC-Expire=86400&HW-CC-Sign=356322504A044D4D514C94AA94DD81D976685424F72AAF5F4D6121C0DD3546B5)

 
深色模式效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fT3Cc3T9RXul72bkn9doKQ/zh-cn_image_0000002628409528.png?HW-CC-KV=V1&HW-CC-Date=20260723T013010Z&HW-CC-Expire=86400&HW-CC-Sign=EE5FB3627D48A5D6ED17DB546B81CFA1EF72D3FC059EC3BF6FA2617A8284130A)
