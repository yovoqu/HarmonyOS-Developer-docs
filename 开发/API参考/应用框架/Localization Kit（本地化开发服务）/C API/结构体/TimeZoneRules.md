# TimeZoneRules

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct TimeZoneRules {...} TimeZoneRules
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

完整的时区规则。
 
**起始版本：** 22
 
**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)
 
**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| InitialTimeZoneRule initial | 起始时区规则。 |
| TimeArrayTimeZoneRule* timeArrayRules | 起始时间戳数组定义的时区规则数组。 |
| AnnualTimeZoneRule* annualRules | 每年生效的时区规则数组。 |
| size_t numTimeArrayRules | 起始时间戳数组定义的时区规则数组的大小。 |
| size_t numAnnualRules | 每年生效的时区规则数组的大小。 |
