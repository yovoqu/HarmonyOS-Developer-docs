# native_audiocapturer.h

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

声明音频采集的相关接口。
 
**引用文件：** <ohaudio/native_audiocapturer.h>
 
**库：** libohaudio.so
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**起始版本：** 10
 
**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)
 
  

##### 汇总

  

##### 函数
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer) | - | 释放输入音频流。 |
| OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer) | - | 启动音频采集器，开始获取音频数据。 |
| OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer) | - | 暂停输入音频流。在暂停音频，后续需要恢复录音的场景，建议使用pause。 |
| OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer) | - | 停止音频采集器，停止输入音频流。如果需要彻底结束录音，建议使用stop。 |
| OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer) | - | 丢弃获取的音频数据。 |
| OH_AudioStream_Result OH_AudioCapturer_GetCurrentState(OH_AudioCapturer* capturer, OH_AudioStream_State* state) | - | 查询当前音频流状态。 |
| OH_AudioStream_Result OH_AudioCapturer_GetLatencyMode(OH_AudioCapturer* capturer, OH_AudioStream_LatencyMode* latencyMode) | - | 查询当前音频流时延模式。 |
| OH_AudioStream_Result OH_AudioCapturer_GetStreamId(OH_AudioCapturer* capturer, uint32_t* streamId) | - | 查询当前输入音频流ID。 |
| OH_AudioStream_Result OH_AudioCapturer_GetSamplingRate(OH_AudioCapturer* capturer, int32_t* rate) | - | 查询当前输入音频流采样率。 |
| OH_AudioStream_Result OH_AudioCapturer_GetChannelCount(OH_AudioCapturer* capturer, int32_t* channelCount) | - | 查询当前音频流通道数。 |
| OH_AudioStream_Result OH_AudioCapturer_GetSampleFormat(OH_AudioCapturer* capturer, OH_AudioStream_SampleFormat* sampleFormat) | - | 查询当前输入音频流采样格式。 |
| OH_AudioStream_Result OH_AudioCapturer_GetEncodingType(OH_AudioCapturer* capturer, OH_AudioStream_EncodingType* encodingType) | - | 查询当前音频流编码类型。 |
| OH_AudioStream_Result OH_AudioCapturer_GetCapturerInfo(OH_AudioCapturer* capturer, OH_AudioStream_SourceType* sourceType) | - | 查询当前音频流工作场景类型。 |
| OH_AudioStream_Result OH_AudioCapturer_GetFrameSizeInCallback(OH_AudioCapturer* capturer, int32_t* frameSize) | - | 在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。 |
| OH_AudioStream_Result OH_AudioCapturer_GetTimestamp(OH_AudioCapturer* capturer, clockid_t clockId,int64_t* framePosition, int64_t* timestamp) | - | 获取输入音频流时间戳和当前数据帧位置信息。 该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。 |
| OH_AudioStream_Result OH_AudioCapturer_GetFramesRead(OH_AudioCapturer* capturer, int64_t* frames) | - | 查询自创建流以来已读取的帧数。 |
| OH_AudioStream_Result OH_AudioCapturer_SetMuteHint(OH_AudioCapturer* capturer, bool mute) | - | 应用将当前录音流的自身静音状态传递给系统音频模块。该接口用于向系统音频模块上报应用自身的静音状态，不会改变录音流的实际静音状态。当前仅在部分PC/2in1设备上，系统音频模块会基于设置的状态调整策略以降低功耗。该接口仅在录音流处于运行态时允许调用，否则返回错误AUDIOSTREAM_ERROR_ILLEGAL_STATE。同一录音流同时设置流级静音提示接口（本接口）和会话级静音提示接口时，流级（本接口）优先级更高，数值以流级（本接口）设置值为准。 |
| OH_AudioStream_Result OH_AudioCapturer_GetOverflowCount(OH_AudioCapturer* capturer, uint32_t* count) | - | 查询当前录制音频流过载数。 |
| typedef void (*OH_AudioCapturer_OnReadDataCallback)(OH_AudioCapturer* capturer, void* userData, void* audioData, int32_t audioDataSize) | OH_AudioCapturer_OnReadDataCallback | 读取音频数据的回调函数。为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。 |
| typedef void (*OH_AudioCapturer_OnDeviceChangeCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioDeviceDescriptorArray* deviceArray) | OH_AudioCapturer_OnDeviceChangeCallback | 音频录制流的设备变化事件回调函数。 |
| typedef void (*OH_AudioCapturer_OnInterruptCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint) | OH_AudioCapturer_OnInterruptCallback | 音频录制流的中断事件回调函数。 |
| typedef void (*OH_AudioCapturer_OnErrorCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_Result error) | OH_AudioCapturer_OnErrorCallback | 音频录制流的错误事件回调函数。 |
| OH_AudioStream_Result OH_AudioCapturer_GetFastStatus(OH_AudioCapturer* capturer, OH_AudioStream_FastStatus* status) | - | 获取音频录制过程中的运行状态，是否在低时延状态下工作。 |
| typedef void (*OH_AudioCapturer_OnFastStatusChange)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_FastStatus status) | OH_AudioCapturer_OnFastStatusChange | 音频录制过程中低时延状态改变事件的回调函数。 |
| typedef void (*OH_AudioCapturer_OnPlaybackCaptureStartCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_PlaybackCaptureStartState state) | OH_AudioCapturer_OnPlaybackCaptureStartCallback | 音频录制过程中用于内录（录制的是设备内部应用的声音）启动结果的回调函数。该API暂不对外支持。 |
| OH_AudioStream_Result OH_AudioCapturer_RequestPlaybackCaptureStart(OH_AudioCapturer* capturer, OH_AudioCapturer_OnPlaybackCaptureStartCallback callback, void* userData) | - | 异步请求启动内录流。该函数是非阻塞的，意味着系统在接收到启动请求后，将继续处理用户授权和内录流的启动。 最终结果将通过回调函数返回。该API暂不对外支持。 |
| OH_AudioStream_Result OH_AudioCapturer_SetIndependentAudioSessionStrategy(OH_AudioCapturer* capturer, const OH_AudioSession_Strategy* strategy, uint32_t behavior) | - | 设置独立的音频会话策略和行为参数。当音频采集器在运行状态时调用此接口后，必须重新调用接口OH_AudioCapturer_Start使其生效。 |
 
 
  

