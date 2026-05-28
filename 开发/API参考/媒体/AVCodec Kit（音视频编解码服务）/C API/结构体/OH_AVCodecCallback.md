# OH_AVCodecCallback

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodeccallback
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_AVCodecCallback {...} OH_AVCodecCallback
```


##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVCodec实例中，并处理回调上报的信息，以保证OH_AVCodec的正常运行。

使用指导请参见[视频编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding)中的“Surface模式步骤-4或Buffer模式步骤-3”。

**起始版本：** 11

**相关模块：** [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)

**所在头文件：** [native_avcodec_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)



##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV



##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

| 名称 | 描述 |
| --- | --- |
| OH_AVCodecOnError onError | 监控编解码器操作错误。 |
| OH_AVCodecOnStreamChanged onStreamChanged | 监控编解码器流变化。 |
| OH_AVCodecOnNeedInputBuffer onNeedInputBuffer | 监控编解码器需要输入数据。 |
| OH_AVCodecOnNewOutputBuffer onNewOutputBuffer | 监控编解码器已生成输出数据。 |
