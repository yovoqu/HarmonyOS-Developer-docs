# Canvas绘制矩形无法覆盖文字

更新时间：2026-08-13 01:23:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1141

#### 问题现象

利用Canvas绘制矩形和文字，矩形无法覆盖文字范围。
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CanvasTestPage </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'Harmony</span><span style="color: rgb(132,63,161);">你好</span>\n<span style="color: rgb(132,63,161);">测试一下换行的测试一下换行</span>\n<span style="color: rgb(132,63,161);">测试制表</span>\t<span style="color: rgb(132,63,161);">哈哈</span><span style="color: rgb(132,63,161);">'</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">font </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'18vp sans-serif'</span>
          let <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextMetrics </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(255,0,170);">)</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'rgba(0,0,0,0.3)'</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillRect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(255,0,170);">)</span>

          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'rgb(0,0,255)'</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/TAh1sALVQoym6QzcW6qrJw/zh-cn_image_0000002658808969.png?HW-CC-KV=V1&HW-CC-Date=20260813T095603Z&HW-CC-Expire=86400&HW-CC-Sign=9E32BC0D4133A3AA463D226AF81F7BD68A7A5F8B0171AC94967EAD364635EBF1)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ktq9CvNARiSta-L1hcrFOw/zh-cn_image_0000002628569606.png?HW-CC-KV=V1&HW-CC-Date=20260813T095603Z&HW-CC-Expire=86400&HW-CC-Sign=893A57A7D2AC44E2D5BE51F74EAB0B47E6B031874BA1E6C6023E553EE5547E57)

 
 

#### 背景知识

- [fillRect](https://developer.huawei.com/consumer/cn/doc/atomic-ascf/apis-canvas-rendering-context-2d#canvasrenderingcontext2dfillrect)：填充一个矩形，四个必填参数依次为矩形左上角点的x坐标、矩形左上角点的y坐标、指定矩形的宽度、指定矩形的高度，根据四个参数即可完成一个矩形的绘制。
- [fillText](https://developer.huawei.com/consumer/cn/doc/atomic-ascf/apis-canvas-rendering-context-2d#canvasrenderingcontext2dfilltext)：填充文本，三个必填参数依次为文本内容、文本绘制起点的x轴坐标、文本绘制起点的y轴坐标，根据三个参数即可确定填充文本的坐标。

 
 

#### 问题定位

根据问题代码运行效果可以看出：灰色矩形宽度和文本宽度一致，x轴起点保持一致，但是蓝色文字y轴起点和灰色矩形y轴起点不一致，可以发现问题出现在fillRect绘制的y轴起点上。
 
```text
this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(255,0,170);">)</span>
```
 
该错误代码设置文本的y轴起点为“100+文本高度”。
 
 

#### 分析结论

根据fillRect和fillText参数可知，保持矩形左上角点的y坐标和文本绘制起点的y轴坐标一致，即可保持绘制时在同一个y轴起点。
 
 

#### 修改建议
1. 修改fillText的文本起点y轴坐标。
2. [textBaseline](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-common-property#textbaseline)可以设置文本绘制中的水平对齐方式，将其设置成top对齐，实现文本基线在文本块的顶部。若不设置，则默认为alphabetic对齐（按字母对齐）。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">CanvasFillRectPage </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RenderingContextSettings </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RenderingContextSettings</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">CanvasRenderingContext2D </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">CanvasRenderingContext2D</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">settings</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'Harmony</span><span style="color: rgb(132,63,161);">你好</span>\n<span style="color: rgb(132,63,161);">测试一下换行的测试一下换行</span>\n<span style="color: rgb(132,63,161);">测试制表</span>\t<span style="color: rgb(132,63,161);">哈哈</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Canvas</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">font </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'18vp sans-serif'</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">textBaseline </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'top'</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TextMetrics </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">measureText</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'rgba(0,0,0,0.3)'</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillRect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">text</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fillStyle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'rgb(0,0,255)'</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fillText</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">drawText</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
