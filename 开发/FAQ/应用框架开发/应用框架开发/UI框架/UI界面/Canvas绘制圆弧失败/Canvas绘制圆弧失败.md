# Canvas绘制圆弧失败

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-668

#### 问题现象

在以下使用CanvasRenderingContext2D的arc方法绘制圆弧的过程中，无论如何修改percent的值以改变弧线的终止弧度，运行代码后都会出现一个完整的圆弧。
 
问题示例如下：
 
```text
const <span style="color: rgb(0,0,255);">FULL_CIRCLE_RADIAN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PI </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">2</span>
const <span style="color: rgb(0,0,255);">CHECK_GREEN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#00CC66'</span>

<span style="color: rgb(181,106,1);">@Component</span>
<span style="color: rgb(181,106,1);">@Entry</span>
export struct <span style="color: rgb(0,0,255);">ReceiptIcon </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">radiusPx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span>
  <span style="color: rgb(0,0,255);">percent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span>
  <span style="color: rgb(181,106,1);">@State </span>private <span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span>
  private <span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
  private <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(0,0,255);">)</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onSizeChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SizeOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SizeOptions</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">min</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.5</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.125</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">beginPath</span><span style="color: rgb(0,0,255);">()</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CHECK_GREEN</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arc</span><span style="color: rgb(0,0,255);">(</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">          -</span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">,</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">percent </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">FULL_CIRCLE_RADIAN</span>
        <span style="color: rgb(0,0,255);">)</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(0,0,255);">()</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">beginPath</span><span style="color: rgb(0,0,255);">()</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CHECK_GREEN</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">()</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 背景知识

- [CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)组件可在Canvas画布组件上进行绘制，绘制对象可以是图形、文本、线段、图片等，该组件的[arc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#arc)方法用于绘制弧线路径。
- 弧度是角的度量单位。它是由国际单位制导出的单位，英文缩写为rad。其定义为：弧长等于圆半径的弧所对应的圆心角为1rad。一个完整的圆所对应的弧度是2π。

 
 

#### 问题定位

注意到开发者在arc方法的第四个参数为-90，应该是将弧度误用成了角度。
 
 

#### 分析结论

在HarmonyOS中，关于角度的使用都是使用弧度，而不是角度。弧度和角度的具体换算方法如下：
 
弧度转角度：1rad=(180/π)°，角度转弧度：1°=(π/180)rad。
 
 

#### 修改建议

将第四个参数-90改成-(π/2)，对应到代码中即为-(FULL_CIRCLE_RADIAN / 4)，代码修改如下所示：
 
```text
const <span style="color: rgb(0,0,255);">FULL_CIRCLE_RADIAN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PI </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">CHECK_GREEN </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#00CC66'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">ReceiptIcon </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">radiusPx</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">percent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span>private <span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">settings</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onSizeChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SizeOptions</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SizeOptions</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">min</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">Number</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">?? </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)) </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.125</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">beginPath</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CHECK_GREEN</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arc</span><span style="color: rgb(0,0,255);">(</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">radiusPx </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">0.5</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
<span style="color: rgb(181,106,1);">          -</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FULL_CIRCLE_RADIAN </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">4</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">percent </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">FULL_CIRCLE_RADIAN</span>
        <span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">beginPath</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">CHECK_GREEN</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
