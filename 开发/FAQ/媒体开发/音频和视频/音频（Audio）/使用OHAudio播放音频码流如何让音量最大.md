# 使用OHAudio播放音频码流如何让音量最大

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-41

#### 问题现象

使用OHAudio播放音频码流如何让声音最大？
 
 

#### 背景知识

- [OH_AudioRenderer_SetVolume](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_setvolume)可以设置当前音频流音量值。
- [OH_AudioRenderer_SetDefaultOutputDevice()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_setdefaultoutputdevice)可以设置默认本机内置发声设备。
- PCM码流本身也可以通过乘数的方式手动提高音量。

 
 

#### 解决方案

使用OHAudio播放音频码流可以通过以下三种方式提高音量：
 
- 开发者可使用OH_AudioRenderer_SetVolume接口设置当前音频流音量值，1.0为最大值。
```text
<em>// 要设置的音量值，音量值的范围是[0.0f, 1.0f]。</em>
float volume = 1.0f;
<em>// 设置当前音频流音量值。</em>
OH_AudioStream_Result state = OH_AudioRenderer_SetVolume(m_renderer, volume);
```

- 当音频流类型[OH_AudioStream_Usage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage)为语音消息、VoIP语音通话或者VoIP视频通话的场景时可以使用OH_AudioRenderer_SetDefaultOutputDevice()方法设置本机内置发声设备为扬声器获得最大音量的效果。
```text
<em>// 设置本机内置发声设备为扬声器。</em>
OH_AudioRenderer_SetDefaultOutputDevice(m_renderer, AUDIO_DEVICE_TYPE_SPEAKER);
```

- PCM码流本身可以直接做乘以系数的操作以提高音量。
```text
void AudioHelper::RaiseVolume(char *buf, uint32_t size, double vol) {
    OH_LOG_INFO(LOG_APP, "RaiseVolume");
    if (!size) {
        return;
    }
    for (int i = 0; i < size; i += 2) {
       <em> // 根据不同位数的PCM数据设置上下界，此处以16位PCM为例</em>
        signed long minData = -0x8000;
        signed long maxData = 0x7FFF;
      <em>  // 拼接单个16位样本</em>
        signed short wData = buf[i + 1];
        wData = MAKEWORD(buf[i], buf[i + 1]);
        signed long dwData = wData;
      <em>  // 对样本做数乘和上下限控制</em>
        dwData = dwData * vol;
        if (dwData < minData) {
            dwData = minData;
        } else if (dwData > maxData) {
            dwData = maxData;
        }
        wData = LOWORD(dwData);
      <em>  // 将处理后的数据保存</em>
        buf[i] = LOBYTE(wData);
        buf[i + 1] = HIBYTE(wData);
    }
}
```
 OH_AudioRenderer_SetDefaultOutputDevice()接口允许在AudioRenderer创建以后的任何时间被调用，系统会记录应用设置的默认本机内置发声设备。在应用启动播放时，若有外接设备如蓝牙耳机/有线耳机接入，系统优先从外接设备发声；否则系统遵循应用设置的默认本机内置发声设备发声。
