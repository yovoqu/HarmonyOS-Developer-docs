# 如何解决Scroll组件嵌套Web组件后无法跟随页面整体滚动的问题

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-132

#### 问题现象

在Scroll组件内嵌套使用Web组件和其他容器组件的组合时，嵌套布局如下：
 
```text
<span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{}</span>
  <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{}</span>
  <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{}</span>
  <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
Web组件显示不全或只能单独滚动，无法实现与Row、List等组件连为一个整体进行滚动。
 
 

#### 背景知识

- [layoutMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#layoutmode11)：设置Web布局模式。当属性没有显式调用时，默认Web布局跟随系统模式。
- [RenderMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#rendermode12)：定义Web组件的渲染方式，默认为异步渲染模式。建议使用异步渲染模式，异步渲染模式有更好的性能和更低的功耗。

 
 

#### 问题定位

从问题现象可以看出当前有两种状态：Web组件会单独滚动以及内容显示不全。
 
分析两种状态的原因：
 1. Web组件单独滚动是因为固定了组件的高度，且该高度小于内容高度。
2. Web组件内容显示不全是因为在第1点的基础上禁止了Web的滚动。
 
 

#### 分析结论

问题的关键在于如何控制Web组件的高度，让其可以适应内容高度，从而将Web变成一个完全展开的view。
 
 

#### 解决方案

通过设置layoutMode属性为WebLayoutMode.FIT_CONTENT让Web自适应内容高度。
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">webview </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">WebFit </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">webviewController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(255,255,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">测试顶部</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">网页内容过宽或者过长时需要设置为</span><span style="color: rgb(128,128,128);">RenderMode.SYNC_RENDER</span></em>
        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'test.html'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">webviewController</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">renderMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">RenderMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SYNC_RENDER </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">metaViewport</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">WebLayoutMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FIT_CONTENT</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">Web</span><span style="color: rgb(128,128,128);">组件高度进行自适应</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">overScrollMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">OverScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">NEVER</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭过界回弹效果</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zoomAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">关闭手势缩放</span></em>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">测试底部</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'30%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Gray</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
```text
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">!DOCTYPE </span><span style="color: rgb(128,128,128);">html</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">html</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">head</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">charset</span><span style="color: rgb(80,160,79);">="UTF-8"</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">meta </span><span style="color: rgb(128,128,128);">name</span><span style="color: rgb(80,160,79);">="viewport" </span><span style="color: rgb(128,128,128);">content</span><span style="color: rgb(80,160,79);">="width=device-width, initial-scale=1, user-scalable=no"</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">title</span><span style="color: rgb(181,106,1);">></span>Fit-Content<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/title</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/head</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">body</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
    <span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">p</span><span style="color: rgb(181,106,1);">></span>这就是一个测试话题。<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/p</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/body</span><span style="color: rgb(181,106,1);">></span>
<span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">/html</span><span style="color: rgb(181,106,1);">></span>
```
 
 

#### 总结

通过layoutMode属性使Web组件的大小根据页面内容自适应变化，当Web页面宽高超过7680px（物理像素），建议设置渲染模式为同步渲染：renderMode: RenderMode.SYNC_RENDER。
