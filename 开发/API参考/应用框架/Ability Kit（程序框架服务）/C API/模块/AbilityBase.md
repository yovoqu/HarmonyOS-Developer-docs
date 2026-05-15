# AbilityBase

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

作为Ability Kit的基础定义模块，AbilityBase提供了组件启动参数[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-want-h)的定义与接口，可以用于应用组件间的信息传递。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 15


## 文件汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [ability_base_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-base-common-h) | 声明AbilityBase定义的相关错误码。 |
| [want.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-want-h) | Want是对象间信息传递的载体, 可以用于应用组件间的信息传递。 Want的使用场景之一是作为startAbility的参数, 其包含了指定的启动目标, 以及启动时需携带的相关数据, 如bundleName和abilityName字段分别指明目标Ability所在应用的Bundle名称以及对应包内的Ability名称。当Ability A需要启动Ability B并传入一些数据时, 可使用Want作为载体将这些数据传递给Ability B。 |
