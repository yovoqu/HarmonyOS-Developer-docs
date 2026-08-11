# 手势拖拽时和Swiper组件滑动发生冲突如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-810

#### 问题现象

当Swiper组件与子组件发生手势冲突，或者Swiper组件的滑动与嵌套了Swiper的外部组件的gesture手势冲突时，如何解决？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VloEHRzcShiQJ2spexrtGg/zh-cn_image_0000002628557800.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=F0D43D01B36DAE3DF31AC0C313F1DA2BAC47782A58F5CFD4AF40C1FC6D80ADC6)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件是滑块视图容器，提供子组件滑动轮播显示的能力。
- [TapGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture)手势支持单击、双击和多次点击事件的识别。

 
 

#### 解决方案

Swiper嵌套的页面包含[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)时，使Canvas不响应左右滑动事件，不会触发Swiper切换显示。可以通过以下步骤实现：
 1. 通过[priorityGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings#prioritygesture)给画布绑定优先识别手势，使得画布组件Canvas优先于其他组件响应滑动事件。
2. 通过[触摸测试控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)来处理滑动冲突，确保在滑动Swiper时，Canvas组件不会被滑动。
3. 在主组件Index中，创建Swiper组件，同时在Swiper中调用自定义组件CanvasExample，使得画布在Swiper的页面中可见。
 
```text
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CanvasExampleOne </span><span style="color: rgb(181,106,1);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用来配置</span><span style="color: rgb(128,128,128);">CanvasRenderingContext2D</span><span style="color: rgb(128,128,128);">对象的参数，包括是否开启抗锯齿，</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">表明开启抗锯齿。</span></em>
  private <span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">用来创建</span><span style="color: rgb(128,128,128);">CanvasRenderingContext2D</span><span style="color: rgb(128,128,128);">对象，通过在</span><span style="color: rgb(128,128,128);">canvas</span><span style="color: rgb(128,128,128);">中调用</span><span style="color: rgb(128,128,128);">CanvasRenderingContext2D</span><span style="color: rgb(128,128,128);">对象来绘制。</span></em>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Canvas'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">在</span><span style="color: rgb(128,128,128);">canvas</span><span style="color: rgb(128,128,128);">中调用</span><span style="color: rgb(128,128,128);">CanvasRenderingContext2D</span><span style="color: rgb(128,128,128);">对象。</span></em>
      <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffffffff'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
     <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可以在这里绘制内容。</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeRect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">150</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">priorityGesture</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">GestureGroup</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">GestureMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Exclusive</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">SwipeGesture</span><span style="color: rgb(255,0,170);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAction</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Canvas</span><span style="color: rgb(132,63,161);">响应，</span><span style="color: rgb(132,63,161);">swiper</span><span style="color: rgb(132,63,161);">不响应</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,0,170);">        ))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Block</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'80%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'50%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffbfffff'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">GestureDragAndSwiper </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SwiperController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SwiperController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'0'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ff96b1ff'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffffdcc6'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffc9ffd9'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">CanvasExampleOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：场景二中除了使用优先识别手势priorityGesture，还有其他替代方案吗？
 
A：可以使用自定义手势判定方法[onGestureJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#ongesturejudgebegin)，实现对[手势的自定义判定](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge#示例1自定义手势判定)。
