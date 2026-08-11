# Swiper在末尾实现添加按钮

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1307

#### 问题现象

在Swiper最后一项的尾部设置一个添加按钮，并自定义按钮的大小。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/eD3bcx09SuG7eT1nx1-YMA/zh-cn_image_0000002628758912.png?HW-CC-KV=V1&HW-CC-Date=20260811T005751Z&HW-CC-Expire=86400&HW-CC-Sign=F82FAB0A0B0E2CBC10EAE8C23FF3A8E8EE0A0F1204A2481D0343A8F3AD93093D)

 
 

#### 背景知识

[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
 
- [scrollEdge](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrolledge)：设置滚动到容器的边缘位置。
- [onScrollStop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#onscrollstop9)：滚动停止时触发回调。
- [onDidScroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#ondidscroll12)：滚动事件回调，返回当前帧滚动的偏移量和当前滚动状态。

 
[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)：滑块视图容器，提供子组件滑动轮播显示的能力。其子组件默认填充满Swiper组件，滑动时为整页滑动，不受子组件宽高影响。
 
 

#### 解决方案

在外层使用Scroll组件，内部依次排列Swiper组件和添加按钮，设置Swiper优先滑动。当Swiper滑动到末尾时，继续滑动的为外层Scroll组件，显示出添加按钮。
 
- 在Scroll的滚动事件onDidScroll回调中，当Scroll的偏移量offset不为0时，设置Swiper不可滚动，当Scroll的偏移量为0时，重新设置Swiper可以滚动交互，以避免手指往回滑动Scroll时，Swiper也被滑动。
- 在Scroll的滚动停止onScrollStop回调中，根据手指滑动方向，设置Scroll滚动的边缘效果，以实现添加按钮跟随手指滑动的边缘对齐逻辑。

 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SwiperButtonDemo </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Scroller </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">Scroller</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">bgColors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">swiperEnable</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// Swiper</span><span style="color: rgb(128,128,128);">是否可交互</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">directionRight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">控制外层</span><span style="color: rgb(128,128,128);">Scroll</span><span style="color: rgb(128,128,128);">是否向右滑动</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Scroll</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">bgColors</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'24fp'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'16'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">enabled</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperEnable</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'25%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nestedScroll</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">SwiperNestedScrollMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SELF_FIRST</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// Swiper</span><span style="color: rgb(128,128,128);">优化</span><span style="color: rgb(128,128,128);">Scroll</span><span style="color: rgb(128,128,128);">滑动</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicator</span><span style="color: rgb(255,0,170);">(</span>
          <span style="color: rgb(255,255,255);">Indicator</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">dot</span><span style="color: rgb(255,0,170);">()</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedItemWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedItemHeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#FFFFFF'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">color</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#80ffffff'</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,0,170);">        )</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">itemSpace</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">6</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextMargin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">prevMargin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">effectMode</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">EdgeEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">None</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

        if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">bgColors</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">10</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">添加</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">bgColors</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">增加</span><span style="color: rgb(128,128,128);">Swiper</span><span style="color: rgb(128,128,128);">数据的数量</span></em>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">+= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(132,63,161);">'right'</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'10vp' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'16'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#F1F3F5'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'40vp' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollable</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ScrollDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Horizontal</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollBar</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">BarState</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Off</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onDidScroll</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">xOffset</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">xOffset </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">directionRight </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">xOffset </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">directionRight </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentOffset</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">xOffset </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperEnable </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperEnable </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onScrollStop</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">scroller</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scrollEdge</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">directionRight </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">Edge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Edge</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Top</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
