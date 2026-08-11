# 停止XComponent渲染数据

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-978

#### 问题现象

使用XComponent组件进行YUV数据渲染时，如何停止XComponent渲染数据？
 
 

#### 背景知识

- [XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)提供一个用于图形绘制和媒体数据写入的Surface，能够将其嵌入到视图中，并支持应用自定义Surface的位置和大小。
- ArkTS提供了渲染控制能力。[条件渲染](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)可根据应用状态，使用if、else和else if渲染相应的UI内容。

 
 

#### 解决方案
1. 获取XComponent的完整工程代码如下：[基于XComponent组件实现OpenGL图形绘制及YUV图像渲染功能](https://gitee.com/harmonyos_samples/ndk-xcomponent)。
2. YUVView页面是一个使用XComponent组件进行渲染的实例。现对该页面进行如下修改：为XComponent组件添加条件渲染逻辑，当flag值为true时渲染该组件，为false时则销毁该组件，并添加onDestroy方法以在控制面板中查看组件销毁状态。
3. 在Column组件中添加一个销毁按钮，并为其绑定点击事件。当点击按钮且flag为true时，将其值改为false，点击销毁按钮时，触发XComponent组件的onDestroy函数，表示该组件已被销毁。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">fileIo </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">YUVViewStopPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">isClick</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">xComponentContext</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(181,106,1);">{}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">flag</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">void </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">writeYUVFile</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">flag</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span><em> </em><em><span style="color: rgb(128,128,128);">// flag</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">true</span><span style="color: rgb(128,128,128);">时渲染该组件，为</span><span style="color: rgb(128,128,128);">false</span><span style="color: rgb(128,128,128);">时销毁该组件</span></em>
          <span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">id</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'XComponentId'</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">TEXTURE</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">libraryname</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'LIBRARY_NAME'</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onLoad</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">xComponentContext</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(181,106,1);">object </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">xComponentContext</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xComponentContext </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">xComponentContext </span>as <span style="color: rgb(181,106,1);">Record</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDestroy</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{ </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断是否销毁</span></em>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`XComponent</span><span style="color: rgb(132,63,161);">已销毁</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">销毁</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">18</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'20%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">flag </span><span style="color: rgb(181,106,1);">=== </span>true<span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">flag </span><span style="color: rgb(181,106,1);">= !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">flag</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  async <span style="color: rgb(0,0,255);">writeYUVFile</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      const <span style="color: rgb(255,255,255);">resourceManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(255,255,255);">imageArray </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMediaContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">id</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">此处仅为样例，请开发者更换为可用图片</span></em>
      let <span style="color: rgb(255,255,255);">path</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">!.</span><span style="color: rgb(255,255,255);">filesDir </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'/image.yuv'</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">file </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">path</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">READ_WRITE </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(255,255,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">CREATE</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">write</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">imageArray</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">buffer</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">closeSync</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">file</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">    }</span>
<span style="color: rgb(181,106,1);">  }</span>
<span style="color: rgb(181,106,1);">}</span>
```
