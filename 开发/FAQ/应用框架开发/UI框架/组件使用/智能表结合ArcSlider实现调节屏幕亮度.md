# 智能表结合ArcSlider实现调节屏幕亮度

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-987

#### 问题现象

智能表为圆形屏幕的穿戴设备，如何在页面显示弧形滑动条，并通过滑动条调节屏幕亮度？
 
 

#### 背景知识

- [ArcSlider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcslider)：弧形滑动条组件，通常用于在圆形屏幕的穿戴设备中快速调节设置值，如音量调节、亮度调节等应用场景。
- [setWindowBrightness](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowbrightness9)：允许应用主窗口设置屏幕亮度值，使用callback异步回调，智能表应用也支持使用。

 
 

#### 解决方案
1. 添加ArcSlider组件实现弧形滑动条，[ArcSliderOptionsConstructorOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcslider#arcslideroptionsconstructoroptions)的onChange事件中把ArcSlider当前的进度值设置为屏幕亮度值。
2. 通过window实例提供的setWindowBrightness方法设置屏幕亮度。
 
完整示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">ArcSlider</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderValueOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderLayoutOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderStyleOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderValueOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderLayoutOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderStyleOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">ArcSliderOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,255,255);">window</span>
<span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">通过</span><span style="color: rgb(128,128,128);">window</span><span style="color: rgb(128,128,128);">实例提供的</span><span style="color: rgb(128,128,128);">setWindowBrightness()</span><span style="color: rgb(128,128,128);">方法，即可设置屏幕亮度。</span></em>
  <span style="color: rgb(0,0,255);">changeBrightness</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">brightness</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">promise </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getLastWindow</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,255,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setWindowBrightness</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">brightness</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          const <span style="color: rgb(255,255,255);">errCode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">;</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">errCode</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to set the Brightness value. Cause code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
            return<span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">exception</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to set the Brightness value. Cause code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">exception</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">exception</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

 <em> <span style="color: rgb(128,128,128);">// ArcSliderValueOptions</span><span style="color: rgb(128,128,128);">的构造信息，设置当前进度值、最小值和最大值</span></em>
  <span style="color: rgb(255,255,255);">valueOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderValueOptionsConstructorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">progress</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// ArcSliderLayoutValueOptions</span><span style="color: rgb(128,128,128);">的构造信息，设置弧形</span><span style="color: rgb(128,128,128);">Slider</span><span style="color: rgb(128,128,128);">从下往上滑动</span></em>
  <span style="color: rgb(255,255,255);">layoutOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderLayoutOptionsConstructorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">reverse</span><span style="color: rgb(181,106,1);">: </span>true
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
 <em> <span style="color: rgb(128,128,128);">// ArcSliderStyleOptions</span><span style="color: rgb(128,128,128);">的构造信息，设置弧形</span><span style="color: rgb(128,128,128);">Slider</span><span style="color: rgb(128,128,128);">的描边粗细、描边背景色、描边高亮色、描边背景模糊值</span></em>
  <span style="color: rgb(255,255,255);">styleOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderStyleOptionsConstructorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">trackThickness</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">activeTrackThickness</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">24</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">trackColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ffd5d5d5'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">selectedColor</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'#ff2787d9'</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">trackBlur</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">20</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">valueOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderValueOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArcSliderValueOptions</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">valueOptionsConstructorOptions</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">layoutOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderLayoutOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArcSliderLayoutOptions</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">layoutOptionsConstructorOptions</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">styleOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderStyleOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArcSliderStyleOptions</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">styleOptionsConstructorOptions</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">arcSliderOptionsConstructorOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderOptionsConstructorOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">valueOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">valueOptions</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">layoutOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">layoutOptions</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">styleOptions</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">styleOptions</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(255,255,255);">digitalCrownSensitivity</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">CrownSensitivity</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">HIGH</span><span style="color: rgb(181,106,1);">,</span>
<em>    <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">弧形</span><span style="color: rgb(128,128,128);">Slider</span><span style="color: rgb(128,128,128);">的进度值发生变化时触发</span></em>
    <span style="color: rgb(255,255,255);">onChange</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">progress</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">changeBrightness</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">progress</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

      let <span style="color: rgb(255,255,255);">windowClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Window </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(181,106,1);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">promise </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">window</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getLastWindow</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">promise</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">windowClass </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">data</span><span style="color: rgb(181,106,1);">;</span>
        try <span style="color: rgb(181,106,1);">{</span>
          let <span style="color: rgb(255,255,255);">properties </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">windowClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getWindowProperties</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(255,255,255);">bright </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">properties</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(255,255,255);">brightness </span><span style="color: rgb(181,106,1);">?? -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getPromptAction</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openToast</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">屏幕亮度值</span><span style="color: rgb(132,63,161);">: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">bright</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2000</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Failed to open Toast.'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to get the Window Properties. Cause code: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, message: </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">      }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">arcSliderOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ArcSliderOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">ArcSliderOptions</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arcSliderOptionsConstructorOptions</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">canIUse</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'SystemCapability.ArkUI.ArkUI.Circle'</span><span style="color: rgb(255,0,170);">)) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ArcSlider</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">options</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">arcSliderOptions </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
