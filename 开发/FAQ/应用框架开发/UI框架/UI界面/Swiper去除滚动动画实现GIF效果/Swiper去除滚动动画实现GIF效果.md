# Swiper去除滚动动画实现GIF效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-562

#### 问题现象

如何消除Swiper的滚动动画，实现类似GIF动图的效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/NEAAGH0jSwO9yt8yS5qz-A/zh-cn_image_0000002628392130.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072439Z&HW-CC-Expire=86400&HW-CC-Sign=CE98704D52E8B198C230CAFCCD24E5928ECC1E4E1ABD51A303A8ED7B1BC3F271)

 
 

#### 背景知识

- [Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)是滑块视图容器，提供子组件滑动轮播显示的能力。
[duration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#duration)设置子组件切换的动画时长。curve默认曲线为[interpolatingSpring](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curvesinterpolatingspring10)，此时动画时长只受曲线自身参数影响，不受duration的控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。
- [curve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#curve8)设置Swiper的动画曲线，默认为弹簧插值曲线，常用曲线参考[Curve枚举说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#curve)。

 - [ImageAnimator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator)提供帧动画组件来实现逐帧播放图片的能力，可以配置需要播放的图片列表，每张图片可以配置时长。

 
 

#### 解决方案

- **方案一**：使用duration设置Swiper的切换动画时长为0，同时通过curve设置动画曲线为Linear，再设置Swiper自动切换图片，实现类似GIF图效果，可以通过interval设置每帧图片的展示时间，避免图片切换过快。
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SwiperGifDemo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceStr</span><span style="color: rgb(255,0,170);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">[]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">图片资源需自行替换</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.img1'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.img2'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.img3'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.img4'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">newsItem</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceStr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">newsItem</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">4 </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(80,160,79);">3</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">id</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Fill</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'12vp'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toString</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">autoPlay</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自动切换</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">indicator</span><span style="color: rgb(255,0,170);">(</span>false<span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">循环播放</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">动画时长</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">curve</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Linear</span><span style="color: rgb(255,0,170);">) </span><em>// </em><em><span style="color: rgb(128,128,128);">动画曲线</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">interval</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">300</span><span style="color: rgb(255,0,170);">) </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">切换时间间隔</span></em>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">disableSwipe</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">禁止滑动切换</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'12vp'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

- **方案二**：使用ImageAnimator播放图片集合，可以设置图片的播放时长和播放次数，实现类似GIF的效果。示例代码参考[播放Resource动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator#示例1播放resource动画)。
