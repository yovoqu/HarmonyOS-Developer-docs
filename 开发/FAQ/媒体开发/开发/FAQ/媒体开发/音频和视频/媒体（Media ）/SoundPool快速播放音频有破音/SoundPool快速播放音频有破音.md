# SoundPool快速播放音频有破音

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-32

#### 问题现象

使用SoundPool快速下发音频会导致音频播放时破音，问题代码片段如下：
 
```text
<span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"1"</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Pink</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">"80%"</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PlaySoundPool_1</span><span style="color: rgb(0,0,255);">()</span>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
```
 
 

#### 背景知识

[SoundPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#soundpool)（音频池）：提供了短音频的加载、播放等功能。当应用开发时，经常需要使用一些急促简短的音效（如点击键盘、系统通知音效等），此时建议调用SoundPool，实现一次加载，多次低时延播放。
 
 

#### 问题定位

在查看PCM文件时，发现客户端下发的两段音频数据存在重叠。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/yZiEY8hxTuaRDY6f86kd1A/zh-cn_image_0000002628552674.png?HW-CC-KV=V1&HW-CC-Date=20260811T005549Z&HW-CC-Expire=86400&HW-CC-Sign=9D8240E8F798C7D242EEB92493C8CF562991E00937DB860787D075A69FFD5D5E)

 
具体表现为：Demo中音频源的正常播放时间为45毫秒，但在播放到第20毫秒时，接收到新的音频片段播放请求，导致当前音频未播放完即被中断，新音频随即开始播放，从而产生破音现象。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/nHFBYzrlTuCMh44bqlmfbg/zh-cn_image_0000002658911993.png?HW-CC-KV=V1&HW-CC-Date=20260811T005549Z&HW-CC-Expire=86400&HW-CC-Sign=27C36DDD6E0D87C943CCF8441A29A8BA6053A082251D86621857E12A5CCEBB24)

 
 

#### 分析结论

音频框架会对每一段音频进行淡入淡出处理，如果连续不断地将数据发送到框架中，框架只会对第一帧音频执行淡入效果，并在最后一帧执行淡出效果，而中间的所有帧不会处理。这样一来，音频播放时就会出现断续或失真的现象。
 
 

#### 修改建议

针对连续快速下发两次音频时出现的pop音问题，已知底层音频处理采用了淡入淡出效果，并且音频播放限于单一路流的原则。基于此现状，提出以下优化方案以提升用户体验和系统稳定性：
 
- 集成防抖逻辑以平滑音频下发频率：实施策略应考虑将两次连续的音频下发合并在一次指令中，以此避免短时间内对音频下发操作的频繁调用，进而缓解系统资源压力。建议根据应用实际下发音频数据的长度来调整下发频率间隔，适当延长这一间隔有助于优化音频处理过程。一种可行的技术方案是在下发逻辑中添加防抖(debounce)逻辑控制，保证频次适中。

  
```text
<em>// </em><em><span style="color: rgb(128,128,128);">防抖 在一段时间内函数被多次触发，防抖让函数在一段时间后最终只执行一次</span></em>
export function <span style="color: rgb(0,0,255);">debounce</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">func</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">delay</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">timer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">clearTimeout</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">timer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">func</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">delay </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">delay </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```

- 运用播放完成回调机制：

  引入SoundPool播放完成回调功能，即在上一路流的播放彻底完成后，再执行下一次音频数据的下发动作。该机制能够确保各音频指令按序无误地执行，避免因未等前一音频播放结束就下发新音频而导致的音质问题。
```text
<em>//</em><em><span style="color: rgb(128,128,128);"> 加载完成回调</span></em>
<span style="color: rgb(0,0,255);">async </span><span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'loadComplete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">soundId_</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`loadComplete,soundId:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">soundId_</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<em>//</em><em><span style="color: rgb(128,128,128);"> 播放完成回调</span></em>
<span style="color: rgb(0,0,255);">async </span><span style="color: rgb(0,0,255);">finishPlayCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'playFinished'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'receive play finished message'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
```


 
完整示例参考如下：
 
```text
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">audio </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AudioKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">media </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MediaKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">common </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.AbilityKit'</span><span style="color: rgb(181,106,1);">;</span>

<em>// </em><em><span style="color: rgb(128,128,128);">防抖 在一段时间内函数被多次触发，防抖让函数在一段时间后最终只执行一次</span></em>
export function <span style="color: rgb(0,0,255);">debounce</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">func</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(0,0,255);">void</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">delay</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
  let <span style="color: rgb(0,0,255);">timer</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(181,106,1);">;</span>
  return <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">ClickEvent</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">clearTimeout</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">timer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">timer </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">setTimeout</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">func</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">delay </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(0,0,255);">delay </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1000</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SoundPool</span><span style="color: rgb(181,106,1);">|</span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">soundId_1</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">() </span>as <span style="color: rgb(0,0,255);">common</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">UIAbilityContext</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">audioRendererInfo</span><span style="color: rgb(181,106,1);">:</span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioRendererInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">usage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STREAM_USAGE_MUSIC</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">rendererFlags</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">1</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
  <em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);"> 加载完成回调</span></em>
  async <span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'loadComplete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">soundId_</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">number</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`loadComplete,soundId:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">soundId_</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em>//</em><em><span style="color: rgb(128,128,128);"> 播放完成回调</span></em>
  async <span style="color: rgb(0,0,255);">finishPlayCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'playFinished'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'receive play finished message'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
  <em>//</em><em><span style="color: rgb(128,128,128);"> 错误类型回调</span></em>
  async <span style="color: rgb(0,0,255);">setErrorCallback</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'error'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`error happened,message is :</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <em>//</em><em><span style="color: rgb(128,128,128);"> 加载琴键音效</span></em>
  async <span style="color: rgb(0,0,255);">InitSoundPool</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSoundPool</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">3</span><span style="color: rgb(181,106,1);">, </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">audioRendererInfo</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setErrorCallback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">fileDescriptor </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFdSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1_DO.mp3'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundId_1 </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">load</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">fileDescriptor</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileDescriptor</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">offset</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileDescriptor</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  <em>//</em><em><span style="color: rgb(128,128,128);"> 播放钢琴键音效</span><span style="color: rgb(128,128,128);">DO</span></em>
  async <span style="color: rgb(0,0,255);">PlaySoundPool_1</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundPool</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">soundId_1</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">finishPlayCallback</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'play success'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'soundpool play failed and catch error is ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Loading'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Pink</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">InitSoundPool</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'1'</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">20</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">White</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">type</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ButtonType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Capsule</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Pink</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'80%'</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">50</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">margin</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">10</span><span style="color: rgb(0,0,255);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">debounce</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PlaySoundPool_1</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`event:</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">event</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,0);">40</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PlaySoundPool_1</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
 

#### 总结

在使用SoundPool快速连续播放短音频时发现破音现象，表现为当前音频片段未播完即被新片段中断，源于音频框架处理中的淡入淡出效果无法正常应用。当前修改建议包含两个关键策略：
- 一是集成防抖(debounce)逻辑，以合并连续的音频调用指令，减少系统压力。
- 二是利用SoundPool播放完成回调机制确保每个音频顺序播放，避免重叠。

 
 
> [!NOTE]
> 以上方案实现效果为上一段音频播放完后衔接下一段音频来实现淡入淡出的效果，不适用于打断上一个音频来衔接播放的连续点击效果，在听感上仍然会有破音的影响。
