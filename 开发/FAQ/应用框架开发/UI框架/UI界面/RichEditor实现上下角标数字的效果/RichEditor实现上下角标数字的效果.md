# RichEditor实现上下角标数字的效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-750

#### 问题现象

如何在RichEditor组件中实现上下角标的输入？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/SMJAbSFxQ86Arkz78rHitg/zh-cn_image_0000002658794735.png?HW-CC-KV=V1&HW-CC-Date=20260723T013043Z&HW-CC-Expire=86400&HW-CC-Sign=D50BDEA828F66A0532A7AAE9AA6E2A05B53BF5660E0ACBF2BCF5BF391D3EE794)

 
 

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
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RichEditorExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件初始化完成后会触发</span><span style="color: rgb(128,128,128);">onReady</span><span style="color: rgb(128,128,128);">回调</span></em>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在</span><span style="color: rgb(128,128,128);">addTextSpan</span><span style="color: rgb(128,128,128);">第一个参数中输入文本值，在第二个参数添加</span><span style="color: rgb(128,128,128);">style</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">style</span><span style="color: rgb(128,128,128);">中</span><span style="color: rgb(128,128,128);">fontFeature</span><span style="color: rgb(128,128,128);">属性为</span><span style="color: rgb(128,128,128);">subs</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTextSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">下角标效果示例：二氧化碳，</span><span style="color: rgb(132,63,161);">CO2</span>\n<span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">:</span>
                <span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,255,255);">fontFeature</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span>\"<span style="color: rgb(132,63,161);">subs</span>\"<span style="color: rgb(132,63,161);">'</span>
                <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">              }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTextSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">上角标效果示例：</span><span style="color: rgb(132,63,161);">X</span><span style="color: rgb(132,63,161);">的平方，</span><span style="color: rgb(132,63,161);">X2</span>\n<span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">:</span>
                <span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,255,255);">fontFeature</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span>\"<span style="color: rgb(132,63,161);">sups</span>\"<span style="color: rgb(132,63,161);">'</span>
                <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">              }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