##### 函数说明

  

##### OH_AudioCapturer_Release()

```text
OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer)
```
 
**描述**
 
释放输入音频流。
 
**需要权限：** ohos.permission.MICROPHONE
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_Start()

```text
OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer)
```
 
**描述**
 
启动音频采集器，开始获取音频数据。
 
**需要权限：** ohos.permission.MICROPHONE
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_Pause()

```text
OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer)
```
 
**描述**
 
暂停输入音频流。在暂停音频，后续需要恢复录音的场景，建议使用pause。
 
**需要权限：** ohos.permission.MICROPHONE
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_Stop()

```text
OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer)
```
 
**描述**
 
停止音频采集器，停止输入音频流。如果需要彻底结束录音，建议使用stop。
 
**需要权限：** ohos.permission.MICROPHONE
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_Flush()

```text
OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer)
```
 
**描述**
 
丢弃获取的音频数据。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_GetCurrentState()

```text
OH_AudioStream_Result OH_AudioCapturer_GetCurrentState(OH_AudioCapturer* capturer, OH_AudioStream_State* state)
```
 
**描述**
 
查询当前音频流状态。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_State* state | 指向一个用来接收音频流状态的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetLatencyMode()

```text
OH_AudioStream_Result OH_AudioCapturer_GetLatencyMode(OH_AudioCapturer* capturer,OH_AudioStream_LatencyMode* latencyMode)
```
 
**描述**
 
查询当前音频流时延模式。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_LatencyMode* latencyMode | 指向一个用来接收音频流时延模式的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetStreamId()

```text
OH_AudioStream_Result OH_AudioCapturer_GetStreamId(OH_AudioCapturer* capturer, uint32_t* streamId)
```
 
**描述**
 
查询当前输入音频流ID。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| uint32_t* streamId | 指向一个用来接收音频流ID的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetSamplingRate()

```text
OH_AudioStream_Result OH_AudioCapturer_GetSamplingRate(OH_AudioCapturer* capturer, int32_t* rate)
```
 
**描述**
 
查询当前输入音频流采样率。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| int32_t* rate | 指向一个用来接收音频流采样率的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetChannelCount()

```text
OH_AudioStream_Result OH_AudioCapturer_GetChannelCount(OH_AudioCapturer* capturer, int32_t* channelCount)
```
 
**描述**
 
查询当前音频流通道数。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| int32_t* channelCount | 指向一个用来接收音频流通道数的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetSampleFormat()

```text
OH_AudioStream_Result OH_AudioCapturer_GetSampleFormat(OH_AudioCapturer* capturer,OH_AudioStream_SampleFormat* sampleFormat)
```
 
**描述**
 
