# TriggerInfo

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-triggerinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

作为[trigger](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagenttrigger)的入参定义执行WantAgent所需要的信息。

> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。



#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { wantAgent } from '@kit.AbilityKit';
```



#### 属性

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示传递的公共事件数据，仅当WantAgent实例的OperationType类型是'SEND_COMMON_EVENT'时有效。该字段与发布者使用commonEventManager.publish发布公共事件时，传递CommonEventPublishData公共事件数据中的code字段含义一致。取值根据公共事件类型确定。 |
| want | Want | 否 | 是 | 对象间信息传递的载体，可以用于应用组件间的信息传递。 |
| permission | string | 否 | 是 | 表示公共事件订阅者的权限。仅当WantAgent实例的OperationType类型是'SEND_COMMON_EVENT'时，该字段生效。若权限为null，则接收方无需具备任何权限。 |
| extraInfo | { [key: string]: any } | 否 | 是 | 额外数据，用于传递自定义扩展信息。参数为键值对对象，key为字符串类型的键名，value为任意类型的值。建议优先使用类型安全的extraInfos属性替代本属性。设置extraInfos属性后，本属性将不再生效。 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 额外数据，用于传递自定义键值对信息，类型安全。推荐使用该属性替代extraInfo。当需要在触发WantAgent时携带额外的自定义数据时传入此参数，不传入时默认为null，不会携带额外数据。 |
