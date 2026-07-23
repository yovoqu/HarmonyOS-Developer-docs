# Swiper如何实现惯性滚动效果

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1512

#### 问题现象

Swiper组件在滑动时只能一次滚动一页，在需要一次滑动多个页面的场景下效率较低，Swiper组件如何实现惯性滚动效果，提高滑动效率？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/FirrMhCdSSKQurRC15Xcaw/zh-cn_image_0000002658845805.png?HW-CC-KV=V1&HW-CC-Date=20260723T012759Z&HW-CC-Expire=86400&HW-CC-Sign=DFAEB380943AD604721F06F797A8D5447D002A93C1C54E00933BD7D8A079BCAC)

 
 

#### 背景知识

- [parallelGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding#parallelgesture并行手势绑定方法)：parallelGesture是并行的手势绑定方法，在父子组件上绑定可以同时响应的相同手势。
- [changeIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#changeindex15)：Swiper翻页至指定页面。

 
 

#### 解决方案

方案逻辑：向后翻动几页；如果抬手时速度小于设置的值，则保持原来每次翻一页的效果。通过以上逻辑实现快速滑动Swiper时，可以惯性向后翻几页。
 
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parallelGesture</span><span style="color: rgb(255,0,170);">( </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">同步手势</span></em>
  <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(255,0,170);">()</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手势结束，获取当前的速度</span></em>
      let <span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeIndex</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">SwiperAnimationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FAST_ANIMATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeIndex</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">SwiperAnimationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FAST_ANIMATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,0,170);">)</span>
```
 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Swiper1 </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SwiperController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SwiperController</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(132,63,161);">'1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'4'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'5'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'6'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'7'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'8'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'9'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'10'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(132,63,161);">'11'</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(255,255,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">160</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(0xf1f3f5)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">textAlign</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">TextAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">12</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">cachedCount</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicator</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">itemSpace</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">5</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Friction</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">prevMargin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">35</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">nextMargin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">35</span><span style="color: rgb(181,106,1);">, </span>true<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">parallelGesture</span><span style="color: rgb(255,0,170);">( </span><em>// </em><em><span style="color: rgb(128,128,128);">同步手势</span></em>
        <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(255,0,170);">()</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionEnd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">e </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">手势结束，获取当前的速度</span></em>
            let <span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">|| </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeIndex</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">SwiperAnimationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FAST_ANIMATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">velocityX </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);"> -</span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">swiperController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeIndex</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">currentIndex </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">2</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">SwiperAnimationMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">FAST_ANIMATION</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(255,0,170);">      )</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
 

#### 常见FAQ

Q：如何实现自定义组件滑动时的惯性效果？
 
A：与解决方案同理，使用PanGesture手势即可实现惯性滑动效果，具体可以参考示例[如何通过PanGesture手势或者SwipeGesture手势实现自定义组件的惯性滚动效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-33)。
