# AutoFillType

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofilltype
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示提供自动填充类型的枚举。
 
**起始版本：** 26.0.0
  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { autoFillManager } from '@kit.AbilityKit';
```
 
  

#### AutoFillType

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**起始版本：** 26.0.0
 
**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。
 
**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
 
**模型约束**：此接口仅可在Stage模型下使用。
  
| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未定义的类型。 |
| PASSWORD | 1 | 密码类型。 |
| USER_NAME | 2 | 用户名类型。 |
| NEW_PASSWORD | 3 | 新密码类型。 |
