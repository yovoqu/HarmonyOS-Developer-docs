# 如何根据API版本动态增加Image组件的属性

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1172

#### 问题现象

如何根据不同的API版本动态设置Image组件的属性？如：orientation属性在API 14及以上版本上生效，如何动态添加此属性？
 
 

#### 背景知识

- [deviceInfo (设备信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info)：获取终端设备信息，其中sdkApiVersion表示系统软件API版本。
- [attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)：动态属性设置，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。

 
 

#### 解决方案

可以通过获取[deviceInfo.sdkApiVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info#常量)判断当前系统的API版本再使用[动态属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)设置需要的属性，如：
 
为Image组件设置attributeModifier动态属性：
 
```text
import { deviceInfo } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  @State modifierImg: ImageModifier = new ImageModifier();


  aboutToAppear(): void {
  <em>  // 设置动态属性判断的API版本</em>
    this.modifierImg.sdkApiVersionInfo = deviceInfo.sdkApiVersion;
  }


  build() {
    Flex({justifyContent: FlexAlign.Center}) {
    <em>  // 加载的图片请替换为实际项目所需图片资源</em>
      Image($r('app.media.img'))
        .width(100)
        .height(100)
        .draggable(true)
        .attributeModifier(this.modifierImg)
    }
  }
}
```
 
通过判断API版本动态设置orientation属性：
 
```text
export class ImageModifier implements AttributeModifier<ImageAttribute> {
  <em>// 可以实现一个Modifier，定义私有的成员变量，外部可动态修改</em>
  sdkApiVersionInfo: number = 12;
  applyNormalAttribute(instance: ImageAttribute): void {
    if (deviceInfo.sdkApiVersion >= 14) {<em> // 支持业务逻辑实现</em>
    <em>  // 属性变化触发apply函数时，变化前已设置并且变化后未设置的属性会恢复为默认值</em>
      instance.orientation(ImageRotateOrientation.RIGHT);
    }
  }
}
```
 
示例代码运行效果如下：
 
系统API版本小于API 14：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/E3_a5plyS_CmlVYoInbEIg/zh-cn_image_0000002628569782.png?HW-CC-KV=V1&HW-CC-Date=20260730T072343Z&HW-CC-Expire=86400&HW-CC-Sign=A592EB0C2A1097C39F807F2767996A71AA050C9D4190CD87A4334B0CDEDF926C)

 
系统API版本大于API 14：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9UnMBnl2SYyIVU1wgt_lqA/zh-cn_image_0000002628409878.png?HW-CC-KV=V1&HW-CC-Date=20260730T072343Z&HW-CC-Expire=86400&HW-CC-Sign=6887E3F430FB6DA87418B97033E6B8A3BBE587449B448E659679032252464554)
