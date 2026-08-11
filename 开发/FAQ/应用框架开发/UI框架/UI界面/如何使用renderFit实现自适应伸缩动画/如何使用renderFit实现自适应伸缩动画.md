# 如何使用renderFit实现自适应伸缩动画

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-596

#### 问题现象

在animateTo动画中，给组件添加了renderFit属性后，组件宽高也没有跟随动画实时宽高变化。希望在宽度变化时，音乐+滑动条+人声这一个Row的宽度实时变化，请问该如何实现？
 
 

#### 背景知识

- HarmonyOS提供[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。
- [renderFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-renderfit#renderfit)用于设置宽高动画过程中的组件内容填充方式，当不设置renderFit属性时，取默认值RenderFit.TOP_LEFT。
- [clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)通用属性可用于对组件进行裁剪、遮罩处理。

 
 

#### 解决方案
1. 使用@State定义透明度，布局宽度，圆角大小等状态变量，这些变量在用户交互或者动画过程中会被更新，从而更新动画的显示。
2. 在Row组件中定义Text，Slider等组件，实现音乐播放条动画。
3. 为父组件添加renderFit属性，将该属性参数设置为RESIZE_CONTAIN，保持动画终态内容的宽高比，使内容完整显示在组件内，且与组件保持中心对齐。
 
完整示例参考如下：
 
```text
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">curves </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">controlViewOpacity</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">透明度</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">controlViewShow</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">是否展示</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">controlViewWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">240</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">布局宽度</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">controlViewBorderRadius</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">布局的圆角大小</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">controlViewPaddingLeft</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">内边距大小</span></em>
  <span style="color: rgb(255,255,255);">finalControlViewWidth</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">240</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">最终布局宽度</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">音乐</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OutSet</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">selectedColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffcb67'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">trackColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#ffcb67'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">人声</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">renderFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">RenderFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RESIZE_CONTAIN</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// renderFit</span><span style="color: rgb(128,128,128);">设置宽高跟随动画实时变化</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">opacity</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewOpacity</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">visibility</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewShow </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Visible </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">Visibility</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">None</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">layoutWeight</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(255,0,170);">(</span>true<span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">伸缩时裁剪超出部分</span></em>

        <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">$r</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'app.media.startIcon'</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">10 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">点击图标执行显示动画</span></em>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">animateTo</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">5000</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">curve</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">curves</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">springMotion</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0.5</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">iterations</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">,</span>

          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewWidth </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewWidth </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">finalControlViewWidth</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewBorderRadius </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewPaddingLeft </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">10</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewOpacity </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewShow </span><span style="color: rgb(181,106,1);">= </span>true<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewWidth </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewBorderRadius </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">25</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewPaddingLeft </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewOpacity </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">;</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewShow </span><span style="color: rgb(181,106,1);">= </span>false<span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">renderFit</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">RenderFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">RESIZE_CONTAIN</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#000'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewWidth</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewPaddingLeft</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">right</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">borderRadius</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">controlViewBorderRadius</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">50</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