查询当前输入音频流采样格式。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_SampleFormat* sampleFormat | 指向一个用来接收音频流采样格式的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetEncodingType()

```text
OH_AudioStream_Result OH_AudioCapturer_GetEncodingType(OH_AudioCapturer* capturer,OH_AudioStream_EncodingType* encodingType)
```
 
**描述**
 
查询当前音频流编码类型。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_EncodingType* encodingType | 指向一个用来接收音频流编码类型的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetCapturerInfo()

```text
OH_AudioStream_Result OH_AudioCapturer_GetCapturerInfo(OH_AudioCapturer* capturer,OH_AudioStream_SourceType* sourceType)
```
 
**描述**
 
查询当前音频流工作场景类型。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_SourceType* sourceType | 指向一个用来接收输入类型音频流的工作场景的变量。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_GetFrameSizeInCallback()

```text
OH_AudioStream_Result OH_AudioCapturer_GetFrameSizeInCallback(OH_AudioCapturer* capturer,int32_t* frameSize)
```
 
**描述**
 
在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| int32_t* frameSize | 指向将为帧大小设置的变量的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_GetTimestamp()

```text
OH_AudioStream_Result OH_AudioCapturer_GetTimestamp(OH_AudioCapturer* capturer, clockid_t clockId,int64_t* framePosition, int64_t* timestamp)
```
 
**描述**
 
获取输入音频流时间戳和当前数据帧位置信息。
 
 该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| clockid_t clockId | 时钟标识符，使用CLOCK_MONOTONIC。 |
| int64_t* framePosition | 指向要接收位置的变量的指针。 |
| int64_t* timestamp | 指向接收时间戳的变量的指针，单位为纳秒。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM： 1. 参数capturer为nullptr； 2. 参数clockId无效。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
 
 
  

##### OH_AudioCapturer_GetFramesRead()

```text
OH_AudioStream_Result OH_AudioCapturer_GetFramesRead(OH_AudioCapturer* capturer, int64_t* frames)
```
 
**描述**
 
查询自创建流以来已读取的帧数。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| int64_t* frames | 指向将为帧计数设置的变量的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_SetMuteHint()

```text
OH_AudioStream_Result OH_AudioCapturer_SetMuteHint(OH_AudioCapturer* capturer, bool mute)
```
 
**描述**
 
应用将当前录音流的自身静音状态传递给系统音频模块。该接口用于向系统音频模块上报应用自身的静音状态，不会改变录音流的实际静音状态。当前仅在部分PC/2in1设备上，系统音频模块会基于设置的状态调整策略以降低功耗。该接口仅在录音流处于运行态时允许调用，否则返回错误AUDIOSTREAM_ERROR_ILLEGAL_STATE。同一录音流同时设置流级静音提示接口（本接口）和会话级静音提示接口时，流级（本接口）优先级更高，数值以流级（本接口）设置值为准。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| bool mute | 当应用自身已将录音流静音时，传入true，表示将目标流标记为静音。解除静音时，传入false。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：操作状态异常，录音流未处于running状态。 AUDIOSTREAM_ERROR_SYSTEM：系统异常，例如系统服务异常退出等。 |
 
 
  

##### OH_AudioCapturer_GetOverflowCount()

```text
OH_AudioStream_Result OH_AudioCapturer_GetOverflowCount(OH_AudioCapturer* capturer, uint32_t* count)
```
 
**描述**
 
查询当前录制音频流过载数。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| uint32_t* count | 指向一个用来接收音频流过载数的变量的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 |
 
 
  

##### OH_AudioCapturer_OnReadDataCallback()

```text
typedef void (*OH_AudioCapturer_OnReadDataCallback)(OH_AudioCapturer* capturer, void* userData, void* audioData,int32_t audioDataSize)
```
 
**描述**
 
读取音频数据的回调函数。为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 指向应用自定义的数据存储区域，方便应用给自身传递数据。 |
| void* audioData | 指向录制数据存储区域，用于应用读取录制数据。 |
| int32_t audioDataSize | 录制数据的长度，单位为字节。 |
 
 
  

##### OH_AudioCapturer_OnDeviceChangeCallback()

```text
typedef void (*OH_AudioCapturer_OnDeviceChangeCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioDeviceDescriptorArray* deviceArray)
```
 
**描述**
 
音频录制流的设备变化事件回调函数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 指向应用自定义的数据存储区域。 |
| OH_AudioDeviceDescriptorArray* deviceArray | 音频设备描述符数组。 |
 
 
  

