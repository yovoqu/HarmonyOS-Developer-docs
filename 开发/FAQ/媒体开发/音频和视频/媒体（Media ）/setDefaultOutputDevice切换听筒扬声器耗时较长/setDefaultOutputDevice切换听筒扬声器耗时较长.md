# setDefaultOutputDevice切换听筒扬声器耗时较长

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-49

#### 问题现象

使用setDefaultOutputDevice接口切换扬声器听筒时，耗时较长，中断时间较长，什么原因？
 
 

#### 背景知识

AudioRenderer的[setDefaultOutputDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setdefaultoutputdevice12)支持应用切换听筒和扬声器设备。
 
 

#### 问题定位

- 根据hilog日志，搜索[SetDefaultOutputDevice]set to找到切换设备的地方。
- 日志中发现有6条音频输出流，并且有4条是usage等于17-VoIP视频通话流，音频流类型可查看[StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage)。
```text
I C02B8B/audio_server/AudioCoreService: [comm][DeviceFetchStart] by SetDefaultOutputDevice for 6 output streams
```

- 输出设备切换时，会对每个音频输出流做静音操作，避免切换时的杂音，可查看到日志中存在多条静音与取消静音操作日志，音频流切换时间是累计的，共耗时约1.1s，有明显的中断。
```text
I C02B89/audio_server/AudioRenderSink: [SetSinkMuteForSwitchDevice]set primary mute 1 <em>// 静音操作</em>
...
I C02B89/audio_server/AudioRenderSink: [SetSinkMuteForSwitchDevice]set voip mute 0 <em>// 取消静音操作</em>
```
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Evt4nCtiQpu3snbrUrEIGw/zh-cn_image_0000002658792059.png?HW-CC-KV=V1&HW-CC-Date=20260730T072631Z&HW-CC-Expire=86400&HW-CC-Sign=093B0B9226A253C1698C0A7EB51C487468FBCE41A783DC6050373A10B01C0399)


 
 

#### 分析结论

应用起了多条音频输出流，切换设备时每条音频流会有静音和取消静音操作，操作耗时会累计，出现明显中断现象。
 
 

#### 修改建议

应用侧排查，不使用的音频流及时[release释放](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#release8)掉，避免切换耗时。
