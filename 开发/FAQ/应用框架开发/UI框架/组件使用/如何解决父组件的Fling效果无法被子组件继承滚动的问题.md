# 如何解决父组件的Fling效果无法被子组件继承滚动的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1643

#### 问题现象

父组件为Scroll组件，其子组件包含一个List组件，且位于Scroll组件底部。当滑动触点在Scroll组件内容区域进行快速滑动，滚动到底部List组件位置的时，位于底部的List组件无法继承父组件的剩余滚动速度，进行完整的惯性滚动。
 
滑动前效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Y87GJ_nlTEi1s0wGdTVDfw/zh-cn_image_0000002628821082.png?HW-CC-KV=V1&HW-CC-Date=20260701T041318Z&HW-CC-Expire=86400&HW-CC-Sign=0E9A08F55C33B8041C112EAB16E95DF1D5B48865FE2E50DC93454C7D20F4A04C)

 
滑动后效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/wIfIOJkxSQmWj3K2puR8Jg/zh-cn_image_0000002659020395.png?HW-CC-KV=V1&HW-CC-Date=20260701T041318Z&HW-CC-Expire=86400&HW-CC-Sign=569E7E44E0DB2D82C0218E405472C6591C7BD9807E4F691DFB56CB07E367E998)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/HU0qMfZ2Sbu-01xEieowvQ/zh-cn_image_0000002628661192.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041318Z&HW-CC-Expire=86400&HW-CC-Sign=E534F6F14F401539FF76D696B21554E20F5285B69C15EA2F95AC34DEEFC6854C)

 
 

#### 背景知识

Fling效果，又被称为惯性滚动，是在App中的常见交互设计。在[List组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)中，有如下方法：
 
- [edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#edgeeffect)：用于设置边缘滑动效果。List组件默认为EdgeEffect.Spring（惯性滚动），Scroll组件默认为EdgeEffect.None（无效果）。
- [nestedScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#nestedscroll10)：用于设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。
- [onScrollFrameBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list#onscrollframebegin9)：每帧开始滚动时触发，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

 
 

#### 问题定位

如果只是简单的进行可滚动容器组件的嵌套，那么当父级Scroll组件滚动到底部List组件时，子级List组件会视为Scroll组件的一部分，跟随Scroll组件进行整体滚动，那么就无法实现子组件继承父组件组件的惯性滚动的剩余速度。
 
 

#### 分析结论

实现子组件继承父组件组件的惯性滚动的剩余速度思路如下：
 1. 首先设置组件的边缘滑动效果为惯性滚动，即[EdgeEffect.Spring](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#edgeeffect)。
2. 在父级组件onScrollStart，onScrollStop事件中记录父级组件的滚动状态。
3. 在父级组件onTouch事件中记录上下滑动的方向。
4. 在父级组件onScrollFrameBegin进行剩余滚动量的计算，并通过子组件Scroller控制器，按照剩余滚动量计算值视情况进行滚动，同时返回最终计算后父级组件的实际滚动量。
 
 

#### 修改建议

根据定位思路，Fling效果继承滚动的主要实现代码如下，代码中附加一部分顶部tabbar吸顶逻辑：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">StickyNestedScroll </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义状态变量，用于存储列表数据。</span></em>
  private <span style="color: rgb(0,0,255);">touchDown</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">listTouchDown</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">scrolling</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">listScroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">CONTENT_HEIGHT </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">400</span><span style="color: rgb(181,106,1);">;</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">定义样式类</span><span style="color: rgb(128,128,128);">listCard</span><span style="color: rgb(128,128,128);">，用于统一</span><span style="color: rgb(128,128,128);">ListItem</span><span style="color: rgb(128,128,128);">样式。</span></em>
  <span style="color: rgb(181,106,1);">@Styles</span>
  <span style="color: rgb(0,0,255);">listCard</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">72</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    for <span style="color: rgb(0,0,255);">(</span>let <span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">30</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">i</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Scroll Area'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTENT_HEIGHT</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'# 0080DC'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Tabs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">barPosition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BarPosition</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Start </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listScroller </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
             <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">使用</span><span style="color: rgb(128,128,128);"> ForEach</span><span style="color: rgb(128,128,128);">遍历</span><span style="color: rgb(128,128,128);">arr</span><span style="color: rgb(128,128,128);">数组生成列表项。</span></em>
              <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">arr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
                  <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'item' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span>
                    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">16</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listCard</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">应用</span><span style="color: rgb(128,128,128);">listCard</span><span style="color: rgb(128,128,128);">样式。</span></em>
              <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Spring</span><span style="color: rgb(0,0,255);">)</span>
           <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置嵌套滚动模式。</span></em>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">scrollForward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PARENT_FIRST</span><span style="color: rgb(181,106,1);">,</span>
              <span style="color: rgb(0,0,255);">scrollBackward</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">NestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SELF_FIRST</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TouchEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listTouchDown </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Up</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listTouchDown </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Tab One'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

          <span style="color: rgb(0,0,255);">TabContent</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
<span style="color: rgb(255,0,170);">          }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">tabBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Tab Two'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">vertical</span><span style="color: rgb(0,0,255);">(</span>false<span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onTouch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TouchEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Down</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touchDown </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(0,0,255);">TouchType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Up</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touchDown </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义滚动帧开始时的处理逻辑。</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollFrameBegin</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果正在滚动且偏移量大于</span><span style="color: rgb(128,128,128);">0</span><span style="color: rgb(128,128,128);">（向下滚动）。</span></em>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrolling </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        let <span style="color: rgb(0,0,255);">yOffset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentOffset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">yOffset</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">获取当前滚动偏移量。</span></em>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">yOffset </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTENT_HEIGHT</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listScroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offsetRemain</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
      <em>  <span style="color: rgb(128,128,128);">// </span></em><em>如果滚动将超过内容区域底部。</em>
        else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">yOffset </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTENT_HEIGHT</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listScroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBy</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">yOffset </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">- </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTENT_HEIGHT</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          return <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offsetRemain</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CONTENT_HEIGHT </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">yOffset </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">返回原始偏移量。</span></em>
      return <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">offsetRemain</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollStart</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">如果父</span><span style="color: rgb(128,128,128);">Scroll</span><span style="color: rgb(128,128,128);">被触摸且</span><span style="color: rgb(128,128,128);">List</span><span style="color: rgb(128,128,128);">未被触摸，则标记为正在滚动。</span></em>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">touchDown </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);"> !</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">listTouchDown</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrolling </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollStop</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrolling </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">edgeEffect</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Spring</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'#DCDCDC'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Off</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结
1. 通过父组件的onScrollFrameBegin事件，可以明确的知道组件即将发生的滑动量，并根据需要计算实际需要的滑动量，作为返回值返回。
2. 再结合onTouch，onScrollStart等事件，收集具体的滑动行为。
3. 最后通过滚动组件的Scroll控制器，触发惯性滑动效果。
