# 如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-20

#### 问题现象

使用AVRecorder录制WAV格式音频时，发生异常错误。
 
 

#### 问题原因

AVRecorderProfile参数配置错误，WAV格式需要匹配相应的比特率、声道数、编码格式、采样率和封装格式。
 
 

#### 解决措施

给[AVRecorderProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9)配置相应的比特率、声道数、编码格式、采样率和封装格式。
 
```text
private avProfile: media.AVRecorderProfile = {
  audioBitrate: 64000, <em>// set audioBitrate according to device ability.</em>
  audioChannels: 1, <em>// set audioChannels,valid value 1-8,CFT_WAV supports 1.</em>
  audioCodec: media.CodecMimeType.AUDIO_G711MU, <em>// set audioCodec,AUDIO_G711MU matching CFT_WAV.</em>
  audioSampleRate: 8000, <em>// set audioSampleRate according to device ability.</em>
  fileFormat: media.ContainerFormatType.CFT_WAV <em>// set fileFormat,CFT_WAV.</em>
}
```
