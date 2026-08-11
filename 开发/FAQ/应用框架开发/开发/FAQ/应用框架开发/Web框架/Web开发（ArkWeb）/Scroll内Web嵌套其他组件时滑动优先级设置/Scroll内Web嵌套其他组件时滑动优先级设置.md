# Scroll内Web嵌套其他组件时滑动优先级设置

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-170

#### 问题现象

Scroll内Web组件头尾存在其他组件时，头部组件只有在Web内容滑动至顶部时才显示，尾部组件只有在Web内容滑动至底部时才显示。
 
 

#### 背景知识

- [onVisibleAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event#onvisibleareachange)：组件可见区域变化时触发该回调。
- [nestedScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common#nestedscroll11)设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

 
 

#### 解决方案

通过给头尾组件设置onVisibleAreaChange可见区域变化回调：当头部组件或尾部组件可见时，设置Web的滑动优先级为父组件先滚动；当头部组件或尾部组件不可见时，设置Web的滑动优先级为自身先滚动。
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">webview </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkWeb'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ScrollerDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">webview</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">WebviewController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">scrollMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">标题</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">600</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">lineHeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">23</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'90%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">24 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
     <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断可见区域变化</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onVisibleAreaChange</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isExpanding</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">currentRatio</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isExpanding </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">currentRatio </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可见时，设置</span><span style="color: rgb(128,128,128);">Web</span><span style="color: rgb(128,128,128);">的滑动优先级为父组件先滚动</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">isExpanding </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">currentRatio </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">不可见时，设置</span><span style="color: rgb(128,128,128);">Web</span><span style="color: rgb(128,128,128);">的滑动优先级为自身先滚动</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>

        <span style="color: rgb(0,0,255);">Web</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处</span><span style="color: rgb(128,128,128);">'www.example.com'</span><span style="color: rgb(128,128,128);">仅作示例。</span></em>
          <span style="color: rgb(0,0,255);">src</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'www.example.com'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">controller</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fileAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">geolocationAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">domStorageAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">javaScriptAccess</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zoomAccess</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">scrollForward</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(0,0,255);">scrollBackward</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">阅读量：</span><span style="color: rgb(255,0,170);">  12345`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">End</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">VerticalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
        <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">判断可见区域变化</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onVisibleAreaChange</span><span style="color: rgb(0,0,255);">([</span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">1.0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isExpanding</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">currentRatio</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isExpanding </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">currentRatio </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em>     <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">可见时，设置</span><span style="color: rgb(128,128,128);">Web</span><span style="color: rgb(128,128,128);">的滑动优先级为父组件先滚动</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>

          if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(181,106,1);">!</span><span style="color: rgb(0,0,255);">isExpanding </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">currentRatio </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0.0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
         <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">不可见时，设置</span><span style="color: rgb(128,128,128);">Web</span><span style="color: rgb(128,128,128);">的滑动优先级为自身先滚动</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollMode </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">14</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">14</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
