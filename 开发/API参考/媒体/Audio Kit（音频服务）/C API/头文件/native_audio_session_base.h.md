# native_audio_session_base.h

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-base-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

声明音频会话基础数据结构。
 
**引用文件：** <ohaudio/native_audio_session_base.h>
 
**库：** libohaudio.so
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**起始版本：** 24
 
**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)
 
  

##### 汇总

  

##### 结构体
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioSession_Strategy | OH_AudioSession_Strategy | 音频会话策略。 |
 
 
  

##### 枚举
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioSession_BehaviorFlags | OH_AudioSession_BehaviorFlags | 音频会话行为标志。 |
| OH_AudioSession_ConcurrencyMode | OH_AudioSession_ConcurrencyMode | 音频并发模式。 |
 
 
  

##### 枚举类型说明

  

##### OH_AudioSession_BehaviorFlags

```text
enum OH_AudioSession_BehaviorFlags
```
 
**描述**
 
音频会话行为标志。
 
**起始版本：** 24
  
| 枚举项 | 描述 |
| --- | --- |
| DEFAULT_BEHAVIOR = 0x00000000 | 默认行为，用于清除会话行为标记。 起始版本： 24 |
| MUTE_WHEN_INTERRUPTED = 0x00000002 | 当音频流被打断时，使用静音替代。通过接口OH_AudioSessionManager_SetBehavior设置该行为的同时，也需要调用接口OH_AudioSessionManager_SetScene使其生效。当播放被静音时，应用将收到OH_AudioStream_Usage.AUDIOSTREAM_INTERRUPT_HINT_MUTE通知，并且在恢复时会收到OH_AudioStream_Usage.AUDIOSTREAM_INTERRUPT_HINT_UNMUTE通知。 起始版本： 24 |
 
 
  

##### OH_AudioSession_ConcurrencyMode

```text
enum OH_AudioSession_ConcurrencyMode
```
 
**描述**
 
音频并发模式。
 
从API version 24开始，此枚举由native_audio_session_manager.h移动至此头文件。
 
在API version 24之前，使用该枚举请引用native_audio_session_manager.h头文件；从API version 24开始，引用native_audio_session_manager.h或native_audio_session_base.h均可正常使用该枚举。
 
**起始版本：** 12
  
| 枚举项 | 描述 |
| --- | --- |
| CONCURRENCY_DEFAULT = 0 | 默认使用系统策略。 |
| CONCURRENCY_MIX_WITH_OTHERS = 1 | 当前应用与其他应用混音播放。 |
| CONCURRENCY_DUCK_OTHERS = 2 | 当前应用播放时会压低其他正在播放的应用音量。 |
| CONCURRENCY_PAUSE_OTHERS = 3 | 当前应用播放时会暂停其他正在播放的应用。 |
