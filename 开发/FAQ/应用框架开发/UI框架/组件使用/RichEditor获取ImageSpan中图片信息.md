# RichEditor获取ImageSpan中图片信息

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-943

#### 问题现象

在RichEditor组件中通过\$r('app.media.background')方式添加ImageSpan，并使用getSpans获取span信息时，由于base目录中的资源文件会被编译成二进制文件并分配资源ID，导致获取的图片名称与实际图片名称不一致。
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vKmRvw4ySVmhQHnG8bEk9w/zh-cn_image_0000002658800487.png?HW-CC-KV=V1&HW-CC-Date=20260701T041247Z&HW-CC-Expire=86400&HW-CC-Sign=CB9CA43AF42BCA5D0FDFF7813E7F49596E88BA6CDC30F301D133CEEE516E5412)

 
 

#### 背景知识

[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)是支持图文混排和文本交互式编辑的组件，可以通过[getSpans](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#getspans)方法获取所有span信息。
 
 

#### 解决方案

将图片资源放到rawfile文件夹下，再通过getSpans获取valueResourceStr字段，能够正常获取到图片的名称。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">RichEditorPage </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">RichEditorController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">RichEditorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">RichEditor</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onReady</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addTextSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击按钮在此处添加</span><span style="color: rgb(132,63,161);">image</span><span style="color: rgb(132,63,161);">。</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">fontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(255,255,255);">fontSize</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">15</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">添加图片</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">buttonStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonStyleMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NORMAL</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">13</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">addImageSpan</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'background.png'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">imageStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(255,255,255);">size</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'57px'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'57px'</span><span style="color: rgb(255,0,170);">]</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">获取图片</span><span style="color: rgb(132,63,161);">span'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">buttonStyle</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">ButtonStyleMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NORMAL</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getSpans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">start</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`imageName is : </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item </span>as <span style="color: rgb(181,106,1);">RichEditorImageSpanResult</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">valueResourceStr</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SpaceAround</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">border</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/C_cNKk7OSTiC_HyiHa5AQw/zh-cn_image_0000002628561128.png?HW-CC-KV=V1&HW-CC-Date=20260701T041247Z&HW-CC-Expire=86400&HW-CC-Sign=59E76522D071283422A8C64A07E16961DEFABC41299138359470D9A7C524D89D)
