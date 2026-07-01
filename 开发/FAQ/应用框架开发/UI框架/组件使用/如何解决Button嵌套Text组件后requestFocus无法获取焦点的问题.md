# 如何解决Button嵌套Text组件后requestFocus无法获取焦点的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-927

#### 问题现象

在组件嵌套的使用场景下，例如Button组件中嵌套Text组件，此时使用requestFocus()方法发现无法使Button组件获取到焦点；但是如果只有一个Button组件，能够正常获取到焦点。在组件嵌套时，如何能正常获焦？
 
问题示例代码如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RequestFocusDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">buttonColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onDidBuild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2000</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Normal </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这是一个文本</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听第一个组件的获焦事件，获焦后改变颜色</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
该代码在onDidBuild执行2S后主动走焦到Button组件上，但Button组件背景颜色没有按预期变为指定颜色。
 
 

#### 背景知识

- 焦点：指向当前应用界面上唯一的可交互元素，对于使用键盘、遥控器等非指向性输入设备与应用程序进行交互时，基于焦点的导航和交互是重要的输入手段。
- 走焦：是指焦点在应用内的组件之间转移的行为。这一过程对用户是透明的，但开发者可以通过监听onFocus（焦点获取）和onBlur（焦点失去）事件来捕捉焦点转移的变化。
- 主动走焦：除了使用外接键盘的按键走焦（TAB键/Shift+TAB键/方向键）主动控制焦点，也可用[requestFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#requestfocus12)接口获取焦点、[clearFocus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller#clearfocus12)接口清除焦点、[focusOnTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusontouch9)接口点击申请焦点主动控制焦点转移。
- [focusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focusable)赋予组件可以获焦的能力，但前提是目标组件本身就拥有获焦的能力但默认情况下不可获焦。一些组件在设计上就无法获焦因此该属性对这些组件无效。

 
 

#### 问题定位

在ArkUI中，不是所有的组件都有默认获焦的能力，组件获焦能力可分为如下三类：
 
- 默认可获焦的组件，例如Button、TextInput等有交互行为的组件；
- 有获焦能力，但默认不可获焦的组件：典型的是Text、Image组件，此类组件默认情况下无法获焦，需要使用通用属性focusable(true)使能组件的获焦能力，或者为该组件配置onClick或单指单击的Tap手势事件，将该组件隐式成为可获焦组件；
- 无获焦能力的组件，通常是无任何交互行为的展示类组件，如Blank、Circle组件，此类组件无法通过focusable属性使其获焦。

 
关于组件获焦能力的说明可参考：[组件获焦能力说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#组件获焦能力说明)。以下是表中对Button和Text组件的说明：
  
| 基础组件 | 是否有获焦能力 | focusable默认值 |
| --- | --- | --- |
| Button | 是 | true |
| Text | 是 | false |
 
 
 

#### 分析结论

由上表可知：Button默认下就有获焦能力，而Text是有获焦能力，但默认不可获焦的组件。因此在Button组件嵌套了Text组件后，虽然Button组件本身默认可获焦，但由于子组件Text默认不可获焦，导致无法正常获焦。
 
 

#### 修改建议

- 方案一：将子组件Text使用通用属性focusable，设置为true使能默认获焦能力，见运行效果图“这是一个文本1”。
- 方案二：在子组件Text上增加点击事件，使其隐式成为可获焦组件，见运行效果图“这是一个文本2”。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RequestFocusDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">buttonColor1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">buttonColor2</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">onDidBuild</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">两秒后使</span><span style="color: rgb(128,128,128);">“</span><span style="color: rgb(128,128,128);">这是一个文本</span><span style="color: rgb(128,128,128);">1”</span><span style="color: rgb(128,128,128);">聚焦</span></em>
    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId1'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">2000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ROUNDED_RECTANGLE </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这是一个文本</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听第一个组件的获焦事件，获焦后改变颜色</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId1'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor1</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ROUNDED_RECTANGLE </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">这是一个文本</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">点击使</span><span style="color: rgb(128,128,128);">“</span><span style="color: rgb(128,128,128);">这是一个文本</span><span style="color: rgb(128,128,128);">2”</span><span style="color: rgb(128,128,128);">聚焦</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getFocusController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">requestFocus</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId2'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">focusable</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
      <em>// </em><em><span style="color: rgb(128,128,128);">监听第一个组件的获焦事件，获焦后改变颜色</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onFocus</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor2 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#0A59F7'</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'buttonId2'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">buttonColor2</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SpaceAround</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果图如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/EKtaDXJXSEiZWgSRQPecSA/zh-cn_image_0000002628560230.png?HW-CC-KV=V1&HW-CC-Date=20260701T041313Z&HW-CC-Expire=86400&HW-CC-Sign=5CE802FB0A3C944152C351CDE999D5C6864F4110BFAE8E1DD106451E49518A69)


 
 

#### 总结

对于组件嵌套的场景，需要注意父组件、子组件是否具有并且使能了获焦能力，以实现正常的焦点控制。
