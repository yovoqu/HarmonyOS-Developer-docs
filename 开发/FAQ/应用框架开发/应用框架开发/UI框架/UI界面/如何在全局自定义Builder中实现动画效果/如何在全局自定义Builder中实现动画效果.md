# 如何在全局自定义Builder中实现动画效果

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1009

#### 问题现象

在全局自定义Builder函数中，通过修改组件的属性，如何实现动画效果？问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">bottomViewBuilder</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.start_branding_light_icon'</span><span style="color: rgb(255,0,170);">))</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">150</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'bottomRectHeight'</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.color.background_color_level2'</span><span style="color: rgb(255,0,170);">))</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowWidth</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">windowHeight </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">adHeight</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Linear</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(255,0,170);">)</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
以上代码中windowWidth、windowHeight、adHeight为全局变量，当全局变量修改时，无法触发动画效果。
 
 

#### 背景知识

- [实现属性动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-animation-apis)：通过可动画属性改变引起UI上产生的连续视觉效果，即为属性动画。属性动画是最基础易懂的动画，ArkUI提供三种动画接口[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)、[animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty#animation)和[keyframeAnimateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto)驱动组件属性按照动画曲线等动画参数进行连续的变化，产生属性动画。
- [Builder函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)：该函数分为[全局自定义构建函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#全局自定义构建函数)和[私有自定义构建函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#私有自定义构建函数)两种形式，全局函数调用时，无法直接通过this指针调用父组件的状态变量，必须通过传参的方式调用@Component父组件内声明的状态变量。同时，如果@Builder传入的参数是两个或两个以上，不会触发动态渲染UI，也就不会触发动画渲染。

 
 

#### 解决方案

- **方案一**：采用animateTo的方式实现全局自定义构建函数的动画效果。1. 由于Builder函数的参数限制，若需实现由多个参数触发的动画效果，建议将多个参数封装为可深度观测的类，通过[@Observed/@ObjectLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)、[@ObservedV2/@Trace](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)修饰类，实现深度观测，并传递至Builder内。

2. 将传递的参数绑定可动画的属性，即可在属性修改时触发动画效果。

3. 在animateTo内绑定动画的参数，并修改可动画的属性。

  
```text
<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">bottomViewBuilderOne</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimatesOne</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">150</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'bottomRectHeight'</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowWidth</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowHeight </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">adHeight</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">动画属性只支持状态变量的修改，同时由于</span><span style="color: rgb(128,128,128);">Builder</span><span style="color: rgb(128,128,128);">的传参限制，建议封装为一个可深度观测的类</span></em>
class <span style="color: rgb(0,0,255);">AnimatesOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">windowWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">windowHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">adHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">OptionOne </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimatesOne </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AnimatesOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始动画</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Linear</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">onFinish</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'play end'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">;</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">adHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">bottomViewBuilderOne</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```

- **方案二**：采用animation属性动画，实现方式与方案一类似，将方案一的步骤3的动画参数绑定在animation内。
```text
<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">bottomViewBuilderTwo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimatesTwo</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">150</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">bottom</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">AppStorage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">get</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'bottomRectHeight'</span><span style="color: rgb(255,0,170);">) </span>as <span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowWidth</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowHeight </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">adHeight</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">3000</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Curve</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Linear</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onAppear</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

class <span style="color: rgb(0,0,255);">AnimatesTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">windowWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">windowHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Track </span><span style="color: rgb(255,255,255);">adHeight</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">OptionTwo </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">AnimatesTwo </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AnimatesTwo</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">开始动画</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">windowWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">200</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">adHeight </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">bottomViewBuilderTwo</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">simple</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 效果预览：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/07aaHNNOSW2jy-qOkLmbpg/zh-cn_image_0000002658804043.png?HW-CC-KV=V1&HW-CC-Date=20260811T005701Z&HW-CC-Expire=86400&HW-CC-Sign=1BB88BF09B7392CA486E8371092C6457F214B1029B1CB4A952A4B05EE6847459)


  由于全局自定义函数的Builder的父容器Column组件没有设置宽高限制，导致Column组件自适应子组件大小，所以Text组件也跟随移动。
