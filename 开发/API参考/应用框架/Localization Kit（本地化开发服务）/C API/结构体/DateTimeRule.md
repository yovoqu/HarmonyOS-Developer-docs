# DateTimeRule

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-datetimerule
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct DateTimeRule {...} DateTimeRule
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

时间日期规则。
 
**起始版本：** 22
 
**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)
 
**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t month | 月份。 |
| int32_t dayOfMonth | 当月的第几天。 |
| int32_t dayOfWeek | 当周的第几天。 |
| int32_t weekInMonth | 当月的第几周。 |
| int32_t millisInDay | 从当天凌晨0点开始到当前时间的毫秒值。 |
| DateRuleType dateRuleType | 日期规则类型。 |
| TimeRuleType timeRuleType | 时间规则类型。 |
