# 如何让Slider不显示进度变化动画

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-998

#### 问题现象

Slider在点击和长按某个位置时，如何让进度直接展示，不显示进度变化动画？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ZkkJTh5jR_6ArUusJmuy_Q/zh-cn_image_0000002658804037.png?HW-CC-KV=V1&HW-CC-Date=20260730T072336Z&HW-CC-Expire=86400&HW-CC-Sign=7FF1A33CF1495C92F1E33C041B4A050809E525DCE7B87583B91051CA439BC18B)

 
 

#### 背景知识

- [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)：滑动条组件，通常用于快速调节设置值。可以通过[SliderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider#slideroptions对象说明)滑动条信息对象设置value控制当前进度值。
- [enabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable#enabled)可以设置组件是否可交互。当未设置enabled时，组件默认可交互。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。可以在组件加载完成时获取组件的宽高等信息。
- [onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)手指触摸动作触发该回调。通过该回调可以得到触摸事件的类型[TouchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#touchtype)和触点信息[TouchObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#touchobject)等。

 
 

#### 解决方案

可以禁用Slider原本的交互逻辑，通过其他事件修改Slider的进度值value，让滑块直接跳转到进度值对应的位置，从而不显示动画，具体步骤如下：
 1. 首先给Slider的值设置一个状态变量，通过enabled属性设置为false，禁用Slider原本的交互逻辑。在Slider外加一层容器组件。
```text
<span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#f1f3f5'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. [Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)未设置宽度或高度时，在主轴或交叉轴方向上自适应子组件大小。通过onAreaChange可以直接获取到滑动条组件的宽度，当滑动条的style为[SliderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider#sliderstyle枚举说明).OutSet时，左右间距分别为[blockSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider#blocksize10)宽度的一半（SliderStyle.OutSet时blockSize默认宽高18vp），滑动条组件宽度减18vp可以得到滑动条的长度。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算得到滑动条的长度（</span><span style="color: rgb(128,128,128);">18</span><span style="color: rgb(128,128,128);">是滑动条的左右边距）</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span>as <span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```

3. 给Slider外的容器组件添加触摸事件，根据触摸时x的坐标计算当前按下位置在整个滑动条的占比，再用最大值计算出按下时滑动条所在的值。通过这种方式修改value不会出现动画效果。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">按下时触发</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过触摸位置和滑动条长度计算占比，得到滑动条的值（</span><span style="color: rgb(128,128,128);">9</span><span style="color: rgb(128,128,128);">是滑动条的左边距）</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">拖动触发</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Move</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

 
完整代码如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SliderExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动条的值</span>
  <span style="color: rgb(0,0,255);">sliderLength</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动条的长度</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#f1f3f5'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Area</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算得到滑动条的长度（</span><span style="color: rgb(128,128,128);">18</span><span style="color: rgb(128,128,128);">是滑动条的左右边距）</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span>as <span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">18</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">按下时触发</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过触摸位置和滑动条长度计算占比，得到滑动条的值（</span><span style="color: rgb(128,128,128);">9</span><span style="color: rgb(128,128,128);">是滑动条的左边距）</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">拖动触发</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Move</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">value </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">sliderLength </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touches</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">9</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
