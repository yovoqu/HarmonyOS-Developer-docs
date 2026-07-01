# 如何解决Scroll组件嵌套Web组件滑动冲突问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-567

#### 问题现象

当Scroll组件嵌套Web组件滑动时，滑动冲突，如何处理？
 
 

#### 背景知识

- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
- [ArkWeb](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview?ha_source=sousuo&ha_sourceId=89000251)：ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。
- [触摸测试控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)可以设置不同的触摸测试响应模式，影响组件的触摸测试收集结果，最终影响后续的触屏事件分发。

 
 

#### 解决方案

Web组件和Scroll组件在同一页面时，会存在Web获取焦点，导致Scroll无法上下滑动。
 
解决思路是可以通过设置边界调节来屏蔽其中一个的滑动响应来实现避免冲突的效果。
 
- **方案一**：屏蔽Web响应。可以在Scroll的onWillScroll事件中增加判断，在Scroll滑动到底部之前屏蔽所有Web响应，不过需要注意的是，如果Web本身也需要滑动的话，该方法不太适用，这种场景下可以使用方案二来处理冲突。

  
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillScroll</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isAtEnd</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`webEnable: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`webEnable: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/XXyYpdT4Q4ebLDoe5b1Aeg/zh-cn_image_0000002658911361.png?HW-CC-KV=V1&HW-CC-Date=20260701T041315Z&HW-CC-Expire=86400&HW-CC-Sign=590930F36CA36DAAECEF1AA531413B33172AE5E3A064B14269E134F71E4C5683)

- **方案二**：触摸事件传递。可以使用触摸测试控制来规避此种情况，请给显示在上层的节点设置hitTestBehavior为HitTestMode.Transparent。详情见[参考文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)。

  
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。</span></em>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2Sq-MCe2RNSWGVKI62BiOg/zh-cn_image_0000002628392144.png?HW-CC-KV=V1&HW-CC-Date=20260701T041315Z&HW-CC-Expire=86400&HW-CC-Sign=72F5FE9DF052FCE6424D4A6EEBC922E07939BF8E96A5A4712A2E92B7BAC49288)

- **方案三**：调整嵌套滚动模式。在嵌套滚动组件时，可以通过设置“nestedScroll”属性来控制滚动顺序。

  
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">scrollForward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">向前滚动父容器优先</span></em>
  <span style="color: rgb(0,0,255);">scrollBackward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">向后滚动子组件优先</span></em>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Vdr1_x9jSoeu1DbzDH5sgQ/zh-cn_image_0000002658791425.png?HW-CC-KV=V1&HW-CC-Date=20260701T041315Z&HW-CC-Expire=86400&HW-CC-Sign=564CE307A8D4931A0578A4A2268DC70AC36EDB9E467E2256C2D418E1B98EE9E2)


 
完整示例代码如下：
 
ArkTS页面代码：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution1 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需根据需求替换</span><span style="color: rgb(128,128,128);">src</span></em>
          <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ScrollWeb.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">150</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onWillScroll</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isAtEnd</span><span style="color: rgb(0,0,255);">()) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`webEnable: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`webEnable: </span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webEnable</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution2 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需根据需求替换</span><span style="color: rgb(128,128,128);">src</span></em>
          <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ScrollWeb.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">150</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">hitTestBehavior</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HitTestMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Transparent</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。</span></em>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Solution3 </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">webController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
         <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开发者需根据需求替换</span><span style="color: rgb(128,128,128);">src</span></em>
          <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$rawfile</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'ScrollWeb.html'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">webController</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">scrollForward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">向前滚动父容器优先</span></em>
            <span style="color: rgb(0,0,255);">scrollBackward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST </span><em>// </em><em><span style="color: rgb(128,128,128);">向后滚动子组件优先</span></em>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">150</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#F1F3F5'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">TabsExample </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#182431'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">selectedFontColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'#007DFF'</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">selectedIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TabsController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TabsController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">name</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedFontColor </span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">500 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">22</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">17</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">7 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">Divider</span><span style="color: rgb(0,0,255);">()</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#007DFF'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">opacity</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">barPosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BarPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Solution1</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Solution2</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>

        <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Solution3</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">方案</span><span style="color: rgb(255,0,170);">3'</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
    <em>  <span style="color: rgb(128,128,128);">//.vertical(false)</span></em>
<em><span style="color: rgb(128,128,128);">      //.barMode(BarMode.Fixed)</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barWidth</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">360</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">barHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">56</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animationDuration</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
       <em> <span style="color: rgb(128,128,128);">// currentIndex</span><span style="color: rgb(128,128,128);">控制</span><span style="color: rgb(128,128,128);">TabContent</span><span style="color: rgb(128,128,128);">显示页签</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAnimationStart</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">targetIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TabsAnimationEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">targetIndex</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          return<span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`event currentOffset </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentOffset</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <em>  <span style="color: rgb(128,128,128);">// selectedIndex</span><span style="color: rgb(128,128,128);">控制自定义</span><span style="color: rgb(128,128,128);">TabBar</span><span style="color: rgb(128,128,128);">内</span><span style="color: rgb(128,128,128);">Image</span><span style="color: rgb(128,128,128);">和</span><span style="color: rgb(128,128,128);">Text</span><span style="color: rgb(128,128,128);">颜色切换</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">targetIndex</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">expandSafeArea</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(0,0,255);">SafeAreaType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SYSTEM</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">TOP</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">SafeAreaEdge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">BOTTOM</span><span style="color: rgb(0,0,255);">])</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
html页面代码：
 
```text
<em><!-- index.html --></em>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .lightgray {
          background-color: #D1D1D6;
        }
        .midgray {
          background-color: #C7C7CC;
        }
        .lightgray, .midgray {
         font-size:16px;
         height:200px;
         text-align: center;   <em>    /* 水平居中 */</em>
         line-height: 200px;      <em> /* 垂直居中（值等于容器高度） */</em>
        }
    </style>
</head>
<body>
<div class="lightgray" >webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
<div class="midgray">webArea</div>
<div class="lightgray">webArea</div>
</body>
</html>
```
 
 

#### 总结

当两个可响应滑动的组件（如Web和Scroll）共存时，可能出现焦点抢占导致某一组件无法滑动的问题。
 
通过控制组件的交互响应优先级，避免冲突，主要有三类方案：
 1. 动态启用/禁用组件响应：根据外部条件（如滚动位置）切换组件的交互状态，在需要某一组件响应时，禁用另一组件。

  例：Scroll未滑到底部时禁用Web的交互，滑到底部后再启用Web。
2. 控制触摸事件传递：通过设置组件的触摸测试行为（如hitTestBehavior），自身和子节点均响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。

  例：给Scroll设置hitTestBehavior属性为HitTestMode.Transparent，使自身和子节点均可响应。
3. 自定义滚动优先级：为嵌套的滚动组件配置滚动顺序规则（如nestedScroll），明确父/子组件的滚动优先级，按规则依次响应。

  例：向前滚动时父组件优先，向后滚动时子组件优先。
