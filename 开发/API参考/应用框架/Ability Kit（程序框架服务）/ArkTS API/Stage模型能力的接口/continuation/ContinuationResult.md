# ContinuationResult

更新时间：2026-04-10 09:55:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult
**支持设备：** Phone | PC/2in1 | Tablet | TV

流转管理入口返回的设备信息。

> [!NOTE]
> 本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用 分布式设备管理 替代。 本模块接口仅可在Stage模型下使用。



##### ContinuationResult(deprecated)

**支持设备：** Phone | PC/2in1 | Tablet | TV

ContinuationManager的[on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager#continuationmanagerondeviceselecteddeprecated)接口返回此对象表示流转管理入口返回的设备信息。

> [!NOTE]
> 从API version 22开始废弃，建议使用 DeviceBasicInfo 代替。


**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示设备标识。 |
| type | string | 否 | 否 | 表示设备类型。 |
| name | string | 否 | 否 | 表示设备名称。 |
