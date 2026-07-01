# animation播放动画异常突变

更新时间：2026-06-26 09:07:13

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-634

#### 问题现象

转场动画期望由大缩小，且动画连贯流畅。但是实际的情况是，当页面显示发生转场，页面中圆初始显示为小的状态，待延时结束，再突然变大，然后由大缓慢缩小。其中突然变大导致整体效果不连贯，如何实现转场动画从页面开始显示，圆一直保持大的状态到延时结束，然后缩小？
 
问题代码示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">ShackHand </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Param </span><span style="color: rgb(255,255,255);">serverActive</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">boolean </span><span style="color: rgb(181,106,1);">= </span>false
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">动画点信息</span></em>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(255,255,255);">colorArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">JumpTrans</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#802d2de3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#802d2de3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">]</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">colorArray</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">JumpTrans</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">Circle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'180lpx'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'180lpx' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">30</span>
          <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'5lpx'</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(255,0,170);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">generateEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(255,0,170);">))</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">设置动画效果</span></em>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>

    <span style="color: rgb(181,106,1);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'600lpx'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'600lpx'</span><span style="color: rgb(255,0,170);">)</span>

  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">动画效果</span></em>
function <span style="color: rgb(0,0,255);">generateEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TransitionEffect </span><span style="color: rgb(181,106,1);">{</span>
  return <span style="color: rgb(255,255,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Reverse</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">动画反向播放</span></em>
      <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">delay</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>

<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">信息类</span></em>
class <span style="color: rgb(0,0,255);">JumpTrans </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceColor</span>
  <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span>

  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceColor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">color </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">color</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">delay </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">delay</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
 
问题效果预览：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/UAFfOda8S3G5Mzf8b-sYwA/zh-cn_image_0000002628394280.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041147Z&HW-CC-Expire=86400&HW-CC-Sign=93670287BF28FEC6D8E311D5C29D1BB425F6E9FB91662440F97C16D16AC26802)

 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/AsEgnbwFS02KATkuWlin1Q/zh-cn_image_0000002658913495.gif?HW-CC-KV=V1&HW-CC-Date=20260701T041147Z&HW-CC-Expire=86400&HW-CC-Sign=4AA4A4D0D94C7C6E5F3A491ABBF66A034CBA927C14F190CBEE6AB35D0DC9597B)

 
 

#### 背景知识

- [组件内转场 (transition)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
- [属性动画 (animation)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty)组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。其中[delay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-animator#delay18)属性用于设置动画延迟播放时间，[PlayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#playmode)用于设置动画的播放方式。

 
 

#### 问题定位

该问题涉及动画播放的两个阶段：
 
- 动画之前形态：transition会在转场动画播放前保持设置的动画初始形态，即scale({ x: 0.1, y: 0.1 })。因为delay延迟了动画播放，所以这个形态会展示到UI。
- 动画开始形态：因为使用了PlayMode.Reverse动画反向播放，所以动画的开始形态变成了scale({ x: 1, y: 1 })。

 
由上述可知动画播放之前形态和动画开始形态有较大差距，因此出现突兀变化。
 
 

#### 分析结论

delay和PlayMode.Reverse属性设置不当会导致动画播放前出现组件形态的突兀变化，因此不建议组合使用。
 
 

#### 修改建议

若有延时效果，建议使用PlayMode.Normal，同时动画效果与目标状态翻转设置一下即可。
 
完整示例参考如下：
 
```text
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">JumpTransCustom </span><span style="color: rgb(181,106,1);">{</span>
<em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">动画数据</span></em>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(255,255,255);">colorArray</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">JumpTrans</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(255,0,170);">[</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#802d2de3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">1500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#802d2de3'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2000</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
    new <span style="color: rgb(0,0,255);">JumpTrans</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'#8002ECFC'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(80,160,79);">2500</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">RelativeContainer</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">colorArray</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">JumpTrans</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">Circle</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'180lpx'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'180lpx' </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stroke</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">White</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(255,255,255);">left</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">* </span><span style="color: rgb(80,160,79);">30</span>
            <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">strokeWidth</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'5lpx'</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(255,0,170);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">transition</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(0,0,255);">generateEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">jump</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(255,0,170);">)) </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">调用动画函数</span></em>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.1</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">0.1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Black</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'600lpx'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'600lpx'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">动画效果</span></em>
function <span style="color: rgb(0,0,255);">generateEffect</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">TransitionEffect </span><span style="color: rgb(181,106,1);">{</span>
  return <span style="color: rgb(255,255,255);">TransitionEffect</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scale</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">x</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">8</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">y</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">8 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">animation</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">duration</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1000</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">playMode</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">PlayMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">Normal</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">delay</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<em>// </em><em><span style="color: rgb(128,128,128);">数据类</span></em>
class <span style="color: rgb(0,0,255);">JumpTrans </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceColor</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">ResourceColor</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">color </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">color</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">delay </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">delay</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>
```
