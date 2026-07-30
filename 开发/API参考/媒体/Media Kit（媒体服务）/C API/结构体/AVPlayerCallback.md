# AVPlayerCallback

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct AVPlayerCallback {...} AVPlayerCallback
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

AVPlayerCallback是AVPlayer的回调管理结构体，包含了播放过程信息OH_AVPlayerOnInfo和错误信息OH_AVPlayerOnError的回调函数指针。应用需注册此实例结构体到OH_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。通过注册这些回调，开发者可以实时监控AVPlayer的播放状态、获取播放过程信息（如缓冲进度、播放位置等）和错误事件，及时响应和处理播放过程中的各种事件，适用于需要对播放流程进行细粒度控制（Fine-grained Control）和监控的场景。
 
**起始版本：** 11
 
**废弃版本：** 12
 
**替代接口：** [OH_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback)或[OH_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback)。
 
**相关模块：** [AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer)
 
**所在头文件：** [avplayer_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_AVPlayerOnInfo onInfo | 监控AVPlayer过程信息，需注册此回调到AVPlayer实例中使用，详细内容参考OH_AVPlayerOnInfo。 起始版本： 11 废弃版本： 12 替代接口： OH_AVPlayerOnInfoCallback |
| OH_AVPlayerOnError onError | 监控AVPlayer操作错误，需注册此回调到AVPlayer实例中使用。回调签名为OH_AVPlayerOnError。回调参数信息请参考OH_AVPlayerOnError。 起始版本： 11 废弃版本： 12 替代接口： OH_AVPlayerOnErrorCallback |
