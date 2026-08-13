# avrecorder_base.h

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义了媒体AVRecorder的结构体、枚举和回调函数。
 
**引用文件：** <multimedia/player_framework/avrecorder_base.h>
 
**库：** libavrecorder.so
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVRecorder_Profile | OH_AVRecorder_Profile | 定义音视频录制的详细参数。 |
| OH_AVRecorder | OH_AVRecorder | 音视频录制的结构体类型，表示AVRecorder实例，支持音视频数据采集与录制，适用于将音视频内容录制保存为文件的场景。 |
| OH_AVRecorder_Location | OH_AVRecorder_Location | 提供媒体资源的地理位置信息。 |
| OH_AVRecorder_MetadataTemplate | OH_AVRecorder_MetadataTemplate | 定义AVRecorder录制元数据的基本模板。 |
| OH_AVRecorder_Metadata | OH_AVRecorder_Metadata | 定义录制元数据信息的数据结构。 |
| OH_AVRecorder_Config | OH_AVRecorder_Config | 提供媒体AVRecorder的配置定义。 |
| OH_AVRecorder_Range | OH_AVRecorder_Range | 表示参数的取值范围，包含最小值和最大值。 |
| OH_AVRecorder_EncoderInfo | OH_AVRecorder_EncoderInfo | 提供AVRecorder的音视频编码器信息，用于查询和选择合适的编码器。 |
 
 
  

#### 枚举

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVRecorder_AudioSourceType | OH_AVRecorder_AudioSourceType | AVRecorder的音频源类型。 |
| OH_AVRecorder_VideoSourceType | OH_AVRecorder_VideoSourceType | AVRecorder的视频源类型。 |
| OH_AVRecorder_CodecMimeType | OH_AVRecorder_CodecMimeType | 编码器MIME类型，用于指定录制时音视频数据的编码格式。编码器类型需与容器格式类型匹配使用。 |
| OH_AVRecorder_ContainerFormatType | OH_AVRecorder_ContainerFormatType | 容器格式类型（CFT），用于指定录制文件的封装格式。容器格式需与编码器MIME类型兼容，不同容器格式支持不同的编码器类型。 |
| OH_AVRecorder_State | OH_AVRecorder_State | AVRecorder状态。 |
| OH_AVRecorder_StateChangeReason | OH_AVRecorder_StateChangeReason | AVRecorder状态变化的原因。 |
| OH_AVRecorder_FileGenerationMode | OH_AVRecorder_FileGenerationMode | 录制文件的生成模式，用于指定录制生成媒体文件的创建方式，适用于需要选择由应用自行管理文件还是由系统自动管理文件的录制场景。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder, OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData) | OH_AVRecorder_OnStateChange | 当录制状态发生变化时调用。 |
| typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData) | OH_AVRecorder_OnError | 当录制过程中发生错误时调用。 |
| typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData) | OH_AVRecorder_OnUri | 当录制文件的生成模式为OH_AVRecorder_FileGenerationMode.AVRECORDER_AUTO_CREATE_CAMERA_SCENE时调用，用于通知应用获取录制生成的媒体资源。 |
 
 
  

#### 枚举类型说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AVRecorder_AudioSourceType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_AudioSourceType
```
 
**描述**
 
AVRecorder的音频源类型。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_DEFAULT = 0 | 默认音频源类型。适用于无需指定特定音频源类型的通用录制场景。 |
| AVRECORDER_MIC = 1 | 麦克风音频源类型。 |
| AVRECORDER_VOICE_RECOGNITION = 2 | 语音识别场景的音频源。 |
| AVRECORDER_VOICE_COMMUNICATION = 7 | 语音通话场景的音频源。 |
| AVRECORDER_VOICE_MESSAGE = 10 | 语音消息的音频源。 |
| AVRECORDER_CAMCORDER = 13 | 相机录像的音频源。 |
 
 
  

#### OH_AVRecorder_VideoSourceType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_VideoSourceType
```
 
**描述**
 
AVRecorder的视频源类型。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_SURFACE_YUV = 0 | 原始数据Surface。适用于需要对原始视频帧数据进行编码处理的场景。 |
| AVRECORDER_SURFACE_ES = 1 | ES数据Surface。适用于已有编码数据（如硬编码输出）无需再次编码的场景。 |
 
 
  

#### OH_AVRecorder_CodecMimeType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_CodecMimeType
```
 
**描述**
 
编码器MIME类型，用于指定录制时音视频数据的编码格式。编码器类型需与容器格式类型匹配使用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_VIDEO_AVC = 2 | H.264视频编码器MIME类型。 |
| AVRECORDER_AUDIO_AAC = 3 | AAC音频编码器MIME类型。 |
| AVRECORDER_AUDIO_MP3 = 4 | MP3音频编码器MIME类型。 |
| AVRECORDER_AUDIO_G711MU = 5 | G711-mulaw音频编码器MIME类型。 |
| AVRECORDER_VIDEO_MPEG4 = 6 | MPEG4视频编码器MIME类型。 |
| AVRECORDER_VIDEO_HEVC = 8 | H.265视频编码器MIME类型。 |
| AVRECORDER_AUDIO_AMR_NB = 9 | AMR_NB音频编码器MIME类型。 |
| AVRECORDER_AUDIO_AMR_WB = 10 | AMR_WB音频编码器MIME类型。 |
 
 
  

#### OH_AVRecorder_ContainerFormatType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_ContainerFormatType
```
 
**描述**
 
