# Scroll滚动到顶/底部后，下/上拖执行自定义方法

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-839

#### 问题现象

Scroll滚动到顶部时继续下拖和滚动到底部时继续上拖，如何执行自定义方法？
 
 

#### 背景知识

- [Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
[currentOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#currentoffset)获取Scroll当前的偏移量。
- [isAtEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#isatend10)查询Scroll是否滚动到底部。

 - [PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)可以为组件绑定滑动手势事件，其中手势回调的event.offsetY在从上向下滑动为正，反之为负。

 
 

#### 解决方案

使用PanGesture为Scroll绑定平移事件，在滑动结束即onActionEnd中判断Scroll位置以进行相应处理。
 
- Scroll滑到顶部继续下拖判断：
调用currentOffset获取Scroll当前位置，若Y方向小于等于0，则已滑至顶部。
- 通过onActionEnd的event判断是否继续下拖，若event.offsetY大于0表示继续下拖，则执行自定义操作。

 - Scroll滑到底部继续上拖判断：
调用isAtEnd判断Scroll是否已滑至底部。
- 通过onActionEnd的event判断是否继续上拖，若event.offsetY小于0表示继续上拖，则执行自定义操作。

 
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">ScrollDemo </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">panOption</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">PanGestureOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">PanGestureOptions</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PanDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Vertical </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">scrollerForScroll</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scrollerForScroll</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">此处</span><span style="color: rgb(128,128,128);">'app.media.startIcon'</span><span style="color: rgb(128,128,128);">仅作示例</span></em>
        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">size</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">400</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1050 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Spring</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parallelGesture</span><span style="color: rgb(255,0,170);">(</span>
        <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">panOption</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">GestureEvent</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'PanGesture end'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动到底部并且继续滑动</span></em>
            if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scrollerForScroll</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isAtEnd</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetY </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">执行自定义操作</span><span style="color: rgb(132,63,161);">1'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
         <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动到顶部并且继续滑动</span></em>
            const <span style="color: rgb(255,255,255);">offsetRes </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scrollerForScroll</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentOffset</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取</span><span style="color: rgb(128,128,128);">Scroll</span><span style="color: rgb(128,128,128);">现在的位置</span></em>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">offsetRes</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">yOffset </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(255,255,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offsetY </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">执行自定义操作</span><span style="color: rgb(132,63,161);">2'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">GestureMask</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
