# native_audio_vivid.h

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

## native_audio_vivid.h
 
 

##### 概述

声明Audio Vivid相关的函数和枚举。
 
**引用文件：** <multimedia/player_framework/native_audio_vivid.h>
 
**库：** libnative_media_core.so
 
**系统能力：** SystemCapability.Multimedia.Media.Core
 
**起始版本：** 26.0.0
 
**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)
 
  

##### 汇总

  

##### [h2]结构体
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CartesianPosition | OH_CartesianPosition | 表示对象声源在笛卡尔坐标系（Cartesian coordinate system）中的位置。笛卡尔坐标系使用x、y、z轴定义三维空间中的位置。 |
| OH_PolarPosition | OH_PolarPosition | 表示极坐标系（polar coordinate system，也叫球坐标系）中的位置。极坐标系使用方位角、俯仰角和距离定义对象声源在三维空间中的位置。 |
| OH_AudioObjectPosition | OH_AudioObjectPosition | 表示音频对象声源在三维空间中的位置。该位置可以用笛卡尔坐标或极坐标表示。 |
| OH_AudioVividMetaBuilderStruct | OH_AudioVividMetaBuilder | OH_AudioVividMetaBuilder的前向声明。 |
 
 
  

##### [h2]枚举
 
| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioVividSignalFormat | OH_AudioVividSignalFormat | Audio Vivid编码器信号格式枚举。 |
 
 
  

##### [h2]函数
 
| 名称 | 描述 |
| --- | --- |
| OH_AVErrCode OH_AudioVividMetaBuilder_Create(OH_AudioVividMetaBuilder **builder, const OH_AVFormat *format) | 创建Audio Vivid元数据构建器。 |
| OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectPos(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, OH_AudioObjectPosition pos) | 更新Audio Vivid信号格式为OH_AudioVividSignalFormat.OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX时的音频对象位置。在此信号格式下，输入编码的PCM（Pulse Code Modulation）数据中，声道排列顺序为：声床声道在前，对象声道在后。  对象声道按顺序与objectIndex对应，从0开始编号。 |
| OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectGain(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, float gain) | 更新Audio Vivid信号格式为OH_AudioVividSignalFormat.OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX时的音频对象渲染的线性增益。 |
| OH_AVErrCode OH_AudioVividMetaBuilder_GetMetaLen(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, int32_t *len) | 获取元数据长度。 |
| OH_AVErrCode OH_AudioVividMetaBuilder_GetMeta(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, uint8_t *buffer, int32_t len) | 获取元数据缓冲区。 |
| OH_AVErrCode OH_AudioVividMetaBuilder_Destroy(OH_AudioVividMetaBuilder *builder) | 销毁Audio Vivid元数据构建器并释放资源。 |
 
 
  

##### 枚举类型说明

  

##### [h2]OH_AudioVividSignalFormat

```text
enum OH_AudioVividSignalFormat
```
 
**描述**
 
Audio Vivid编码器信号格式枚举。
 
**起始版本：** 26.0.0
  
| 枚举项 | 描述 |
| --- | --- |
| OH_AUDIO_VIVID_SIGNAL_FORMAT_MONO = 0 | Audio Vivid信号格式为单声道，编码器接收单声道数据，内部标记声道布局为OH_AudioChannelLayout.CH_LAYOUT_MONO。 |
| OH_AUDIO_VIVID_SIGNAL_FORMAT_STEREO = 1 | Audio Vivid信号格式为立体声，编码器接收双声道数据，内部标记声道布局为OH_AudioChannelLayout.CH_LAYOUT_STEREO。 |
| OH_AUDIO_VIVID_SIGNAL_FORMAT_MC = 2 | Audio Vivid信号格式为多声道，编码器支持声道布局OH_AudioChannelLayout.CH_LAYOUT_5POINT1、OH_AudioChannelLayout.CH_LAYOUT_5POINT1POINT2、OH_AudioChannelLayout.CH_LAYOUT_5POINT1POINT4、OH_AudioChannelLayout.CH_LAYOUT_7POINT1、OH_AudioChannelLayout.CH_LAYOUT_7POINT1POINT2、OH_AudioChannelLayout.CH_LAYOUT_7POINT1POINT4。 |
| OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX = 4 | Audio Vivid信号格式为混合模式，包含声床（Bed）和对象（object）。声床的声道布局支持OH_AudioChannelLayout.CH_LAYOUT_STEREO、OH_AudioChannelLayout.CH_LAYOUT_5POINT1、OH_AudioChannelLayout.CH_LAYOUT_5POINT1POINT2、OH_AudioChannelLayout.CH_LAYOUT_5POINT1POINT4、OH_AudioChannelLayout.CH_LAYOUT_7POINT1、OH_AudioChannelLayout.CH_LAYOUT_7POINT1POINT2、OH_AudioChannelLayout.CH_LAYOUT_7POINT1POINT4。 |
 
 
  

##### 函数说明

  

