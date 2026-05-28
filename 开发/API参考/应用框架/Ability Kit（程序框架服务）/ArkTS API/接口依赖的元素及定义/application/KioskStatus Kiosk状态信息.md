# KioskStatus (Kiosk状态信息)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。
 
> [!NOTE]
> 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。

  

#### KioskStatus

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isKioskMode | boolean | 否 | 否 | 当前系统是否处于Kiosk模式。true表示处于Kiosk模式，false表示不处于。 |
| kioskBundleName | string | 否 | 否 | 进入Kiosk模式的应用的名称。 |
| kioskBundleUid | number | 否 | 否 | 进入Kiosk模式的应用的UID。 |
