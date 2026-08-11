# 怎么解决Progress组件配合animateTo实现循环动画无反应问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-508

#### 问题现象

使用Progress组件配合animateTo来实现进度条循环动画，动画效果失效无反应。
 
```text
<em>/** </em><em><span style="color: rgb(128,128,128);">进度条最小值</span><span style="color: rgb(128,128,128);"> */</span></em>
const <span style="color: rgb(255,255,255);">PROGRESS_MIN1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
<em>/** </em><em><span style="color: rgb(128,128,128);">进度条最大值</span><span style="color: rgb(128,128,128);"> */</span></em>
const <span style="color: rgb(255,255,255);">PROGRESS_MAX1 </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ProgressAnimWithProblem </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">/** </span><span style="color: rgb(128,128,128);">进度条当前值</span><span style="color: rgb(128,128,128);"> */</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">progressValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">PROGRESS_MIN1</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">UIContext </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">!</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">warn</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'no uiContext'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">uiContext</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">-1</span><span style="color: rgb(128,128,128);">表示动画无限循环</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">PROGRESS_MAX1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Progress</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条当前进度值</span></em>
        <span style="color: rgb(255,255,255);">total</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PROGRESS_MAX1</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">进度条总长</span></em>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ProgressType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Ring</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">进度条类型，分为</span><span style="color: rgb(128,128,128);">Linear</span><span style="color: rgb(128,128,128);">线性样式、</span><span style="color: rgb(128,128,128);">ScaleRing</span><span style="color: rgb(128,128,128);">环形有刻度样式、</span><span style="color: rgb(128,128,128);">Ring</span><span style="color: rgb(128,128,128);">环形无刻度样式、</span><span style="color: rgb(128,128,128);">Eclipse</span><span style="color: rgb(128,128,128);">圆形样式、</span><span style="color: rgb(128,128,128);">Capsule</span></em><em>胶囊样式</em>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">style</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条宽度，默认</span><span style="color: rgb(128,128,128);">4vp</span></em>
          <span style="color: rgb(255,255,255);">enableSmoothEffect</span><span style="color: rgb(181,106,1);">: </span>true <em>// </em><em><span style="color: rgb(128,128,128);">进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值</span><span style="color: rgb(128,128,128);">true</span></em>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条组件宽度</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#0A59F7'</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条前景色</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条背景色</span></em>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 
 

#### 背景知识

- [进度条（Progress）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator)：用于显示内容加载或操作处理等进度。可以有多种表现形式，官方提供胶囊型、环形有刻度、环形无刻度、圆形，且支持自定义图形样式。
- 显式动画（animateTo）：提供全局[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、Canvas的内容等。
- [定时器（Timer）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer)：[setInterval()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#setinterval)方法重复调用一个函数，在每次调用之间具有固定的时间延迟。此方法创建一个定时器并返回该定时器ID，删除该定时器需要手动调用[clearInterval()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer#clearinterval)。

 
 

#### 问题定位

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），问题代码使用animateTo改变Progress组件的进度值，结果是进度条从0到100动画仅执行一次。可见不支持使用animateTo控制Progress组件进度条循环效果。
 
 

#### 分析结论

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），不支持使用animateTo控制Progress组件进度值变化来实现进度条循环效果。
 
 

#### 修改建议

可以使用定时器来控制Progress组件进度值变化。用setInterval()方法创建定时任务，每间隔一段时间（如20毫秒）均匀地改变Progress组件进度值（如每次加1），即可实现预期效果。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/6PBO4eIsSv-yFu51GT99tw/zh-cn_image_0000002628388622.png?HW-CC-KV=V1&HW-CC-Date=20260811T005825Z&HW-CC-Expire=86400&HW-CC-Sign=9A257846E4C218D61E83E7872078DDB746753D0E8CD30AEEB1C34A44C9C56B8B)

 
```text
<em>/** </em><em><span style="color: rgb(128,128,128);">进度条最小值</span><span style="color: rgb(128,128,128);"> */</span></em>
const <span style="color: rgb(255,255,255);">PROGRESS_MIN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
<em>/** </em><em><span style="color: rgb(128,128,128);">进度条最大值</span><span style="color: rgb(128,128,128);"> */</span></em>
const <span style="color: rgb(255,255,255);">PROGRESS_MAX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ProgressAnim </span><span style="color: rgb(181,106,1);">{</span>
 <em> <span style="color: rgb(128,128,128);">/** </span><span style="color: rgb(128,128,128);">进度条当前值</span><span style="color: rgb(128,128,128);"> */</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">progressValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">PROGRESS_MIN</span><span style="color: rgb(181,106,1);">;</span>


  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进入界面时即启动进度条动画</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAnim</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Progress</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条当前进度值</span></em>
        <span style="color: rgb(255,255,255);">total</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PROGRESS_MAX</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条总长</span></em>
        <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ProgressType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Ring</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条类型，分为</span><span style="color: rgb(128,128,128);">Linear</span><span style="color: rgb(128,128,128);">线性样式、</span><span style="color: rgb(128,128,128);">ScaleRing</span><span style="color: rgb(128,128,128);">环形有刻度样式、</span><span style="color: rgb(128,128,128);">Ring</span><span style="color: rgb(128,128,128);">环形无刻度样式、</span><span style="color: rgb(128,128,128);">Eclipse</span><span style="color: rgb(128,128,128);">圆形样式、</span><span style="color: rgb(128,128,128);">Capsule</span></em><em>胶囊样式</em>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">style</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">进度条宽度，默认</span><span style="color: rgb(128,128,128);">4vp</span></em>
          <span style="color: rgb(255,255,255);">enableSmoothEffect</span><span style="color: rgb(181,106,1);">: </span>true <em>// </em><em><span style="color: rgb(128,128,128);">进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值</span><span style="color: rgb(128,128,128);">true</span></em>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条组件宽度</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#0A59F7'</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条前景色</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">进度条背景色</span></em>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开启进度条动画</span></em>
  private <span style="color: rgb(0,0,255);">startAnim</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// intervalId</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">null</span><span style="color: rgb(128,128,128);">时表示未启动</span><span style="color: rgb(128,128,128);">interval</span></em>
    <span style="color: rgb(0,0,255);">setInterval</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">setInterval()</span><span style="color: rgb(128,128,128);">方法重复执行以下代码片段，在每次调用之间具有固定的时间间隔</span><span style="color: rgb(128,128,128);">20</span><span style="color: rgb(128,128,128);">毫秒</span></em>
<em>      <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">每次进度值</span><span style="color: rgb(128,128,128);">+1</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue</span><span style="color: rgb(181,106,1);">++;</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当进度值达到最大值时，将进度值重置为最小值，循环往复</span></em>
      if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,255,255);">PROGRESS_MAX</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">progressValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">PROGRESS_MIN</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
```
