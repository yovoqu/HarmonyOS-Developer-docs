# 组件复用时，如何解决animation动画不停止的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1433

#### 问题现象

使用linearGradient给List子组件设置线性渐变颜色，并使用@Reusable设置子组件复用，复用时animation属性动画不停止。问题现象如下：开始给item0，item1，item2加上背景渐变的属性动画，快速滑动页面，item27，item28，item29三项使用了复用的组件，但背景渐变动画没有及时停止。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Ova0nHxJT6m2ycK_Ww4uSw/zh-cn_image_0000002628763652.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012750Z&HW-CC-Expire=86400&HW-CC-Sign=47055AD3CE1246177DFD04BC85294A343298ADA8FE54CB74A76219EB87F2426C)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/-7ASTt64RGODHdp3SfwjBA/zh-cn_image_0000002658962967.gif?HW-CC-KV=V1&HW-CC-Date=20260723T012750Z&HW-CC-Expire=86400&HW-CC-Sign=9DEE829277AB58C3BAC752DB1B1005A2C7C30E5F5FACCA92282D734AEF9D0F13)

 
 

#### 背景知识

- [@Reusable装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-reusable)标记的自定义组件可以复用。在从组件树中移除时，组件及其对应的JS对象将被放入复用缓存中，后续创建新自定义组件节点时，将复用缓存中的节点。
- [linearGradient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color#lineargradient)设置组件的颜色线性渐变效果。颜色渐变属于组件内容，绘制在背景上方。
- [onVisibleAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event#onvisibleareachange)组件可见区域变化时触发该回调，触发条件为输入的阈值数组。
- [animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)设置组件的属性动画。入参AnimateParam包含部分参数如下：
duration：动画持续时间，单位为毫秒。
- curve：动画曲线。

 
 
 

#### 解决方案

动画未停止原因：背景色渐变色动画未结束，滑动页面，组件对象放入缓存中等待复用，此时缓存中组件为播放动画的状态，当新的列表项复用此组件对象时，会按照放入缓存时的状态重新播放动画。若是等待动画结束后滑动页面，可以看到动画问题不会出现，因为组件对象放入缓存中是动画已经结束的状态。
 
可以通过状态变量控制animation动画的持续时间来避免此问题。
 1. 使用@State装饰器创建状态变量duration，作为animation的入参，控制动画持续时间。
2. 监听复用组件的可见区域变化事件。
- 当组件复用放入缓存中，触发onVisibleAreaChange回调，设置duration为0，清除动画状态。

3. 当组件从缓存中取出复用后，触发onVisibleAreaChange回调，重新设置duration为2500。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onVisibleAreaChange</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2500</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">组件从缓存取出复用</span></em>
  <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件放入缓存</span></em>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```


  完整示例参考如下：

  
List父组件页面代码：
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ListRepeatPage </span><span style="color: rgb(255,0,170);">{</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">复用组件的背景渐变色</span></em>
  static readonly <span style="color: rgb(0,0,255);">colorsGreen</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">ResourceColor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">][]</span> <span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
<span style="color: rgb(0,0,255);">    [</span><span style="color: rgb(255,0,170);">'#00008A5C'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'#66008A5C'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">  ]</span><span style="color: rgb(181,106,1);">;</span>
  static readonly <span style="color: rgb(0,0,255);">colorsDefault</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">ResourceColor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">][]</span> <span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
<span style="color: rgb(0,0,255);">    [</span><span style="color: rgb(255,0,170);">'#00000000'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,170);">'#00000000'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span>
<span style="color: rgb(0,0,255);">  ]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">StockListData </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">StockListData</span><span style="color: rgb(0,0,255);">([])</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始化显示数据</span></em>
    const <span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">50</span><span style="color: rgb(181,106,1);">; ++</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">stockName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'item' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(0,0,255);">bgState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span>new <span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">stockName</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">modifyAllData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">开始</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">前三项渐变色</span></em>
          for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">; ++</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            const <span style="color: rgb(0,0,255);">bg </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bg </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">LazyForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">list</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">ItemView</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">info </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">radius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'6vp' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stockName </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'type' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'16vp'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- List子组件代码如下：可被复用，使用状态变量控制动画展示。
```text
<span style="color: rgb(181,106,1);">@Reusable</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ItemView </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@ObjectLink @Watch</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'infoUpdate'</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">linearGradientBgStatus</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2500</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">infoUpdate</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">status </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">status</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Flex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stockName </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,170);">'-in-' </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'16'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">minFontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'8'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxLines</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'36.27%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'16'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBlur</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fractionStops</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">[[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.33</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0.66</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">]]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GradientDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradient</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GradientDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Right</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">ListRepeatPage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">colorsGreen </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ListRepeatPage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">colorsDefault</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">FastOutLinearIn</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">绿色渐变结束后，渐变回原来的颜色</span></em>
          if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">!== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
            if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">!== </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">linearGradientBgStatus </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onVisibleAreaChange</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isVisible</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2500</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件从缓存取出复用</span></em>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件放入缓存</span></em>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- List数据源结构：
```text
<span style="color: rgb(181,106,1);">@Observed</span>
class <span style="color: rgb(0,0,255);">ItemInfo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">stockName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'--'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(0,0,255);">bgState</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bg</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stockName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">bgState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">bg</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

class <span style="color: rgb(0,0,255);">StockListData </span>implements <span style="color: rgb(0,0,255);">IDataSource </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">[]) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">dataArray</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">totalCount</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">getData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo </span><span style="color: rgb(255,0,170);">{</span>
    return this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  public <span style="color: rgb(0,0,255);">modifyAllData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ItemInfo</span><span style="color: rgb(0,0,255);">[])</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">data</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">registerDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">unregisterDataChangeListener</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indexOf</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">splice</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">notifyDataReload</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listeners</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">DataChangeListener</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">listener</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDataReloaded</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
