# TextTimer展示纯秒数时间格式设置

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1515

#### 问题现象

将TextTimer组件的format设置为'ss'，发现当倒计时大于等于60秒时，显示效果不符合预期：60秒显示为'00'(01:00)，实际希望显示'60'，70秒显示为'10'(01:10)，实际希望显示'70'，没有分钟位的显示。如何设置TextTimer才能让它正确显示'60'、'70'这样的纯秒数样式？
 
 

#### 效果预览


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/rdvdL9WYR1GXsWVaArt9yg/zh-cn_image_0000002628606558.gif?HW-CC-KV=V1&HW-CC-Date=20260730T072407Z&HW-CC-Expire=86400&HW-CC-Sign=AB8580E40C98939BCC689620BEED0210AECEC1CB1965B4CD510A8A2800A140F4)

 
 

#### 背景知识

[TextTimer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer)通过文本显示计时信息并控制其计时器状态的组件，可以自定义显示HH、mm、ss、SS等格式，对于个性化需求，可以使用[contentModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer#contentmodifier12)方法定制TextTimer内容区，开发者需要自定义class实现ContentModifier接口。
 
 

#### 解决方案

使用contentModifier自定义显示内容，用Text显示剩余秒数。[TextTimerConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer#texttimerconfiguration12对象说明)包含了计时器设定时间count和经过时间elapsedTime，count减去elapsedTime即为计时器需要显示的剩余时间。
 
计算时需要注意单位转换，count单位为ms，elapsedTime为设置格式的最小单位，如format设为'mm:ss'则单位为秒、设为'mm'则单位为分。
 
```text
class <span style="color: rgb(0,0,255);">MyTextTimerModifier </span>implements <span style="color: rgb(0,0,255);">ContentModifier</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">TextTimerConfiguration</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">applyContent</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">WrappedBuilder</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(0,0,255);">TextTimerConfiguration</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    return <span style="color: rgb(0,0,255);">wrapBuilder</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">buildTextTimer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Builder</span>
function <span style="color: rgb(0,0,255);">buildTextTimer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextTimerConfiguration</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Stack</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">alignContent</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Alignment</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Circle</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">150</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">150 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fill</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">started </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">isCountDown </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">0xFF232323 </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">0xFF717171) </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">0xFF929292)</span><span style="color: rgb(181,106,1);">;</span>
    <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">剩余时间：用初始时间减去计时器经过的时间</span></em>
      <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Math</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">max</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">1000 </span><span style="color: rgb(181,106,1);">- </span><span style="color: rgb(0,0,255);">config</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">elapsedTime </span><span style="color: rgb(181,106,1);">/ </span><span style="color: rgb(255,0,0);">100</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">toFixed</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">))</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">MyTextTimerDemo </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">70000</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@State </span><span style="color: rgb(0,0,255);">myTimerModifier</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">MyTextTimerModifier </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">MyTextTimerModifier</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(0,0,255);">countDownTextTimerController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">TextTimerController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">TextTimerController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">TextTimer</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">isCountDown</span><span style="color: rgb(181,106,1);">: </span>true<span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">count</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">countDownTextTimerController </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">contentModifier</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">myTimerModifier</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义显示的内容</span></em>
      <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'start'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">countDownTextTimerController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">start</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'pause'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">countDownTextTimerController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">pause</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'reset'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">countDownTextTimerController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 常见FAQ

Q：TextTimer倒计时结束后怎么执行相应回调？
 
A：[onTimer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer#ontimer)：时间文本发生变化时触发该事件。锁屏状态和应用后台状态下不会触发该事件。onTimer(event: (utc: number, elapsedTime: number) => void)。在onTimer回调里判断elapsedTime是否到达设定值，来实现执行相应回调。
