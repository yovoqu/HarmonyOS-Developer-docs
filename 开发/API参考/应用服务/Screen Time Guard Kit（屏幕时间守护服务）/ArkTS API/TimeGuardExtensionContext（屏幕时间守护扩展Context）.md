# @hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext（屏幕时间守护扩展Context）

更新时间：2026-07-03 02:18:23

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensioncontext
**支持设备：** Phone | Tablet

#### 模块概述

**支持设备：** Phone | Tablet

屏幕时间守护ExtensionContext模块提供了获取[TimeGuardExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensionability)上下文的能力。TimeGuardExtensionContext继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)，是TimeGuardExtensionAbility的上下文环境，开发者可用于查询所属TimeGuardExtensionAbility的信息、Module的配置信息以及HAP包的信息，并根据自身业务需求使用对应的信息。
 
**起始版本：** 6.0.0(20)
 
  

#### 导入模块

**支持设备：** Phone | Tablet

```text
import { TimeGuardExtensionContext } from '@kit.ScreenTimeGuardKit';
```
 
  

#### TimeGuardExtensionContext

**支持设备：** Phone | Tablet

**模型约束：** 此接口仅可在Stage模型下使用。
 
**系统能力：** SystemCapability.ScreenTimeGuard.GuardService
 
**起始版本：** 6.0.0(20)
 
本类继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。相较于ExtensionContext，TimeGuardExtensionContex未新增功能，只是命名区分。