##### OH_AudioCapturer_OnInterruptCallback()

```text
typedef void (*OH_AudioCapturer_OnInterruptCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
```
 
**描述**
 
音频录制流的中断事件回调函数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 指向应用自定义的数据存储区域。 |
| OH_AudioInterrupt_ForceType type | 音频流中断类型。 |
| OH_AudioInterrupt_Hint hint | 音频流中断提示类型。 |
 
 
  

##### OH_AudioCapturer_OnErrorCallback()

```text
typedef void (*OH_AudioCapturer_OnErrorCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioStream_Result error)
```
 
**描述**
 
音频录制流的错误事件回调函数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 指向应用自定义的数据存储区域。 |
| OH_AudioStream_Result error | 音频流录制错误结果。 |
 
 
  

##### OH_AudioCapturer_GetFastStatus()

```text
OH_AudioStream_Result OH_AudioCapturer_GetFastStatus(OH_AudioCapturer* capturer,OH_AudioStream_FastStatus* status)
```
 
**描述**
 
获取音频录制过程中的运行状态，是否在低时延状态下工作。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioStream_FastStatus* status | 指向接收低时延状态的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数capturer为nullptr。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常，仅在释放状态之前可用。 |
 
 
  

##### OH_AudioCapturer_OnFastStatusChange()

```text
typedef void (*OH_AudioCapturer_OnFastStatusChange)(OH_AudioCapturer* capturer,void* userData,OH_AudioStream_FastStatus status)
```
 
**描述**
 
音频录制过程中低时延状态改变事件的回调函数。
 
**起始版本：** 20
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 指向应用自定义的数据存储区域。 |
| OH_AudioStream_FastStatus status | 返回当前低时延状态。 |
 
 
  

##### OH_AudioCapturer_OnPlaybackCaptureStartCallback()

```text
typedef void (*OH_AudioCapturer_OnPlaybackCaptureStartCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_PlaybackCaptureStartState state)
```
 
**描述**
 
音频录制过程中用于内录（录制的是设备内部应用的声音）启动结果的回调函数。该API暂不对外支持。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| void* userData | 通过OH_AudioCapturer_RequestPlaybackCaptureStart指向应用自定义的数据存储区域。 |
| OH_AudioStream_PlaybackCaptureStartState state | 表示内录请求是否成功的状态。 |
 
 
  

##### OH_AudioCapturer_RequestPlaybackCaptureStart()

```text
OH_AudioStream_Result OH_AudioCapturer_RequestPlaybackCaptureStart(OH_AudioCapturer* capturer, OH_AudioCapturer_OnPlaybackCaptureStartCallback callback, void* userData)
```
 
**描述**
 
异步请求启动内录流。该函数是非阻塞的，意味着系统在接收到启动请求后，将继续处理用户授权和内录流的启动。
 
 最终结果将通过回调函数返回。该API暂不对外支持。
 
**起始版本：** 23
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| OH_AudioCapturer_OnPlaybackCaptureStartCallback callback | 用于接收启动请求最终结果的回调函数。 |
| void* userData | 指向应用自定义的数据存储区域, 该结构将传递给回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：capturer或callback是无效的。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：如果流已经在运行中或者已释放则是非法状态。 AUDIOSTREAM_ERROR_SYSTEM：系统内部错误，比如音频服务错误。 |
 
 
  

##### OH_AudioCapturer_SetIndependentAudioSessionStrategy()

```text
OH_AudioStream_Result OH_AudioCapturer_SetIndependentAudioSessionStrategy(OH_AudioCapturer* capturer, const OH_AudioSession_Strategy* strategy, uint32_t behavior)
```
 
**描述**
 
设置独立的音频会话策略和行为参数。当音频采集器在运行状态时调用此接口后，必须重新调用接口[OH_AudioCapturer_Start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_start)使其生效。
 
**起始版本：** 24
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioCapturer* capturer | 指向OH_AudioStreamBuilder_GenerateCapturer创建的音频流实例。 |
| const OH_AudioSession_Strategy* strategy | 用于设置独立的音频会话策略。 |
| uint32_t behavior | 音频会话行为标志，可以是单个标志，也可以是多个标志的按位OR组合。当前支持的音频会话行为详见OH_AudioSession_BehaviorFlags。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AudioStream_Result | AUDIOSTREAM_SUCCESS：函数执行成功。 AUDIOSTREAM_ERROR_INVALID_PARAM：参数为空指针或超出范围。 AUDIOSTREAM_ERROR_ILLEGAL_STATE：执行状态异常。 |
