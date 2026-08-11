# AudioRenderer设置音频流后输出设备不符合预期

更新时间：2026-08-05 01:18:37

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-44

#### 问题现象

```text
export class <span style="color: rgb(0,0,255);">AudioRenderPlayer </span><span style="color: rgb(255,0,170);">{</span>
  private <span style="color: rgb(0,0,255);">renderModel</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioRenderer </span><span style="color: rgb(181,106,1);">| </span><span style="color: rgb(0,0,255);">undefined </span><span style="color: rgb(181,106,1);">= </span>undefined<span style="color: rgb(181,106,1);">;</span>
  private <span style="color: rgb(0,0,255);">audioStreamInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioStreamInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">samplingRate</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioSamplingRate</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SAMPLE_RATE_16000</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">采样率</span></em>
    <span style="color: rgb(0,0,255);">channels</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioChannel</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">CHANNEL_1</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">通道</span></em>
    <span style="color: rgb(0,0,255);">sampleFormat</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioSampleFormat</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">SAMPLE_FORMAT_S16LE</span><span style="color: rgb(181,106,1);">,</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">采样格式</span></em>
    <span style="color: rgb(0,0,255);">encodingType</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioEncodingType</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">ENCODING_TYPE_RAW </span><em>// </em><em><span style="color: rgb(128,128,128);">编码格式</span></em>
  <span style="color: rgb(255,0,170);">}</span>
  private <span style="color: rgb(0,0,255);">audioRendererInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioRendererInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">usage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STREAM_USAGE_VOICE_COMMUNICATION</span><span style="color: rgb(181,106,1);">, </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音频流使用类型</span></em>
    <span style="color: rgb(0,0,255);">rendererFlags</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0</span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">音频渲染器标志</span></em>
  <span style="color: rgb(255,0,170);">}</span>
  private <span style="color: rgb(0,0,255);">audioRendererOptions</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioRendererOptions </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">streamInfo</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">audioStreamInfo</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(0,0,255);">rendererInfo</span><span style="color: rgb(181,106,1);">: </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">audioRendererInfo</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
通过以上代码配置音频渲染参数以便后面创建AudioRenderer实例，预期使用扬声器播放，实际从听筒发出声音，为什么？
 
 

#### 背景知识

音频流类型是定义音频数据播放和录制方式的关键属性。对于播放流，其类型由[StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage)确定。音频流类型对输出设备的选择具有决定性影响。
 
 

#### 问题定位

问题代码中音频流类型是**STREAM_USAGE_VOICE_COMMUNICATION**，从音频流使用类型可知，**STREAM_USAGE_VOICE_COMMUNICATION**的播放流类型为语音消息，在[音频流类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype)中应属于VOICE_CALL。
 
 

#### 分析结论

**STREAM_USAGE_VOICE_COMMUNICATION**音频流所属的音量类型为通话音量，[默认输出设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-right-streamusage-for-playback#输出设备选择)为听筒，所以音频声音会从听筒发出。
 
 

#### 修改建议

- 可以尝试更换音频流类型为**STREAM_USAGE_MUSIC**，默认会从扬声器播放。
```text
let <span style="color: rgb(0,0,255);">audioRendererInfo</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">AudioRendererInfo </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">usage</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">audio</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">StreamUsage</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">STREAM_USAGE_MUSIC</span><span style="color: rgb(181,106,1);">, </span><em>// </em><em><span style="color: rgb(128,128,128);">音频流使用类型：音乐。根据业务场景配置，参考</span><span style="color: rgb(128,128,128);">StreamUsage</span><span style="color: rgb(128,128,128);">。</span></em>
  <span style="color: rgb(0,0,255);">rendererFlags</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">0 </span><em>// </em><em><span style="color: rgb(128,128,128);">音频渲染器标志。</span></em>
<span style="color: rgb(255,0,170);">}</span><span style="color: rgb(181,106,1);">;</span>
```
 完整代码可参考：使用AudioRenderer开发音频播放功能[完整示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback#完整示例)。
- 若默认的输入/输出设备不符合使用诉求，应用也可以调用[setDefaultOutputDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setdefaultoutputdevice12)接口主动修改默认输出设备，值得注意的是，该接口仅适用于StreamUsage为语音消息（STREAM_USAGE_VOICE_MESSAGE）、VoIP语音通话（STREAM_USAGE_VOICE_COMMUNICATION）或者VoIP视频通话（STREAM_USAGE_VIDEO_COMMUNICATION）的场景。
