# 如何在List使用懒加载时动态修改最后一条数据样式

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1305

#### 问题现象

在List使用懒加载加载下一页时，如何确保每次加载完数据后都能动态更新最后一条数据的样式？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/9TVz5nB0SQ6o_T90tnHX4Q/zh-cn_image_0000002658838283.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005805Z&HW-CC-Expire=86400&HW-CC-Sign=31E358E446DC2848E82A3F747F00E1B8AE76066C696D414AE43FF1FC85DAFBF7)

 
 

#### 背景知识

- [List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。List列表可使用[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)进行懒加载。
- [if/else：条件渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)可根据应用状态，使用if、else和else if渲染相应的UI内容。
- [onAppear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide#onappear)：组件挂载后触发此回调。

 
 

#### 解决方案

使用LazyForEach加载列表数据，在ListItem下使用条件渲染来判断List列表中的最后一项，并对最后一项通过挂载回调事件onAppear进行条件渲染。
 
```text
class <span style="color: rgb(0,0,255);">BasicDataSource </span>implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">originDataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">originDataArray</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">该方法为框架侧调用，为</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件向其数据源处添加</span><span style="color: rgb(128,128,128);">listener</span><span style="color: rgb(128,128,128);">监听</span></em>
  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'add listener'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">该方法为框架侧调用，为对应的</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件在数据源处去除</span><span style="color: rgb(128,128,128);">listener</span><span style="color: rgb(128,128,128);">监听</span></em>
  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'remove listener'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件需要重载所有子组件</span></em>
  <span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataReloaded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件需要在</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">对应索引处添加子组件</span></em>
  <span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件在</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">对应索引处数据有变化，需要重建该子组件</span></em>
  <span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件需要在</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">对应索引处删除该子组件</span></em>
  <span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通知</span><span style="color: rgb(128,128,128);">LazyForEach</span><span style="color: rgb(128,128,128);">组件将</span><span style="color: rgb(128,128,128);">from</span><span style="color: rgb(128,128,128);">索引和</span><span style="color: rgb(128,128,128);">to</span><span style="color: rgb(128,128,128);">索引处的子组件进行交换</span></em>
  <span style="color: rgb(0,0,255);">notifyDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

class <span style="color: rgb(0,0,255);">MyDataSource </span>extends <span style="color: rgb(0,0,255);">BasicDataSource </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">pushData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MyComponent1 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MyDataSource </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MyDataSource</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Hello </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">21</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pushData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Hello </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">3 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">80</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"appear:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addData</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
                <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"appear:" </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
> [!NOTE]
> 如上示例中，在首次渲染时只加载前20位，直到Hello20，并且因为此时Hello20为最后一位，所以Hello20的fontSize为100，其余项的fontSize为50；在滑到最后一位时触发增加数据的操作，此时数组内有40位数据，并且Hello20不再是最后一位元素，因此fontSize恢复为50，同时Hello40为最后一位数据，fontSize为100。
