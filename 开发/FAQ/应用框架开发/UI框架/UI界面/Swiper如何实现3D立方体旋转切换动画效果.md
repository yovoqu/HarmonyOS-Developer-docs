# Swiper如何实现3D立方体旋转切换动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-919

#### 问题现象

通常Swiper组件，提供平面滑动轮播显示的效果，如何通过Swiper组件实现对子组件3D立方体旋转切换动画效果？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/97ClRHuASkWB4B2kH_GkUQ/zh-cn_image_0000002628400290.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041143Z&HW-CC-Expire=86400&HW-CC-Sign=0E8A6FD2AE27CC28051A8392EF6429AE599DFB07E5C2087C759A4A70685992AC)

 
 

#### 背景知识

- [Swiper组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)：滑块视图容器组件，它提供了子组件滑动轮播显示的能力。
- [customContentTransition属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#customcontenttransition12)：用于实现自定义的过渡动画效果，该属性允许开发者通过回调函数动态控制轮播切换过程中的动画细节，特别是可结合进度参数进行精细化动画控制。
- [rotate属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)：主要用于设置组件的旋转，可使组件在以组件左上角为坐标原点的坐标系中进行旋转。其中，（x，y，z）指定一个矢量，作为旋转轴。旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。默认值：在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。

 
 

#### 解决方案
1. 给Swiper组件内的子组件设置旋转属性rotate。
```text
<span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperItemSlotParam</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<em>// </em><em><span style="color: rgb(128,128,128);">设置组件旋转</span></em>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rotate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">angle</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">angleList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">centerX</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">centerY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">centerZ</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">perspective</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

2. 给Swiper组件设置页面切换动画属性customContentTransition，在页面切换时逐帧触发回调，在回调中设置子组件的rotate属性值。
```text
<em>// </em><em><span style="color: rgb(128,128,128);">自定义</span><span style="color: rgb(128,128,128);">Swiper</span><span style="color: rgb(128,128,128);">页面切换动画</span></em>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customContentTransition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">页面移除视窗时超时</span><span style="color: rgb(128,128,128);">1000ms</span><span style="color: rgb(128,128,128);">下渲染树</span></em>
  <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperContentTransitionProxy</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">旋转角度</span></em>
    let <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'proxy.position===</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'proxy.index===</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// position</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面相对于</span><span style="color: rgb(128,128,128);">selectedIndex</span><span style="color: rgb(128,128,128);">对应页面的起始位置的移动比例，向左移动减小，向右移动增加。</span></em>
    if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当前页向左滑出或上一页向右滑入</span></em>
      <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">;</span>
   <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面的旋转中心轴为右侧边缘</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当前页向右滑出或下一页向左滑入</span></em>
      <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">;</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面的旋转中心轴为左侧边缘</span></em>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'0%'</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
   <em>   <span style="color: rgb(128,128,128);">// position</span><span style="color: rgb(128,128,128);">小于</span><span style="color: rgb(128,128,128);">-1</span><span style="color: rgb(128,128,128);">时表示向左完全滑出区域，大于</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">时表示向右完全滑出区域，重置角度</span></em>
      <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">修改</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页的旋转角</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">angleList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">angle</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
```

 
完整示例参考如下：
 
```json
<span style="color: rgb(181,106,1);">@Component</span>
<span style="color: rgb(181,106,1);">@Entry</span>
export struct <span style="color: rgb(0,0,255);">Swiper3D </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// Swiper</span><span style="color: rgb(128,128,128);">数据</span></em>
  private <span style="color: rgb(0,0,255);">swiperList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">=</span>
    <span style="color: rgb(0,0,255);">[</span>new <span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">模块</span><span style="color: rgb(255,0,170);">1'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'#4B48F7'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      new <span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">模块</span><span style="color: rgb(255,0,170);">2'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'#46B1E3'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">,</span>
      new <span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'</span><span style="color: rgb(255,0,170);">模块</span><span style="color: rgb(255,0,170);">3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">'#61CFBE'</span><span style="color: rgb(0,0,255);">)]</span>
  <span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
     <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">轮播网格</span></em>
      <span style="color: rgb(0,0,255);">Custom3DComponentPage</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">items</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperList</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">swiperItemSlotParam</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mySwiperItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">      }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义</span><span style="color: rgb(128,128,128);">3D</span><span style="color: rgb(128,128,128);">立方体旋转轮播项</span><span style="color: rgb(128,128,128);">UI</span><span style="color: rgb(128,128,128);">内容</span></em>
  <span style="color: rgb(181,106,1);">@Builder</span>
  <span style="color: rgb(0,0,255);">mySwiperItem</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MySwiperItem</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">24</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

export class <span style="color: rgb(0,0,255);">MySwiperItem </span><span style="color: rgb(255,0,170);">{</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">标题</span></em>
  <span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">颜色</span></em>
  <span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Color </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">title </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">title</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">colors </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">colors</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">Custom3DComponentPage </span><span style="color: rgb(255,0,170);">{</span>
  <em><span style="color: rgb(128,128,128);">// --------------------</span><span style="color: rgb(128,128,128);">暴露外部属性</span><span style="color: rgb(128,128,128);">----------------------------</span></em>
<em><span style="color: rgb(128,128,128);">  // </span><span style="color: rgb(128,128,128);">动画持续时间，默认</span><span style="color: rgb(128,128,128);">500ms</span></em>
  <span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">500</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否自动播放</span></em>
  <span style="color: rgb(0,0,255);">autoPlay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否循环播放</span></em>
  <span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">轮播数据</span></em>
  <span style="color: rgb(0,0,255);">items</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">轮播页插槽参数</span></em>
  <span style="color: rgb(181,106,1);">@BuilderParam </span><span style="color: rgb(0,0,255);">swiperItemSlotParam</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// --------------------</span><span style="color: rgb(128,128,128);">私有属性</span><span style="color: rgb(128,128,128);">----------------------------</span></em>
<em><span style="color: rgb(128,128,128);">  // </span><span style="color: rgb(128,128,128);">当前项下标</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">currentIndex</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
  <em>// </em><em><span style="color: rgb(128,128,128);">旋转角度列表</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">angleList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">[] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">旋转中心点列表</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">轮播控制器</span></em>
  private <span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SwiperController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Swiper</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperController</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">items</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">swiperItemSlotParam</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置组件旋转</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rotate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">z</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">angle</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">angleList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">centerX</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">centerY</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">'50%'</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">centerZ</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">perspective</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ESObject</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">item</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">_</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loop</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">autoPlay</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">autoPlay</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">duration</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">currentIndex </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义</span><span style="color: rgb(128,128,128);">Swiper</span><span style="color: rgb(128,128,128);">页面切换动画</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">customContentTransition</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
      <em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">页面移除视窗时超时</span><span style="color: rgb(128,128,128);">1000ms</span><span style="color: rgb(128,128,128);">下渲染树</span></em>
      <span style="color: rgb(0,0,255);">timeout</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SwiperContentTransitionProxy</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">旋转角度</span></em>
        let <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'proxy.position===</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'proxy.index===</span><span style="color: rgb(255,0,170);">></span><span style="color: rgb(255,0,170);">' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
       <em> <span style="color: rgb(128,128,128);">// position</span><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面相对于</span><span style="color: rgb(128,128,128);">selectedIndex</span><span style="color: rgb(128,128,128);">对应页面的起始位置的移动比例，向左移动减小，向右移动增加。</span></em>
        if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
          <em>// </em><em><span style="color: rgb(128,128,128);">当前页向左滑出或上一页向右滑入</span></em>
          <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">;</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面的旋转中心轴为右侧边缘</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0 </span><span style="color: rgb(181,106,1);">&</span><span style="color: rgb(181,106,1);">&</span> <span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">当前页向右滑出或下一页向左滑入</span></em>
          <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">position </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">90</span><span style="color: rgb(181,106,1);">;</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页面的旋转中心轴为左侧边缘</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">centerXList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'0%'</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
       <em>   <span style="color: rgb(128,128,128);">// position</span><span style="color: rgb(128,128,128);">小于</span><span style="color: rgb(128,128,128);">-1</span><span style="color: rgb(128,128,128);">时表示向左完全滑出区域，大于</span><span style="color: rgb(128,128,128);">1</span><span style="color: rgb(128,128,128);">时表示向右完全滑出区域，重置角度</span></em>
          <span style="color: rgb(0,0,255);">angle </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span>
       <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">修改</span><span style="color: rgb(128,128,128);">index</span><span style="color: rgb(128,128,128);">页的旋转角</span></em>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">angleList</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">proxy</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">index</span><span style="color: rgb(0,0,255);">] </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">angle</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
