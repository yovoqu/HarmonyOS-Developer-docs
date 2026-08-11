# LazyForEach实现骨架屏预加载效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-705

#### 问题现象

如何实现骨架屏预加载效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/hAvegf_SSiuumkuMhGG5pw/zh-cn_image_0000002658914207.png?HW-CC-KV=V1&HW-CC-Date=20260811T005642Z&HW-CC-Expire=86400&HW-CC-Sign=D28B0BCBAC16D8C15659D3A6AB55C82A58D694F2A314030846918952928DD598)

 
 

#### 背景知识

- [LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)为开发者提供了基于数据源渲染出一系列子组件的能力。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
- 骨架屏通过显示简单的灰色块和线条，让用户在等待内容加载时获得视觉反馈。

 
 

#### 解决方案
1. 使用LazyForEach对数据源中的每个数据进行预加载。
2. 在Stack组件中，首先设置背景色为rgba(0,0,0,0.1)，然后通过linearGradient设置组件的颜色渐变效果，并结合animation方法设置动画的持续时间和循环次数。
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">用户自定义数据源</span></em>
class <span style="color: rgb(0,0,255);">MyDataSourceLOne </span>implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[]) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">list </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">BackGroundColorGradualChange </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">MyDataSourceLOne </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MyDataSourceLOne</span><span style="color: rgb(255,0,170);">([])</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">listScroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ListScroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ListScroller</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">translateX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'-100%'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    let <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">7</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MyDataSourceLOne</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">list</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">initialIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">listScroller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
           <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置组件的背景色</span></em>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">()</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'rgba(0,0,0,0.1)'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">()</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">translate</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">translateX </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">translateX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
             <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置动画的持续时间和循环次数</span></em>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">1</span>
                <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
              <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置颜色渐变效果</span></em>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradient</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
                  <span style="color: rgb(255,255,255);">angle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">90</span><span style="color: rgb(181,106,1);">,</span>
                  <span style="color: rgb(255,255,255);">colors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span>
<span style="color: rgb(255,0,170);">                    [</span><span style="color: rgb(132,63,161);">'rgba(255,255,255,0)'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">,</span>
                    <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'rgba(255,255,255,1)'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">,</span>
                    <span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'rgba(255,255,255,0)'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">]</span>
<span style="color: rgb(255,0,170);">                  ]</span>
                <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0xFFFFFF)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listDirection</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Axis</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Vertical</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Off</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">friction</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0.6</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Spring</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0xDCDCDC)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 总结

使用linearGradient设置骨架屏的渐变效果，可增强用户体验，提升用户停留时长。
