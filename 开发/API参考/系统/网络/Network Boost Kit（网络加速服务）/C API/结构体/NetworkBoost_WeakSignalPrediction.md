# NetworkBoost_WeakSignalPrediction

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network_boost_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| bool [isLastPredictionValid](#islastpredictionvalid) | 最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。 |
| uint32_t [startTime](#starttime) | 预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。 |
| uint32_t [duration](#duration) | 预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet


### duration
**支持设备：** Phone / PC/2in1 / Tablet


```text
uint32_t NetworkBoost_WeakSignalPrediction::duration
```

**描述**

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。


### isLastPredictionValid
**支持设备：** Phone / PC/2in1 / Tablet


```text
bool NetworkBoost_WeakSignalPrediction::isLastPredictionValid
```

**描述**

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。


### startTime
**支持设备：** Phone / PC/2in1 / Tablet


```text
uint32_t NetworkBoost_WeakSignalPrediction::startTime
```

**描述**

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。
