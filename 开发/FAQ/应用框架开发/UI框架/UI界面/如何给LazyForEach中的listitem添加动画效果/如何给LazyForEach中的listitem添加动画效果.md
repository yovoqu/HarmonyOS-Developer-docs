# 如何给LazyForEach中的listitem添加动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-565

#### 问题现象

使用LazyForEach渲染一个List，如何给每个ListItem都添加动画效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/SyWZ9iH9S_qIHKBZ6Ero-A/zh-cn_image_0000002658911355.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005712Z&HW-CC-Expire=86400&HW-CC-Sign=97D0CFAAC7D128CA959C41BDE8596ADDBF28AC212F375A33AFBCFE29944D4D98)

 
 

#### 背景知识

- [@AnimatableExtend](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animatable-extend)可以将一个属性定义为可动画属性，例如给fontSize添加可动画属性即可实现字体大小变化时的动画。
- 开发者可以使用[@ObservedV2装饰器和@Trace装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)装饰类以及类中的属性。使被@Trace装饰的属性成为状态变量，从而去刷新UI动画。

 
 

#### 解决方案
1. 定义LazyForEach的数据类MaterialWrap，并用@ObservedV2装饰器和@Trace装饰器观察其中属性。
```text
<span style="color: rgb(181,106,1);">@ObservedV2</span>
export class <span style="color: rgb(0,0,255);">MaterialWrap </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

2. 使用@AnimatableExtend定义用于执行动画的属性。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">fontSize</span><span style="color: rgb(128,128,128);">作为动画属性</span></em>
<span style="color: rgb(181,106,1);">@AnimatableExtend</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">)</span>
function <span style="color: rgb(0,0,255);">animatableFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

3. 使用LazyForEach进行渲染时利用item.size的变化去执行动画效果。
```text
<span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">24 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">materialsDataSource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'button'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animatableFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Linear </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
完整示例参考如下：
 
```text
class <span style="color: rgb(0,0,255);">BasicDataSource </span>implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">originDataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">originDataArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">originDataArray</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'add listener'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'remove listener'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">pos</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataReloaded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataAdd</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataDelete</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataMove</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">from</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">to</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">notifyDatasetChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">operations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataOperation</span><span style="color: rgb(0,0,255);">[])</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDatasetChange</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">operations</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

class <span style="color: rgb(0,0,255);">FilterItemDataSource </span>extends <span style="color: rgb(0,0,255);">BasicDataSource </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">filterDataItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filterDataItems</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filterDataItems</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">pushData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filterDataItems</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataAdd</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filterDataItems</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@ObservedV2</span>
export class <span style="color: rgb(0,0,255);">MaterialWrap </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Trace </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">AnimatableList </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span>private <span style="color: rgb(0,0,255);">materialsDataSource</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FilterItemDataSource </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">FilterItemDataSource</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">dataOrign</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataOrign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">materialsDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">filterDataItems </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dataOrign</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">materialsDataSource</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">24 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">materialsDataSource</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'button'</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animatableFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">)</span>
              <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Linear </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MaterialWrap</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>

      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignListItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ListItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);">fontSize</span><span style="color: rgb(128,128,128);">作为动画属性</span></em>
<span style="color: rgb(181,106,1);">@AnimatableExtend</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">)</span>
function <span style="color: rgb(0,0,255);">animatableFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
