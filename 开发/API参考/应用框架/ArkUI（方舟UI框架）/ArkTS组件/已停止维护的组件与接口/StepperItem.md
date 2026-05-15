# StepperItem

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepperitem
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

用作[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)组件的页面子组件。


## 子组件
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

支持单个子组件。


## 接口
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

StepperItem()

创建[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)组件的页面子组件。


> [!NOTE]
> 从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#属性)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


## 属性
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### prevLabel(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

prevLabel(value: string)

设置左侧文本按钮内容，第一页没有左侧文本按钮，当步骤导航器大于一页时，除第一页外默认值都为“返回”。


> [!NOTE]
> 从API version 8开始支持，从API version 22开始废弃，建议使用[showPrevious](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#showprevious)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 左侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |


### nextLabel(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

nextLabel(value: string)

设置右侧文本按钮内容，最后一页默认值为“开始”，其余页默认值为“下一步”。


> [!NOTE]
> 从API version 8开始支持，从API version 22开始废弃，建议使用[showNext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#shownext)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 右侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |


### status(deprecated)
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

status(value?: ItemState)

设置步骤导航器nextLabel的显示状态。


> [!NOTE]
> 从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicatorinteractive12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**


| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ItemState](#itemstate枚举说明) | 否 | 步骤导航器nextLabel的显示状态。 默认值：ItemState.Normal |


## ItemState枚举说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

步骤导航器nextLabel的显示状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full


| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用[index](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#index)替代。 |
| Disabled | 1 | 不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicatorinteractive12)替代。 |
| Waiting | 2 | 等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)替代。 |
| Skip | 3 | 跳过状态，右侧文本按钮默认显示“跳过”，此时可在Stepper的onSkip回调中自定义相关逻辑。 说明： 从API version 8开始支持，从API version 22开始废弃，建议使用[index](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#index)替代。 |


## 示例
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

见[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)。
