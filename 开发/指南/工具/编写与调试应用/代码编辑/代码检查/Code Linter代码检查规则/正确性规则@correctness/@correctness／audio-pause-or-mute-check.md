# @correctness/audio-pause-or-mute-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-pause-or-mute-check

建议应用在播放声音的场景下，监听音频发声设备变化。
 
改善[音视频播放](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change#音频流输出设备变更原因)体验场景下，建议优先修改。
 

##### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    "@correctness/audio-pause-or-mute-check": "warn"
  }
}
```
 
 

##### 选项

该规则无需配置额外选项。
 
 

##### 正例

```text
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
export class AudioPauseNoReport {
  demoCallBack() {
    let audioStreamInfo1: audio.AudioStreamInfo = {
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
      channels: audio.AudioChannel.CHANNEL_1,
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
    };
    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
      rendererFlags: 0
    };
    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo1,
      rendererInfo: audioRendererInfo
    };
    media.createAVPlayer((error: BusinessError, player) => {
      if (player) {
        player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        player.on('audioOutputDeviceChangeWithInfo', ()=>{
          console.error(`createAVPlayer audioOutputDeviceChangeWithInfo`);
        });
        console.info('Succeeded in creating AVPlayer.');
      } else {
        console.error(`Failed to create AVPlayer, error message:${error.message}`);
      }
    });
    audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
      if (err) {
        console.error(`AudioRenderer Created: Error: ${err}`);
      } else {
        audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        audioRenderer.on('outputDeviceChangeWithInfo', ()=>{
          console.error(`createAudioRenderer outputDeviceChangeWithInfo`);
        })
        console.info('AudioRenderer Created: Success: SUCCESS');
      }
    });
  }
}
```
 
 

##### 反例

```text
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
let audioStreamInfo1: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
  channels: audio.AudioChannel.CHANNEL_1,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  rendererFlags: 0
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo1,
  rendererInfo: audioRendererInfo
};
function demoCallBack() {
  // warning line
  media.createAVPlayer((error: BusinessError, player: media.AVPlayer) => {
    if (player != null) {
      player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('Succeeded in creating AVPlayer.');
    } else {
      console.error(`Failed to create AVPlayer, error message:${error.message}`);
    }
  });
  // warning line
  audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
    if (err) {
      console.error(`AudioRenderer Created: Error: ${err}`);
    } else {
      audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('AudioRenderer Created.');
    }
  });
}
```
 
 

##### 规则集

```text
<span style="color: rgb(6,125,23);">plugin:@correctness/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
