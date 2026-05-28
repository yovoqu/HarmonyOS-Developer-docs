# OHAudio

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

提供音频模块C接口定义。
 
**系统能力：** SystemCapability.Multimedia.Audio.Core
 
**起始版本：** 10
 
  

#### 文件汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| native_audiocapturer.h | 声明音频采集的相关接口。 |
| native_audio_manager.h | 声明音频管理相关的接口。 |
| native_audio_resource_manager.h | 声明音频资源管理相关的接口。 |
| native_audio_routing_manager.h | 声明与音频路由管理器相关的接口。 包含用于创建audioRoutingManager，设备连接状态发生变化时的注册和注销功能，以及存储设备信息的指针数组的释放。 |
| native_audio_session_manager.h | 声明音频会话管理相关的接口。 包含创建音频会话管理器、激活/停用音频会话、检查音频会话是否已激活，以及监听音频会话停用事件。 |
| native_audio_stream_manager.h | 声明与音频流管理器相关的接口。 该文件接口用于创建audioStreamManager以及音频流设置和管理。 |
| native_audio_volume_manager.h | 声明音频音量管理器接口。该文件接口用于创建AudioVolumeManager。 |
| native_audiorenderer.h | 声明输出类型的音频流相关接口。 |
| native_audio_common.h | 声明音频公共基础数据结构。 定义音频接口的公共返回值的类型。 |
| native_audio_device_base.h | 定义音频设备参数的类型以及获取每个设备参数的接口。 |
| native_audiostream_base.h | 声明OHAudio基础的数据结构。 |
| native_audiostreambuilder.h | 声明音频流构造器相关接口。 包含构造和销毁构造器，设置音频流属性，回调等相关接口。 |
