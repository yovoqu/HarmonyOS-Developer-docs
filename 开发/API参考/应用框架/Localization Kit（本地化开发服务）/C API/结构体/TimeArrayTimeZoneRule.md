# TimeArrayTimeZoneRule

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct TimeArrayTimeZoneRule {...} TimeArrayTimeZoneRule
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

起始时间戳数组定义的时区规则。

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| char* name | 时区规则的名称。 |
| int32_t rawOffset | 时区的原始偏移量。 |
| int32_t dstSavings | 夏令时的偏移量。 |
| double* startTimes | 规则生效的起始时间戳数组。 |
| int32_t numStartTimes | 规则生效的起始时间戳数组的大小。 |
| [TimeRuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h#timeruletype) timeRuleType | 时间规则类型。 |
