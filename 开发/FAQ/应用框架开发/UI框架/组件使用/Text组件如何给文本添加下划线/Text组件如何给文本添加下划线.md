# Text组件如何给文本添加下划线

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-513

#### 问题现象

Text组件本身支持decoration属性，设置文本装饰线样式及其颜色。下划线是用于标注重要文字，突出显示重点内容的重要工具，需要更多的灵活配置和更丰富的显示效果。
 
 

#### 背景知识

- Text组件的[decoration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#decoration)属性只能修改线条样式和颜色，无法修改高度和位置。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)是在组件显示的尺寸、位置等发生变化时触发的事件。
- [shadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadow)：为组件添加阴影效果。
- [border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)：设置组件边框样式。通过链式调用.border()方法，分别配置边框宽度、颜色、样式。
- [Web组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web)：Web组件提供了网页显示能力，根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。

 
 

#### 解决方案

- **方案一**：将Text文字和底部下划线使用Column容器封装成一个组件，在需要的地方应用。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World!'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">textLength</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Length </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">isKey</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isKey </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,170);">'#0A59F7' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#cd202021'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textLength </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义选中文本底部导航条</span><span style="color: rgb(128,128,128);">--</span><span style="color: rgb(128,128,128);">单直线</span></em>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isKey</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textLength</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>

       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义选中文本底部导航条</span><span style="color: rgb(128,128,128);">--</span><span style="color: rgb(128,128,128);">线性渐变</span></em>
        if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isKey</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textLength</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradient</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GradientDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Right</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[[</span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.9</span><span style="color: rgb(0,0,255);">]]</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/bVbNRzBYSYWFRY-pHZ0xPg/zh-cn_image_0000002658907835.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=283A2233C0D3996A3A283AC044C6E03385B6B1A8FE30E188827C21600056B0A1)

- **方案二**：通过Text组件的decoration参数直接设置基础线条样式。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Scene2 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">messageBorder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'overlay</span><span style="color: rgb(255,0,170);">中</span><span style="color: rgb(255,0,170);">border</span><span style="color: rgb(255,0,170);">绘制下划线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">messageDecoration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'overlay</span><span style="color: rgb(255,0,170);">中</span><span style="color: rgb(255,0,170);">decoration</span><span style="color: rgb(255,0,170);">绘制下划线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">messageTwoLine</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">绘制</span><span style="color: rgb(255,0,170);">2</span><span style="color: rgb(255,0,170);">条装饰线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">上划线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Overline </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">中划线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">LineThrough </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">下划线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">装饰线颜色跟随</span><span style="color: rgb(255,0,170);">fontColor'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">透明装饰线</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'#00FFFFFF' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

  <em>    <span style="color: rgb(128,128,128);">// overlay</span><span style="color: rgb(128,128,128);">中</span><span style="color: rgb(128,128,128);">decoration</span><span style="color: rgb(128,128,128);">绘制下划线，注意</span><span style="color: rgb(128,128,128);">y</span><span style="color: rgb(128,128,128);">的位置有下划线避让</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageDecoration</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">overlay</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OverlayNodeDecoration</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>

    <em>  <span style="color: rgb(128,128,128);">// overlay</span><span style="color: rgb(128,128,128);">中</span><span style="color: rgb(128,128,128);">border</span><span style="color: rgb(128,128,128);">绘制下划线，注意</span><span style="color: rgb(128,128,128);">y</span><span style="color: rgb(128,128,128);">的位置没有下划线避让</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageBorder</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">overlay</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OverlayNodeBorder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageTwoLine</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">overlay</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OverlayNodeTwoLine</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>

     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">字体放大后，下划线避让非常明显</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">下划线避让</span><span style="color: rgb(255,0,170);"> gjyqp'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">25</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

     <em> <span style="color: rgb(128,128,128);">// border</span><span style="color: rgb(128,128,128);">绘制的下划线，位置更靠下</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'border</span><span style="color: rgb(255,0,170);">绘制下划线</span><span style="color: rgb(255,0,170);"> gjyqp'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">25</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">OverlayNodeDecoration</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageDecoration</span><span style="color: rgb(0,0,255);">)</span>
    <em>  <span style="color: rgb(128,128,128);">// decoration</span><span style="color: rgb(128,128,128);">绘制下划线，下划线避让，会导致</span><span style="color: rgb(128,128,128);">y</span><span style="color: rgb(128,128,128);">的位置出现一段空白</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">decoration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Underline</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextDecorationStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SOLID</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">配置浮层不阻塞交互</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">OverlayNodeBorder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageBorder</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">配置浮层不阻塞交互</span></em>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">OverlayNodeTwoLine</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">messageTwoLine</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">配置浮层不阻塞交互</span></em>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/eF07obbQRISKoJHpdJNOKw/zh-cn_image_0000002658787897.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=9DD4DE317EA71F2DC2277240AEFE0EE42CACE7CD29367B96B25FC0216AF15B40)

- **方案三**：通过border属性给Text组件添加下边框来实现文字下划线的效果。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Scene3 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">测试文字</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BorderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Solid </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">线条样式（实线）</span></em>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案四**：给组件添加阴影效果，通过shadow()方法设置参数,设置垂直方向偏移量（使阴影位于组件下方），最后限制容器高度，强制触发布局约束，实现文字下划线的效果。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Scene4 </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">测试文字</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">15</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">shadow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Green</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">offsetY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(181,106,1);">: </span>true
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- **方案五**：通过Web组件加载本地HTML文件实现特定样式效果。

  在rawfile文件夹新建Index.html。
```text
<em><!DOCTYPE html></em>
<html>
<body>
<p><span class='test-underline'>我是通过Web组件添加的</span></p>
</body>
<style>
    .test-underline{
     font-size:50px;
     text-decoration: underline;
     text-decoration-color:black;
     text-decoration-thickness: 0.1em;
   }
</style>
</html>
```


  Index.ets。
```text
import <span style="color: rgb(0,0,255);">web_webview </span>from <span style="color: rgb(255,0,170);">'@ohos.web.webview'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebComponent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">web_webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">web_webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">$rawfile</span><span style="color: rgb(128,128,128);">加载本地资源文件。</span></em>
      <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Index.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/YLnaeX6lTi6jF7cBUGv0tw/zh-cn_image_0000002628388624.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=AD478A7B1CD9CED4301395B77B79845435688A95AFDFAE1C79A3FC27EBC74E91)
