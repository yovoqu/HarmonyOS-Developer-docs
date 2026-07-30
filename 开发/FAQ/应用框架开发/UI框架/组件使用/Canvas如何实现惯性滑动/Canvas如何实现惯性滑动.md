# Canvas如何实现惯性滑动

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-989

#### 问题现象

Canvas绘制一个数字列表，需要添加滑动手势才能实现滑动，但在手指松开之后，滑动就会停止，无法达到惯性滑动的效果，Canvas如何才能实现惯性滑动的效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/k-vhNSplT8e6uRqWk3TSpA/zh-cn_image_0000002628401810.png?HW-CC-KV=V1&HW-CC-Date=20260730T072336Z&HW-CC-Expire=86400&HW-CC-Sign=7DFE49D6B6B23E8E73BB9564D16368C13DC1BA7686C765B95ABC5993C6C29E2A)

 
 

#### 背景知识

[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas)可用于自定义绘制图形，如：形状、文本、图片等。创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。
 
 

#### 解决方案

整体思路如下：
 1. 监听[滑动手势结束回调](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture#onactionend)事件，触发执行惯性滚动的函数。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollFling</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```

2. 计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果</span></em>
const <span style="color: rgb(0,0,255);">v </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">speed </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">E</span><span style="color: rgb(181,106,1);">, -</span><span style="color: rgb(0,0,255);">frictionFactor </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">speed </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">distance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">distance</span><span style="color: rgb(181,106,1);">;</span>
```

3. 启动一个定时器，每次达到定时时间，则根据上一步计算出的滑动距离，重新绘制画布。
```text
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTimerId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setInterval</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">redrawCanvas</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

4. 在滑动时间不足或滑动距离超出范围时，则停止定时器。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">偏移量不在</span><span style="color: rgb(128,128,128);">[-maxOffset, 0]</span><span style="color: rgb(128,128,128);">区间时，需修正偏移量，并停止定时器</span></em>
if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxOffset</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
```text
if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTime </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动时间不足时，停止定时器</span></em>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  return<span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

 
完整示例参考如下：
 
```text
const <span style="color: rgb(0,0,255);">DRAW_SPACE</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">CANVAS_HEIGHT</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CanvasFling </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">startX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">maxOffset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">flingTime</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">flingTimerId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>

  private <span style="color: rgb(0,0,255);">initCanvas</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">map</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">_</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">drawCanvas</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  private <span style="color: rgb(0,0,255);">drawCanvas</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxOffset</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">= -</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxOffset</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">font </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'normal normal 24vp sans-serif'</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#000000'</span><span style="color: rgb(181,106,1);">;</span>

    let <span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">metrics </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">DRAW_SPACE </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">x </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listData</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">metrics</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxOffset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  private <span style="color: rgb(0,0,255);">onPanGestureUpdate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startX</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">drawCanvas</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  private <span style="color: rgb(0,0,255);">scrollFling</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">speed</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(181,106,1);">;      </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">假设每隔</span><span style="color: rgb(128,128,128);">16ms</span><span style="color: rgb(128,128,128);">进行画布重绘</span></em>
    const <span style="color: rgb(0,0,255);">frictionFactor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;   </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">摩擦系数，系数越大阻力越大</span></em>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">speed</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTime </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abs</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">frictionFactor</span><span style="color: rgb(181,106,1);">;</span>

    const <span style="color: rgb(0,0,255);">redrawCanvas </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTime </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{ </span><em>// </em><em><span style="color: rgb(128,128,128);">滑动时间不足时，停止定时器</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>

      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX </span><span style="color: rgb(181,106,1);">-= </span><span style="color: rgb(0,0,255);">frictionFactor </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTime </span><span style="color: rgb(181,106,1);">-= </span><span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(181,106,1);">;</span>

  <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">计算滑动速度和滑动距离，示例使用指数函数方式计算速度和距离，以达到先快后慢的效果</span></em>
      const <span style="color: rgb(0,0,255);">v </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">speed </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">E</span><span style="color: rgb(181,106,1);">, -</span><span style="color: rgb(0,0,255);">frictionFactor </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">speed </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(0,0,255);">distance </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">v </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">frameTime </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(0,0,255);">distance</span><span style="color: rgb(181,106,1);">;</span>

     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">偏移量不在</span><span style="color: rgb(128,128,128);">[-maxOffset, 0]</span><span style="color: rgb(128,128,128);">区间时，需修正偏移量，并停止定时器</span></em>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxOffset</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>

      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">drawCanvas</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stopTimer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTimerId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setInterval</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">redrawCanvas</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">frameTime</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  private <span style="color: rgb(0,0,255);">stopTimer</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTimerId </span><span style="color: rgb(181,106,1);">!== -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">clearInterval</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTimerId</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTimerId </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  private <span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">flingTime </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stopTimer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">canvas</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CANVAS_HEIGHT </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Gray</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">initCanvas</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
          <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(0,0,255);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionStart</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionUpdate</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onPanGestureUpdate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollFling</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">velocityX</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">        )</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'100%' </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
