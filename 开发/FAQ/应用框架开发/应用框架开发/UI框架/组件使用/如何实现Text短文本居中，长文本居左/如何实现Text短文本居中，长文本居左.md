# 如何实现Text短文本居中，长文本居左

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1606

#### 问题现象

如何实现Text组件短文本时居中，长文本时居左的效果？
 
 

#### 背景知识

- [margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)能够设置组件的外边距属性，可以与[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)文本组件配合使用。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)是在组件区域变化时触发的回调，仅会在布局变化所导致的组件大小、位置发生变化时响应，适合动态调整变量。

 
 

#### 解决方案

可以使用[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)属性实现，通过计算Text组件的长度，判断其是否超出展示区域，如果超出，就通过设置margin属性实现居左效果，如果不超出，则不设置margin，保持居中。
 
- Index：在build方法中，创建一个可滚动的Scroll组件，在Scroll组件内部，创建一个Column组件，包含一个AppBar组件。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AppBar </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'../components/AppBar'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">testBuilder</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">      }</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Blue</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">      }</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Green</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">AppBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">actions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">testBuilder</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Spring</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alwaysEnabled</span><span style="color: rgb(181,106,1);">: </span>false <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Top</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- AppBar：使用Stack和RelativeContainer组件构建布局。Text文本组件使用自定义的AppBarTitleModifier类进行属性修饰，并且使用onAreaChange事件监听器，根据标题的宽度和容器的宽度比较，动态调整isneed状态变量，以决定是否需要通过调整margin来调整Text布局。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">AppBarTitleModifier </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'./AppBarTitleModifier'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@ComponentV2</span>
export struct <span style="color: rgb(0,0,255);">AppBar </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Param </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ResourceStr </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@BuilderParam </span><span style="color: rgb(0,0,255);">actions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CustomBuilder</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Param </span><span style="color: rgb(0,0,255);">barForegroundColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ResourceColor </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">null </span><span style="color: rgb(181,106,1);">= </span>null<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">leadingWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">actionsWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">isneed</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private readonly <span style="color: rgb(0,0,255);">titleId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'AppBar_Title_Component'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">UIContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MeasureUtils </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContext</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMeasureUtils</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">attributeModifier</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">AppBarTitleModifier</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barForegroundColor</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">titleId</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isneed </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">leadingWidth </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isneed </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">actionsWidth </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignRules</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">middle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">center</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">anchor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'__container__'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">align</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          let <span style="color: rgb(0,0,255);">w </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">s </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2vp</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">uiContextMeasure</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">textContent</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">s </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">w</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isneed </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`oldValue</span><span style="color: rgb(255,0,170);">：</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'100%' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 定义AppBarTitleModifier类实现AttributeModifier接口，用于修饰Text组件的属性。
```text
export class <span style="color: rgb(0,0,255);">AppBarTitleModifier </span>implements <span style="color: rgb(0,0,255);">AttributeModifier</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">TextAttribute</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">字体颜色</span></em>
  private <span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">ResourceColor</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">ResourceColor</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">applyNormalAttribute</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">instance</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextAttribute</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">instance</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textOverflow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">overflow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextOverflow</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Ellipsis </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FontWeight</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bold</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
短文本效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/JyXUXofFRFWD6CnsK0FMqg/zh-cn_image_0000002628773272.png?HW-CC-KV=V1&HW-CC-Date=20260811T005807Z&HW-CC-Expire=86400&HW-CC-Sign=7305F35ACDABF2AD88496FD963371244C08CCD5E476527913BAC6A69F6F4D227)

 
长文本效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/CK3Q-VCmQhiCWGh2U8liNQ/zh-cn_image_0000002628613374.png?HW-CC-KV=V1&HW-CC-Date=20260811T005807Z&HW-CC-Expire=86400&HW-CC-Sign=6375A2F6C87ADEC32B3A2B371276E0E7D9575A22BC11D1757ECD5323B03C40E3)
