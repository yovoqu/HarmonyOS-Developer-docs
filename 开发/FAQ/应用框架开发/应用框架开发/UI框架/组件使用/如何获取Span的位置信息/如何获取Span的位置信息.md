# 如何获取Span的位置信息

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1314

#### 问题现象

在UI开发中，如何获取Text中某个Span的位置信息？
 
 

#### 背景知识

- [Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。
- [ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)：Text、ContainerSpan组件的子组件，用于显示行内图片。
- [onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

 
 

#### 解决方案

Text中的ImageSpan支持onAreaChange事件，可通过在Span前添加一个宽高均为0的ImageSpan，在ImageSpan的onAreaChange获取到ImageSpan的位置，即为Span的位置。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SpanPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">span2x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">span2y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Span1'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">18</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">ImageSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAreaChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">oldValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Area</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">span2x </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">globalPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">x </span>as <span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">span2y </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">globalPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">y </span>as <span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Span2</span><span style="color: rgb(132,63,161);">相对页面左上角的</span><span style="color: rgb(132,63,161);">x</span><span style="color: rgb(132,63,161);">坐标为</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">globalPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">,y</span><span style="color: rgb(132,63,161);">坐标为</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">newValue</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">globalPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">y</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Span2'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">18</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Span2</span><span style="color: rgb(132,63,161);">相对页面左上角的</span><span style="color: rgb(132,63,161);">x</span><span style="color: rgb(132,63,161);">坐标为</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">span2x</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">,y</span><span style="color: rgb(132,63,161);">坐标为</span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">span2y</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
