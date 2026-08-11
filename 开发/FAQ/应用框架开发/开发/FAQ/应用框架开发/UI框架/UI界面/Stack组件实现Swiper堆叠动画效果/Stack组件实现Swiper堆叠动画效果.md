# Stack组件实现Swiper堆叠动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-561

#### 问题现象

Swiper如何实现卡片堆叠样式：
 
- 上下堆叠：Swiper内容像卡片堆叠，在底部留部分空间显示下一页的内容，上下滑实现卡片切换。
- 左右堆叠：Swiper内容像卡片堆叠，在右侧留部分空间显示下一页的内容，左右滑实现卡片切换。

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-looping)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。
- [Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)是堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
- [gesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings#gesture)可以为组件绑定手势方法进行相应处理，如滑动手势事件[PanGesture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture)。
- [animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)指定由于闭包代码导致的状态变化插入过渡动效。

 
 

#### 解决方案

- **上下堆叠实现。**自定义实现卡片堆叠的组件：使用Stack组件堆叠需要展示的图片，设置最上面的图片向上偏移部分距离，露出下一张图片的底部。为Stack绑定上下滑动的手势处理，实现切换图片逻辑，同时使用animateTo接口设置图片切换动画。

  
```text
export class <span style="color: rgb(0,0,255);">SwiperData </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Resource</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">SwiperStackComponent </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@Link </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Prop </span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">halfCount</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">floor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3 </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">2</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">automaticSlidingDuration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">300</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em>// </em><em><span style="color: rgb(128,128,128);">修改堆叠方向系数计算</span></em>
  <span style="color: rgb(0,0,255);">getImgCoefficients</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    const <span style="color: rgb(0,0,255);">coefficient </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">tempCoefficient </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">coefficient</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tempCoefficient </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">halfCount</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return <span style="color: rgb(0,0,255);">coefficient</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    const <span style="color: rgb(0,0,255);">dataLength </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">tempOffset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">dataLength </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">tempCoefficient</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tempOffset </span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">halfCount</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      return <span style="color: rgb(0,0,255);">coefficient </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">? -</span><span style="color: rgb(0,0,255);">tempOffset </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">tempOffset</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">修改堆叠方向偏移量计算</span></em>
  <span style="color: rgb(0,0,255);">getOffSet</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">offsetIndex </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImgCoefficients</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    const <span style="color: rgb(0,0,255);">tempOffset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abs</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">offsetIndex</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    let <span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tempOffset </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">offsetIndex </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">offsetIndex </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(0,0,255);">offset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">50 </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(0,0,255);">offsetIndex</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    return <span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">startAnimation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">isLeft</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      const <span style="color: rgb(0,0,255);">dataLength</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(181,106,1);">;</span>
      const <span style="color: rgb(0,0,255);">tempIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">isLeft </span><span style="color: rgb(181,106,1);">? </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,0,0);">1 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">dataLength</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">tempIndex </span><span style="color: rgb(181,106,1);">% </span><span style="color: rgb(0,0,255);">dataLength</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Cover</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getOffSet</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">shadow</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ShadowStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OUTER_DEFAULT_SM</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">blur</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">!== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">12 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">animateTo</span><span style="color: rgb(128,128,128);">实现动画并且同时改变</span><span style="color: rgb(128,128,128);">currentIndex</span><span style="color: rgb(128,128,128);">数据中间值来判断组件</span><span style="color: rgb(128,128,128);">zIndex</span><span style="color: rgb(128,128,128);">实现切换动画</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">zIndex</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">!== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImgCoefficients</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,0,0);">0 </span>?
          <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">2 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">abs</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getImgCoefficients</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">310</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index </span><span style="color: rgb(181,106,1);">!== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,0,0);">130 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">180</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">200</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
      <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PanDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Vertical </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionStart</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAnimation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetY </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">automaticSlidingDuration</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">    )</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">12 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 在页面中直接使用上面封装好的SwiperStackComponent即可，示例如下：传给SwiperStackComponent要堆叠的图片。

  
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">StackSwiperDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">图片资源需自行配置</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[</span>
    new <span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.img1'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.img2'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">SwiperData</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'app.media.img3'</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">SwiperStackComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperData</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MDjGkCXwTPSS8uRCndGLug/zh-cn_image_0000002628552022.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005647Z&HW-CC-Expire=86400&HW-CC-Sign=D148749A7AED5646EF800FB65538A8643826B4CD83D5EB427B970D67984A3101)


 
- **左右堆叠实现。**和上下堆叠实现类似，只需微调SwiperStackComponent代码即可。

1. 将内层Stack在Y方向上的偏移改为X方向上的偏移。
```text
<span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Bottom </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imageSrc</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Cover</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">8</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getOffSet</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">偏移改为</span><span style="color: rgb(128,128,128);">X</span><span style="color: rgb(128,128,128);">方向上的偏移</span></em>
```


2. 外层Stack的滑动手势改为左右滑动，动画效果改为X方向上的判断。
```text
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">gesture</span><span style="color: rgb(0,0,255);">(</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">滑动手势改为左右滑动</span></em>
  <span style="color: rgb(0,0,255);">PanGesture</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">direction</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">PanDirection</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Horizontal </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onActionStart</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">GestureEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">改成</span><span style="color: rgb(128,128,128);">X</span><span style="color: rgb(128,128,128);">轴方向判定</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">startAnimation</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offsetX </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">automaticSlidingDuration</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(0,0,255);">)</span>
```


3. 由于屏幕X方向比Y方向要窄，可以修改getOffSet函数改变偏移的距离。
```text
<span style="color: rgb(255,255,255);">offset </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">20 </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,255,255);">offsetIndex</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">改变偏移的距离</span></em>
```


  效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/VXw9uYg-TGGFtErOCrDlPA/zh-cn_image_0000002658911343.gif?HW-CC-KV=V1&HW-CC-Date=20260811T005647Z&HW-CC-Expire=86400&HW-CC-Sign=53F4310E61997B7D6AB5A176A5111CD584E01D1BCC914AEC669835E3E6DAB733)


 
> [!NOTE]
> 堆叠方向的偏移量可根据需求，通过修改自定义组件SwiperStackComponent的getImgCoefficients函数和getOffSet函数来调整。
