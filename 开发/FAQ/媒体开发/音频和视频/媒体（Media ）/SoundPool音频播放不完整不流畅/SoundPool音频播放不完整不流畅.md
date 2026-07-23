# SoundPool音频播放不完整不流畅

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-24

#### 问题现象

SoundPool播放音频文件时会出现如下问题：
 
- 音频文件稍微大时会出现播放不完整。
- 触发音频播放后没立即播放或不流畅。
- 乐器等场景音频资源超过32个会播放失败。

 
 

#### 背景知识

- [SoundPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundpool-for-playback)（音频池）接口可以实现低时延短音播放，如相机快门音效、系统通知音效等，实现一次加载，多次低时延播放。

 
- SoundPool支持的音频播放格式如下：

| 音频容器规格 | 规格描述 |

| --- | --- |

| m4a | 音频格式：AAC。 |

| aac | 音频格式：AAC。 |

| mp3 | 音频格式：MP3。 |

| ogg | 音频格式：VORBIS。 |

| wav | 音频格式：PCM。 |
- 使用接口[createSoundPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreatesoundpool10)创建音频池实例，当API 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。当API 18及API 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

 
 

#### 问题定位

- 检查音频资源的大小是否满足SoundPool接口要求。
SoundPool当前支持播放解码后1MB以下的音频资源，解码后大小超过1MB的长音频将截取前面的1MB大小数据进行播放，这相当于44.1kHz的16bit位深的立体声下约5.6秒的音频时长（在较低采样率或单声道配置下，持续时间会相应延长）。
- 可通过如下日志计算解码后的播放时长。

1. 搜索日志”CacheBuffer stream write finish, cacheDataFrameIndex_:“，获取资源大小cacheDataFrameIndex_，buffer大小length。
2. 搜索日志”audioRenderer normal stop.|audioRenderer fast renderer pause.“。若出现”audioRenderer normal stop.“，表示普通通路，buffer写入间隔=20ms。若出现”audioRenderer fast renderer pause.“，表示低时延通路，buffer写入间隔=5ms。
3. 计算播放时长，单位为ms：播放时长=资源大小/buffer大小*buffer写入间隔。
 