##### [h2]OH_AudioVividMetaBuilder_Create()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_Create(OH_AudioVividMetaBuilder **builder, const OH_AVFormat *format)
```
 
**描述**
 
创建Audio Vivid元数据构建器。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/5nNgiZHkRaGGbVwJIjjYNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025452Z&HW-CC-Expire=86400&HW-CC-Sign=EC95681F34E292C55DEE77A5510FF37C0BB123775E59A003E11934033CC64C0E)
 
 
生命周期管理：
  
- 通过本函数创建的实例不再使用时，必须调用[OH_AudioVividMetaBuilder_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h#oh_audiovividmetabuilder_destroy)手动释放，以避免内存泄漏。

  

 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioVividMetaBuilder **builder | 输出参数，用于获取OH_AudioVividMetaBuilder实例指针的指针。 |
| const OH_AVFormat *format | 指向包含音频格式信息的OH_AVFormat指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：参数builder或format为空指针或无效。  AV_ERR_UNSUPPORT：当前设备不支持此功能。  AV_ERR_UNKNOWN：创建构建器失败，属于未知错误，请查看日志获取详细信息。 |
 
 
  

##### [h2]OH_AudioVividMetaBuilder_UpdateObjectPos()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectPos(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, OH_AudioObjectPosition pos)
```
 
**描述**
 
更新Audio Vivid信号格式为[OH_AudioVividSignalFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h#oh_audiovividsignalformat).OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX时的音频对象位置。在此信号格式下，输入编码的PCM（Pulse Code Modulation）数据中，声道排列顺序为：声床声道在前，对象声道在后。
 
 对象声道按顺序与objectIndex对应，从0开始编号。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioVividMetaBuilder *builder | 指向OH_AudioVividMetaBuilder的指针。 |
| int32_t objectIndex | 要更新的音频对象索引，从0开始，不超过在OH_AudioVividMetaBuilder_Create创建builder时入参format设置的OH_MD_KEY_AUDIO_OBJECT_NUMBER对应的值。 |
| OH_AudioObjectPosition pos | 音频对象声源的新位置。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：参数builder为空指针或无效，objectIndex或pos无效。 |
 
 
  

##### [h2]OH_AudioVividMetaBuilder_UpdateObjectGain()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_UpdateObjectGain(OH_AudioVividMetaBuilder *builder, int32_t objectIndex, float gain)
```
 
**描述**
 
更新Audio Vivid信号格式为[OH_AudioVividSignalFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-vivid-h#oh_audiovividsignalformat).OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX时的音频对象渲染的线性增益。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioVividMetaBuilder *builder | 指向OH_AudioVividMetaBuilder的指针。 |
| int32_t objectIndex | 要更新的音频对象索引，从0开始，不超过在OH_AudioVividMetaBuilder_Create创建builder时入参format设置的OH_MD_KEY_AUDIO_OBJECT_NUMBER对应的值。 |
| float gain | 对象渲染时应用的线性增益值，范围为[0.0, 6.0]，线性增益0.0为静音，1.0为不变。此参数可选，如未设置则不应用增益。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：参数builder为空指针或无效，objectIndex或gain无效。 |
 
 
  

##### [h2]OH_AudioVividMetaBuilder_GetMetaLen()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_GetMetaLen(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, int32_t *len)
```
 
**描述**
 
获取元数据长度。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const OH_AudioVividMetaBuilder *builder | 指向OH_AudioVividMetaBuilder的指针。 |
| bool withStaticMeta | 设置输出的长度是否包含静态元数据。true表示输出长度包含静态元数据；false表示输出长度仅包含动态元数据。 |
| int32_t *len | 用于接收元数据长度的指针。单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：参数builder为空指针或无效，len为空指针。 |
 
 
  

##### [h2]OH_AudioVividMetaBuilder_GetMeta()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_GetMeta(const OH_AudioVividMetaBuilder *builder, bool withStaticMeta, uint8_t *buffer, int32_t len)
```
 
**描述**
 
获取元数据缓冲区。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const OH_AudioVividMetaBuilder *builder | 指向OH_AudioVividMetaBuilder的指针。 |
| bool withStaticMeta | 设置输出的长度是否包含静态元数据。true表示输出缓冲区包含静态元数据；false表示输出缓冲区仅包含动态元数据。 |
| uint8_t *buffer | 用于接收元数据内容的缓冲区指针。 |
| int32_t len | 缓冲区长度。单位为字节。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：builder为空指针或无效，buffer为空指针或len不足。 |
 
 
  

##### [h2]OH_AudioVividMetaBuilder_Destroy()

```text
OH_AVErrCode OH_AudioVividMetaBuilder_Destroy(OH_AudioVividMetaBuilder *builder)
```
 
**描述**
 
销毁Audio Vivid元数据构建器并释放资源。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_AudioVividMetaBuilder *builder | 指向待销毁的OH_AudioVividMetaBuilder的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_AVErrCode | AV_ERR_OK：执行成功。  AV_ERR_INVALID_VAL：参数builder为空指针。 |
