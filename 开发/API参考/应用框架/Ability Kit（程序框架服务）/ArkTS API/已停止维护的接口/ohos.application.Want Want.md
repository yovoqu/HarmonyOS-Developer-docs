# @ohos.application.Want (Want)

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

Want是对象间信息传递的载体，可以用于应用组件间的信息传递。Want的使用场景之一是作为startAbility的参数，其包含了指定的启动目标，以及启动时需携带的相关数据，如bundleName和abilityName字段分别指明目标Ability所在应用Bundle名称以及对应包内的Ability名称。当Ability A需要启动Ability B并传入一些数据时，可使用Want作为载体将这些数据传递给Ability B。


> [!NOTE]
> 本模块首批接口从API version 8 开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)。后续版本的新增接口，采用上角标单独标记接口的起始版本。


## 导入模块
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```ts
import Want from '@ohos.application.Want';
```


## Want
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

**系统能力**：SystemCapability.Ability.AbilityBase


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 表示运行指定Ability的设备ID。如果未设置该字段，则表明指定本设备。 |
| bundleName | string | 否 | 是 | 表示Bundle名称。 |
| abilityName | string | 否 | 是 | 表示待启动的Ability名称。如果在Want中该字段同时指定了BundleName和AbilityName，则Want可以直接匹配到指定的Ability。AbilityName需要在一个应用的范围内保证唯一。 |
| uri | string | 否 | 是 | 表示Uri描述。如果在Want中指定了Uri，则Want将匹配指定的Uri信息，包括scheme、schemeSpecificPart、authority和path信息。 |
| type | string | 否 | 是 | 表示MIME type类型描述，打开文件的类型，主要用于文管打开文件。比如：'text/xml' 、 'image/*'等，MIME定义参考：https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com。 |
| flags | number | 否 | 是 | 表示处理Want的方式。默认传数字，具体参考：[flags说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant#flags)。 |
| action | string | 否 | 是 | 表示要执行的通用操作（如：查看、分享、应用详情）。在隐式Want中，您可以定义该字段，配合uri或parameters来表示对数据要执行的操作。具体参考：[action说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant#action)。隐式Want定义及匹配规则参考：[显式Want与隐式Want匹配规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings)。 |
| parameters | { [key: string]: any } | 否 | 是 | 表示WantParams描述，由开发者自行决定传入的键值对。默认会携带以下key值：          ohos.aafwk.param.callerPid 表示拉起方的pid。          ohos.aafwk.param.callerToken 表示拉起方的token。          ohos.aafwk.param.callerUid 表示[bundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo#bundleinfodeprecated)中的uid，应用包里应用程序的uid。          - component.startup.newRules：表示是否启用新的管控规则。          - moduleName：表示拉起方的模块名，该字段的值即使定义成其他字符串，在传递到另一端时会被修改为正确的值。          - ohos.dlp.params.sandbox：表示dlp文件才会有。 |
| entities | Array&lt;string&gt; | 否 | 是 | 表示目标Ability额外的类别信息（如：浏览器、视频播放器）。在隐式Want中是对action字段的补充。在隐式Want中，您可以定义该字段，来过滤匹配Ability类型。具体参考：[entity说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant#entity)。 |


**示例：**


- 基础用法(在UIAbility对象中调用，其中示例中的context为UIAbility的上下文对象)。       __PREBLOCK_1__
- 通过自定字段传递数据，以下为当前支持类型(在UIAbility对象中调用，其中示例中的context为UIAbility的上下文对象)。               字符串（String）         __PREBLOCK_2__
- 数字（Number）         __PREBLOCK_3__
- 布尔（Boolean）         __PREBLOCK_4__
- 对象（Object）         __PREBLOCK_5__
- 数组（Array）         __PREBLOCK_6__
- 文件描述符（FD）         __PREBLOCK_7__