容器格式类型（CFT），用于指定录制文件的封装格式。容器格式需与编码器MIME类型兼容，不同容器格式支持不同的编码器类型。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_CFT_MPEG_4 = 2 | 视频容器格式类型mp4。 |
| AVRECORDER_CFT_MPEG_4A = 6 | 音频容器格式类型m4a。 |
| AVRECORDER_CFT_AMR = 8 | 音频容器格式类型amr。 |
| AVRECORDER_CFT_MP3 = 9 | 音频容器格式类型mp3。 |
| AVRECORDER_CFT_WAV = 10 | 音频容器格式类型wav。 |
| AVRECORDER_CFT_AAC = 11 | 音频容器格式类型aac（带ADTS头）。 起始版本： 20 |
 
 
  

#### OH_AVRecorder_State

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_State
```
 
**描述**
 
AVRecorder状态。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_IDLE = 0 | 空闲状态。此时可以调用OH_AVRecorder_Prepare接口设置录制参数，进入AVRECORDER_PREPARED状态。 |
| AVRECORDER_PREPARED = 1 | 准备状态。参数设置完成，此时可以调用OH_AVRecorder_Start接口开始录制，进入AVRECORDER_STARTED状态。 |
| AVRECORDER_STARTED = 2 | 启动状态。正在录制，此时可以调用OH_AVRecorder_Pause接口暂停录制，进入AVRECORDER_PAUSED状态。 也可以调用OH_AVRecorder_Stop接口结束录制，进入AVRECORDER_STOPPED状态。 |
| AVRECORDER_PAUSED = 3 | 暂停状态。此时可以调用OH_AVRecorder_Resume接口继续录制，进入AVRECORDER_STARTED状态。 也可以调用OH_AVRecorder_Stop接口结束录制，进入AVRECORDER_STOPPED状态。 |
| AVRECORDER_STOPPED = 4 | 停止状态。此时可以调用OH_AVRecorder_Prepare接口设置录制参数，重新进入AVRECORDER_PREPARED状态。 |
| AVRECORDER_RELEASED = 5 | 释放状态。录制资源释放，此时不能再进行任何操作。在任何其他状态下，均可以通过调用OH_AVRecorder_Release接口进入AVRECORDER_RELEASED状态。 |
| AVRECORDER_ERROR = 6 | 错误状态。当AVRecorder实例发生不可逆错误，会转换至当前状态。 切换至AVRECORDER_ERROR状态时会伴随OH_AVRecorder_OnError事件，该事件会上报详细错误原因。 在AVRECORDER_ERROR状态时，不能再进行录制相关操作，用户需要调用OH_AVRecorder_Reset接口重置AVRecorder实例，或者调用OH_AVRecorder_Release接口释放资源。 |
 
 
  

#### OH_AVRecorder_StateChangeReason

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_StateChangeReason
```
 
**描述**
 
AVRecorder状态变化的原因。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_USER = 0 | 用户操作导致的状态变化。例如用户主动调用Start、Pause、Resume、Stop等接口时触发。 |
| AVRECORDER_BACKGROUND = 1 | 后台操作导致的状态变化。例如因音频打断、录制超时等原因自动改变录制状态时触发。 |
 
 
  

#### OH_AVRecorder_FileGenerationMode

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
enum OH_AVRecorder_FileGenerationMode
```
 
**描述**
 
录制文件的生成模式，用于指定录制生成媒体文件的创建方式，适用于需要选择由应用自行管理文件还是由系统自动管理文件的录制场景。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
  
| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER_APP_CREATE = 0 | 由应用自行在沙箱中创建媒体文件，此模式下不会触发OH_AVRecorder_OnUri回调。 |
| AVRECORDER_AUTO_CREATE_CAMERA_SCENE = 1 | 由系统创建媒体文件，此模式下会触发OH_AVRecorder_OnUri回调，应用可通过回调获取录制生成的媒体资源对象。仅在应用使用相机进行录制时生效。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_AVRecorder_OnStateChange()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder, OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData)
```
 
**描述**
 
当录制状态发生变化时调用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AVRecorder *recorder | OH_AVRecorder实例的指针。 |
| OH_AVRecorder_State state | 表示录制器状态。 |
| OH_AVRecorder_StateChangeReason reason | 录制器状态变化的原因。 |
| void *userData | 用户特定数据的指针。 |
 
 
  

#### OH_AVRecorder_OnError()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)
```
 
**描述**
 
当录制过程中发生错误时调用。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AVRecorder *recorder | OH_AVRecorder实例的指针。 |
| int32_t errorCode | 错误码，详细说明请参见OH_AVErrCode。 |
| const char *errorMsg | 描述错误详情的字符串，用于说明错误的具体内容。 |
| void *userData | 用户特定数据的指针。 |
 
 
  

#### OH_AVRecorder_OnUri()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
```
 
**描述**
 
当录制文件的生成模式为[OH_AVRecorder_FileGenerationMode](#oh_avrecorder_filegenerationmode).AVRECORDER_AUTO_CREATE_CAMERA_SCENE时调用，用于通知应用获取录制生成的媒体资源。
 
**系统能力：** SystemCapability.Multimedia.Media.AVRecorder
 
**起始版本：** 18
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AVRecorder *recorder | OH_AVRecorder实例的指针。 |
| OH_MediaAsset *asset | OH_MediaAsset实例的指针，用于返回系统自动创建的媒体资源对象，应用可通过该对象访问录制生成的媒体文件。 |
| void *userData | 用户特定数据的指针。 |
