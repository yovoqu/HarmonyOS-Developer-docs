# AVPlayer播放相册中的视频

更新时间：2026-08-13 01:23:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-24

#### 问题现象

如何使用AVPlayer播放用户从系统图库中选择的视频文件。
 
 

#### 背景知识

- [AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)：AVPlayer可将音视频媒体资源转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。AVPlayer提供功能完善一体化播放能力，应用只需要提供流媒体来源，不负责数据解析和解码就可以达成播放效果。
- [PhotoViewPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker)：PhotoViewPicker用于拉起系统图库，供用户选择媒体库中的图片/视频，返回对应的只读媒体文件uri。

 
 

#### 解决方案
1. 创建PhotoViewPicker实例，调用[PhotoViewPicker.select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker#select)接口拉起系统图库界面供用户选择需要播放的视频文件，用户选择完成后，返回图库视频文件的uri。
2. 使用[fileIo.openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)接口，通过返回的uri以只读方式打开视频文件，得到文件描述符fd。拼接得到字符串fd://${fd}，用于设置AVPlayer的uri，播放系统图库中的视频。参考代码如下：

  
```json
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">photoAccessHelper </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MediaLibraryKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">BusinessError </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.BasicServicesKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">fileIo </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.CoreFileKit'</span><span style="color: rgb(181,106,1);">;</span>
import <span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">media </span><span style="color: rgb(255,0,170);">} </span>from <span style="color: rgb(255,0,170);">'@kit.MediaKit'</span><span style="color: rgb(181,106,1);">;</span>

class <span style="color: rgb(0,0,255);">AVPlayerManager </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">?: </span><span style="color: rgb(0,0,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AVPlayer</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">surfaceId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>

  async <span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    try <span style="color: rgb(255,0,170);">{</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">= </span>await <span style="color: rgb(0,0,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">createAVPlayer</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`create avplayer failed: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setEventListening</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">setSurfaceId</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">surfaceId</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">surfaceId</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  async <span style="color: rgb(0,0,255);">getTrack</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">=== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`get audio track while avplayer is undefined`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">tracks </span><span style="color: rgb(181,106,1);">= </span>await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getTrackDescription</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Video Track: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">tracks</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  async <span style="color: rgb(0,0,255);">setMediaAsset</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">=== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`set media asset, avplayer is undefined`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    let <span style="color: rgb(0,0,255);">videoFd </span><span style="color: rgb(181,106,1);">= -</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
    try <span style="color: rgb(255,0,170);">{</span>
      let <span style="color: rgb(0,0,255);">videoFile </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">openSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">fileIo</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">OpenMode</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">READ_ONLY</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(0,0,255);">videoFd </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">videoFile</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fd</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">} </span>catch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed to open file: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">filePath</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      return<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">url </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">`fd://</span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">videoFd</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  async <span style="color: rgb(0,0,255);">release</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">!== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
      this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">  }</span>

  private <span style="color: rgb(0,0,255);">setEventListening</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'error'</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`AVPlayer error: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">JSON</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">stringify</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">reset</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">on</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'stateChange'</span><span style="color: rgb(181,106,1);">, </span>async <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">media</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AVPlayerState</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`AVPlayer state change to </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      if <span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer </span><span style="color: rgb(181,106,1);">=== </span>undefined<span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'AVPlayer is undefined when state change'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        return<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(128,128,128);">// AVPlayer</span><span style="color: rgb(128,128,128);">状态机</span>
      switch <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        case <span style="color: rgb(255,0,170);">'idle'</span><span style="color: rgb(181,106,1);">:</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'initialized'</span><span style="color: rgb(181,106,1);">:</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">surfaceId </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">surfaceId</span><span style="color: rgb(181,106,1);">;</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">prepare</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'prepared'</span><span style="color: rgb(181,106,1);">:</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayer</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">play</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'playing'</span><span style="color: rgb(181,106,1);">:</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'completed'</span><span style="color: rgb(181,106,1);">:</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'paused'</span><span style="color: rgb(181,106,1);">:</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'stopped'</span><span style="color: rgb(181,106,1);">:</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'released'</span><span style="color: rgb(181,106,1);">:</span>
          break<span style="color: rgb(181,106,1);">;</span>
        case <span style="color: rgb(255,0,170);">'error'</span><span style="color: rgb(181,106,1);">:</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">release</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          break<span style="color: rgb(181,106,1);">;</span>
        default<span style="color: rgb(181,106,1);">:</span>
          <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`AVPlayer change to unknown state: </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">state</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
          break<span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">    }</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
<span style="color: rgb(255,0,170);">}</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">videoUri</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">''</span><span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">avPlayerMgr</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">AVPlayerManager </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">mXComponentController</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">XComponentController </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">XComponentController</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">20 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">XComponent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">type</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">XComponentType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SURFACE</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(0,0,255);">controller</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mXComponentController</span><span style="color: rgb(181,106,1);">,</span>
      <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">aspectRatio</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">renderFit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">RenderFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">RESIZE_CONTAIN</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Pick Video'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">从相册选择视频</span>
          let <span style="color: rgb(0,0,255);">photoSelectOptions </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoSelectOptions</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">maxSelectNumber </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,0);">1</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">MIMEType </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoViewMIMETypes</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">VIDEO_TYPE</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">Array</span><span style="color: rgb(181,106,1);"><</span><span style="color: rgb(0,0,255);">string</span><span style="color: rgb(181,106,1);">></span><span style="color: rgb(181,106,1);"> = </span><span style="color: rgb(0,0,255);">[]</span><span style="color: rgb(181,106,1);">;</span>
          let <span style="color: rgb(0,0,255);">photoViewPicker </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoViewPicker</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          <span style="color: rgb(0,0,255);">photoViewPicker</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">select</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">photoSelectOptions</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">then</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">photoAccessHelper</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">PhotoSelectResult</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">uris </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">photoSelectResult</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">photoUris</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`photoViewPicker.select to file succeed and uris are: ` </span><span style="color: rgb(181,106,1);">+ </span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              if <span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">length </span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
                this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">videoUri </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(0,0,255);">uris</span><span style="color: rgb(0,0,255);">[</span><span style="color: rgb(255,0,0);">0</span><span style="color: rgb(0,0,255);">]</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">} </span>else <span style="color: rgb(255,0,170);">{</span>
                <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`failed to get media video uri`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
              <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">            }</span><span style="color: rgb(0,0,255);">)</span>
            <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">catch</span><span style="color: rgb(0,0,255);">((</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">BusinessError</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
              <span style="color: rgb(0,0,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">error</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">`Invoke photoViewPicker.select failed, code is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">code</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">, message is </span><span style="color: rgb(255,0,170);">${</span><span style="color: rgb(0,0,255);">err</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(255,0,170);">`</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
            <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>

      <span style="color: rgb(0,0,255);">Button</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'Play Video'</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">padding</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">5</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontSize</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,0);">30</span><span style="color: rgb(0,0,255);">)</span>
        <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">onClick</span><span style="color: rgb(0,0,255);">(</span>async <span style="color: rgb(0,0,255);">() </span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(181,106,1);">></span> <span style="color: rgb(255,0,170);">{</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayerMgr </span><span style="color: rgb(181,106,1);">= </span>new <span style="color: rgb(0,0,255);">AVPlayerManager</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayerMgr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setSurfaceId</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">mXComponentController</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getXComponentSurfaceId</span><span style="color: rgb(0,0,255);">())</span><span style="color: rgb(181,106,1);">;</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayerMgr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">init</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">;</span>
          await this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">avPlayerMgr</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">setMediaAsset</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">videoUri</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
        <span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">justifyContent</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">FlexAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">alignItems</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">HorizontalAlign</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Center</span><span style="color: rgb(0,0,255);">)</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
