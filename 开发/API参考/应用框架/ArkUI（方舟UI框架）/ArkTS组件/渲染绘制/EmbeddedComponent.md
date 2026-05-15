# EmbeddedComponent

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

EmbeddedComponent用于支持在当前页面嵌入本应用内其他[EmbeddedUIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability)提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成页面布局和渲染。

通常用于有进程隔离诉求的模块化开发场景。


> [!NOTE]
> 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。


## 使用约束
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

EmbeddedComponent仅支持在拥有多进程权限的设备上使用。

EmbeddedComponent只能在UIAbility中使用，且被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。


## 子组件
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

无


## 接口
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

EmbeddedComponent(loader: Want, type: EmbeddedType)

创建跨进程嵌入式组件，用于显示同包名EmbeddedUIExtensionAbility的UI。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loader | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#embeddedtype12) | 是 | 提供方的类型。 |


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。


> [!NOTE]
> EmbeddedComponent组件宽高默认值和最小值均为10vp。不支持如下与宽高相关的属性："constraintSize"、"aspectRatio"、"layoutWeight"、"flexBasis"、"flexGrow"和"flexShrink"。


## 事件
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

与屏幕坐标相关的事件信息会基于EmbeddedComponent的位置宽高进行坐标转换后传递给被拉起的EmbeddedUIExtensionAbility处理。

不支持[点击](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click)等通用事件。仅支持以下事件：


### onTerminated
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onTerminated(callback: Callback<TerminationInfo>)

被拉起的EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession#terminateselfwithresult)或者[terminateSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession#terminateself)正常退出时，触发本回调函数。


> [!NOTE]
> 该接口不支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#callback)&lt;[TerminationInfo](#terminationinfo)&gt; | 是 | 回调函数，入参用于接收EmbeddedUIExtensionAbility的返回结果，类型为[TerminationInfo](#terminationinfo)。 |


### onError
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

onError(callback: ErrorCallback)

被拉起的EmbeddedUIExtensionAbility在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理，业务错误码详细介绍请参见[UIExtension错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiextension)。


> [!NOTE]
> 该接口不支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback) | 是 | 回调函数，入参用于接收异常信息，类型为[BusinessError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#businesserror)，可通过参数中的code、name和message获取错误信息并做处理。 |


> [!NOTE]
> 如下情形会触发本回调：


## TerminationInfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

用于表示被拉起的EmbeddedUIExtensionAbility的返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 被拉起EmbeddedUIExtensionAbility退出时返回的结果码，返回的结果码由terminateSelfWithResult或者terminateSelf被调用时传入的数据决定。 |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 否 | 是 | 被拉起EmbeddedUIExtensionAbility退出时返回的数据。 |


## 示例（加载EmbeddedComponent）
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

本示例展示EmbeddedComponent组件和EmbeddedUIExtensionAbility的基础使用方式，示例应用的bundleName为"com.example.embeddeddemo", 同应用下被拉起的EmbeddedUIExtensionAbility为"ExampleEmbeddedAbility"。本示例仅支持在拥有多进程权限的设备上运行，如2in1。


- 示例应用中的EntryAbility(UIAbility)加载首页文件ets/pages/Index.ets，其中内容如下：       __PREBLOCK_0__
- EmbeddedComponent拉起的ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)在ets/extensionAbility/ExampleEmbeddedAbility.ets文件中实现，内容如下：       __PREBLOCK_1__
- ExampleEmbeddedAbility(EmbeddedUIExtensionAbility)的入口页面文件ets/pages/extension.ets内容如下，同时需要在resources/base/profile/main_pages.json文件中配置该页面路径：       __PREBLOCK_2__
- 在module.json5配置文件的"extensionAbilities"标签下增加ExampleEmbeddedAbility配置，其type类型为embeddedUI，具体内容如下：       __PREBLOCK_3__
- 文件目录结构如下：       __PREBLOCK_4__
- 示例图如下：       ![](assets/EmbeddedComponent/file-20260514164121553-0.png)