```text
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">41.901   </span>com.examp...graphics  I     [IncSoundData][[<span style="color: rgb(0,0,255);">102076</span>]RendererInClient] channel: <span style="color: rgb(0,0,255);">2</span>, L=1630, R=1661, counts: <span style="color: rgb(0,0,255);">400</span>
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">43.905   </span>com.examp...graphics  I     [IncSoundData][[<span style="color: rgb(0,0,255);">102076</span>]RendererInClient] channel: <span style="color: rgb(0,0,255);">2</span>, L=3776, R=3873, counts: <span style="color: rgb(0,0,255);">500</span>
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.864   </span>com.examp...graphics  I     #<span style="color: rgb(0,0,255);">362 </span>CacheBuffer stream write finish, cacheDataFrameIndex_:<span style="color: rgb(0,0,255);">1050624</span>, havePlayedCount_:<span style="color: rgb(0,0,255);">0</span>, loop:<span style="color: rgb(0,0,255);">0</span>, streamID_:<span style="color: rgb(0,0,255);">1</span>, length: <span style="color: rgb(0,0,255);">1920</span>
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.865   </span>com.examp...graphics  I     #<span style="color: rgb(0,0,255);">449 </span>CacheBuffer::Stop soundID_:<span style="color: rgb(0,0,255);">1</span>, streamID:<span style="color: rgb(0,0,255);">1</span>
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.866   </span>com.examp...graphics  I     #<span style="color: rgb(0,0,255);">463 </span>audioRenderer normal stop.
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.866   </span>com.examp...graphics  I     StreamClientState for Renderer::Stop. id: <span style="color: rgb(0,0,255);">102076</span>
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.866   </span>com.examp...graphics  I     [WriteUnderrunEvent]AudioRendererPrivate WriteUnderrunEvent!
10-28 <span style="color: rgb(0,0,255);">14</span>:<span style="color: rgb(0,0,255);">50</span>:<span style="color: rgb(0,0,255);">44.866   </span>com.examp...graphics  I     [StopAudioStream]Stop begin for sessionId <span style="color: rgb(0,0,255);">102076 </span>uid: <span style="color: rgb(0,0,255);">20020275</span>
```
 
 
- 音频资源未加载完成。SoundPool是预解析的，播放前资源必须先[load](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#load)加载完毕，即收到[on('loadComplete')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#onloadcomplete)回调之后再执行play操作。
```text
<span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SoundPool</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'loadComplete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'loadComplete, soundId: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```

- SoundPool实例的最大播放流数是32个，预加载资源的数量放宽到了128个。
当加载更多音频资源时会加载报错“5400102 load sound failed”。
- 当需要加载更多音频时，可以将之前加载的空闲音频通过[unload](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#unload)卸载掉（注意不是release释放实例），继续加载新的音频播放。以下代码示例展示了加载“rawfile/soundpool”目录下所有音频进行播放及卸载：
```json
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">media </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.MediaKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">audio </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.AudioKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">BusinessError </span><span style="color: rgb(181,106,1);">} </span>from <span style="color: rgb(132,63,161);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>

let <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SoundPool</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@ObservedV2</span>
class <span style="color: rgb(0,0,255);">SoundFile </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(181,106,1);">@Trace</span>
  <span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(132,63,161);">''</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Trace</span>
  <span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(181,106,1);">;</span>

  constructor<span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filename </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Builder</span>
export function <span style="color: rgb(0,0,255);">PageBuilder</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
  <span style="color: rgb(0,0,255);">TestPage</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@ComponentV2</span>
struct <span style="color: rgb(0,0,255);">TestPage </span><span style="color: rgb(181,106,1);">{</span>
  private <span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Context </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(255,0,170);">() </span>as <span style="color: rgb(181,106,1);">Context</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">@Local </span><span style="color: rgb(255,255,255);">soundFilesArr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">SoundFile</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span>new <span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">Promise</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(181,106,1);">void</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">create</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(0,0,255);">NavDestination</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(0,0,255);">List</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">2 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(0,0,255);">ForEach</span><span style="color: rgb(255,0,170);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundFilesArr</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SoundFile</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">index</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
            <span style="color: rgb(0,0,255);">ListItem</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
              <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(181,106,1);">{ </span><span style="color: rgb(255,255,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
                <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">index </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(80,160,79);">1 </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">'-' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">加载</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(132,63,161);">播放</span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundId </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(80,160,79);">0 </span><span style="color: rgb(181,106,1);">? </span><span style="color: rgb(132,63,161);">'Ready' </span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(132,63,161);">'UnReady'</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
                <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">卸载</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
                  <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
                    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">unload</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filename</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">item</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
                  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
              <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">            }</span>
<span style="color: rgb(181,106,1);">          }</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">}</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'100%'</span><span style="color: rgb(255,0,170);">)</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  async <span style="color: rgb(0,0,255);">create</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">创建</span><span style="color: rgb(128,128,128);">soundPool</span><span style="color: rgb(128,128,128);">实例</span></em>
    let <span style="color: rgb(255,255,255);">audioRendererInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">AudioRendererInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">usage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,255,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">StreamUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">STREAM_USAGE_MUSIC</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音频流使用类型：音乐。根据业务场景配置，参考</span><span style="color: rgb(128,128,128);">StreamUsage</span></em>
      <span style="color: rgb(255,255,255);">rendererFlags</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">1 </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音频渲染器标志</span></em>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">soundPool </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createSoundPool</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(80,160,79);">32</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">audioRendererInfo</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'load raw file error ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>

    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">监听</span><span style="color: rgb(128,128,128);">loadComplete</span></em>
    await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">scanRawFile</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">扫描</span><span style="color: rgb(128,128,128);">rawfile</span><span style="color: rgb(128,128,128);">音频资源</span></em>
  <span style="color: rgb(181,106,1);">}</span>

  async <span style="color: rgb(0,0,255);">scanRawFile</span><span style="color: rgb(255,0,170);">() </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">resourceManager </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">;</span>
      let <span style="color: rgb(255,255,255);">files </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileList</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'soundpool/'</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">//</span><span style="color: rgb(128,128,128);">确保目录存在，并包含音频文件</span></em>
      for <span style="color: rgb(255,0,170);">(</span>let <span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(80,160,79);">0</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i </span><span style="color: rgb(181,106,1);"><</span> <span style="color: rgb(255,255,255);">files</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(181,106,1);">++</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        let <span style="color: rgb(255,255,255);">soundFile</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">SoundFile </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">SoundFile</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">files</span><span style="color: rgb(255,0,170);">[</span><span style="color: rgb(255,255,255);">i</span><span style="color: rgb(255,0,170);">]</span><span style="color: rgb(181,106,1);">, -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundFilesArr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">push</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundFile</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    } </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'getRawFileList error' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  async <span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    try <span style="color: rgb(181,106,1);">{</span>
      let <span style="color: rgb(255,255,255);">rowFd </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">context</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFd</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'soundpool/' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'file uri: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">fileName </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(132,63,161);">',' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">rowFd</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      await <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">load</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">rowFd</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">fd</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">rowFd</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">offset</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">rowFd</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">length</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">updListArrSoundId</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
          <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'load sound err: '</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">e</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">} </span>catch <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'load raw file error' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">))</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">  }</span>

  async <span style="color: rgb(0,0,255);">play</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">开始播放，这边</span><span style="color: rgb(128,128,128);">play</span><span style="color: rgb(128,128,128);">也可带播放的参数</span><span style="color: rgb(128,128,128);">PlayParameters</span><span style="color: rgb(128,128,128);">，请在音频资源加载完毕，即收到</span><span style="color: rgb(128,128,128);">loadComplete</span><span style="color: rgb(128,128,128);">回调之后再执行</span><span style="color: rgb(128,128,128);">play</span><span style="color: rgb(128,128,128);">操作</span></em>
    await <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(255,0,170);">(</span>async <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">streamId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'play sound success soundid:' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">streamId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`play sound Error: errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, errMessage is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  async <span style="color: rgb(0,0,255);">unload</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">unload</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">BusinessError</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">`Failed to unload soundPool: errCode is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">code</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">, errMessage is </span><span style="color: rgb(181,106,1);">${</span><span style="color: rgb(255,255,255);">error</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">message</span><span style="color: rgb(181,106,1);">}</span><span style="color: rgb(132,63,161);">`</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">} </span>else <span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'Succceeded in unload soundPool'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
        this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">updListArrSoundId</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(181,106,1);">, -</span><span style="color: rgb(80,160,79);">1</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>

  <span style="color: rgb(0,0,255);">loadCallback</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">SoundPool</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">soundPool</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'loadComplete'</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'loadComplete, soundId: ' </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span>


  <span style="color: rgb(0,0,255);">updListArrSoundId</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">string</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(181,106,1);">number</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
  <em>  <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">更新</span><span style="color: rgb(128,128,128);">list</span><span style="color: rgb(128,128,128);">记录</span><span style="color: rgb(128,128,128);">soundId</span></em>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundFilesArr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">forEach</span><span style="color: rgb(255,0,170);">((</span><span style="color: rgb(255,255,255);">soundFile</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(181,106,1);">{</span>
      if <span style="color: rgb(255,0,170);">(</span><span style="color: rgb(255,255,255);">soundFile</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">filename </span><span style="color: rgb(181,106,1);">== </span><span style="color: rgb(255,255,255);">fileName</span><span style="color: rgb(255,0,170);">) </span><span style="color: rgb(181,106,1);">{</span>
        <span style="color: rgb(255,255,255);">soundFile</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(255,255,255);">soundId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,255,255);">soundId</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">    }</span><span style="color: rgb(255,0,170);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(181,106,1);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(181,106,1);">}</span>
```


 
 
 

#### 分析结论

当音频不满足组件规格，或者未正确使用播放组件时，会造成SoundPool音频播放异常。
 
 

#### 修改建议

使用SoundPool音频播放时，需正确按照组件规格进行调用，并遵守SoundPool播放顺序，详情参考官网[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundpool-for-playback#运行示例工程)。
 1. 创建SoundPool实例。
2. 加载音频资源。
3. 设置播放参数（循环模式/播放优先级等）。
4. 播放控制（播放/停止）。
5. 释放资源。
 
 

#### 常见FAQ

Q：SoundPool支持暂停后继续播放吗？
 
A：目前不支持。
 
Q：SoundPool当前支持播放解码后1MB以下的音频资源，有个1MB以下的MP3音频播放时为什么被截取？
 
A：MP3是常见的压缩率优良的音频编码格式，可以使用FFmpeg工具将MP3文件解码为WAV格式（WAV是一种未压缩的音频格式），通过查看WAV文件大小获取MP3音频解码后的大小，从而判断MP3音频资源是否符合SoundPool的使用要求。
