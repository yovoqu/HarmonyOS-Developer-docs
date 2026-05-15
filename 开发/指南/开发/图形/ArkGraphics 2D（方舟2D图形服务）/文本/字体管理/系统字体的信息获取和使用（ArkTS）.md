# 系统字体的信息获取和使用（ArkTS）

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-font-arkts

## 场景介绍

系统字体是指操作系统预设的字体，用于在没有指定自定义字体时显示文本，确保文本的可读性和一致性。 **使用系统字体**的情况通常是在应用未注册自定义字体，或在没有显式指定文本样式时，系统会使用默认的系统字体。另外，系统字体有多种，开发者可以先获取系统字体的配置信息，并根据信息中的字体家族名来进行系统字体的切换和使用。 当前ArkTS侧暂不支持禁用系统字体，Native侧支持禁用系统字体。

## 接口说明

以下是系统字体相关的常用接口和结构体，ArkTS侧对外接口由ArkUI提供，详细接口说明请见[@ohos.font](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font)。
| 接口名 | 描述 |
| --- | --- |
| getUIFontConfig() : UIFontConfig | 获取系统字体配置。 |


## 获取系统字体信息

导入依赖的相关模块。
```text
import { font } from '@kit.ArkUI'
```

获取系统字体信息。
```text
let fontConfig = font.getUIFontConfig();
```

在获取系统字体信息之后通过日志打印字体信息。
```text
console.info('sysFontMfg::font-dir -----------' + String(fontConfig.fontDir.length));
for (let i = 0; i           以下打印的示例为应用设备系统对应的部分系统字体配置信息情况，不同设备系统配置信息可能不同，此处仅示意。     ![](assets/系统字体的信息获取和使用（ArkTS）/file-20260514131642958-0.png)

## 使用或切换系统字体

     系统字体可以有多种，可以先获取系统字体配置信息，再根据其中的字体家族名（即TextStyle中的fontFamilies）来进行系统字体的切换和使用。     如果不指定使用任何字体时，会使用系统默认字体“HarmonyOS Sans”显示文本。                  导入依赖的相关模块。
```text
import { text } from '@kit.ArkGraphics2D';
```

             创建textStyle1，指定fontFamilies为“HarmonyOS Sans SC”，默认中文字体为“HarmonyOS Sans SC”。
```text
let textStyle1: text.TextStyle = {
color: { alpha: 255, red: 255, green: 0, blue: 0 },
fontSize: 100,
fontFamilies: ['HarmonyOS Sans SC']
};
```

             创建textStyle2，指定fontFamilies为“HarmonyOS Sans TC”（该两种字体易于观察同一文字字型差异）。
```text
let textStyle2: text.TextStyle = {
color: { alpha: 255, red: 255, green: 0, blue: 0 },
fontSize: 100,
fontFamilies: ['HarmonyOS Sans TC']
};
```

             创建段落生成器。
```text
// 创建一个段落样式对象，以设置排版风格
let myParagraphStyle: text.ParagraphStyle = {
textStyle: textStyle1,
align: 3,
wordBreak: text.WordBreak.NORMAL
};
// 获取全局字体集实例
let fontCollection = text.FontCollection.getGlobalInstance(); //获取Arkui全局FC
// 创建一个段落生成器
let ParagraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
```

             先后将textStyle1和textStyle2添加到段落样式中并添加文字。
```text
let str:string = '模块描述\n';
// 添加第一种文本样式和对应文本内容
ParagraphGraphBuilder.pushStyle(textStyle1);
ParagraphGraphBuilder.addText(str);
// 添加第二种文本样式和对应文本内容
ParagraphGraphBuilder.pushStyle(textStyle2);
ParagraphGraphBuilder.addText(str);
```

             生成段落，用于后续绘制使用。
```text
let paragraph = ParagraphGraphBuilder.build();
```

          效果展示如下：     ![](assets/系统字体的信息获取和使用（ArkTS）/file-20260514131642958-1.png)
