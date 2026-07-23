# RichEditor实现同时设置删除线和下划线

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-999

#### 问题现象

使用RichEditorController控制器初始化的RichEditor富文本组件，如何同时设置删除线和下划线。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/HHcYvJMSRzqKNduPfSHjGw/zh-cn_image_0000002628404768.png?HW-CC-KV=V1&HW-CC-Date=20260723T012642Z&HW-CC-Expire=86400&HW-CC-Sign=5DA6257603B1F6493AC316F90448B0499D2517594F2FFE5AA73451FBDC88D568)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)支持图文混排和文本交互式编辑的组件，[RichEditorController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorcontroller)是RichEditor组件的控制器，[RichEditorStyledStringController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorstyledstringcontroller12)是使用属性字符串构建的RichEditor组件的控制器，均继承自[RichEditorBaseController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#richeditorbasecontroller12)，两种控制器都可以实现同时设置删除线与下划线。
 
 

#### 解决方案

RichEditorStyledStringController实现方案可参考官网[设置装饰线](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor#设置装饰线)来实现。如果项目中是用RichEditorController来初始化RichEditor，想要实现同时设置两种装饰线，可使用[fromStyledString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#fromstyledstring12)方法将属性字符串转换为span信息，通过addTextSpan方法添加到RichEditor组件。示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">LengthMetrics </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RichEditorExample </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">richEditorController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mutString</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MutableStyledString </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MutableStyledString</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">设置富文本多装饰线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span>
    <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">StyledStringKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">FONT</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledValue</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">TextStyle</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">LengthMetrics</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">vp</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">25</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">StyledStringKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DECORATION</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledValue</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">DecorationStyle</span><span style="color: rgb(0,0,255);">(</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开启多装饰线</span>
          <span style="color: rgb(0,0,255);">enableMultiType</span><span style="color: rgb(181,106,1);">: </span>true
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">StyledStringKey</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">DECORATION</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">styledValue</span><span style="color: rgb(181,106,1);">: </span>new <span style="color: rgb(0,0,255);">DecorationStyle</span><span style="color: rgb(0,0,255);">(</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">LineThrough</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开启多装饰线</span>
          <span style="color: rgb(0,0,255);">enableMultiType</span><span style="color: rgb(181,106,1);">: </span>true
        <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">isTextSpanResult</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RichEditorImageSpanResult </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">RichEditorTextSpanResult</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(255,0,170);">{</span>
    return typeof <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item </span>as <span style="color: rgb(0,0,255);">RichEditorImageSpanResult</span><span style="color: rgb(0,0,255);">)[</span><span style="color: rgb(255,0,170);">'imageStyle'</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,0,170);">'undefined'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">richEditorController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"</span><span style="color: rgb(255,0,170);">调用</span><span style="color: rgb(255,0,170);">fromStyledString"</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        try <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">将属性字符串转换成</span><span style="color: rgb(128,128,128);">span</span><span style="color: rgb(128,128,128);">信息</span>
          let <span style="color: rgb(0,0,255);">spans </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">richEditorController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fromStyledString</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mutString</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">for</span><span style="color: rgb(128,128,128);">循环拿出属性字符串的装饰信息，添加到</span><span style="color: rgb(128,128,128);">richEditorController</span>
          <span style="color: rgb(0,0,255);">spans</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RichEditorTextSpanResult </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">RichEditorImageSpanResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isTextSpanResult</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(255,0,170);">{</span>
              let <span style="color: rgb(0,0,255);">richSpan </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">item </span>as <span style="color: rgb(0,0,255);">RichEditorTextSpanResult</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">richEditorController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTextSpan</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">richSpan</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">:</span>
                <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">richSpan</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textStyle</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">richSpan</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textStyle</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">richSpan</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span>
                <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">              }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'fromStyledString error'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
