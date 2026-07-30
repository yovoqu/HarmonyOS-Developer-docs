# 使用Slider时如何判断点击的是滑块还是进度条

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-588

#### 问题现象

点击滑块希望可以控制暂停或者恢复播放，需要判断点击的是滑块还是进度条。
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Mv2ecYvvTkelDO5jOPpuPA/zh-cn_image_0000002628552394.png?HW-CC-KV=V1&HW-CC-Date=20260730T072320Z&HW-CC-Expire=86400&HW-CC-Sign=FDE30FD6461C4F96047AC81ADAC973F9B238796E0957068DE8AF6CB50FA77389)

 
 

#### 背景知识

- [Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)：滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
- [SliderChangeMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider#sliderchangemode枚举说明)：滑块的状态值。Slider拖动或点击时触发[onChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider#onchange)后可获取，包括按下、拖动、离开以及点击滑动条。

 
 

#### 解决方案

在Slider中，点击滑块如果没有发生滑动，滑动条进度值是不会发生变化的。而点击滑轨会改变滑块位置，同时也会让滑动条进度产生变化。所以可以通过Slider的onChange事件，在滑动条中按下时判断滑动进度值是否和上一次一致，可以知道点击的是滑动条还是滑块。方案如下：
 1. 通过onChange事件获取用户按下时滑动条的值value。
2. 根据按下前滑动条的值lastValue和按下时滑动条的值value进行判断，如果值一致说明用户点击了滑块，不一致则是点击了滑动条。
3. 用户离开滑动条时将离开时的值赋值给lastValue。
 
```text
<em>// </em><em><span style="color: rgb(128,128,128);">完整代码示例</span></em>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">SliderClickDetector </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">初始值</span></em>
  <span style="color: rgb(255,255,255);">lastValue</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">30</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">记录上一次滑动条的值</span></em>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(255,255,255);">sliderState</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">滑块状态</span></em>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">显示当前进度条值</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">点击位置</span><span style="color: rgb(132,63,161);">: </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toFixed</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">%`</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">20</span><span style="color: rgb(255,0,170);">)</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">核心</span><span style="color: rgb(128,128,128);">Slider</span><span style="color: rgb(128,128,128);">组件</span></em>
      <span style="color: rgb(0,0,255);">Slider</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">$$this</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">min</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">max</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">100</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">step</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(255,255,255);">style</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">SliderStyle</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">OutSet </span><em>// </em><em><span style="color: rgb(128,128,128);">使用凸起样式</span></em>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'90%'</span><span style="color: rgb(255,0,170);">)</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置</span><span style="color: rgb(128,128,128);">Slider</span><span style="color: rgb(128,128,128);">宽度</span></em>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onChange</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">mode</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">SliderChangeMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Begin</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">value </span><span style="color: rgb(181,106,1);">=== </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lastValue</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sliderState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击滑块</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
              this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sliderState </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">点击滑动条</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">          }</span>
          if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">mode </span><span style="color: rgb(181,106,1);">=== </span><span style="color: rgb(255,255,255);">SliderChangeMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">End</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
            this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">lastValue </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">value</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">        }</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">点击位置</span><span style="color: rgb(132,63,161);">: </span><span style="color: rgb(181,106,1);">${</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">sliderState</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">16</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">15</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Center</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
