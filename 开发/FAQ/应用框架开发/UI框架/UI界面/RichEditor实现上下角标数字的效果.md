# RichEditor实现上下角标数字的效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-750

#### 问题现象

如何在RichEditor组件中实现上下角标的输入？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/SMJAbSFxQ86Arkz78rHitg/zh-cn_image_0000002658794735.png?HW-CC-KV=V1&HW-CC-Date=20260701T041142Z&HW-CC-Expire=86400&HW-CC-Sign=EE399EA31B65D4C04F0693D1185E0AD6F204F051E70F238D4850F4C9E75DF5B4)

 
 

#### 背景知识

- [RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor)是支持图文混排和文本交互式编辑的组件，通常用于响应用户对图文混合内容的输入操作，例如可以输入图文的评论区。
- [RichEditorController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorcontroller)是RichEditor组件的控制器，该控制器的[addTextSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#addtextspan)方法可用于添加文本内容并设置文本样式属性。
- [fontFeature](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfeature12)属性可用于设置文字特性效果，其中sups表示上标、subs表示下标。
- [onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#onready)方法是富文本组件提供的一个回调函数，在组件初始化完成后会触发该回调。

 
 

#### 解决方案
1. 创建RichEditor组件与RichEditorController控制器，在该组件的onReady回调方法中，调用控制器的addTextSpan方法，在该方法的第一个参数中输入文本值，在第二个参数设置style中fontFeature属性为subs，用于实现数字的下角标效果。
2. 设置上角标同理，只需在第二个参数中设置fontFeature属性为sups即可。
 
完整示例参考如下：
 
```text
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Row() {
      Column() {
        RichEditor(this.options)
          .onReady(() => { <em>// 组件初始化完成后会触发onReady回调</em>
          <em>  // 在addTextSpan第一个参数中输入文本值，在第二个参数添加style，style中fontFeature属性为subs</em>
            this.controller.addTextSpan('下角标效果示例：二氧化碳，CO2\n',
              {
                style:
                {
                  fontSize: 20,
                  fontFeature: '\"subs\"'
                }
              });
            this.controller.addTextSpan('上角标效果示例：X的平方，X2\n',
              {
                style:
                {
                  fontSize: 20,
                  fontFeature: '\"sups\"'
                }
              });
          })
          .borderWidth(1)
          .padding(5)
          .width('100%')
      }
      .width('100%')
    }
  }
}
```
