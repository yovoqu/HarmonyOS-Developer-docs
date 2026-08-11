# Text组件嵌套多个Span组件的布局效果示例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-647

#### 问题现象

开发者使用Text组件中嵌套多个Span组件时，想要实现以下两个效果：
 
- 效果一：需要给Span组件设置最大的字符数，超出部分用省略号显示。
- 效果二：其中一个Span组件排不下一行时可以自动换行不会被截断。

 
 

#### 背景知识

- [if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)：条件渲染可根据应用的不同状态，使用if、else和else if渲染对应状态下的UI内容。
- [display.getDefaultDisplaySync()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9)：获取当前默认的[Display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)对象。
- [measureText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils#measuretext12)：计算指定文本的宽度。

 
 

#### 解决方案

- **场景一**：单独实现以上两个效果。
针对效果一：可以使用if()条件渲染方法实现。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CombinedSpanExampleOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">testInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">旨在指导开发者和设计师打造统一</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">testInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">testInfo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">slice</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">' ... '</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">testInfo</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">从理念到实现</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">好的用户体验</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">合理设计理念</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">完美视觉风格</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">交互事件归一</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'85%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">220 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/AzzYjzhPRp-ZtPbw8zbrRg/zh-cn_image_0000002628394514.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=ACA7EBAC2ADF2150349E81EAB890EF3E3152F007CCDD9D3766032DD5697B9242)

- 针对效果二：先获取当前屏幕宽度，再计算指定文本的宽度，将两者对比判断是否需要换行，如果需要换行，则插入一个换行符来实现。
```text
import <span style="color: rgb(255,255,255);">display </span>from <span style="color: rgb(132,63,161);">'@ohos.display'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">MeasureUtils </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CombinedSpanExampleTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">msg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">为你提供全端侧的针对性设计建议</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">和谐的数字世界</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">msgAdd</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">共同构建一个和谐的数字世界</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MeasureUtils </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMeasureUtils</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">textWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDefaultDisplaySync</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">vp2px</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">60</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">msg</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ff2f69ff'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeLine</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">msg</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span>\n<span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
          <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Start</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffe9e9e9'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">38 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">changeLine</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">msg1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(255,255,255);">j</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
    while <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">j </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">msg1</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">j</span><span style="color: rgb(181,106,1);">++;</span>
      if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTextWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">msg1</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">j</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">textWidth</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">j </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`msgAdd </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">msgAdd</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTextWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">msg1</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTextWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">textWidth</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getTextWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    const <span style="color: rgb(255,255,255);">width </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">textContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">fontSize</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`getTextWidth: content: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">content</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, width: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 当changeLine方法传入的文本（msgAdd）和msg加起来超过一行时，会进行换行。

  换行效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/oqfIi_2zTxqqi98QxzwQkg/zh-cn_image_0000002658793781.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=47874E16E9F40E250DF7D80DFC1AF1DA82549D083F0E2C3DD98DD77FD75CD800)


  当changeLine方法传入的文本（message）和msg加起来不超过一行时，不会进行换行。

  不换行效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/OEz5CWX7STm2tfHJmdUBnA/zh-cn_image_0000002628554404.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=75C79DE9DFA79A55623CF3A03E970544434092A9157BF358881C91403FABF0FC)


 - **场景二**：将以上两个效果结合在一起实现。使用substring()方法截取指定长度字符，通过三元运算符来动态截断文本换行并添加省略号实现以上两个效果。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CombinedSpanExampleThree </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">longText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">第一行需要截断的文本内容结束第二行开始需要自动换行的长文本第三行要显示全部的文本部分且没有省略号不会被截断可以换行</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTruncatedText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Blue</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTruncatedText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">14</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textBackgroundStyle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Yellow </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTruncatedText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Infinity</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">29</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Green</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'80%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textOverflow</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">overflow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">TextOverflow</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">None </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#FFEAEAEA'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  private <span style="color: rgb(0,0,255);">getTruncatedText</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">maxLength</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">startIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">{</span>
    const <span style="color: rgb(255,255,255);">targetText </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">longText</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">startIndex</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    return <span style="color: rgb(255,255,255);">targetText</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">maxLength </span>?
      <span style="color: rgb(255,255,255);">targetText</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">substring</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">maxLength</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'...' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'</span>\n<span style="color: rgb(132,63,161);">' </span><span style="color: rgb(181,106,1);">:</span>
      <span style="color: rgb(255,255,255);">targetText</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/7x1WMC49Tw6tc-_SPDmt8Q/zh-cn_image_0000002658913729.png?HW-CC-KV=V1&HW-CC-Date=20260811T005755Z&HW-CC-Expire=86400&HW-CC-Sign=67568B4DDA21E7905680A2DC983787E3060B6FB2BC10780F42A76D5465311AB1)


 
 

#### 常见FAQ

Q：Text组件如何实现以字母为单位进行截断效果。
 
A：通过[wordBreak](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#wordbreak11)属性设置断行规则WordBreak.BREAK_ALL即可实现字母为单位进行截断效果。可以参考[示例4（设置文本断行及折行）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#示例4设置文本断行及折行)。
 
Q：Span组件如何设置背景色。
 
A：可以添加[textBackgroundStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span#textbackgroundstyle11)属性来给Span组件设置背景色。
