# @performance/timezone-interface-check

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-timezone-interface-check

在获取非本地时间时，建议使用统一标准的i18n.Calendar接口获取时间时区相关信息。
 

#### 规则配置

```json
// code-linter.json5
{
  <span style="color: rgb(135,16,148);">"rules"</span>: {
    <span style="color: rgb(135,16,148);">"@performance/timezone-interface-check"</span>: <span style="color: rgb(6,125,23);">"suggestion"</span>,
  }
}
```
 
 

#### 选项

该规则无需配置额外选项。
 
 

#### 正例1

```text
import i18n from '@ohos.i18n';

let calendar = i18n.getCalendar(i18n.getSystemLocale());
calendar.setTimeZone(i18n.getTimeZone().getID());
```
 
 

#### 正例2

```text
import i18n from '@ohos.i18n';

let timeZone1 = '123';
let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
calendar1.setTimeZone(timeZone1);
calendar1.get('zone_offset'); 
calendar1.get('dst_offset');
```
 
 

#### 反例1

```text
import i18n from '@ohos.i18n';

let timeZone1 = '123';
let calendar1 = i18n.getCalendar(i18n.getSystemLocale());
calendar1.setTimeZone(timeZone1);
//告警，缺少获取dst_offset
calendar1.get('zone_offset'); 
//calendar1.get('dst_offset');
```
 
 

#### 反例2

```text
import moment from '@hview/moment';
//告警
moment().utcOffset();
//告警
moment().utcOffset(120);
//告警
moment().utcOffset("+08:00");
//告警
moment().utcOffset(-5, true);
```
 
 

#### 规则集

```text
<span style="color: rgb(106,135,89);">plugin:@performance/all</span>
```
 
Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
