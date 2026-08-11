# DPI相关单位换算

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1273

#### 问题现象

为了在不同的手机上都能够显示准确的毫米值，想清楚屏幕DPI像素单位px与1mm间有何转换关系，以及px与尺寸单位vp之间又该如何转换？
 
 

#### 背景知识

[@ohos.display](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display)是HarmonyOS中的一个模块，用于管理和控制设备的屏幕属性。它提供了许多接口和方法，允许开发者获取和设置屏幕的相关信息，如分辨率、刷新率等，具体可以查看[display屏幕实例属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)，其属性DPI指的是显示设备屏幕的物理像素密度，表示每英寸上的像素点数。一英寸为25.4毫米。
 
 

#### 解决方案

- 实现px与1mm之间转换，需要通过display中getDefaultDisplaySync方法获取屏幕DPI及每英寸上的像素点数，再通过一英寸等于25.4毫米进行计算得出。
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">display </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.ArkUI'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">px2mm</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    let <span style="color: rgb(0,0,255);">displayClass</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Display </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">display</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getDefaultDisplaySync</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取屏幕高度（以像素为单位）</span></em>
    let <span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">displayClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">;</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">获取屏幕的垂直方向的</span><span style="color: rgb(128,128,128);">DPI</span><span style="color: rgb(128,128,128);">（每英寸点数）</span></em>
    let <span style="color: rgb(0,0,255);">dpi </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">displayClass</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">yDPI</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">屏幕</span><span style="color: rgb(255,0,170);">Y</span><span style="color: rgb(255,0,170);">方向对应的</span><span style="color: rgb(255,0,170);">DPI:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">dpi</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">屏幕宽度的物理长度（</span><span style="color: rgb(255,0,170);">mm</span><span style="color: rgb(255,0,170);">）</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">height </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(0,0,255);">dpi </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(255,0,0);">25.4</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">屏幕宽度一毫米有多少</span><span style="color: rgb(255,0,170);">px:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">dpi </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">25.4</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2mm </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">dpi </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">25.4</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">屏幕宽度一</span><span style="color: rgb(255,0,170);">mm</span><span style="color: rgb(255,0,170);">有</span><span style="color: rgb(255,0,170);">:</span><span style="color: rgb(255,0,170);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">px2mm</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">px`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">top</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">100 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 实现px与尺寸单位vp之间的转换，需在明确目标设备的屏幕DPI后，通过转换公式px=vp*(DPI/160)计算即可。

 
 

#### 常见FAQ

Q：display中getDefaultDisplaySync方法获取屏幕DPI受到系统缩放影响，若开发者不希望应用受显示缩放影响布局，使用setDefaultDensityEnabled()设置应用是否使用系统默认Density，如何获取默认DPI值？
 
A：可以用getWindowDensityInfo，里面的defaultDensity是设备的默认densityPixels，不会跟随系统变化。systemDensity是会跟随系统变化的。而customDensity是受windowStage.setDefaultDensityEnabled()影响，true时不跟随系统变化，false时跟随，[参考链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowdensityinfo15)。
