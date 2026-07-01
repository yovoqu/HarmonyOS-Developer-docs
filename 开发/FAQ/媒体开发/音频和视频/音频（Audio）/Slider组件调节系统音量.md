# Slider组件调节系统音量

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-52

#### 问题现象

自定义[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)组件如何调节系统音量，同时系统音量调节如何同步到Slider组件？
 
 

#### 背景知识

[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。[音量面板AVVolumePanel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avvolumepanel)提供展示和调节系统音量的统一面板。[on('streamVolumeChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#onstreamvolumechange20)监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。
 
 

#### 解决方案

Slider组件可以通过音量面板AVVolumePanel调节系统音量，同时可以通过on('streamVolumeChange')监听系统音量变化同步给Slider组件。示例代码如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">AVVolumePanel </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AudioKit'</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(0,0,255);">streamUsage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamUsage </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STREAM_USAGE_MUSIC</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">audioManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getAudioManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">audioVolumeManager</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioVolumeManager </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audioManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getVolumeManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">volumeMin</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audioVolumeManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMinVolumeByStream</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">streamUsage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
let <span style="color: rgb(0,0,255);">volumeMax</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audioVolumeManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getMaxVolumeByStream</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">streamUsage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
const <span style="color: rgb(0,0,255);">tag </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'[SliderVolumeDemo]'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
export struct <span style="color: rgb(0,0,255);">SliderVolumeDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">volumeLevel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);"> 音量值和滑块值使用同一个变量</span></em>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> volume min:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">volumeMin</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> max:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">volumeMax</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volumeLevel </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">audioVolumeManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getVolumeByStream</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">streamUsage</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听音量变化，同时改变滑块值</span></em>
    <span style="color: rgb(0,0,255);">audioVolumeManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'streamVolumeChange'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">streamUsage</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">streamVolumeEvent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamVolumeEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">tag</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);"> volumeLevel:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">streamVolumeEvent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volume</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volumeLevel </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">streamVolumeEvent</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volume</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">8 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volumeLevel</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">volumeMin</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">volumeMax</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OutSet</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">showTips</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>

      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音量面板</span></em>
        <span style="color: rgb(0,0,255);">AVVolumePanel</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(0,0,255);">volumeLevel</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">volumeLevel</span><span style="color: rgb(181,106,1);">,</span>
          <span style="color: rgb(0,0,255);">volumeParameter</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
            <span style="color: rgb(0,0,255);">position</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1100</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音量面板位置，当不需要显示面板时，</span><span style="color: rgb(128,128,128);">position</span><span style="color: rgb(128,128,128);">的</span><span style="color: rgb(128,128,128);">x</span><span style="color: rgb(128,128,128);">，</span><span style="color: rgb(128,128,128);">y</span><span style="color: rgb(128,128,128);">值可设置负数</span></em>
              <span style="color: rgb(0,0,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">300</span>
            <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">          }</span>
<span style="color: rgb(255,0,170);">        }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
