# CustomDialog如何添加平移动画，实现从底部右侧平移进入/滑出

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-844

#### 问题现象

CustomDialog如何添加平移动画，从底部右侧平移进入和离开时平移从底部滑出？
 
 

#### 背景知识

- [自定义弹窗（CustomDialog）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
- [出现/消失转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-enter-exit-transition)：[transition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component#transitioneffect10对象说明)的组合使用，定义出各式效果。
- [animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)：显式动画是一个用于平滑过渡动画的方法，通常用于在UI元素中实现平滑的移动、缩放或其他变化效果。它允许你指定一个目标值，并以指定的时间和曲线进行动画过渡。

 
 

#### 解决方案

- **方案一**：通过combine属性对TransitionEffect进行链式组合，以形成包含多种转场效果的TransitionEffect，另外使用translate属性设置组件转场时的平移效果，其中设置的x值为横向的平移距离。

  完整示例参考如下：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">curves </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@CustomDialog</span>
struct <span style="color: rgb(0,0,255);">CustomDialogExample </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">showFlag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Visibility </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Visible</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">effect</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TransitionEffect </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(255,255,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OPACITY</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">添加平移转场效果，这里的动画参数使用指定的</span><span style="color: rgb(128,128,128);">springMotion()</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">combine</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">translate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">150 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">关闭弹窗</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">400</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">showFlag</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">effect</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">showFlag </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Hidden</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">close</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">400</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CustomDialogUser </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CustomDialogExample</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">customStyle</span><span style="color: rgb(181,106,1);">: </span>true
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'click me'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">open</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

- **方案二**：定义状态变量translateX用于设置组件在x轴的平移距离；定义状态变量transparency用于设置组件的不透明度。打开和关闭弹窗的过程中，使用显式动画动态控制translateX和transparency，实现平移进入/滑出动画。

  完整示例参考如下：
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">curves </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@CustomDialog</span>
struct <span style="color: rgb(0,0,255);">CustomDialogExampleTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">showFlag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Visibility </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Visible</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">translateX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置组件在</span><span style="color: rgb(128,128,128);">x</span><span style="color: rgb(128,128,128);">轴的平移距离</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">transparency</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置组件的不透明度</span></em>
  <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">400</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">关闭弹窗</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">400</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">showFlag</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">opacity</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">transparency</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">translate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">translateX </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">translateX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">transparency </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">cancel</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">      }</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">transparency </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">translateX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

    <span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">close</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CustomDialogUserTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CustomDialogController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CustomDialogController</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">builder</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CustomDialogExampleTwo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">alignment</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">DialogAlignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Bottom</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">autoCancel</span><span style="color: rgb(181,106,1);">: </span>false<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">customStyle</span><span style="color: rgb(181,106,1);">: </span>true
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'click me'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">dialogController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">open</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
