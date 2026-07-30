# OH_AVRecorder_EncoderInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-encoderinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVRecorder_EncoderInfo {...} OH_AVRecorder_EncoderInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供编码器信息。
 
**起始版本：** 18
 
**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)
 
**所在头文件：** [avrecorder_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AVRecorder_CodecMimeType mimeType | 编码器MIME类型名称。与type相对应，音频编码器对应音频MIME类型，视频编码器对应视频MIME类型。 |
| char* type | 编码器类型，audio表示音频编码器，video表示视频编码器。 |
| OH_AVRecorder_Range bitRate | 编码器支持的比特率的范围，比特率单位为比特每秒（bit/s）。音频和视频编码器均适用。 |
| OH_AVRecorder_Range frameRate | 编码器支持的视频帧率的范围，帧率单位为帧每秒（FPS）。仅适用于视频编码器。 |
| OH_AVRecorder_Range width | 编码器支持的视频帧宽度的范围，视频帧宽度单位为像素（px）。仅适用于视频编码器。 |
| OH_AVRecorder_Range height | 编码器支持的视频帧高度的范围，视频帧高度单位为像素（px）。仅适用于视频编码器。 |
| OH_AVRecorder_Range channels | 编码器支持的音频采集声道数的范围。仅适用于音频编码器。 |
| int32_t* sampleRate | 音频采样率列表，包含所有可以使用的音频采样率值，单位为赫兹（Hz）。仅适用于音频编码器。 |
| int32_t sampleRateLen | 音频采样率列表长度，与sampleRate字段配合使用，仅适用于音频编码器。 |
