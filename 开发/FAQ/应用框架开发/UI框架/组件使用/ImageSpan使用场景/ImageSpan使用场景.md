# ImageSpan使用场景

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-575

#### 问题现象

如何实现下图中的追加评论效果？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/q-rZSLXGR0-dZgSnfG2Tpg/zh-cn_image_0000002658791437.png?HW-CC-KV=V1&HW-CC-Date=20260811T005744Z&HW-CC-Expire=86400&HW-CC-Sign=7A98DB80EFB11BFAFE4766FE9AF07B23A0EB33A4532BBCBFD8311D92EBBA3C81)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/GdwJ2MLkSPaoVqW41lMWew/zh-cn_image_0000002628552050.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005744Z&HW-CC-Expire=86400&HW-CC-Sign=4B360711D19CD161BC5E229A7C4CAC5FD486A82CB7FE88A3AB757717C1C83CBE)

 
 

#### 背景知识

- [Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。
- [ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)：Text、ContainerSpan组件的子组件，用于显示行内图片。

 
 

#### 解决方案

将图片换成镂空图，ImageSpan使用margin属性调整位置。
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ImageSpanExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">content</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">到了绿湖底部，面上神色一动。</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"</span>\n<span style="color: rgb(255,0,170);">" </span><span style="color: rgb(181,106,1);">+ </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">content</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(0,0,255);">Span</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'  11  '</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(0,0,255);">ImageSpan</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.startIcon'</span><span style="color: rgb(0,0,255);">))  </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">需开发者换成镂空的图</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'26vp'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'26vp'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">27</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
