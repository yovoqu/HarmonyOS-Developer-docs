# EntityType（实体类型）

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-entity-type-api
**支持设备：** Phone | PC/2in1 | Tablet

实体类别的枚举类。
 
**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing
 
**模型约束：** 此接口仅可在Stage模型下使用。
 
**起始版本：** 5.0.0(12)
 
**导入模块：**
 
```text
import { EntityType } from '@kit.NaturalLanguageKit';
```
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATETIME | datetime | 时间实体 |
| EMAIL | email | 邮箱实体 |
| EXPRESS_NO | expressNo | 快递单号实体 |
| FLIGHT_NO | flightNo | 航班号实体 |
| LOCATION | location | 地点实体 |
| NAME | name | 姓名实体 |
| PHONE_NO | phoneNo | 手机号实体 |
| URL | url | url实体 |
| VERIFICATION_CODE | verificationCode | 验证码实体 |
| ID_NO | idNo | 身份证号实体 |
