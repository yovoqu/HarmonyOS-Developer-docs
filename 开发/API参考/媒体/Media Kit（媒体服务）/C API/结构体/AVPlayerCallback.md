# AVPlayerCallback

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct AVPlayerCallback {...} AVPlayerCallback
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

包含了OH_AVPlayerOnInfo和OH_AVPlayerOnError回调函数指针的集合。应用需注册此实例结构体到OH_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback) [OH_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback)

**相关模块：** [AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer)

**所在头文件：** [avplayer_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| OH_AVPlayerOnInfo onInfo | 监控AVPlayer过程信息，参考[OH_AVPlayerOnInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfo)。 起始版本： 11 废弃版本： 12 替代接口： [OH_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback) |
| OH_AVPlayerOnError onError | 监控AVPlayer操作错误，参考[OH_AVPlayerOnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerror)。 起始版本： 11 废弃版本： 12 替代接口： [OH_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback) |
